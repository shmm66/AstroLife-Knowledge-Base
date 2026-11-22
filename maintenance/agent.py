#!/usr/bin/env python3
"""Metadata-first AstroLife astronomy source monitor. It never edits release payloads."""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, re, sys
import urllib.error, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "maintenance" / "sources.json"
DEFAULT_STATE = ROOT / "maintenance" / "state" / "source-state.json"
DEFAULT_CANDIDATES = ROOT / "maintenance" / "candidates"
DEFAULT_REPORT = ROOT / "maintenance" / "reports" / "run-report.json"
USER_AGENT = "AstroLife-Knowledge-Maintenance-Agent/1.0 (+https://github.com/shmm66/AstroLife-Knowledge-Base)"
MAX_BYTES, TIMEOUT = 8 * 1024 * 1024, 25
ATOM = {"a": "http://www.w3.org/2005/Atom"}

class SourceError(RuntimeError):
    pass

def timestamp():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

def digest(data):
    return hashlib.sha256(data).hexdigest()

def read_json(path, fallback=None):
    return json.loads(path.read_text(encoding="utf-8-sig")) if path.is_file() else fallback

def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)

def validate_config(config):
    if config.get("schema_version") != "1.0" or not isinstance(config.get("sources"), list):
        raise ValueError("Unsupported maintenance source configuration.")
    kinds = {"page", "horizons_probe", "mpc_probe", "tap_count", "json_probe", "atom_feed", "crossref_feed"}
    seen = set()
    for s in config["sources"]:
        sid = s.get("id", "")
        parsed = urllib.parse.urlparse(s.get("url", ""))
        if not re.fullmatch(r"[A-Z0-9_]{3,80}", sid) or sid in seen:
            raise ValueError("Invalid or duplicate source id: " + str(sid))
        seen.add(sid)
        if s.get("kind") not in kinds or parsed.scheme != "https" or not parsed.hostname:
            raise ValueError("Invalid adapter or non-HTTPS URL for " + sid)
        if not s.get("title") or not s.get("role"):
            raise ValueError("Missing title or role for " + sid)
        if s.get("change_action") not in {"health_only", "human_review", "dataset_candidate", "literature_candidate"}:
            raise ValueError("Invalid change action for " + sid)
    if not seen:
        raise ValueError("No sources configured.")
    return config["sources"]

def fetch(source, url=None, body=None):
    target = url or source["url"]
    parsed = urllib.parse.urlparse(target)
    if parsed.scheme != "https" or not parsed.hostname:
        raise SourceError("Only HTTPS sources are allowed.")
    allowed = {parsed.hostname.lower()}
    allowed.update(x.lower() for x in source.get("allowed_redirect_hosts", []))
    headers = {"User-Agent":USER_AGENT,"Accept":"application/json, application/atom+xml, application/xml, text/html;q=0.9, */*;q=0.5","Cache-Control":"no-cache"}
    if body is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(target, data=body, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            final = urllib.parse.urlparse(response.geturl())
            if final.scheme != "https" or not final.hostname or final.hostname.lower() not in allowed:
                raise SourceError("Redirected to an unapproved host.")
            data = response.read(MAX_BYTES + 1)
            if len(data) > MAX_BYTES:
                raise SourceError("Response exceeds 8 MiB safety limit.")
            meta = {"http_status":getattr(response,"status",200),"final_url":response.geturl(),
                    "content_type":response.headers.get("Content-Type",""),"etag":response.headers.get("ETag"),
                    "last_modified":response.headers.get("Last-Modified"),"bytes":len(data)}
            return data, meta
    except urllib.error.HTTPError as exc:
        raise SourceError("HTTP " + str(exc.code)) from exc
    except urllib.error.URLError as exc:
        raise SourceError("Network error: " + str(exc.reason)) from exc
    except TimeoutError as exc:
        raise SourceError("Request timed out.") from exc

def horizons_url(base):
    day = dt.datetime.now(dt.timezone.utc).date()
    params = {"format":"json","COMMAND":"'499'","OBJ_DATA":"'NO'","MAKE_EPHEM":"'YES'","EPHEM_TYPE":"'OBSERVER'",
              "CENTER":"'500@399'","START_TIME":f"'{day.isoformat()}'","STOP_TIME":f"'{(day+dt.timedelta(days=1)).isoformat()}'",
              "STEP_SIZE":"'1 d'","QUANTITIES":"'1,9,20,23,24,29'"}
    return base + "?" + urllib.parse.urlencode(params)

def parse_horizons(data):
    p = json.loads(data.decode("utf-8-sig"))
    sig, result = p.get("signature") or {}, p.get("result")
    if not sig.get("version") or not isinstance(result,str) or not result.strip() or p.get("error"):
        raise SourceError("Horizons signature/result validation failed.")
    return {"api_version":str(sig["version"]),"result_sha256":digest(result.encode()),"result_bytes":len(result.encode())}

def parse_atom(data):
    root = ET.fromstring(data)
    records = []
    for entry in root.findall("a:entry", ATOM):
        ident = (entry.findtext("a:id",default="",namespaces=ATOM) or "").strip()
        title = (entry.findtext("a:title",default="",namespaces=ATOM) or "").strip()
        published = (entry.findtext("a:published",default="",namespaces=ATOM) or "").strip()
        link = entry.find("a:link",ATOM)
        if ident:
            records.append({"id":ident,"title":title[:350],"published":published,
                            "url":link.attrib.get("href",ident) if link is not None else ident})
    return records

def parse_crossref(data):
    rows = (json.loads(data.decode("utf-8-sig")).get("message") or {}).get("items") or []
    records = []
    for row in rows:
        doi = str(row.get("DOI","")).strip().lower()
        title = row.get("title") or []
        date_parts = (row.get("published-print") or row.get("published-online") or {}).get("date-parts") or []
        if doi:
            records.append({"id":"https://doi.org/"+doi,"title":str(title[0])[:350] if title else "",
                            "published":"-".join(map(str,date_parts[0])) if date_parts else "",
                            "url":str(row.get("URL") or "https://doi.org/"+doi),
                            "publisher":str(row.get("publisher",""))[:180],"type":str(row.get("type",""))[:80]})
    return records

def parse_tap_count(payload):
    rows = payload if isinstance(payload,list) else payload.get("data",[]) if isinstance(payload,dict) else []
    if isinstance(rows,list) and rows and isinstance(rows[0],dict):
        for key,value in rows[0].items():
            if "count" in str(key).lower():
                return int(value)
    if isinstance(payload,dict):
        for key in ("count","COUNT","COUNT(*)","row_count"):
            if key in payload:
                return int(payload[key])
    raise SourceError("TAP output contains no recognizable COUNT field.")

def probe(source):
    kind = source["kind"]
    if kind == "horizons_probe":
        data,meta = fetch(source,horizons_url(source["url"]))
        info = parse_horizons(data)
        return {"status":"ok",**meta,**info},{"api_version":info["api_version"]}
    if kind == "mpc_probe":
        body = json.dumps({"list":"neos","limit":1,"order":"DESC"}).encode()
        data,meta = fetch(source,body=body)
        payload = json.loads(data.decode("utf-8-sig"))
        if not isinstance(payload.get("items"),list) or "request" not in payload:
            raise SourceError("MPC List API response shape changed.")
        return {"status":"ok",**meta,"sample_items":len(payload["items"])},{"probe":"ok"}
    data,meta = fetch(source)
    if kind == "page":
        value = digest(data)
        return {"status":"ok",**meta,"content_sha256":value},{"fingerprint":value}
    if kind == "tap_count":
        value = parse_tap_count(json.loads(data.decode("utf-8-sig")))
        return {"status":"ok",**meta,"row_count":value},{"row_count":value}
    if kind == "json_probe":
        payload = json.loads(data.decode("utf-8-sig"))
        if not isinstance(payload,(dict,list)):
            raise SourceError("JSON probe returned unexpected shape.")
        return {"status":"ok",**meta,"json_shape":"object" if isinstance(payload,dict) else "array"},{"probe":"ok"}
    if kind in {"atom_feed","crossref_feed"}:
        items = parse_atom(data) if kind == "atom_feed" else parse_crossref(data)
        if not items:
            raise SourceError("Literature feed returned no usable records.")
        return {"status":"ok",**meta,"items_seen":len(items),"latest":items[0]},{"items":items}
    raise SourceError("No adapter for " + kind)

def candidate(source, kind, previous, current, stamp):
    return {"candidate_id":source["id"]+"-"+stamp[:10],"status":"candidate_only","requires_human_approval":True,
            "source_watch_id":source["id"],"registered_source_id":source.get("registered_source_id"),
            "suggested_source_id":source.get("suggested_source_id"),"source_title":source["title"],
            "source_url":source["url"],"evidence_class":source["evidence_class"],"candidate_type":kind,
            "observed_at":stamp,"previous_observation":previous,"new_observation":current,"permitted_use":source["role"],
            "review_checklist":["Verify the canonical source, not a search snippet.",
            "Confirm publisher authority for this exact claim.","Check licence, citation and redistribution terms.",
            "Preserve units, uncertainty, epoch, time scale, frame, observer/centre and query settings.",
            "Assign the evidence class and record limitations.","Prepare original Persian and English summaries with equivalent scope.",
            "Run validators and inspect the diff before approval."],"promotion_blocked_until_review":True}

def changes(source, previous, current, stamp):
    if source["change_action"] == "health_only" or previous is None:
        return []
    kind = source["kind"]
    if kind == "page":
        old,new = previous.get("fingerprint"),current.get("fingerprint")
        return [candidate(source,"source_page_changed",old,new,stamp)] if old and new and old != new else []
    if kind == "tap_count":
        old,new = previous.get("row_count"),current.get("row_count")
        return [candidate(source,"dataset_metadata_changed",{"row_count":old},{"row_count":new},stamp)] if old is not None and new is not None and old != new else []
    if kind in {"atom_feed","crossref_feed"}:
        known = {x.get("id") for x in previous.get("items",[])}
        added = [x for x in current.get("items",[]) if x.get("id") not in known]
        return [candidate(source,"new_literature_metadata",{"known_items":len(known)},{"new_items":added[:30]},stamp)] if added else []
    return []

def run(config_path=DEFAULT_CONFIG,state_path=DEFAULT_STATE,candidate_dir=DEFAULT_CANDIDATES,report_path=DEFAULT_REPORT):
    config = read_json(config_path)
    if not isinstance(config,dict):
        raise ValueError("Configuration is not a JSON object.")
    sources = validate_config(config)
    state = read_json(state_path,{"schema_version":"1.0","sources":{}})
    if state.get("schema_version") != "1.0" or not isinstance(state.get("sources"),dict):
        raise ValueError("Invalid monitoring state schema.")
    stamp,records,files,failures = timestamp(),[],[],0
    for source in sources:
        try:
            summary,current = probe(source)
            previous = state["sources"].get(source["id"])
            found = changes(source,previous,current,stamp)
            paths = []
            for item in found:
                path = candidate_dir/(source["id"].lower()+"-"+stamp[:10]+"-"+item["candidate_type"]+".json")
                write_json(path,item)
                rel = str(path.relative_to(ROOT)).replace("\\","/")
                files.append(rel); paths.append(rel)
            state["sources"][source["id"]] = current
            records.append({"id":source["id"],"title":source["title"],**summary,"change_detected":bool(found),"candidate_files":paths})
        except Exception as exc:
            failures += 1
            records.append({"id":source["id"],"title":source["title"],"status":"error","error":str(exc)[:350],"change_detected":False})
    write_json(state_path,state)
    report = {"agent":"AstroLife Astronomy Knowledge Maintenance Agent","agent_version":"1.0.0","observed_at":stamp,
              "status":"ok" if failures == 0 else ("partial" if failures < len(sources) else "unavailable"),
              "source_count":len(sources),"successful_sources":len(sources)-failures,"failed_sources":failures,
              "candidate_count":len(files),"candidate_files":files,"source_results":records,
              "safety":{"corpus_modified":False,"release_manifest_modified":False,"ranker_retrained":False,
                        "automatic_approval":False,"user_data_collected":False,"third_party_source_text_copied":False},
              "next_step":"Verify candidates at their canonical source. Human approval is required before release changes."}
    write_json(report_path,report)
    return report

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config",type=Path,default=DEFAULT_CONFIG)
    parser.add_argument("--state",type=Path,default=DEFAULT_STATE)
    parser.add_argument("--candidate-dir",type=Path,default=DEFAULT_CANDIDATES)
    parser.add_argument("--report",type=Path,default=DEFAULT_REPORT)
    args = parser.parse_args()
    try:
        report = run(args.config,args.state,args.candidate_dir,args.report)
    except Exception as exc:
        print("MAINTENANCE_AGENT_FATAL: "+str(exc),file=sys.stderr)
        return 2
    print("Status: "+report["status"])
    print(f"Sources: {report['successful_sources']}/{report['source_count']} successful")
    print("Review candidates: "+str(report["candidate_count"]))
    print("Report: "+str(args.report))
    for item in report["source_results"]:
        line = item["id"]+": "+item["status"]
        if item.get("error"): line += " — "+item["error"]
        print(line)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
