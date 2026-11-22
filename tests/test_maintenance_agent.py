from __future__ import annotations
import importlib.util, json, tempfile, unittest
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "maintenance" / "agent.py"
SPEC = importlib.util.spec_from_file_location("astrolife_maintenance_agent", PATH)
agent = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(agent)

class AgentTests(unittest.TestCase):
    def test_source_registry_is_valid(self):
        cfg = agent.read_json(agent.DEFAULT_CONFIG)
        items = agent.validate_config(cfg)
        self.assertGreaterEqual(len(items), 10)
        self.assertEqual(len({x["id"] for x in items}), len(items))

    def test_rejects_http_sources(self):
        cfg = {"schema_version":"1.0","sources":[{"id":"BAD","kind":"page","url":"http://bad.test","title":"bad","role":"test","change_action":"human_review"}]}
        with self.assertRaises(ValueError): agent.validate_config(cfg)

    def test_horizons_signature_required(self):
        good = b'{"signature":{"version":"1.3"},"result":"valid"}'
        self.assertEqual(agent.parse_horizons(good)["api_version"],"1.3")
        with self.assertRaises(Exception): agent.parse_horizons(b'{"result":"missing signature"}')

    def test_atom_feed_excludes_abstract(self):
        xml = b'<feed xmlns="http://www.w3.org/2005/Atom"><entry><id>https://arxiv.org/abs/2601.00001</id><title>Orbital dynamics</title><published>2026-01-01</published><link href="https://arxiv.org/abs/2601.00001"/><summary>Not retained</summary></entry></feed>'
        item = agent.parse_atom(xml)[0]
        self.assertNotIn("summary",item)
        self.assertEqual(item["title"],"Orbital dynamics")

    def test_crossref_excludes_abstract(self):
        raw = json.dumps({"message":{"items":[{"DOI":"10.1234/test","title":["Astrology study"],"abstract":"not retained","URL":"https://doi.org/10.1234/test"}]}}).encode()
        item = agent.parse_crossref(raw)[0]
        self.assertNotIn("abstract",item)
        self.assertEqual(item["id"],"https://doi.org/10.1234/test")

    def test_first_observation_is_baseline(self):
        src = {"id":"TEST","kind":"page","title":"Test","url":"https://example.org","evidence_class":"astronomical_measurement","change_action":"human_review","role":"Test"}
        self.assertEqual(agent.changes(src,None,{"fingerprint":"x"},"2026-11-22T00:00:00Z"),[])

    def test_page_change_requires_human_approval(self):
        src = {"id":"TEST","kind":"page","title":"Test","url":"https://example.org","evidence_class":"astronomical_measurement","change_action":"human_review","role":"Test"}
        item = agent.changes(src,{"fingerprint":"old"},{"fingerprint":"new"},"2026-11-22T00:00:00Z")[0]
        self.assertEqual(item["status"],"candidate_only")
        self.assertTrue(item["requires_human_approval"])
        self.assertTrue(item["promotion_blocked_until_review"])

    def test_health_probe_does_not_create_candidate(self):
        src = {"id":"TEST","kind":"horizons_probe","title":"Test","url":"https://example.org","evidence_class":"astronomical_measurement","change_action":"health_only","role":"Test"}
        self.assertEqual(agent.changes(src,{"api_version":"1.2"},{"api_version":"1.3"},"2026-11-22T00:00:00Z"),[])

    def test_tap_count_change_is_metadata_candidate(self):
        src = {"id":"TEST","kind":"tap_count","title":"Test","url":"https://example.org","suggested_source_id":"ARCHIVE","evidence_class":"astronomical_measurement","change_action":"dataset_candidate","role":"Test"}
        item = agent.changes(src,{"row_count":10},{"row_count":11},"2026-11-22T00:00:00Z")[0]
        self.assertEqual(item["candidate_type"],"dataset_metadata_changed")

    def test_run_writes_state_without_touching_release_payload(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cfg = {"schema_version":"1.0","sources":[{"id":"TEST","title":"Test","kind":"page","url":"https://example.org","evidence_class":"astronomical_measurement","change_action":"human_review","role":"Test"}]}
            config = root/"sources.json"
            config.write_text(json.dumps(cfg),encoding="utf-8")
            original = agent.fetch
            agent.fetch = lambda source,url=None,body=None: (b"stable page",{"http_status":200,"final_url":source["url"],"bytes":12})
            try: report = agent.run(config,root/"state.json",root/"candidates",root/"report.json")
            finally: agent.fetch = original
            self.assertEqual(report["candidate_count"],0)
            self.assertFalse(report["safety"]["corpus_modified"])
            self.assertFalse(report["safety"]["release_manifest_modified"])
            self.assertTrue((root/"state.json").is_file())

if __name__ == "__main__":
    unittest.main()
