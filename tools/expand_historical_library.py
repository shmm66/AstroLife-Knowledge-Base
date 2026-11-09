import json
from pathlib import Path
from datetime import date

ROOT = Path(r"C:\Users\Hajix\Documents\GitHub\AstroLife-Pro-src\knowledge-base")
TODAY = date.today().isoformat()

sources = [
 {"id":"MESOPOTAMIAN_ASTROLOGY_MONROE","title":"Mesopotamian astrology","publisher":"M. Willis Monroe, University of British Columbia / Wiley","url":"https://doi.org/10.1111/rec3.12318","source_type":"peer_reviewed_historical_reference","use":"Scholarly overview of the emergence and institutional practice of celestial divination in the ancient Near East.","rights_note":"Original summary only; no protected article text reproduced.","evidence_class":"historical_tradition","accessed_at":TODAY},
 {"id":"MESOPOTAMIAN_CELESTIAL_SPACE_BROWN","title":"The Cuneiform Conception of Celestial Space and Time","publisher":"David Brown, Cambridge Archaeological Journal","url":"https://doi.org/10.1017/S0959774300000044","source_type":"peer_reviewed_historical_research","use":"Context for Babylonian celestial terminology, astronomy, omen traditions and later transmission.","rights_note":"Bibliographic reference and original summary only.","evidence_class":"historical_tradition","accessed_at":TODAY},
 {"id":"PTOLEMY_TETRABIBLOS_LOEB","title":"Ptolemy, Tetrabiblos (Loeb Classical Library translation)","publisher":"Harvard University Press / Loeb Classical Library","url":"https://doi.org/10.4159/dlcl.ptolemy-tetrabiblos.1940","source_type":"primary_text_translation","use":"Historical source for Hellenistic astrology; Book I distinguishes astronomical calculation from less certain astrological inference, while Books II–IV cover general and individual topics.","rights_note":"Do not reproduce protected translation; original summaries and bibliographic references only.","evidence_class":"historical_tradition","accessed_at":TODAY},
 {"id":"ABUMASHAR_IRANICA","title":"Abū Maʿšar (Albumasar)","publisher":"Encyclopaedia Iranica, article by David Pingree","url":"https://www.iranicaonline.org/articles/abu-masar-jafar-b/","source_type":"scholarly_reference","use":"Biographical and transmission context for Abū Maʿšar and the Greek, Indian, Sasanian, Syrian and Arabic sources he synthesized.","rights_note":"Original summary only.","evidence_class":"historical_tradition","accessed_at":TODAY},
 {"id":"ABUMASHAR_MORGAN_MANUSCRIPT","title":"Astrological Treatises, MS M.785","publisher":"The Morgan Library & Museum","url":"https://www.themorgan.org/manuscript/144038","source_type":"illuminated_manuscript_catalogue","use":"Evidence for the illustrated Latin abridgement of Abū Maʿšar and the medieval manuscript tradition; the catalogue notes the linguistic transmission question.","rights_note":"Catalogue metadata only; manuscript images remain subject to the holding institution's terms.","evidence_class":"historical_tradition","accessed_at":TODAY},
 {"id":"BIRUNI_TAFHIM_UNESCO","title":"Al-Tafhīm li-Awāʾil Ṣināʿat al-Tanjīm","publisher":"UNESCO Memory of the World","url":"https://www.unesco.org/en/memory-world/al-tafhim-li-awail-sanaat-al-tanjim","source_type":"manuscript_heritage_catalogue","use":"Documents al-Bīrūnī's Persian and Arabic instructional work in question-and-answer form for learners of mathematics and astrology.","rights_note":"Original summary and catalogue facts only.","evidence_class":"historical_tradition","accessed_at":TODAY},
 {"id":"BIRUNI_TAFHIM_ISMI","title":"Kitāb al-tafhīm (Persian and Arabic manuscript records)","publisher":"Institute for the History of Science / Max Planck Society, ISMI","url":"https://ismi.mpiwg-berlin.mpg.de/node/3939387","source_type":"manuscript_bibliographic_record","use":"Language and bibliographic metadata for the Persian and Arabic versions of al-Bīrūnī's text.","rights_note":"Metadata and original summary only.","evidence_class":"historical_tradition","accessed_at":TODAY},
 {"id":"HEBREW_ASTROLOGY_LEICHT","title":"Toward a History of Hebrew Astrological Literature","publisher":"Reimund Leicht, Cambridge University Press, Science in Medieval Jewish Cultures","url":"https://doi.org/10.1017/CBO9780511976575.018","source_type":"peer_reviewed_historical_reference","use":"Bibliographic survey of medieval Jewish astrological writing and the differing positions of Jewish intellectual authorities.","rights_note":"Original summary only; no chapter text reproduced.","evidence_class":"historical_tradition","accessed_at":TODAY},
 {"id":"IBN_EZRA_CAMBRIDGE","title":"Astronomy and Astrology in the Works of Abraham ibn Ezra","publisher":"Bernard R. Goldstein, Cambridge University Press","url":"https://doi.org/10.1017/S095742390800052X","source_type":"peer_reviewed_historical_research","use":"Context for Ibn Ezra's Hebrew scientific works and the transmission of Arabic astronomy and astrology into Latin and Hebrew scholarship.","rights_note":"Original summary only.","evidence_class":"historical_tradition","accessed_at":TODAY},
 {"id":"JYOTISHA_SANSKRIT_DOCUMENTS","title":"Jyotiṣa Sanskrit text collection","publisher":"Sanskrit Documents","url":"https://sanskritdocuments.org/sanskrit/jyotisha/","source_type":"primary_text_index","use":"Index to Sanskrit text witnesses and public digital editions including Bṛhajjātaka and other Jyotiṣa works; individual editions require provenance checks.","rights_note":"Check rights and edition notes for each linked text; do not assume all scans or translations share one licence.","evidence_class":"historical_tradition","accessed_at":TODAY},
 {"id":"VARAHAMIHIRA_BRIHAT_SAMHITA_WELLCOME","title":"The Bṛihat Saṃhitā of Varāhamihira (1884–1885 translation)","publisher":"Wellcome Collection","url":"https://wellcomecollection.org/works/hzaaf9ak","source_type":"public_domain_historical_translation","use":"Digitized historical English translation and bibliographic record for Varāhamihira's encyclopaedic Sanskrit work.","rights_note":"Wellcome lists the item as Public Domain Mark; verify the status of any separately reused scan or derivative.","evidence_class":"historical_tradition","accessed_at":TODAY},
 {"id":"MAYA_DRESDEN_SLUB","title":"The Dresden Maya Codex: content and astronomical tables","publisher":"Saxon State and University Library Dresden (SLUB)","url":"https://www.slub-dresden.de/en/explore/manuscripts/the-dresden-maya-codex/content","source_type":"manuscript_catalogue_and_interpretation","use":"Catalogue and scholarly institutional explanation of the Dresden Codex Venus and eclipse tables.","rights_note":"Original summary; manuscript images are not copied.","evidence_class":"historical_tradition","accessed_at":TODAY},
 {"id":"MAYA_DRESDEN_LOC","title":"The Dresden Codex","publisher":"Library of Congress","url":"https://www.loc.gov/item/2021667917/","source_type":"manuscript_catalogue","use":"Bibliographic description of the codex, its 39 leaves, Venus calculations, eclipse material and ritual calendars.","rights_note":"Catalogue metadata and original summary only.","evidence_class":"historical_tradition","accessed_at":TODAY},
 {"id":"MAYA_CODICES_SMITHSONIAN","title":"Astronomy in the Maya Codices","publisher":"Harvey M. Bricker and Victoria R. Bricker, Smithsonian Institution","url":"https://www.si.edu/object/astronomy-maya-codices-harvey-m-bricker-and-victoria-r-bricker:siris_sil_1063950","source_type":"scholarly_monograph_catalogue","use":"Scholarly reference on Maya calendrical cycles, Venus, eclipses, planetary and seasonal astronomy in the codices.","rights_note":"Bibliographic reference and original summary only.","evidence_class":"historical_tradition","accessed_at":TODAY},
 {"id":"MAYA_ECLIPSE_TABLE_RESEARCH","title":"The design and reconstructible history of the Mayan eclipse table of the Dresden Codex","publisher":"Proceedings of the National Academy of Sciences / PubMed Central","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC13141895/","source_type":"peer_reviewed_astronomical_history","use":"Research on the 405-lunation structure and historical reconstruction of the Dresden Codex eclipse table; this concerns eclipse prediction, not a Western natal zodiac.","rights_note":"Original summary only; check final publication metadata and version before citing in a formal edition.","evidence_class":"historical_tradition","accessed_at":TODAY}
]

pairs = [
("history.mesopotamia.celestial","MESOPOTAMIAN_CELESTIAL",
 ["MESOPOTAMIAN_ASTROLOGY_MONROE","MESOPOTAMIAN_CELESTIAL_SPACE_BROWN"],
 "رصد آسمان و فالِ بابلی دو لایهٔ مرتبط اما یکسان نبودند",
 "Observation and omen in Mesopotamia were related but distinct",
 ["history","mesopotamia","babylonian","astronomy","omens"],
 "در بین‌النهرین، کاتبان و اخترشناسان پدیده‌های آسمانی را ثبت می‌کردند و در کنار آن، مجموعه‌هایی از نشانه‌ها و تعبیرهای فال‌گونه نیز وجود داشت. متن‌های رصدی و دفترهای نجومی را نباید با فهرست‌های فال یکی گرفت؛ یکی می‌تواند دادهٔ مشاهده باشد و دیگری چارچوب تفسیر تاریخی.",
 "این سنت برای فهم خاستگاه تاریخیِ پیوند آسمان و پیش‌آگاهی اهمیت دارد. در کتابخانهٔ AstroLife، دادهٔ نجومی، گزارش تاریخی و تعبیر نمادین جدا برچسب می‌خورند تا یک مشاهده به‌اشتباه «اثبات پیشگویی» معرفی نشود.",
 "کدام بخش یک متن کهن گزارش مشاهده است و کدام بخش تعبیر فرهنگی آن؟",
 "Mesopotamian scholars recorded celestial phenomena and also maintained collections of omens and their interpretations. Observational diaries and mathematical astronomical texts should not be conflated with omen catalogues: one may preserve observations, while the other records a historical interpretive framework.",
 "This tradition is important for the history of celestial divination. AstroLife keeps astronomical data, historical testimony and symbolic interpretation in separate evidence layers so an observation is never presented as proof of a prediction.",
 "Which part of an ancient record is an observation, and which part is its cultural interpretation?"),
("history.ptolemy.tetrabiblos","PTOLEMY_TETRABIBLOS",
 ["PTOLEMY_TETRABIBLOS_LOEB","PAL_PTOLEMY_TETRABIBLOS"],
 "بطلمیوس میان محاسبهٔ نجومی و داوری طالع‌بینانه فرق می‌گذاشت",
 "Ptolemy distinguished astronomical calculation from astrological judgement",
 ["history","greek","latin","ptolemy","tetrabiblos"],
 "در تترابیبلوس، بطلمیوس میان شناخت حرکت‌ها و نسبت‌های آسمانی از یک سو، و نتیجه‌گیری دربارهٔ اثر آن‌ها بر امور زمینی از سوی دیگر فرق می‌گذارد. او روش دوم را کم‌قطعیت‌تر و وابسته به قضاوت می‌داند. کتاب دوم به موضوع‌های عمومی و کتاب‌های سوم و چهارم به زایش و چارت فردی می‌پردازند.",
 "برای گزارش خوب، این تفکیک هنوز مفید است: جایگاه سیاره باید از محاسبه بیاید؛ معنای آن باید به‌عنوان خوانش تاریخی یا نمادین معرفی شود، نه نتیجهٔ اندازه‌گیری علمی.",
 "در این گزارش کدام جمله دادهٔ محاسبه‌شده است و کدام جمله تفسیر سنتی؟",
 "In the Tetrabiblos, Ptolemy distinguishes the study of celestial motions and configurations from judgements about their effects on earthly affairs. He treats the latter as less certain and dependent on judgement. Book II addresses general or mundane topics, while Books III–IV discuss individual nativities.",
 "This distinction remains useful for responsible reporting: planetary positions come from calculation; their meanings are labelled as historical or symbolic readings, not as scientific measurements.",
 "Which sentence in a report is a calculated fact, and which is an interpretation?"),
("history.abumashar.introduction","ABU_MASHAR",
 ["ABUMASHAR_IRANICA","ABUMASHAR_MORGAN_MANUSCRIPT"],
 "ابومعشر سنت‌های یونانی، هندی و ایرانی را در بغداد به هم پیوند داد",
 "Abū Maʿshar synthesized Greek, Indian and Iranian traditions in Baghdad",
 ["history","arabic","persian","abu-mashar","translation"],
 "ابومعشر بلخی در محیط علمی بغداد از چند میراث فکری، از جمله یونانی، هندی، ساسانی، سریانی و عربی پیشااسلامی بهره گرفت. «مدخل کبیر» او در جهان اسلامی و سپس در ترجمه‌های بیزانسی و لاتین اثرگذار شد. نسخهٔ مصور لاتینِ مورگان، یک تلخیص و مرحله‌ای از تاریخ انتقال متن است، نه نسخهٔ مؤلف.",
 "در کتابخانه، آموزه‌های منسوب به ابومعشر باید با نام اثر، زبان متن، نسخه یا ترجمه و مسیر انتقال ثبت شوند. یک تصویر قرون‌وسطایی را نباید شاهدی از متن اصلی عربی یا فارسی فرض کرد.",
 "آیا این برداشت از متن عربی، ترجمهٔ لاتین یا شرح متأخر گرفته شده است؟",
 "Abū Maʿshar al-Balkhī drew on several intellectual traditions active in Abbasid Baghdad, including Greek, Indian, Sasanian, Syriac and pre-Islamic Arabic materials. His Great Introduction became influential in the Islamic world and through later Byzantine and Latin translations. The Morgan illuminated Latin manuscript is an abridgement and witness to transmission, not the author's autograph.",
 "AstroLife records the work title, language, manuscript or translation, and transmission route. A medieval illustration is not treated as direct evidence for the wording of the original Arabic or Persian text.",
 "Is this interpretation taken from an Arabic text, a Latin translation, or a later commentary?"),
("history.biruni.tafhim","AL_BIRUNI_TAFHIM",
 ["BIRUNI_TAFHIM_UNESCO","BIRUNI_TAFHIM_ISMI"],
 "التفهیم بیرونی؛ آموزش نجوم و احکام نجوم به زبان فارسی و عربی",
 "Al-Bīrūnī's al-Tafhīm: astronomy and astrology taught in Persian and Arabic",
 ["history","persian","arabic","biruni","tafhīm"],
 "ابوریحان بیرونی «التفهیم» را با ساختار پرسش‌وپاسخ و برای فهم آسان‌ترِ دانش‌آموزان نوشت؛ نسخه‌های فارسی و عربی آن شناخته شده‌اند. ارزش این اثر فقط در احکام نجومی نیست: واژگان، ریاضیات، شناخت آسمان و شیوهٔ آموزش را نیز در بر می‌گیرد.",
 "این اثر برای طراحی توضیح‌های سادهٔ برنامه الگوی زبانی خوبی است: نخست اصطلاح را تعریف کن، سپس با مثال توضیح بده و بعد روشن کن کدام بخش اندازه‌گیری است و کدام بخش باور تاریخی.",
 "اگر کاربر هیچ اصطلاحی نداند، این مفهوم را چگونه در سه جمله توضیح می‌دهید؟",
 "Abū Rayḥān al-Bīrūnī wrote al-Tafhīm in an accessible question-and-answer format for learners. Persian and Arabic versions are documented. The work is valuable beyond astrological judgements: it also covers terminology, mathematics, the sky and methods of instruction.",
 "The text offers a useful model for plain-language explanations: define a term, demonstrate it with an example, and then identify which part is measurement and which part is historical belief.",
 "How would you explain this concept in three sentences to a reader with no prior terminology?"),
("history.hebrew.ibn-ezra","HEBREW_ASTROLOGY",
 ["HEBREW_ASTROLOGY_LEICHT","IBN_EZRA_CAMBRIDGE"],
 "دانش نجوم و احکام نجوم در نوشته‌های عبری قرون میانه",
 "Astronomy and astrology in medieval Hebrew scholarship",
 ["history","hebrew","ibn-ezra","medieval-jewish","translation"],
 "در قرون میانه، بخشی از دانش نجوم و احکام نجوم از مسیر عربی به عبری ترجمه و بازپردازی شد. ابراهیم بن عزرا از مهم‌ترین ناقلان این میراث بود و نوشته‌هایش میان نجوم محاسباتی و تفسیر احکامی رفت‌وآمد دارند. متفکران یهودی دربارهٔ اعتبار و حدود احکام نجوم هم‌نظر نبودند.",
 "نباید از «سنت عبری» یک نظام یگانه و مستقل ساخت. هر متن باید با مؤلف، زبان، دوره، منابع پیشین و دیدگاه انتقادی همان نویسنده معرفی شود.",
 "این آموزه در چه دوره‌ای نوشته شده و از چه زبان یا سنتی اثر پذیرفته است؟",
 "In the medieval period, some astronomical and astrological knowledge was translated and recast from Arabic into Hebrew. Abraham ibn Ezra was a major transmitter, and his writings move between mathematical astronomy and astrological interpretation. Jewish intellectuals did not hold one uniform view about the authority or limits of astrology.",
 "AstroLife should not invent a single, isolated 'Hebrew system'. Each text is identified by author, language, period, earlier sources and the author's own critical position.",
 "When was this doctrine written, and which language or tradition influenced it?"),
("history.jyotisha.classical","JYOTISHA",
 ["JYOTISHA_SANSKRIT_DOCUMENTS","VARAHAMIHIRA_BRIHAT_SAMHITA_WELLCOME"],
 "جوتیش؛ سنت هندی با متون و قواعد خاص خود",
 "Jyotiṣa: an Indian tradition with its own texts and methods",
 ["history","jyotisha","sanskrit","varahamihira","india"],
 "جوتیش یک سنت واحد و ساده نیست. متونی مانند بریهات‌جاتکهٔ ورهامی‌هیره و بریهات‌سامهیتا در کنار سنت‌های متأخرترِ هورا، نظام‌های نشان، سیاره، خانه، ناکشاترا، دَشا و تقسیمات چارت را در صورت‌بندی‌های متفاوت به کار می‌برند. تاریخ تدوین برخی متون منسوب به پاراشره محل بحث است و نسخهٔ رایج را نباید بی‌بررسی به دوران باستان نسبت داد.",
 "برای محاسبهٔ جوتیش باید روش سیدریال، آیانامشا و قواعد همان مکتب صریحاً ثبت شود. جایگاه‌های تروپیکالِ گزارش غربی را نمی‌توان بی‌تبدیل، خروجی جوتیش نامید.",
 "این گزارش از کدام آیانامشا و کدام نسخه یا مکتب جوتیش استفاده می‌کند؟",
 "Jyotiṣa is not one simple or static system. Texts such as Varāhamihira's Bṛhajjātaka and Bṛhat Saṃhitā sit alongside later Hora traditions using signs, grahas, houses, nakṣatras, daśā systems and divisional charts in different formulations. The dating and textual layers of works attributed to Parāśara are debated; a later received text should not automatically be labelled ancient.",
 "A Jyotiṣa calculation must declare its sidereal framework, ayanāṃśa and school-specific rules. Tropical positions from a Western report cannot be relabelled as Jyotiṣa without conversion and method documentation.",
 "Which ayanāṃśa, edition and Jyotiṣa school does this report use?"),
("history.maya.dresden.venus","MAYA_DRESDEN_VENUS",
 ["MAYA_DRESDEN_SLUB","MAYA_DRESDEN_LOC","MAYA_CODICES_SMITHSONIAN"],
 "کدکس درسدن و چرخهٔ ۵۸۴روزهٔ ونوس",
 "The Dresden Codex and the 584-day Venus cycle",
 ["history","maya","mesoamerica","dresden-codex","venus"],
 "در صفحات جدول ونوسِ کدکس درسدن، چرخهٔ تقریباً ۵۸۴روزهٔ ونوس و بازگشت‌های آن در بازه‌ای بلند ثبت شده است. این جدول با تقویم و آیین‌های مایا پیوند داشت و در کنار عددها، تصویرها و نشانه‌های آیینی نیز دیده می‌شود. این سنت را نباید به طالع‌بینی ۱۲ نشان غربی تبدیل کرد.",
 "در نرم‌افزار، دادهٔ مایا باید در ماژول تقویم و نجوم تاریخی خودش بماند: چرخهٔ ونوس، روزشماری و متن‌های آیینی؛ نه اینکه به‌زور خانه‌های دوازده‌گانهٔ چارت شخصی بگیرد.",
 "چرخهٔ ونوس در این منبع یک محاسبهٔ تقویمی است یا یک ادعای مربوط به سرنوشت فرد؟",
 "The Dresden Codex Venus tables record the approximately 584-day cycle of Venus and its repetitions over long periods. The tables are tied to Maya calendrics and ritual contexts, alongside numbers, images and ceremonial signs. They should not be converted into a Western twelve-sign horoscope.",
 "In software, Maya data belongs in its own historical astronomy and calendrics module: Venus cycles, day counts and ritual texts, rather than being forced into twelve personal horoscope houses.",
 "Is this Venus cycle a calendrical calculation or a claim about an individual's fate?"),
("history.maya.dresden.eclipse","MAYA_DRESDEN_ECLIPSE",
 ["MAYA_DRESDEN_SLUB","MAYA_DRESDEN_LOC","MAYA_ECLIPSE_TABLE_RESEARCH"],
 "جدول کسوف مایا؛ پیش‌بینی نجومی در چارچوب تقویمی",
 "Maya eclipse tables: astronomical prediction within a calendrical framework",
 ["history","maya","eclipse","dresden-codex","astronomy"],
 "کدکس درسدن جدولی برای بازه‌های امکان وقوع کسوف خورشید و ماه دارد. پژوهش جدید دربارهٔ ساختار ۴۰۵ ماه قمری و شیوهٔ بازسازی تاریخچهٔ جدول بحث می‌کند. این نمونه نشان‌دهندهٔ مهارت محاسباتی و تقویمی است؛ به‌خودی‌خود گواه پیش‌بینی علمی رویدادهای شخصی نیست.",
 "عامل دانش باید «پیش‌بینی کسوف» را از «پیشگویی زندگی فرد» جدا کند. اولی مسئله‌ای نجومی و قابل آزمون است؛ دومی ادعای متفاوتی است و به شواهد مستقل نیاز دارد.",
 "چه چیزی در این جدول با محاسبه آزمون‌پذیر است و چه چیزی تفسیر فرهنگی آن است؟",
 "The Dresden Codex contains tables for intervals in which solar and lunar eclipses may occur. Recent research discusses the 405-lunation structure and the reconstruction of the table's history. This is evidence of calendrical and computational skill, not evidence that personal life events can be predicted.",
 "The knowledge agent must separate an eclipse prediction from a prediction about an individual's life. The former is an astronomical claim that can be tested; the latter is a different claim requiring independent evidence.",
 "Which part of this table can be tested by calculation, and which part is cultural interpretation?"),
("history.latin.fendulus.manuscript","LATIN_ABUMASHAR_MANUSCRIPT",
 ["ABUMASHAR_MORGAN_MANUSCRIPT","ABUMASHAR_IRANICA"],
 "از متن عربی تا نسخهٔ مصور لاتین",
 "From an Arabic treatise to an illuminated Latin manuscript",
 ["history","latin","manuscript","abu-mashar","translation"],
 "نسخهٔ مورگان M.785 که در یا پیش از ۱۴۰۳ میلادی در بروژ نوشته و آراسته شده، تلخیصی مصور از مقدمهٔ ابومعشر است. فندولوس مدعی ترجمه از فارسی است، اما چون ابومعشر به عربی می‌نوشت، احتمالِ استفاده از ترجمهٔ لاتین پیشین مطرح شده است. این نمونه مسیر پیچیدهٔ انتقال دانش را نشان می‌دهد.",
 "عامل باید میان اثر مؤلف، ترجمه، تلخیص و نسخهٔ تصویری فرق بگذارد. نقاشی‌های زیبا برای تاریخ هنر و فهم دریافت قرون‌وسطایی ارزشمندند، اما جای مقابلهٔ متن نسخه‌ها را نمی‌گیرند.",
 "منبع مورد استفاده اصل اثر است، ترجمه است یا نسخهٔ مصورِ تلخیص‌شده؟",
 "Morgan MS M.785, written and illuminated in Bruges in or before 1403, is an illustrated abridgement of Abū Maʿshar's Introduction. Fendulus says he translated from Persian, but because Abū Maʿshar wrote in Arabic, scholars note the possibility that an earlier Latin translation was used. The case reveals a complex transmission history.",
 "The agent distinguishes an author's work, a translation, an abridgement and an illuminated copy. The images are valuable for art history and medieval reception, but they do not replace textual comparison.",
 "Is the cited source the author's original, a translation, or an illustrated abridgement?"),
("method.cross-cultural.integrity","CROSS_CULTURAL_METHOD",
 ["MESOPOTAMIAN_ASTROLOGY_MONROE","PTOLEMY_TETRABIBLOS_LOEB","BIRUNI_TAFHIM_UNESCO","HEBREW_ASTROLOGY_LEICHT","JYOTISHA_SANSKRIT_DOCUMENTS","MAYA_DRESDEN_SLUB"],
 "چندتمدنی‌بودن یعنی احترام به تفاوت روش‌ها",
 "Cross-cultural work means respecting differences between methods",
 ["history","methodology","comparative","sources","traditions"],
 "بابلی، یونانی، عربی‌ـ‌فارسی، عبری، جوتیش هندی و مایا در زبان، تقویم، ریاضیات، ابزار و هدف یکسان نیستند. بعضی منابع برای رصد و محاسبه‌اند، بعضی برای فال یا تفسیر، و بعضی هر دو لایه را کنار هم دارند. مقایسهٔ درست باید تفاوت‌ها را نشان دهد، نه اینکه همه را به یک زودیاک امروزی فروبکاهد.",
 "در هر کارت کتابخانه، سنت، دوره، زبان، نسخه، نوع ادعا و سطح شواهد ثبت می‌شود. اگر روش محاسبه با سیستم گزارش یکی نیست، آن منبع فقط زمینهٔ تاریخی می‌دهد و وارد محاسبه نمی‌شود.",
 "آیا این منبع واقعاً از همان سیستم محاسباتی گزارش پشتیبانی می‌کند؟",
 "Babylonian, Greek, Arabic–Persian, Hebrew, Indian Jyotiṣa and Maya traditions do not share one language, calendar, mathematical framework or purpose. Some records concern observation and calculation, some concern divination or interpretation, and some preserve both. A sound comparison makes the differences visible instead of collapsing them into a modern zodiac.",
 "Every library card records tradition, period, language, edition, claim type and evidence level. If a historical source uses a different calculation system, it provides context only and is not silently inserted into the report's calculations.",
 "Does this source actually support the calculation system used in this report?")
]

def make_card(item, lang):
    (base, entity, src, title_fa, title_en, tags, brief_fa, exp_fa, q_fa, brief_en, exp_en, q_en) = item
    return {
      "id":f"{lang}.{base}",
      "revision":1,
      "language":lang,
      "topic":["history","traditions","methodology"],
      "entity_type":"method",
      "entity":entity,
      "title":title_fa if lang=="fa" else title_en,
      "brief":brief_fa if lang=="fa" else brief_en,
      "expanded":exp_fa if lang=="fa" else exp_en,
      "reflection_question":q_fa if lang=="fa" else q_en,
      "evidence_class":"historical_tradition",
      "source_ids":src,
      "source_note":("خلاصهٔ تألیفی بر پایهٔ منابع ثبت‌شده؛ ادعای اثبات تجربیِ طالع‌بینی نیست." if lang=="fa" else "Original summary based on registered sources; this is not empirical validation of astrology."),
      "tags":tags + (["فارسی","تاریخ"] if lang=="fa" else ["English","history"]),
      "related_ids":[],
      "limitations":["Historical doctrine is not proof of predictive validity.","Do not merge calculation rules from different traditions without an explicit, documented conversion."],
      "license":"CC-BY-4.0",
      "status":"reviewed",
      "updated_at":TODAY
    }

def main():
    source_path=ROOT/"sources"/"sources.json"
    src_doc=json.loads(source_path.read_text(encoding="utf-8-sig"))
    known={s["id"] for s in src_doc["sources"]}
    for s in sources:
        if s["id"] not in known:
            src_doc["sources"].append(s)
    source_path.write_text(json.dumps(src_doc,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

    ids={}
    for lang in ("fa","en"):
        path=ROOT/"data"/lang/"core.jsonl"
        rows=[json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
        existing={r["id"] for r in rows}
        new=[]
        for item in pairs:
            card=make_card(item,lang)
            if card["id"] not in existing:
                new.append(card)
                ids[(lang,item[0])]=card["id"]
        with path.open("a",encoding="utf-8",newline="\n") as f:
            for card in new:
                f.write(json.dumps(card,ensure_ascii=False,separators=(",",":"))+"\n")
        print(f"{lang}: appended {len(new)} historical cards; total {len(rows)+len(new)}")

    # Add grouped bilingual retrieval judgements so the local ranker learns how to route cross-cultural research queries.
    labels_path=ROOT/"training"/"seed-labels.jsonl"
    labels=[json.loads(x) for x in labels_path.read_text(encoding="utf-8-sig").splitlines() if x.strip()]
    existing={(x.get("query_group"),x.get("language"),x.get("entry_id")) for x in labels}
    groups=[
      ("mesopotamia","تاریخ طالع‌بینی بابلی، لوح‌های میخی و دفترهای رصد نجومی","Babylonian omen texts, cuneiform astronomy and observational diaries","history.mesopotamia.celestial"),
      ("ptolemy","تترابیبلوس بطلمیوس و تفاوت نجوم محاسباتی با داوری احکامی","Ptolemy Tetrabiblos and the distinction between astronomy and astrological judgement","history.ptolemy.tetrabiblos"),
      ("abumashar","ابومعشر بلخی و مقدمه کبیر، انتقال دانش یونانی و هندی","Abu Mashar Great Introduction and transmission of Greek and Indian learning","history.abumashar.introduction"),
      ("biruni","کتاب التفهیم بیرونی به فارسی و عربی و آموزش نجوم","Al-Biruni Al-Tafhim in Persian and Arabic, teaching astronomy","history.biruni.tafhim"),
      ("hebrew","ابراهیم بن عزرا و تاریخ احکام نجوم در متون عبری","Abraham ibn Ezra and the history of astrology in Hebrew texts","history.hebrew.ibn-ezra"),
      ("jyotisha","جوتیش هندی، متون سانسکریت، ورهامی‌هیره و پاراشره","Indian Jyotisha, Sanskrit texts, Varahamihira and Parashara","history.jyotisha.classical"),
      ("maya_venus","جدول ونوس ۵۸۴ روزه در کدکس درسدن مایا","The 584-day Venus table in the Maya Dresden Codex","history.maya.dresden.venus"),
      ("maya_eclipse","جدول کسوف مایا و چرخه ۴۰۵ ماه قمری","Maya eclipse table and the 405-lunation cycle","history.maya.dresden.eclipse"),
      ("latin_manuscript","نسخه مصور لاتین ابومعشر مورگان فندولوس","The Morgan Fendulus illuminated Latin manuscript of Abu Mashar","history.latin.fendulus.manuscript"),
      ("cross_cultural","مقایسه تمدن‌ها بدون ادغام روش‌های نجومی و طالع‌بینی","Compare ancient traditions without conflating their calculation methods","method.cross-cultural.integrity")
    ]
    for slug,qfa,qen,base in groups:
        for lang,q in (("fa",qfa),("en",qen)):
            topic="history"
            relevant_id=f"{lang}.{base}"
            # A second adjacent card is positive only where it genuinely supports the same research question.
            second={
              "mesopotamia":f"{lang}.history.ptolemy.tetrabiblos",
              "ptolemy":f"{lang}.history.latin.fendulus.manuscript",
              "abumashar":f"{lang}.history.biruni.tafhim",
              "biruni":f"{lang}.history.abumashar.introduction",
              "hebrew":f"{lang}.method.cross-cultural.integrity",
              "jyotisha":f"{lang}.history.hebrew.ibn-ezra",
              "maya_venus":f"{lang}.history.maya.dresden.eclipse",
              "maya_eclipse":f"{lang}.history.maya.dresden.venus",
              "latin_manuscript":f"{lang}.history.abumashar.introduction",
              "cross_cultural":f"{lang}.history.mesopotamia.celestial"
            }[slug]
            negative={
              "mesopotamia":f"{lang}.history.maya.dresden.venus",
              "ptolemy":f"{lang}.history.maya.dresden.eclipse",
              "abumashar":f"{lang}.history.jyotisha.classical",
              "biruni":f"{lang}.history.maya.dresden.venus",
              "hebrew":f"{lang}.history.maya.dresden.venus",
              "jyotisha":f"{lang}.history.maya.dresden.eclipse",
              "maya_venus":f"{lang}.history.ptolemy.tetrabiblos",
              "maya_eclipse":f"{lang}.history.jyotisha.classical",
              "latin_manuscript":f"{lang}.history.maya.dresden.eclipse",
              "cross_cultural":f"{lang}.planet.sun"
            }[slug]
            for eid,rel in ((relevant_id,1),(second,1),(negative,0)):
                key=(slug,lang,eid)
                if key not in existing:
                    labels.append({"query_group":slug,"query":q,"language":lang,"topic":topic,"entry_id":eid,"relevant":rel})
                    existing.add(key)
    with labels_path.open("w",encoding="utf-8",newline="\n") as f:
        for row in labels:
            f.write(json.dumps(row,ensure_ascii=False,separators=(",",":"))+"\n")

    # Release metadata
    readme=ROOT/"README.md"
    text=readme.read_text(encoding="utf-8")
    text=text.replace("**Release:** 0.2.2","**Release:** 0.2.3")
    text=text.replace("**Curated corpus:** 136 reviewed seed cards — 68 Persian and 68 English","**Curated corpus:** 156 reviewed seed cards — 78 Persian and 78 English")
    text=text.replace("**Registered sources:** 25","**Registered sources:** 40")
    note="""

## Historical traditions expansion (0.2.3)
The corpus now includes bilingual, source-linked editorial cards for Mesopotamian celestial divination; Ptolemy's distinction between astronomical calculation and astrological judgement; Abū Maʿshar's transmission history; al-Bīrūnī's Persian/Arabic *al-Tafhīm*; medieval Hebrew scholarship and Abraham ibn Ezra; Jyotiṣa and Varāhamihira; and the Maya Dresden Codex Venus and eclipse tables. These traditions are documented separately rather than collapsed into a single modern zodiac. The local relevance ranker receives ten new bilingual query families; its metrics still measure retrieval relevance only.
"""
    if "Historical traditions expansion (0.2.3)" not in text:
        text += note
    readme.write_text(text,encoding="utf-8")

    release=ROOT/"RELEASE-NOTES-0.2.3.md"
    release.write_text("""# AstroLife Knowledge Base 0.2.3

- Added 20 bilingual, reviewed historical-research cards across Mesopotamian, Greek/Latin, Arabic-Persian, Hebrew, Jyotisha and Maya materials.
- Registered 15 additional institutional, manuscript, primary-text and peer-reviewed sources.
- Added 10 bilingual grouped query families (60 judgements) for cross-cultural retrieval training.
- All entries are original summaries; protected source text and manuscript images are not reproduced.
- Distinguishes astronomical measurements, historical doctrine, symbolic interpretation and empirical research.
- Explicitly prevents medical diagnosis, deterministic personal outcomes and silent merging of different cultural calculation systems.
""",encoding="utf-8")
    # Update manifest version constant.
    build=ROOT/"tools"/"build_manifest.py"
    bs=build.read_text(encoding="utf-8")
    bs=bs.replace('VERSION = "0.2.2"','VERSION = "0.2.3"')
    build.write_text(bs,encoding="utf-8")
    print(f"New sources: {len(sources)}; total sources: {len(src_doc['sources'])}")
    print(f"New grouped labels: {len(labels)} total")

if __name__=="__main__":
    main()
