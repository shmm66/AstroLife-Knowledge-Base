import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-11-09"

sources = [
    {
        "id": "CHANI_HOROSCOPE_STRUCTURE",
        "title": "CHANI — 2026 Sign-by-sign Horoscopes",
        "publisher": "CHANI",
        "url": "https://www.chani.com/this-year/horoscopes",
        "source_type": "practitioner_reference",
        "use": "Reference for sign-by-sign annual horoscope navigation and the distinction between Sun-sign and rising-sign readings. Used for structure only.",
        "rights_note": "No prose, illustrations or interpretations are copied. AstroLife cards contain original editorial synthesis.",
        "evidence_class": "editorial_method",
        "accessed_at": TODAY
    },
    {
        "id": "CHANI_LONG_TRANSIT_STORYLINES",
        "title": "CHANI — How to work with astrology on a daily basis",
        "publisher": "CHANI",
        "url": "https://www.chani.com/astro-education/how-to-work-with-astrology-on-a-daily-basis",
        "source_type": "practitioner_reference",
        "use": "Reference for explaining transits through houses and life areas, distinguishing short and long transit durations, and following longer storylines through time.",
        "rights_note": "Method and taxonomy reference only; no protected wording or app content is reused.",
        "evidence_class": "editorial_method",
        "accessed_at": TODAY
    },
    {
        "id": "CAFE_ASTROLOGY_MONTHLY_HOROSCOPES",
        "title": "Cafe Astrology — Monthly Horoscopes",
        "publisher": "Cafe Astrology",
        "url": "https://cafeastrology.com/monthlyhoroscopes.html",
        "source_type": "practitioner_reference",
        "use": "Reference for sign-by-sign forecast organisation and separating romance, career and general-life themes. Used to benchmark structure and readability.",
        "rights_note": "No article text, illustrations or interpretations are copied; all AstroLife prose is original.",
        "evidence_class": "editorial_method",
        "accessed_at": TODAY
    },
    {
        "id": "CAFE_ASTROLOGY_PLANETARY_OVERVIEW",
        "title": "Cafe Astrology — 2026 Planetary Overview",
        "publisher": "Cafe Astrology",
        "url": "https://cafeastrology.com/astrology-of-2026.html",
        "source_type": "practitioner_reference",
        "use": "Reference for the chronology of planetary ingresses, retrogrades and year-level event timelines. AstroLife uses its own calculated ephemeris and does not copy the site's dates or interpretations.",
        "rights_note": "Calendar structure only; no proprietary interpretations or images are reused.",
        "evidence_class": "editorial_method",
        "accessed_at": TODAY
    },
    {
        "id": "CAFE_ASTROLOGY_MONTHLY_TRANSIT_CALENDAR",
        "title": "Cafe Astrology — This Month in Astrology",
        "publisher": "Cafe Astrology",
        "url": "https://cafeastrology.com/thismonthinastrology.html",
        "source_type": "practitioner_reference",
        "use": "Reference for pairing a short narrative overview with a chronological planetary-event timeline and sign-by-sign summaries.",
        "rights_note": "Editorial structure only; all AstroLife content is independently authored.",
        "evidence_class": "editorial_method",
        "accessed_at": TODAY
    }
]

cards_fa = [
    ("editorial-method", "FORECAST_EDITORIAL_METHOD", "روش نگارش روایی هوروسکوپ", "تفسیر حرفه‌ای فقط نام سیاره را تکرار نمی‌کند؛ زمان، خانه و موضوع زندگی را به یک خط داستانی روشن وصل می‌کند.", "هر حوزه در دو لایه نوشته می‌شود. لایهٔ تخصصی، سیاره، نشان، خانهٔ خورشیدی و بازهٔ تاریخ را ثبت می‌کند. لایهٔ روایی، همان داده را به زبان روزمره به یک شروع، تغییر مسیر و جمع‌بندی تبدیل می‌کند. روایت باید کوتاه، اختصاصی همان گروه تولد و عاری از جمله‌های عمومی و تکراری باشد.", "کدام گذر، خط اصلی این حوزه را در سال می‌سازد؟", ["روایت","هوروسکوپ","نگارش","ویرایش"]),
    ("timing-story", "FORECAST_TIMING_STORY", "زمان‌بندی؛ از گذر تا نقطهٔ عطف", "سیارات کندرو پس‌زمینهٔ سال را می‌سازند؛ گذرهای کوتاه‌تر فصل‌ها، آغازها و تغییرات میان مسیر را مشخص می‌کنند.", "پنجره‌ها را ابتدا بر اساس تاریخ مرتب کن. گذر طولانی مشتری، زحل، اورانوس، نپتون یا پلوتو می‌تواند خط اصلی یک فصل را بسازد؛ عبورهای کوتاه‌تر خورشید، عطارد، زهره و مریخ نقطهٔ عطف یا خبر تازه را برجسته می‌کنند. اگر دو پنجره هم‌زمان‌اند، یکی را پس‌زمینه و دیگری را رویداد هم‌زمان معرفی کن؛ تاریخ و خانه را عوض نکن.", "کدام گذر زمینهٔ سال است و کدام گذر لحظهٔ تغییر را نشان می‌دهد؟", ["گذر","زمان‌بندی","خط زمانی","پیش‌بینی"]),
    ("relationships-story", "FORECAST_RELATIONSHIP_STORY", "روایت عشق و رابطه", "روایت رابطه باید از خواسته و صمیمیت به گفت‌وگوی تعیین‌کننده، تعهد یا بازتعریف مرزها حرکت کند.", "زهره را در ارتباط با جذب، آشتی و ارزش مشترک بخوان؛ مریخ را برای کشش، پیش‌قدمی و گفت‌وگوی عقب‌افتاده؛ مشتری را برای گسترش دایرهٔ آشنایی؛ زحل را برای تعهد و تعیین تکلیف. خانهٔ فعال مشخص می‌کند داستان بیشتر به عشق، شراکت یا اعتماد و منابع مشترک مربوط است. از نتیجه‌گیری یکسان برای همهٔ ماه‌ها پرهیز کن.", "این سال در رابطه‌ها با چه صحنه‌ای شروع می‌شود و در چه نقطه‌ای جدی‌تر می‌شود؟", ["عشق","روابط","زهره","مریخ","زحل"]),
    ("career-story", "FORECAST_CAREER_STORY", "روایت مسیر شغلی", "داستان شغلی باید حرکت از ایده و مذاکره به اجرا، دیده‌شدن یا تثبیت مسئولیت را روشن کند.", "عطارد را به خبر، قرارداد و مذاکره وصل کن؛ مریخ را به شروع و شتاب پروژه؛ خورشید را به دیده‌شدن و اعتبار؛ مشتری را به توسعه و مسئولیت تازه؛ زحل را به ساختار و جایگاه بلندمدت. خانهٔ فعال، تفاوت میان کار روزانه، مسیر حرفه‌ای و شبکه‌های همکار را مشخص می‌کند.", "کدام اتفاق یا بازه، مسیر کاری را از مرحلهٔ قبلی عبور می‌دهد؟", ["کار","شغل","مشتری","عطارد","خورشید"]),
    ("finance-story", "FORECAST_FINANCE_STORY", "روایت درآمد و منابع مالی", "روایت مالی باید میان درآمد شخصی، ارزش مهارت، قراردادها و منابع مشترک تفاوت بگذارد.", "زهره به ارزش‌گذاری و خرج‌های سلیقه‌ای، عطارد به مذاکره و قرارداد، مشتری به امکان گسترش منابع، زحل به تعهدها و هزینه‌های ثابت و پلوتو به بازآرایی منابع مشترک اشاره می‌کند. خانه‌های دوم، هشتم، دهم و یازدهم معنای دقیق‌تری به پنجره می‌دهند. روایت دربارهٔ مبلغ سود، زیان یا ثروت قطعی عددسازی نمی‌کند.", "کدام جریان درآمد یا تعهد مالی در این سال به مرکز داستان می‌آید؟", ["مالی","درآمد","منابع","قرارداد"]),
    ("family-story", "FORECAST_FAMILY_STORY", "روایت خانه و خانواده", "داستان خانه باید پیوند میان فضای خانه، نقش اعضای خانواده، ریشه‌ها و تغییر حس تعلق را نشان دهد.", "خانهٔ چهارم محور اصلی است. زهره فضای گرم‌تر و میل به زیباسازی خانه را برجسته می‌کند؛ زحل مسئولیت و نقش‌ها را؛ اورانوس تغییر محل یا روال؛ نپتون احساسات ناگفته را؛ پلوتو بازنگری الگوهای ریشه‌دار را. متن را به رفتار و حال‌وهوای قابل‌فهم تبدیل کن، نه فهرست اصطلاحات.", "در فضای خانه چه چیزی تغییر می‌کند و کدام نقش دوباره تعریف می‌شود؟", ["خانواده","خانه","ریشه","تعلق"]),
    ("wellbeing-story", "FORECAST_WELLBEING_STORY", "روایت تندرستی و سبک زندگی", "این روایت بر ریتم روزانه، انرژی، عادت‌ها، خواب و تعادل فعالیت و بازیابی تمرکز می‌کند.", "خورشید را به اولویت و انرژی روزانه، مریخ را به سرعت و فعالیت، زحل را به نظم پایدار، نپتون را به خلوت و استراحت و اورانوس را به تغییر عادت‌ها وصل کن. هر تفسیر باید به خانه و بازهٔ واقعی متصل باشد. از ساختن تشخیص، بیماری یا زمان ابتلا خودداری کن؛ روایت را دربارهٔ سبک زندگی نگه دار.", "ریتم روزانه در کدام بازه تغییر می‌کند و چه عادتی به موضوع اصلی بدل می‌شود؟", ["سلامت","تندرستی","سبک‌زندگی","عادت"]),
    ("growth-story", "FORECAST_GROWTH_STORY", "روایت یادگیری و رشد", "روایت رشد باید مسیر تبدیل یک کنجکاوی به مهارت، سفر، تجربه یا جهان‌بینی تازه را بازسازی کند.", "عطارد را برای مطالعه و گفت‌وگو، مشتری را برای آموزش و افق‌های گسترده‌تر، زحل را برای مهارت عمیق و بلندمدت، اورانوس را برای مسیر غیرمنتظره و نپتون یا پلوتو را برای پژوهش و دگرگونی فکری به کار ببر. خانهٔ سوم، نهم و یازدهم نشان می‌دهند تغییر از یادگیری، سفر یا شبکه‌ها می‌آید.", "کدام علاقه در این سال از یک فکر به مسیر واقعی رشد تبدیل می‌شود؟", ["یادگیری","رشد","آموزش","سفر"])
]

cards_en = [
    ("editorial-method", "FORECAST_EDITORIAL_METHOD", "The narrative horoscope method", "A strong forecast does more than name a planet; it connects timing, house and life topic into a clear storyline.", "Write every life area in two layers. The technical layer records the planet, sign, solar house and date window. The narrative layer translates the same evidence into an opening situation, a turning point and a memorable close. Keep the prose concise, cohort-specific and free of generic repeated lines.", "Which transit gives this area its central storyline for the year?", ["storytelling","horoscope","writing","editorial"]),
    ("timing-story", "FORECAST_TIMING_STORY", "Timing: from transit to turning point", "Slow-moving planets create the year's background; faster transits mark chapters, beginnings and turning points.", "Sort windows chronologically. Longer Jupiter, Saturn, Uranus, Neptune or Pluto periods can establish the main chapter; shorter Sun, Mercury, Venus and Mars periods can mark a turning point or new development. When windows overlap, describe one as the background and the other as the concurrent event. Preserve the supplied dates and houses.", "Which transit sets the background, and which one marks the shift?", ["transits","timing","timeline","forecast"]),
    ("relationships-story", "FORECAST_RELATIONSHIP_STORY", "The relationship storyline", "A relationship forecast should move from attraction and intimacy to a defining conversation, commitment or a new boundary.", "Read Venus through attraction, reconnection and shared values; Mars through chemistry, initiative and delayed conversations; Jupiter through a wider social circle; Saturn through commitment and definition. The active house tells whether the story concerns romance, partnership, trust or shared resources. Avoid giving every birth-month cohort the same storyline.", "What scene opens the relationship story, and when does it become more serious?", ["love","relationships","venus","mars","saturn"]),
    ("career-story", "FORECAST_CAREER_STORY", "The career storyline", "A career forecast should make the movement from idea and negotiation toward execution, visibility or lasting responsibility clear.", "Connect Mercury with news, contracts and negotiation; Mars with starts and project momentum; the Sun with visibility and recognition; Jupiter with expansion and broader responsibility; Saturn with structure and a lasting role. The active house distinguishes daily work, professional direction and collaborative networks.", "Which period moves the career story into its next chapter?", ["career","work","jupiter","mercury","sun"]),
    ("finance-story", "FORECAST_FINANCE_STORY", "The money and resources storyline", "A financial reading should distinguish personal income, the value of skills, contracts and shared resources.", "Venus can describe pricing and discretionary spending; Mercury, negotiations and agreements; Jupiter, the possibility of broader resources; Saturn, obligations and fixed costs; Pluto, restructuring shared resources. Houses two, eight, ten and eleven refine the topic. Do not invent amounts, guaranteed profit or guaranteed loss.", "Which income stream or financial commitment becomes central to the year's story?", ["finance","income","resources","contracts"]),
    ("family-story", "FORECAST_FAMILY_STORY", "The home and family storyline", "A home forecast should connect the household atmosphere, family roles, roots and a changing sense of belonging.", "The fourth house is the central frame. Venus can warm the home atmosphere; Saturn can clarify responsibilities; Uranus can signal a change of place or routine; Neptune can bring unspoken feelings forward; Pluto can reopen entrenched family patterns. Translate these into recognisable life themes rather than a list of jargon.", "What changes at home, and which role is being redefined?", ["family","home","roots","belonging"]),
    ("wellbeing-story", "FORECAST_WELLBEING_STORY", "The wellbeing and lifestyle storyline", "Keep this storyline focused on daily rhythm, energy, habits, sleep and the balance between activity and recovery.", "Use the Sun for personal priorities and daily energy, Mars for pace and activity, Saturn for sustainable routines, Neptune for quiet and rest, and Uranus for changing habits. Tie every reading to the actual house and date window. Do not invent a diagnosis, illness or onset date; keep the narrative about lifestyle.", "Which period changes the daily rhythm, and which habit becomes central?", ["wellbeing","health","lifestyle","habits"]),
    ("growth-story", "FORECAST_GROWTH_STORY", "The learning and growth storyline", "A growth forecast should trace how curiosity becomes a skill, journey, experience or a changed worldview.", "Use Mercury for study and conversation, Jupiter for education and wider horizons, Saturn for deep long-term mastery, Uranus for an unexpected path, and Neptune or Pluto for research and intellectual transformation. Houses three, nine and eleven show whether the development comes through learning, travel or networks.", "Which interest moves from an idea into a real path of growth this year?", ["learning","growth","education","travel"])
]

def make_card(lang, row):
    slug, entity, title, brief, expanded, question, tags = row
    sources_for_method = ["ASTROLIFE_ORIGINAL_CURATION", "CHANI_HOROSCOPE_STRUCTURE", "CHANI_LONG_TRANSIT_STORYLINES", "CAFE_ASTROLOGY_MONTHLY_HOROSCOPES", "CAFE_ASTROLOGY_PLANETARY_OVERVIEW"]
    if slug == "timing-story":
        sources_for_method = ["ASTROLIFE_ORIGINAL_CURATION", "CHANI_LONG_TRANSIT_STORYLINES", "CAFE_ASTROLOGY_PLANETARY_OVERVIEW", "CAFE_ASTROLOGY_MONTHLY_TRANSIT_CALENDAR"]
    return {
        "id": f"{lang}.forecast.{slug}",
        "revision": 1,
        "language": lang,
        "topic": ["forecast", "editorial-method", "narrative"],
        "entity_type": "technique",
        "entity": entity,
        "title": title,
        "brief": brief,
        "expanded": expanded,
        "reflection_question": question,
        "evidence_class": "editorial_method",
        "source_ids": sources_for_method,
        "source_note": "Original AstroLife editorial framework informed by comparison of practitioner structures; no external forecast prose or images are reproduced.",
        "tags": tags,
        "limitations": ["Editorial guidance for interpreting symbolic astrology; it is not evidence that planetary positions predict events."],
        "license": "CC-BY-4.0",
        "status": "reviewed",
        "updated_at": TODAY
    }

def append_jsonl(path, rows):
    existing = [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    ids = {row["id"] for row in existing}
    for row in rows:
        if row["id"] in ids:
            raise SystemExit(f"Card already exists: {row['id']}")
        existing.append(row)
        ids.add(row["id"])
    path.write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in existing), encoding="utf-8")

for lang, rows in (("fa", cards_fa), ("en", cards_en)):
    target = ROOT / "data" / lang / "core.jsonl"
    append_jsonl(target, [make_card(lang, row) for row in rows])

source_path = ROOT / "sources" / "sources.json"
registry = json.loads(source_path.read_text(encoding="utf-8-sig"))
known = {item["id"] for item in registry["sources"]}
for source in sources:
    if source["id"] not in known:
        registry["sources"].append(source)
source_path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print("Added 8 Persian and 8 English editorial/storytelling cards.")
print("Added 5 international practitioner references.")
print("Per-language card counts:", sum(1 for _ in (ROOT / "data/fa/core.jsonl").open(encoding="utf-8")), sum(1 for _ in (ROOT / "data/en/core.jsonl").open(encoding="utf-8")))
print("Registered sources:", len(registry["sources"]))
