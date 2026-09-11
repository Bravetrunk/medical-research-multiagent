# Full Extracted Knowledge Base from Notion



## Topic 1: Healthcare Landscape (ID: 3cc0abc4-4cc7-8186-9c9e-dcf650a84538)

1. The Data-Driven Healthcare Landscape

Mock Test (Concept-Based) — Session 1

Mock Test 2 — Case Vignettes (Session 1)

Mock Test 3 — ถูก/ผิด จับผิดเหตุผล (Session 1)

Mock Test 4 — Transfer & Design (Session 1)

Mock Test #2 — Spot the Flaw (Session 1)

Mock Test #3 — Integrated Case: CKD Program (Session 1)

Mock Test #4 — Concept Discrimination (Session 1)

Foundations_of_Data_Analytics_in_a_Healthcare_Context_compressed.pdf


#### 🧠 1) Healthcare data analytics คืออะไร

- การใช้วิธีทั้ง quantitative และ qualitative อย่างเป็นระบบ เพื่อวิเคราะห์ข้อมูลทางการแพทย์จากหลายแหล่ง
- เป้าหมาย: การตัดสินใจที่อิงข้อมูล (data-driven) และอิงหลักฐาน (evidence-based)
- จุดเฉพาะ: ข้อมูลทางการแพทย์ ซับซ้อน อ่อนไว และ ผลกระทบชีวิต

#### 🧩 2) Interdisciplinary Mandate

ต้องทำงานหลายสาขาพร้อมกัน

```
flowchart LR
  M["🩺 Medicine<br>pathway / physiology / workflow"] --> A["Healthcare Analytics"]
  S["📊 Statistics + Math"] --> A
  C["💻 Computing<br>EHR / cloud / sensors / ML"] --> A
```

- Medicine / Clinical domain — พยาธิวิทยา, เส้นทางคลินิก, workflow โรงพยาบาล
- Statistics and Mathematics
- Computing and Technology — EHR, cloud, sensors + algorithm (ML, Optimization)

#### 📜 3) บทเรียนประวัติศาสตร์

```
flowchart LR
  A["📥 เก็บข้อมูล"] --> B["🔍 วิเคราะห์ + สื่อสาร"]
  B --> C["✅ แทรกที่ชัดเจน"]
```


#### 🌍 4) ระบบนิเวศข้อมูลสุขภาพ

```
flowchart TB
  EHR["📋 EHR<br>structured + notes"] --> ECO["Healthcare Data Ecosystem"]
  CLAIM["💰 Claims / Admin<br>cost, LOS, utilization"] --> ECO
  PGD["⌚ PGD<br>wearable / app / PRO"] --> ECO
  IMG["🧬 Imaging + Signals<br>MRI CT ECG EEG"] --> ECO
  OMICS["🧬 Omics<br>genome / proteome"] --> ECO
  SDOH["🌍 SDOH<br>PM2.5 / เศรษฐกิจ"] --> ECO
```


##### 📋 Electronic Health Records (EHRs)

- คลังข้อมูลทางคลินิกที่ละเอียดที่สุด — longitudinal history ทั้งระดับบุคคลและประชากร
- Structured: ข้อมูลประชากร, lab, การวินิจฉัย, ยา
- Unstructured: clinical notes, operative notes, transcribed reports, SOAP (เช่น chest pain 7/10), โน้ตลายมือ, ผล ultrasound
- วิวัฒนาการ: Paper → Basics EHR → Modern EHR → Future EHR

##### 💰 Administrative and Claims Data

- การเงิน / ต้นทุน / ราคา (แยก Price vs Cost)
- Master data: เตียง, ยา, รายการ
- ใช้วิเคราะห์ utilization, ต้นทุน, ประสิทธิภาพ (เช่น length of stay)
- ตัวอย่างตาราง billing: En_HN, เพศ, วันที่ชำระ, ประเภทผู้ป่วย, product code/name/type (LAB, SUPPLY), จำนวน, ค่า

##### ⌚ Patient-Generated Data (PGD)

- Wearable (หัวใจ, การนอน), mobile health apps, Patient-reported outcomes (PROs)
- สำคัญสำหรับ ติดตามโรคเรื้อรังต่อเนื่อง (ความดัน, น้ำตาล)

##### 🧬 Imaging, Signals, Omics, SDOH

- Imaging / signals: MRI, CT, X-ray, ECG, EEG, vital-sign monitors — volume สูง มีมิติสูง ต้องประมวลผลเฉพาะ
- Omics: high-throughput sequencing — อ่าน DNA หลายพันล้านฐานต่อวัน → ต้อง bioinformatics (จับลำดับ, หา variant, โครงกับ clinical outcome)
- SDOH: รวมข้อมูลคลินิกกับสังคมเศรษฐกิจ / คุณภาพอากาศ (เช่น PM2.5, ไฟป่า) — ตัวอย่างแผนที่ประเทศไทย
- แหล่งอื่น: genome/patient registries, private/government claims, pharmacy claims, mobile/wearables

#### ⚡ 5) ลักษณะและสิ่งท้าทายของข้อมูล


##### 5 Vs

สไลด์ยังแสดง 8 Vs เพิ่ม: Value, Visualisation, Viscosity, Virality


##### Structured vs Unstructured

```
pie title สัดส่วนข้อมูลองค์กร
  "Structured ~20%" : 20
  "Unstructured ~80%" : 80
```

- Structured ~20%: แถว/คอลัมน์ จัดการง่าย ใช้พื้นที่น้อย
- Unstructured ~80%: ภาพ เสียง วิดีโอ อีเมล ข้อความ — เติบโตรวดตั้งแต่ปี 2000

##### 🛡️ กฎหมายสหรัฐ

- HITECH Act 2009: แรงจูงใจให้รับ EHR กว้าง → ดิจิทัลบันทึกช่วง 2010s
- HIPAA: Privacy Rule (ความลับ) + Security Rule (บริหาร / กายภาพ / เทคนิค) + Breach Notification Rule (แจ้ง OCR + ผู้ป่วย + สื่อ ถ้ารัวใหญ่)
- ตัวอย่างการละเมิด: unencrypted data, unauthorized access, data theft, disclosure, weak security, poor training, improper disposal, breach delay

#### 🎯 6) คุณภาพข้อมูลและมาตรฐาน


#### 📈 7) 5 Analytical Disciplines + Maturity

```
flowchart LR
  D["1 Descriptive<br>What happened?"] --> G["2 Diagnostic<br>Why did it happen?"]
  G --> P["3 Predictive<br>What will happen?"]
  P --> R["4 Prescriptive<br>What should we do?"]
  R --> C["5 Discovery<br>What don't I know?"]
```

จาก reactive / hindsight → proactive → AI / ML / self-learning


#### 📊 Descriptive — เกิดอะไรขึ้น?


#### 🔍 Diagnostic — ทำไมจึงเกิด?


#### 🔮 Predictive — จะเกิดอะไร?


#### 🧠 Prescriptive — ควรทำอะไร?


#### 🔬 Discovery — รูปแบบใหม่ที่ซ่อนอยู่?


#### 🏥 8) หกโดเมนการใช้งาน

```
flowchart TB
  A["Healthcare Analytics"] --> B["🏥 Hospital Operations"]
  A --> C["🧠 Clinical Decision-Making"]
  A --> D["🧬 Biomedical Research"]
  A --> E["🌍 Public Health"]
  A --> F["🛡️ Quality and Safety"]
  A --> G["🔗 Informatics Infra"]
```


#### 🏥 8.1 Hospital Operations


#### 🧠 8.2 Clinical Decision-Making / CDSS


#### 🧬 8.3–8.6 โดเมนอื่น


#### ⭐ 9) จุดที่ต้องจำ


#### 🧠 10) คำ / สูตร / ตัวเลขที่น่าจด

📋 Mock Test 2 (Case-Based) — Session 1

⚖️ Mock Test 3 (จับผิดและให้เหตุผล) — Session 1

🧩 Mock Test 4 (จับคู่ · เรียงลำดับ · ออกแบบ) — Session 1


#### 🏥 Case 1 — ห้องฉุกเฉินแออัดช่วงหัวค่ำ

1.1 (MCQ) โดยเฉลี่ยมีผู้ป่วยอยู่ในระบบ ER กี่คน

- (ก) 3.6
- (ข) 6.0
- (ค) 8.0
- (ง) 10.7
💡 เฉลย 1.1

1.2 (สั้น) ก่อนอนุมัติเพิ่มแพทย์ ควรตรวจสอบอะไรก่อน 3 อย่าง และแต่ละอย่างตอบคำถามอะไร

💡 แนวคำตอบ 1.2

1.3 (สั้น) สมมติว่าเพิ่มแพทย์แล้วเวลารอไม่ลดเลย อธิบายสาเหตุที่เป็นไปได้ 2 ข้อ โดยใช้แนวคิดเชิงคิว

💡 แนวคำตอบ 1.3


#### 🧠 Case 2 — โมเดลเตือนภาวะทรุดในหอผู้ป่วย

2.1 (MCQ) ตัวเลข 80% สะท้อนปัญหาหลักข้อใด

- (ก) โมเดลมี AUC ต่ำเกินไป
- (ข) การนำไปใช้ใน workflow ล้มเหลว — alert มีผลตอบแทนต่ำ จนเกิด alert fatigue
- (ค) ข้อมูลมี velocity สูงเกิน
- (ง) ต้องเปลี่ยนไปใช้ deep learning
💡 เฉลย 2.1

2.2 (สั้น) อธิบายว่าทำไมกลุ่มที่เจาะเลือดน้อยจึงแทบไม่เคยถูกเตือน และนี่คืออคติชนิดใด อันตรายต่อใครมากที่สุด

💡 แนวคำตอบ 2.2

2.3 (สั้น) นอกจาก AUC ควรวัดอะไรเพิ่มอีก 3 อย่างก่อนสรุปว่าโมเดลนี้ “ใช้ได้”

💡 แนวคำตอบ 2.3


#### 🔗 Case 3 — ควบรวมข้อมูล 3 โรงพยาบาลในเครือ

3.1 (MCQ) ปัญหาหลักตรงกับมิติคุณภาพข้อมูลข้อใดมากที่สุด

- (ก) Accuracy
- (ข) Completeness
- (ค) Consistency
- (ง) Timeliness
💡 เฉลย 3.1

3.2 (สั้น) ควรใช้มาตรฐานใดกับส่วนไหน และเพราะเหตุใดการมี FHIR อย่างเดียวจึงไม่พอ

💡 แนวคำตอบ 3.2

3.3 (สั้น) การวินิจฉัยที่เก็บเป็น free text — มีทางเลือกอะไรบ้างในการทำให้ใช้งานได้ และแต่ละทางมีความเสี่ยงอะไร

💡 แนวคำตอบ 3.3


#### 🌍 Case 4 — ควบคุมความดันไม่ได้ในบางตำบล

4.1 (MCQ) ก้าวถัดไปที่เหมาะสมที่สุดคือระดับใด

- (ก) Descriptive — ทำแดชบอร์ดเทียบทุกตำบลเพิ่ม
- (ข) Diagnostic — หาว่าอะไรคือตัวที่อธิบายความต่างที่เหลือหลังคุมปัจจัยที่รู้แล้ว
- (ค) Predictive — สร้างโมเดลทำนายว่าใครจะคุมไม่ได้
- (ง) Prescriptive — สั่งเพิ่มยาในตำบลนั้นทันที
💡 เฉลย 4.1

4.2 (สั้น) ควรเชื่อมข้อมูลชุดใดเข้ามา และคาดว่าจะเห็นอะไร — ตอบโดยระบุอย่างน้อย 3 แหล่ง

💡 แนวคำตอบ 4.2

4.3 (สั้น) ถ้าจะเสนอ intervention ระดับ prescriptive ต้องมีอะไรมากกว่าผลทำนาย และต้องระวังอะไรเรื่องความเป็นธรรม

💡 แนวคำตอบ 4.3


#### 🎯 สิ่งที่ชุดนี้ฝึกต่างจากชุดอื่น

คุณภาพข้อมูล (ครบถ้วน / ถูกต้อง / มาตรฐาน) เป็นเงื่อนไข — messy / biased data ทำให้ผลวิเคราะห์คลาดเคลื่อน

Garbage In, Garbage Out — ข้อมูลเลอหรือ biased → analytics ผิด

คุณภาพ 4 ตัว: Accuracy / Completeness / Consistency / Timeliness

สรุปข้อมูลอดีต, คำนวณ KPI, situational awareness

เครื่องมือ: aggregation, summary statistics, dashboards

หา correlation / สาเหตุของรูปแบบ — เช่น root cause medication error, comorbidity กับแทรกซ้อนศัลยกรรม

```
flowchart LR
  E["1 Extract<br>event log HIS/ERP"] --> R["2 Reconstruct"]
  R --> V["3 Visualize<br>as-is"]
  V --> A["4 Analyze<br>bottleneck / RPA"]
```

Process mining keys: Process discovery · Root-cause · Conformance checking (ตรง SOP) · Opportunity identification (RPA) · Process optimization

ตัวอย่างจริง: ไหล OPD (กิอสก์ → วัดชีพจร → แพทย์ → เภสัช) · timeline ยา (P80 จาก submit ถึงจ่ายเสร็จ)

Expectation = เส้นทางตรง vs Reality = เส้นทางจริงยุ่งเหยิง

forecast, risk stratification, anticipate needs

ตัวอย่าง: ความเต็มโรงพยาบาล, 30-day readmission risk

บทบาท: Data Scientist vs Analyst vs Engineer (ทักษะต่างกัน)

ตัวอย่างทำนายเวลาบริการรวม — feature สำคัญ: มียาใหม่, queue number, เวลากิอสก์ก่อนนัด, ชื่อคลินิก, เวลานัด, วันในสัปดาห์, จำนวนผู้ป่วย, late time

แนะนำการตัดสินใจที่เหมาะสม จาก predictive + domain rules

ตัวอย่าง: แผนการรักษาส่วนบุคคล, จัดตารางบุคคลให้ตรงภาระที่คาด, Decision Support System

แผน 3 เฟส OPD / wait time

- Phase 1 (เดือน 1–3): audit timestamp, process discovery, patient feedback, Fast-track คดง่าย, real-time dashboard / command center, ปรับกิอสก์
- Phase 2 (เดือน 3–6): เพิ่มข้อมูลประชากร / acuity, NLP จาก free-text HIS, ฝึกอบรม, Random Forest ทำนาย wait time
- Phase 3 (เดือน 6–12): จำลอง DES/ABM, ออกแผนทางดูแลพลาย, ลงมือแทรกจุด
exploratory / data mining ไม่เริ่มจาก hypothesis

ตัวอย่าง: หา genetic marker ใหม่ / drug repurposing · cluster ผู้ป่วยเป็นกลุ่มโรคที่ยังไม่รู้จัก

flow ผู้ป่วย · utilization · scheduling · efficiency

ถ้าไม่ดี: ช้าการรักษา, staff/ผู้ป่วยหงุดหงิด, ต้นทุนเพิ่ม

Queuing theory — variability สูง, supply ≠ demand → congestion

Lean + analytics ช่วยวัด bottleneck และตัดสินใจ real-time

```
flowchart LR
  ARR["Arrivals λ"] --> WAIT["Waiting area L"]
  WAIT --> SRV["Service node μ"]
  SRV --> DEP["Departures"]
```

Nurse rostering — ข้อจำกัด: จำนวนการเวรกสูงสุด/ต่ำสุด, วันทำติด/วันหยุดติด, เสาร์ติด, จำนวนเสาร์ใน 4 สัปดาห์, หลังเวรกกลางคืนต้องพัก, ชิฟต์เดียวกันทั้ง weekend, unwanted patterns

วิธีแก้: Heuristics, Meta-heuristics, Hyper-heuristics, Mathematical Optimisation, Matheuristics, Hybrid (survey NRP 2012–2021)

Bailey–Welch rule (The Lancet, 1952)

- OPD ผู้ป่วยรอนาน (มัก >1 ชั่วโมง) เพราะกลัวไม่ให้แพทย์ว่าง
- ปัจจัย: punctuality + consulting time — ผู้ป่วยส่วนใหญ่มาก่อน
- หลัก: นัดผู้ป่วยมากั่นน้อยที่ต้น (มัก 2 คน) เพื่อลด idle time แพทย์ แต่ไม่ให้คิวยาว
Health IT ให้ knowledge + ข้อมูลเฉพาะบุคคล ใน workflow (แจ้ง / guideline / diagnostic support)

สิ่งท้าทายการนำไปใช้

- Workflow: stand-alone ต้องกรอกข้อมูลซ้ำ → adoption ต่ำ
- Explainability gap → ต้อง XAI
- Alert fatigue: แจ้งมาก yield ต่ำ → เพิกเฉยแจ้งสำคัญ
การใช้งาน

- ทำนายความเสื่อม (sepsis, respiratory failure, cardiac arrest) จาก EHR + vital → แทรกทันที, ลดการตาย/LOS ใน ICU
- Cleveland Clinic: NLP+ML กับคำสั่งยา → real-time alert → ลด adverse drug event (สไลด์มีการอ้างอิงเอกสารที่ 43 ต้องตรวจว่าเกี่ยวข้อหรือไม่)
Risk models

- CHA2DS2-VASc ความเสี่ยงสตโรก: score 0 = 0.2%/year … score 9 = 12.2%/year
```
xychart-beta
    title "C-statistic ตัวอย่าง 10 ปี"
    x-axis ["Logistic", "BayesNet", "TANB", "EBM", "XGBoost"]
    y-axis "C-stat" 0.75 --> 0.92
    bar [0.80, 0.80, 0.83, 0.87, 0.89]
```

C-statistic: Logistic 0.80 · Bayesian network 0.80 · Tree-augmented Naïve Bayes 0.83 · Explainable boosting 0.87 · XGBoost 0.89 — แม่นไม่เท่ากับความอธิบาย

Risk of the risk model — ต้องรู้ข้อจำกัดของแต่ละมอเดล / ใช้ผิด context

8.3 Biomedical research — computing power สูง + data sharing / collaborative analytics

8.4 Public health — ระดับประชากร: เฝ้าระวังโรค, outbreak detection, epidemiological modeling, forecast

- scenario: “ถ้าวัคซีน 70%?” “ถ้ามี variant ใหม่?”
- ข้อมูลใหม่: social media, web search, mobile mobility, satellite imagery
8.5 Quality and safety — IOM 1999 To Err is Human: ชาวอเมริกันหลายพันคนตายจาก medical error ทุกปี

- ตัวอย่าง CDSS ให้เลือด
- LLM-as-a-judge: “Augmentation rhinoplasty” → code 2185, score 0.004211, judge YES 3:0
8.6 Informatics infra

```
flowchart LR
  EHR["EHR"] --> HL7["HL7"]
  HL7 --> FHIR["FHIR 🔥"]
```

FHIR = มาตรฐานแลกเปลี่ยนข้อมูลทางคลินิกให้ระบบต่างๆ คุยกันได้

- ข้อมูลสุขภาพซับซ้อน อ่อนไว ชีวิต — คุณภาพข้อมูลมาก่อนแม่ลง
- ต้องทำงานหลายสาขา: แพทย์ + สถิติ + computing
- แหล่งข้อมูลกว้าง: EHR, claims, PGD, imaging/signals, omics, SDOH
- มาตรฐาน: ICD, CPT, LOINC, SNOMED CT + HL7/FHIR + HIPAA/HITECH
- 5 ระดับ analytics: Descriptive → Diagnostic → Predictive → Prescriptive → Discovery
- Operations: process mining, Little’s Law, Bailey–Welch, nurse rostering, simulation
- CDSS 2 ประเภท + adoption, alert fatigue, XAI, bias
- เป้าหมายสุดท้าย: วิเคราะห์เพื่อ แทรกที่ชัดเจนและยุติธรรม ไม่ใช่สร้าง dashboard
KPI OPD จริง: อัตราการส่งตรวจพ่วง BUN + Creatinine

วัตถุประสงค์: ลดการส่งที่ไม่จำเป็น

สูตร: (จำนวนส่งพ่วง) / (จำนวนส่ง BUN+Cr ทั้งหมด) × 100%

เป้าหมาย: < 40% · ประเมินทุก 1 เดือน · เริ่ม 1 ต.ค. 67 · benchmark = ข้อมูลเดิม

Little’s Law

L = \lambda W

⁍ = ความยาวในคิว · ⁍ = อัตรามาถึง · ⁍ = เวลารอเฉลี่ย

ตัวอย่าง Starbucks: 11 คนในคิว / บริการ 1 คนต่อนาที = รอ 11 นาที

Case USG scheduling

Overdue rate 40.36% (ข้อมูล 2023–2024 + simulation)

demand ≠ capacity — จันทร์ / ธ.ค. เน้น

แนะนำ: เพิ่ม capacity วันจันทร์และเดือนธันวาคม, ให้ลำดับ short-term → เป้าหมาย overdue < 5%

Algorithmic bias — training data ขาด diversity / สะท้อน inequity → ทายผิดกับกลุ่มชาติ/เศรษฐะธรรม

ผล: ซ้ำเติม health disparity และทำลายความยุติธรรม

John Snow — อหิวาตกโรค 1854

Soho, London — geospatial mapping

บ้านที่ใช้น้ำจากปั๊ม Broad Street ตาย สูงกว่า 14 เท่า

Intervention: ถอดด้ามปั๊ม

Florence Nightingale — 1850s

โรงพยาบาล Scutari, สงครามไครเมีย

สร้าง coxcomb / polar area diagram

พิสูจน์: คนตายส่วนใหญ่จาก โรคติดเชื้อที่ป้องกันได้ ไม่ใช่จากบาดแผล



## Topic 2: Data Wrangling & Cleaning (ID: 3cc0abc4-4cc7-81ba-81ec-fe4cfeb65880)

2. Data Collection, Cleaning, and Preparation for Healthcare Analysis

📝 Mock Test ชุดที่ 1-5 (ง่าย → ยาก) — Data Wrangling, Cleaning, Visualization


#### 📖 สรุปเนื้อหาจากสไลด์ — Data Preparation

> ผู้บรรยาย: Sermkiat Lolak, M.D.

> หัวข้อ: Data Preparation — Wrangling, Cleaning, and Visualization Principles

> 📄 ไฟล์สไลด์ต้นฉบับ

โครงสร้าง: Part 1 – Data Wrangling · Part 2 – Data Cleaning · Part 3 – Data Visualization


### Part 1 — Data Wrangling


#### 1. พื้นฐาน Data Wrangling

Data Wrangling (หรือ data munging / preprocessing) = การนำข้อมูลดิบที่ไม่เป็นระเบียบ มาแปลงให้อยู่ในรูปแบบที่สะอาดและมีโครงสร้าง พร้อมสำหรับการวิเคราะห์

- ข้อมูลมาจากหลายแหล่ง (databases, sensors, spreadsheets) → สกปรกเสมอ
- งานหลักคือ: เลือก subset ที่เกี่ยวข้อง · จัดแนวข้อมูลจากหลายแหล่งให้ตรงกัน · reshape ให้ความสัมพันธ์ที่ซ่อนอยู่ปรากฏชัด
- ประโยชน์: วิเคราะห์ง่ายขึ้น · ลด error · ได้ insight ที่ชัดเจนกว่า · เพิ่ม reproducibility
> 💡 80% ของความพยายามในการวิเคราะห์ข้อมูล หมดไปกับการทำความสะอาดและเตรียมข้อมูลล้วน ๆ — ถ้าไม่มีข้อกำหนดควบคุม ข้อมูลในโลกจริงมักถูกจัดโครงสร้างไว้แบบ "แปลกประหลาด"


#### 2. หลักการ Tidy Data

ค่าทุกค่าในข้อมูลถูกจัดตามสองมิติ:

- Variable (คอลัมน์) — กลุ่มของค่าทั้งหมดที่วัด คุณลักษณะเดียวกัน ข้ามหน่วยต่าง ๆ (เช่น ส่วนสูง อุณหภูมิ ระยะเวลา)
- Observation (แถว) — กลุ่มของค่าทั้งหมดที่วัดจาก หน่วยเดียวกัน ข้ามคุณลักษณะต่าง ๆ (เช่น คนหนึ่งคน วันหนึ่งวัน การมาตรวจหนึ่งครั้ง) → มักคือ n = subjects
Aesthetic Ordering (แนวปฏิบัติที่ดี) — ลำดับไม่เปลี่ยนผลวิเคราะห์ แต่ช่วยให้อ่านง่าย:

- วาง Fixed variables ก่อน (ตัวแปรที่กำหนดโดยการออกแบบการทดลอง เช่น identifier, มิติต่าง ๆ)
- ตามด้วย Measured variables (สิ่งที่วัดจริง)
- เรียงแถวแบบลำดับชั้นตาม fixed variables

#### 3. Taxonomy of Chaos — ข้อมูลรก 5 รูปแบบ

Melting (Wide → Long) — เก็บคอลัมน์ที่เป็นตัวแปรจริงไว้ (colvars) แล้วหมุน "value columns" ที่เหลือลงมาเป็นแถว สร้างตัวแปรใหม่ 2 ตัว: ตัวหนึ่งเก็บชื่อคอลัมน์เดิม อีกตัวเก็บค่า

Casting (Long → Wide / Unstacking) — การกระจายค่าออกไปเป็นคอลัมน์ใหม่

การรวมไฟล์หลายไฟล์ (Type 5)

- อ่านทุกตารางเข้ามาเป็น list
- สำคัญมาก: เพิ่มคอลัมน์ที่บันทึก ชื่อไฟล์ต้นทาง เพราะชื่อไฟล์มักบรรจุค่าของตัวแปรสำคัญ (เช่น ปี หรือสถานที่)
- รวมทุกตารางเป็นโครงสร้างเดียวแบบ stacked
> ⚠️ งานนี้ยากขึ้นมากถ้าโครงสร้าง ชื่อตัวแปร หรือธรรมเนียมการเขียน missing value ต่างกันระหว่างไฟล์


#### 4. Four Fundamental Verbs ของการจัดการข้อมูล


##### 1️⃣ Filter — คัดเลือก/ตัดแถว

- เลือกหรือลบ observations ตามเกณฑ์ตรรกะที่กำหนด — คืนค่า subset ที่เงื่อนไขเป็นจริง
- ⚠️ Noise vs Signal problem: filter ต้องไม่ทิ้งข้อมูลที่มีความหมายไปพร้อมกับ noise เช่น การกรองค่า sensor ที่อยู่นอก "plausible range" ต้องทำอย่างระมัดระวัง เพราะค่าสุดโต่งนั้นอาจเป็นเหตุการณ์จริงที่หายาก

##### 2️⃣ Transform — เพิ่ม/แก้ไขตัวแปร & Reshaping

- การดำเนินการกับตัวแปรเดียว (เช่น log()) หรือหลายตัวแปร (เช่น คำนวณความหนาแน่นจากน้ำหนักและปริมาตร)
- Reshaping: เปลี่ยนทิศทางข้อมูลระหว่าง wide ↔ long

##### 3️⃣ Aggregate — สรุปรวม & Joining

- Aggregate: ยุบค่าหลายค่าให้เหลือค่าสรุปเดียว (sum, mean)
- Joining (Merging): รวมข้อมูลจากหลายตารางผ่าน common key (relational database join)
- หลัก normalization: ข้อมูลถูกเก็บแยกเพื่อเลี่ยงความซ้ำซ้อน เวลาวิเคราะห์จึงต้องประกอบกลับ
- ตัวอย่าง: join ข้อมูลประชากรผู้ป่วย (Patient ID, ชื่อ, อายุ) กับบันทึกการมาตรวจ (Patient ID, วันที่, การวินิจฉัย) ด้วย key = Patient ID
ชนิดของ Join

> ⚠️ Crucial check: ระวัง join key และชนิดของ join — inner join อาจตัดผู้ป่วยที่ไม่มี event ออกไปโดยไม่ตั้งใจ ซึ่งอาจเป็นสิ่งที่ต้องการหรือไม่ก็ได้


##### 4️⃣ Sort — เรียงลำดับ

- เรียงข้อมูลตาม key หนึ่งหรือหลายตัว จากน้อยไปมากหรือมากไปน้อย
- เปลี่ยนแค่ลำดับการนำเสนอ ไม่เปลี่ยนค่าข้อมูล
- ช่วยเผยรูปแบบ และหาค่าสูงสุด (เช่น ค่าใช้จ่ายสูงสุด หรือ length of stay ยาวที่สุด)

### Part 2 — Data Cleaning


#### 1. มิติคุณภาพข้อมูล 6 ด้าน


#### 2. Data Profiling

ขั้นตอนสำคัญ ก่อน ทำความสะอาด — คำนวณสถิติสรุปและตรวจสอบตามแต่ละมิติคุณภาพ

- Completeness: นับ missing values ในแต่ละคอลัมน์
- Validity: ตรวจ min/max ของ field ตัวเลขเทียบกับช่วงที่เป็นไปได้ และดูความถี่ของแต่ละหมวด
- Uniqueness: ไล่ดู record ที่ซ้ำ หรือยืนยันว่า key เป็น unique จริง
เครื่องมือที่ใช้ได้: Excel, Tableau, PowerBI


#### 3. Error ที่พบบ่อย & วิธีจัดการ


##### 3.1 Missing Data (NA, Null)

> y = (1, 2, 4) → mean = 2.33 · y = (1, 2, NA) → คำนวณผิดเป็น 1.5 — missing ทำให้สถิติเพี้ยนทันที

กลไกของการหายไป 3 แบบ

วิธีจัดการ missing data

ก) Complete case analysis (Listwise deletion) — ตัดทั้งแถวที่มี missing

- เสีย precision (95% CI กว้างขึ้น) และ power ลดลง (↓N ⇒ ↓power)
- ถ้าไม่ใช่ MCAR → sample อาจไม่เป็นตัวแทนประชากรเป้าหมายอีกต่อไป (bias)
ข) Available case analysis (Pairwise deletion) — เป็นกรณีพิเศษของ complete case ที่ระดับ bivariate

- ควรเลี่ยง ถ้าจะทำทั้งการวิเคราะห์ bivariate และ multivariable
ค) Imputation


##### 3.2 Outliers

- นิยาม: ค่าที่สูงหรือต่ำผิดปกติเมื่อเทียบกับข้อมูลส่วนที่เหลือ — อาจเป็นค่าจริงที่หายาก หรือเป็น error ก็ได้
- การตรวจจับ: กฎทางสถิติ (1.5 × IQR สำหรับ box plot, ค่าที่ห่างจาก mean เกิน 3 SD) หรือใช้การ visualize
- การจัดการ — ขึ้นกับบริบทอย่างมาก:

##### 3.3 Duplicates

- ชนิด: Exact duplicates (ลบง่าย) vs Partial duplicates (entity เดียวกันแต่ record ไม่เหมือนกันเป๊ะ)
- การตรวจจับ: ใช้ unique key ที่เชื่อถือได้ หรือรวมหลาย field (ชื่อ + วันเกิด) เพื่อหา probabilistic match
- การแก้ไข:
- ⚠️ ระวังลบ record ที่ถูกต้องออกไปโดยบังเอิญ เช่น ผู้ป่วยสองคนที่ชื่อซ้ำกันเพราะเป็นชื่อสามัญ

#### 🎯 ประเด็นสำคัญสำหรับทบทวน

- นิยาม variable vs observation และหลัก tidy data (1 แถว = 1 observation, 1 คอลัมน์ = 1 ตัวแปร)
- ความรก 5 รูปแบบ และ melt vs cast ใช้แก้แบบไหน
- Join 4 ชนิด และผลของการเลือกผิด (โดยเฉพาะ inner join ที่ตัดผู้ป่วยไม่มี event ทิ้ง)
- มิติคุณภาพข้อมูล 6 ด้าน — จำนิยามและตัวอย่างให้ได้
- MCAR / MAR / MNAR — นิยาม ตัวอย่าง และวิธีจัดการที่เหมาะกับแต่ละแบบ (⭐ ออกสอบบ่อย)
- ทำไม mean imputation และ LOCF ถึงไม่แนะนำ และทำไม multiple imputation / MICE ดีกว่า
- ลำดับชั้น Cleveland & McGill — ทำไม bar chart ดีกว่า pie chart
- รูปแบบกราฟหลอกตา โดยเฉพาะ truncated Y-axis, dual Y-axes, และ Lie Factor

#### Session 2

Date: 2 Sep 2026  

Time: 17:00 – 20:00

Title (EN): Statistical Inference and its Application in Clinical Research 1  

Title (TH): อนุมานทางสถิติและการประยุกต์ใช้ในการวิจัยทางคลินิก 1

Instructor: อ.นพ. ชัยวัฒน์ ศุภศิลป์


### Part 3 — Data Visualization


#### 1. ทำไม Visualization จึงสำคัญ — Graphical Perception

- ใช้ประโยชน์จากการรับรู้: การ visualize แปลงข้อมูลเชิงปริมาณที่ซับซ้อนให้เป็นภาพ เพื่อใช้ความสามารถอันโดดเด่นของระบบการมองเห็นมนุษย์ในการจับ pattern, trend และสิ่งผิดปกติ
- Pre-attentive attributes: สมองมนุษย์เก่งมากในการตรวจจับความต่างของ ตำแหน่ง ความยาวเส้น ความเข้มสี และรูปทรง อย่างรวดเร็ว
สองวัตถุประสงค์ของการ visualize


#### 2. ลำดับชั้นการรับรู้กราฟ (Cleveland & McGill)

มนุษย์ถอดรหัสคุณลักษณะทางภาพบางอย่างได้แม่นกว่าอย่างอื่น:

- ดีที่สุด: ตัดสินตำแหน่งบนสเกลร่วมกัน (เช่น ยอดแท่งบนแกนเดียวกัน)
- รองลงมา: เปรียบเทียบตำแหน่งบนสเกลที่เหมือนกันแต่แยกกัน (เช่น small multiples)
- ดี: ตัดสินความยาว และทิศทาง/ความชันของเส้น
- แย่ลง: ตัดสินมุม (ชิ้นของ pie chart) หรือพื้นที่ (ขนาดฟองใน bubble)
- แย่ที่สุด: ตัดสินปริมาตร/มุมมอง 3 มิติ หรือความต่างของความเข้มสี
> ✅ คำแนะนำเชิงปฏิบัติ: ใช้ ตำแหน่งหรือความยาว (bar chart, dot plot) แทน พื้นที่หรือมุม (pie chart) สำหรับการเปรียบเทียบเชิงปริมาณ


#### 3. ชนิดของกราฟ


#### 4. หลีกเลี่ยงกราฟที่ชวนเข้าใจผิด

การรักษา graphical integrity ต้องรู้จักและเลี่ยงวิธีการบิดเบือนเหล่านี้:

- Inappropriate Aggregation / Scaling
- Omitting Uncertainty — นำเสนอค่าเฉลี่ยหรือค่าประมาณโดยไม่มี error bar หรือ CI ทำให้ผู้อ่านเข้าใจผิดว่าความต่างมีนัยสำคัญทางสถิติ ทั้งที่ไม่ใช่
- Truncated Y-Axis / Suppressed Zero — เริ่มแกนของ bar chart เหนือศูนย์ ต้องเลี่ยง เพราะขยายความต่างเล็ก ๆ ให้ดูใหญ่มาก
- Dual Y-Axes — ใช้แกน Y สองแกนที่สเกลต่างกัน สามารถถูกจัดฉากให้ดูเหมือนสองเส้นมีความสัมพันธ์กันทั้งที่ไม่มีจริง มักทำให้ผู้อ่านสับสน — ควรเลี่ยงเว้นแต่จำเป็นเพราะหน่วยต่างกัน
- Cherry-Picking Data — แสดงเฉพาะช่วงข้อมูลที่เล่าเรื่องตามต้องการ แล้วตัดบริบทประวัติศาสตร์ทิ้ง (เช่น โชว์แนวโน้มแบน โดยละเลยรูปแบบวัฏจักรระยะยาว)
- Misuse of Area or Volume — ปรับขนาดวัตถุ 3 มิติ (แท่ง 3D, pictogram) ตามค่า ทำให้เข้าใจผิดอย่างรุนแรง: ค่าเพิ่มสองเท่าอาจทำให้ปริมาตรเพิ่มแปดเท่า → Lie Factor สูง
🟢 ชุดที่ 1 — ระดับง่าย (30 ข้อ)

- Wide format: ตัวแปรหรือจุดเวลาต่าง ๆ กระจายเป็นคอลัมน์
- Long format (Tall/Tidy): 1 แถว = 1 observation, คอลัมน์ = ตัวแปร
- Pivot = long → wide · Melt (Stacking) = wide → long
- Verify & Correct — ถ้ายืนยันว่าเป็น error (เช่น จุดทศนิยมผิดที่) ก็แก้ให้ถูก
- Exclude — ลบ record ถ้าผิดชัดเจนหรืออยู่นอกขอบเขตการวิเคราะห์ (ต้องมีเหตุผลรองรับ)
- Transform — ใช้ log transformation หรือสถิติที่ทนทาน (เช่น median) เพื่อลดอิทธิพล
- Cap or Floor (Winsorize) — แทนค่าสุดโต่งด้วยค่าที่ percentile ที่กำหนด (ลดอิทธิพลแต่ยังเก็บข้อมูลไว้)
- Flag — เก็บ outlier ไว้ แต่สร้างตัวแปร flag เพิ่มเพื่อใช้ในโมเดล
- Consolidate / Merge — รวม field ที่ขัดแย้งหรือไม่ครบให้เป็น record ที่ "ดีที่สุด" (เช่น เอา record ที่สมบูรณ์สุด)
- Survival Rule — ใช้ record ล่าสุด โดยถือว่าเป็นข้อมูลที่ทันสมัยที่สุด
- ใช้ตัวเลขสัมบูรณ์ทั้งที่ควรใช้อัตราต่อประชากร (เช่น เทียบจำนวนอาชญากรรมดิบของเมืองที่ประชากรต่างกันมาก)
- Cumulative counts ทำให้ดูเหมือนเพิ่มขึ้นต่อเนื่องเกินจริง แม้ยอดรายวันจะคงที่


## Topic 3: Statistical Inference 1 (ID: 3cc0abc4-4cc7-8135-92d8-f1840559e539)

3.  Statistical Inference and its Application in Clinical Research 1


#### 📑 สารบัญประจำหน้า (Table of Contents)

ชุดที่ 1 — ระดับง่าย (30 ข้อ)

ชุดที่ 2 — ระดับง่าย-ปานกลาง (30 ข้อ)

ชุดที่ 3 — ระดับปานกลาง (30 ข้อ)

ชุดที่ 4 — ระดับปานกลาง-ยาก (30 ข้อ)

ชุดที่ 5 — ระดับยาก (30 ข้อ)


#### 📖 สรุปเนื้อหา: Statistical Inference and its Application in Clinical Research


##### 1. 🔬 หลักการพื้นฐานของ Clinical Epidemiology

- เปิดด้วยกรณีศึกษาอหิวาตกโรค (Cholera) และแผนที่ของ John Snow เพื่อแสดงต้นแบบของกระบวนการวิจัยทางระบาดวิทยา — Research flow มาตรฐาน: Question (with Hypothesis) → Study design → Data collection → Data Analysis → Results and Discussion
- Clinical Epidemiology = Clinical Medicine + Epidemiology คือการนำหลักระบาดวิทยามาทำนายผลลัพธ์ในผู้ป่วยแต่ละราย โดยอาศัยการนับเหตุการณ์ทางคลินิก (the 5 Ds) ในกลุ่มผู้ป่วยที่คล้ายกัน แล้วใช้วิธีการทางวิทยาศาสตร์ที่เข้มงวดเพื่อทำนายผลลัพธ์
- Outcome ของโรค (5Ds): Death, Disease, Discomfort, Disability, Dissatisfaction (บางครั้งรวม Destitution)
- ตัวแปร: Independent (ตัวทำนาย), Dependent (ผลลัพธ์), Extraneous (ตัวแปรกวน)
- Population vs Sample: ประชากรมี Parameters ส่วนกลุ่มตัวอย่างมี Statistics เชื่อมกันด้วยกระบวนการ Sampling และ Inference
- ความคลาดเคลื่อน (Error): Random error (จากโอกาส) vs Systematic error/Bias (กระบวนการที่ทำให้ผลเบี่ยงเบนจากค่าจริงอย่างเป็นระบบ)
- Internal validity: ผลถูกต้องสำหรับกลุ่มตัวอย่างที่ศึกษา / External validity (generalizability): ผลนำไปใช้ได้กับบริบทอื่น

##### 2. ⚠️ Bias และการควบคุม Confounding

- Selection bias — เปรียบเทียบกลุ่มที่ต่างกันในปัจจัยกำหนดผลลัพธ์อื่นนอกเหนือจากตัวแปรที่ศึกษา
- Measurement bias — วิธีวัดผลไม่เหมือนกันระหว่างกลุ่ม
- Confounding — ปัจจัยสองอย่างเคลื่อนไหวไปด้วยกัน ทำให้ผลของปัจจัยหนึ่งถูกปนกับอีกปัจจัย (ตัวอย่าง: การดื่มชาร้อนกับมะเร็งกระเพาะ ที่มีการสูบบุหรี่เป็นตัวกวน)
- ตัวอย่างเชิงลึก: Berkson bias (สุ่มตัวอย่างจากกลุ่มในโรงพยาบาลแทนที่จะเป็นชุมชน ทำให้ OR เปลี่ยนจาก 1.06 เป็น 4.06) และ Lead-time bias (การวินิจฉัยเร็วขึ้นทำให้ดูเหมือนรอดชีวิตนานขึ้นทั้งที่ผลจริงไม่เปลี่ยน)
🛡️ การควบคุม Confounder:


##### 3. 📉 Disease Frequency (Count, Incidence, Prevalence)

- Count — จำนวนผู้ที่มีโรคหรือลักษณะที่สนใจ (ใช้วางแผนทรัพยากร เช่น ปริมาณ ORS) แต่ขึ้นกับขนาดประชากรและความยาวของช่วงเวลาสังเกต
- Incidence = เคสใหม่ที่เกิดขึ้นในช่วงเวลาที่กำหนด แบ่งเป็น 2 แบบหลัก:
- Prevalence = เคสที่มีอยู่ทั้งหมด ณ จุดเวลาหนึ่งหรือช่วงเวลาหนึ่ง (Point prevalence / Period prevalence) สะท้อนทั้งการเกิดโรคใหม่และการคงอยู่ของโรค

##### 4. ⚖️ Measures of Association: Risk Ratio (RR) และ Odds Ratio (OR)

4.1 ตาราง 2×2 มาตรฐาน

หลักการจำ: "แถวเป็นปัจจัย (Exposed/Non-exposed) — คอลัมน์เป็นผลลัพธ์ (Disease/No Disease)" เริ่มจากมุมซ้ายบนเป็นตัว a เสมอ

4.2 สูตร Risk และ Risk Ratio (RR)

- Risk = จำนวนเคส ÷ จำนวนผู้ที่เสี่ยง มีค่าอยู่ระหว่าง 0 ถึง 1
- Risk in Exposed = a / (a+b) / Risk in Non-exposed = c / (c+d)
- Risk Ratio (RR) = [a/(a+b)] ÷ [c/(c+d)]
- ใช้ได้ดีใน Cohort study และ RCT ที่รู้จำนวนผู้มีความเสี่ยงทั้งหมด (prospective)
4.3 สูตร Odds และ Odds Ratio (OR)

- Odds = จำนวนที่เกิดเหตุการณ์ ÷ จำนวนที่ไม่เกิดเหตุการณ์ สามารถมีค่ามากกว่า 1 ได้ (ต่างจาก Risk)
- Odds in Exposed = a/b / Odds in Non-exposed = c/d
- Odds Ratio (OR) = (a/b) ÷ (c/d) = (a×d) / (b×c)
- ใช้ได้ดีใน Case-control study (คำนวณ RR ไม่ได้), Logistic regression (คำนวณ adjusted OR เป็นหลัก) และ Meta-analysis
- Odds ใช้เมื่อคำนวณ Risk โดยตรงไม่ได้ (โดยเฉพาะ Case-control study ที่ไม่ทราบจำนวนผู้สัมผัสทั้งหมด) และเป็นพื้นฐานของ OR รวมถึง Logistic Regression
4.4 ตัวอย่างคำนวณจาก Handout (Smoking → Disease)

- Risk Exposed = 100/2000 = 0.05 / Risk Non-exposed = 80/8000 = 0.01 → RR = 5 (ความเสี่ยงของกลุ่มสูบบุหรี่เป็น 5 เท่าของกลุ่มไม่สูบ)
- Odds Exposed = 100/1900 ≈ 0.0526 / Odds Non-exposed = 80/7920 ≈ 0.0101 → OR ≈ 5.21
4.5 ทำไมต้องใช้ Odds (จากต้นฉบับ)

- หากเหตุการณ์ที่สนใจพบได้น้อยมาก (rare event) → OR ≈ RR
- Logistic regression คำนวณ adjusted OR ไม่ใช่ RR
- ใน Meta-analysis แต่ละการศึกษาอาจมีความชุกต่างกัน การใช้ OR จึงเหมาะสมกว่า
- Case-control study (retrospective) ไม่สามารถคำนวณ RR ได้โดยตรง เพราะไม่ทราบจำนวนผู้สัมผัสทั้งหมด → ใช้ OR
- Cohort study (prospective) สามารถคำนวณได้ทั้ง RR และ OR
- ทั้ง RR และ OR ควรรายงานคู่กับ 95% Confidence Interval เสมอ
4.6 RR vs OR — ใช้ต่างกันอย่างไร

หลักการเลือกใช้สั้น ๆ: เริ่มจากปัจจัยเสี่ยง → ติดตามผลลัพธ์ = นิยมใช้ RR / เริ่มจากผลลัพธ์ → ย้อนดูปัจจัยเสี่ยง = นิยมใช้ OR

สูตรตัวแปร ⁍ และ ⁍


##### 5. 📊 Measures of Potential Impact: Attributable Risk (AR) และ Population Attributable Risk (PAR)

- Attributable Risk (AR) = Risk difference = Risk_exposed − Risk_non-exposed  
- Attributable Risk Percent (AR%) หรือ Attributable Fraction among Exposed = (AR / Risk_exposed) × 100  
- Population Attributable Risk (PAR) = AR × ความชุกของการสัมผัสในประชากร (หรือ Risk_total − Risk_non-exposed)  
- Population Attributable Risk Percent (PAR%) = (PAR / Risk_total) × 100  

##### 6. 🗂️ สรุปการเลือกใช้ตัวชี้วัดทางระบาดวิทยา


##### 7. ⏳ Survival Analysis

- องค์ประกอบหลัก: Event vs Non-event, Time-to-event, แนวคิดการ censor (loss to follow-up, death, right censor)
- Hazard = อัตราการเกิดเหตุการณ์ ณ ช่วงเวลาหนึ่ง ๆ (ต่างจาก cumulative incidence ที่นับสะสม)
- Hazard Ratio (HR) เช่น HR = 2 หมายถึงกลุ่มเสี่ยงมีอัตราการเกิดเหตุการณ์เป็น 2 เท่าของกลุ่มไม่เสี่ยง ณ ช่วงเวลานั้น
- Cox proportional hazards model ตั้งสมมติฐานว่า HR คงที่ตลอดเวลาระหว่างสองกลุ่ม

##### 8. 📐 สถิติเชิงพรรณนา vs สถิติเชิงอนุมาน, SD vs SE, Confidence Interval

- Descriptive statistics สรุปข้อมูล ใช้ได้ทั้งกับ sample หรือ population
- Inferential statistics ประมาณค่าพารามิเตอร์ของประชากร + ทดสอบสมมติฐาน + ช่วยตัดสินใจเกี่ยวกับประชากร
- Point estimate เช่น ค่าเฉลี่ยอายุจากกลุ่มตัวอย่าง แต่จะแตกต่างกันไปในแต่ละกลุ่มตัวอย่าง จึงต้องรายงานเป็นช่วง (Interval estimate)
- Standard Deviation (SD): วัดการกระจายของข้อมูลในกลุ่มตัวอย่าง (scatter of observations) ใช้สำหรับ descriptive statistics
- Standard Error (SE): วัดความแม่นยำของค่าเฉลี่ยกลุ่มตัวอย่างในการประมาณค่าเฉลี่ยประชากร ใช้คำนวณ CI และทดสอบสมมติฐาน

##### 9. 🧮 Hypothesis Testing

9.1 ประเภทของ Hypothesis

- Clinical / Research Hypothesis → มักตรงกับ Alternative Hypothesis (Hₐ)
- Statistical Hypothesis:
9.2 6 ขั้นตอนของ Hypothesis Testing

1️⃣ Generate null and alternative hypotheses (ตั้งสมมติฐาน H0 / Ha)

2️⃣ Determine the significance level (α) (กำหนดระดับนัยสำคัญ)

3️⃣ Select an appropriate test statistic (เลือกสถิติทดสอบที่เหมาะสม)

4️⃣ Calculate the test statistic (คำนวณค่าสถิติทดสอบ)

5️⃣ Convert the test statistic to p-value (แปลงเป็นค่า p-value)

6️⃣ Draw a conclusion (สรุปผลและตัดสินใจ)

9.3 Type I / Type II Error และ Power

- Type I Error (α): ปฏิเสธ H₀ ทั้งที่จริง H₀ ถูกต้อง (False Positive) — สรุปว่า "มีผล" ทั้งที่จริงแล้ว "ไม่มีผล" (มักตั้งไว้ที่ 0.05)
- Type II Error (β): ไม่ปฏิเสธ H₀ ทั้งที่จริง H₀ ผิด (False Negative) — สรุปว่า "ไม่มีผล" ทั้งที่จริงแล้ว "มีผล" (มักตั้งไว้ที่ 0.20)
- Power of the test = 1 − β คือความสามารถในการตรวจจับความแตกต่างเมื่อมันมีอยู่จริง (มักต้องการ ≥ 0.80)
9.4 ตารางเลือกสถิติทดสอบ (ตัวแปรผลลัพธ์ x ตัวแปรทำนาย)


##### 10. ❓ P-value: ความหมายและข้อควรระวัง

- P-value = ความน่าจะเป็นที่จะได้ผลลัพธ์ที่สุดขั้วเท่ากับหรือมากกว่าที่สังเกตได้ ภายใต้สมมติฐานว่า H0 เป็นจริง
- ถ้า P-value < α → ปฏิเสธ H0 → มีนัยสำคัญทางสถิติ (statistical significance)
- P-value สูง = ข้อมูลสอดคล้องกับ H0 มาก (ความต่างที่เห็นน่าจะเกิดจากโอกาส); P-value ต่ำ = ข้อมูลขัดกับ H0 มาก

##### 11. ⚖️ ตัวอย่างประยุกต์: โปรแกรมลดน้ำหนัก (แสดงความสำคัญของการเลือกสถิติให้ถูกวิธี)

- คำถามวิจัย: "น้ำหนักหลังใช้โปรแกรมลดลงอย่างมีนัยสำคัญหรือไม่"
- ถ้าใช้ Independent t-test (เปรียบเทียบค่าเฉลี่ยก่อน-หลังแบบไม่จับคู่ — วิธีที่ไม่เหมาะสม): P-value = 0.284 → ไม่ปฏิเสธ H0 (สรุปว่าไม่ต่าง)
- ถ้าใช้ Paired/Dependent t-test (วิธีที่ถูกต้องสำหรับข้อมูลคนเดียวกันวัดซ้ำ): ค่าเฉลี่ยผลต่าง = -4.43 กก. (95% CI: -8.63 ถึง -0.23), P-value = 0.042 → ปฏิเสธ H0 (สรุปว่าน้ำหนักลดลงจริงอย่างมีนัยสำคัญ)
- บทเรียน: การเลือกสถิติทดสอบผิดประเภท (ไม่จับคู่ข้อมูลที่จริงเป็น paired) เปลี่ยนข้อสรุปของงานวิจัยได้ทั้งหมด

##### 12. 💡 ข้อคิดสำคัญ (A Little Note)


##### 13. 🧠 เทคนิคจำและ Mental Model สำหรับทบทวน

- หลักการถามคำถาม
- หลักการจับคู่ตรงข้าม
- ภาพในหัว (Mental Model)
> ที่มา: Statistical Inference and its Application in Clinical Research — Chaiyawat Suppasilp, 09.2026 เนื้อหาส่วนสรุปหลักขยายและตรวจทานเพิ่มเติมจาก Handout ต้นฉบับ พร้อมบันทึกการสอนด้วย Feynman Technique เมื่อวันที่ 3 กันยายน 2026 — จัดหน้าใหม่ 3 กันยายน 2026

- ค่า Power of test (1-β) หมายถึงอะไร

##### 📗 ชุดที่ 1 — ระดับง่าย 🟢


##### 📘 ชุดที่ 2 — ระดับง่าย-ปานกลาง 🟢🟡


##### 📙 ชุดที่ 3 — ระดับปานกลาง 🟡


##### 📕 ชุดที่ 4 — ระดับปานกลาง-ยาก 🟡🔴


##### 🔥 ชุดที่ 5 — ระดับยาก 🔴

📉 Disease frequency


##### ชุดที่ 1 — ระดับง่าย 🟢


##### ชุดที่ 2 — ระดับง่าย-ปานกลาง 🟢🟡


##### ชุดที่ 3 — ระดับปานกลาง 🟡


##### ชุดที่ 4 — ระดับปานกลาง-ยาก 🟡🔴


##### ชุดที่ 5 — ระดับยาก 🔴

ทบทวนนิยามและหลักการพื้นฐานของ Clinical Epidemiology

- "5Ds" ในการวัดผลลัพธ์ทางคลินิกตามแนวคิด Clinical Epidemiology ไม่รวมข้อใด
- ข้อใดคือความหมายของ Prevalence
- Bias ชนิดใดเกิดขึ้นเมื่อวิธีการวัดผลไม่เหมือนกันระหว่างกลุ่มที่เปรียบเทียบ
- Error ชนิดใดที่เกิดจากกระบวนการในขั้นตอนใดของการวิจัย (design, conduct, analysis) จนทำให้ผลเบี่ยงเบนจากค่าจริงอย่างเป็นระบบ
- Internal validity หมายถึงอะไร
- ข้อใดคือ "Extraneous variable"
ฝึกคำนวณและประยุกต์ใช้ Incidence, Prevalence, RR, OR, AR/PAR

- จากการสำรวจสตรี 1,150 คนที่คลอดบุตร พบว่า 468 คนทานวิตามินรวมอย่างน้อย 4 ครั้ง/สัปดาห์ก่อนตั้งครรภ์ ค่า 468/1150 ที่คำนวณได้เรียกว่าอะไร
- จากตาราง 2x2: กลุ่มสูบบุหรี่ 2,000 คน (ป่วย 100) กลุ่มไม่สูบ 8,000 คน (ป่วย 80) — Risk Ratio มีค่าประมาณเท่าใด
- เหตุผลใดที่ทำให้นักวิจัยเลือกใช้ Odds Ratio แทน Risk Ratio ใน case-control study
- ถ้าโรคที่ศึกษาเป็นโรคหายาก (rare disease) ความสัมพันธ์ระหว่าง OR กับ RR เป็นอย่างไร
- Population Attributable Risk (PAR) คำนวณจากอะไร
- Confounding factor ต้องมีคุณสมบัติใด
Hypothesis testing, Type I/II error และการเลือกสถิติทดสอบ

- ขั้นตอนแรกของ Hypothesis testing (6 ขั้นตอน) คือข้อใด
- Type I error คือข้อใด
- ต้องการเปรียบเทียบค่าเฉลี่ยน้ำหนัก "ก่อน" และ "หลัง" ในผู้ป่วยกลุ่มเดียวกัน (repeated measure) ข้อมูลกระจายแบบปกติ ควรเลือกใช้สถิติใด
- ถ้าตัวแปรผลลัพธ์เป็น categorical 2 กลุ่มอิสระ และมีเซลล์ที่คาดหวัง (expected cell count) น้อย ควรใช้สถิติใดแทน Chi-square
- ทำไมการเพิ่มขนาดกลุ่มตัวอย่าง (sample size) มักทำให้ได้ p-value ที่มีนัยสำคัญง่ายขึ้น
Point/Interval estimation, SD vs SE และ Survival analysis

- ข้อใดอธิบายความแตกต่างระหว่าง SD และ SE ได้ถูกต้องที่สุด
- "Right censoring" ใน survival analysis หมายถึงกรณีใด
- ถ้า Hazard Ratio (HR) = 2 ที่ปีที่ 3 หมายความว่าอย่างไร
- สมมติฐานหลัก (assumption) ของ Cox proportional hazards model คือข้อใด
- จากตัวอย่าง: กลุ่มตัวอย่าง 750 คน, mean age = 54.42, SD = 12.93 → SE ของค่าเฉลี่ยมีค่าประมาณเท่าใด (SE = SD/√n)
- การเพิ่มขนาดกลุ่มตัวอย่างจาก 30 เป็น 500 คน (mean ใกล้เคียงเดิม) ส่งผลต่อ 95% CI ของค่าเฉลี่ยอย่างไร
การตีความเชิงวิพากษ์: p-value pitfalls, clinical vs statistical significance, และการประยุกต์ข้ามหัวข้อ

- งานวิจัยหนึ่งรายงาน OR ของยา A เทียบยา B = 1.02 (95%CI 1.01-1.03, p<0.001) ข้อใดเป็นการตีความที่ถูกต้องที่สุด
- ศึกษาความสัมพันธ์ระหว่างพฤติกรรมเสี่ยง (สูบบุหรี่ ดื่มแอลกอฮอล์ ออกกำลังกาย) กับ CKD ด้วย Chi-square พบทุกปัจจัยมี p-value > 0.05 ข้อสรุปใด 'ผิด'
- RCT พบ Overall survival ของ Erlotinib+Gemcitabine = 6.24 เดือน vs Gemcitabine อย่างเดียว = 5.91 เดือน (p=0.038) ประเด็นสำคัญที่สุดที่ควรพิจารณาต่อคือ
- นักวิจัยต้องการทดสอบว่าน้ำหนักหลังโปรแกรมในผู้ป่วยกลุ่มเดียวกัน (วัดก่อน-หลัง) ต่างจากศูนย์หรือไม่ แต่ใช้ Independent t-test แทน Paired t-test โดยไม่ตั้งใจ ผลที่เป็นไปได้คือ
- Cohort study เรื่อง AF และ ischemic stroke: กลุ่ม AF (n=500) stroke 2 ราย, กลุ่มไม่มี AF (n=500) stroke 1 ราย, ความชุกของ AF ในประชากรทั่วไป = 30% ลำดับการคำนวณ PAR ที่ถูกต้องคือ
- ข้อใดอธิบายความแตกต่างระหว่าง "Association" และ "Correlation" ในบริบทของ Chi-square test ได้ถูกต้องที่สุด
- เพราะเหตุใด multiple logistic regression จึงรายงานผลเป็น adjusted Odds Ratio แทนที่จะเป็น adjusted Risk Ratio
- ข้อใด "ไม่ใช่" วิธีการควบคุม Confounding ที่ถูกต้อง

##### 🟢 ชุดที่ 1: ทบทวนนิยามและหลักการพื้นฐาน (ระดับง่าย)


##### 1. Disease Frequency

Incidence

- หมายถึงจำนวนเคสใหม่ที่เกิดขึ้นในช่วงเวลาที่กำหนด
- แบ่งเป็น 2 แบบหลัก:
Prevalence

- หมายถึงจำนวนเคสที่มีอยู่ทั้งหมด ณ จุดเวลาหนึ่ง หรือช่วงเวลาหนึ่ง

#### 🧪 Mock Test เตรียมสอบ (5 ชุด: รวม 150 ข้อ)


##### 📋 ตารางสรุปภาพรวมและขอบเขตข้อสอบ (Mock Test Matrix)


##### 3. 📈 การวัดทางระบาดวิทยา (Epidemiological Measures)


##### 4. ⏳ Survival Analysis


##### 5. 📐 สถิติเชิงพรรณนา vs สถิติเชิงอนุมาน

🪜 6 ขั้นตอนของ Hypothesis Testing:

1️⃣ ตั้งสมมติฐาน H0 / Ha

2️⃣ กำหนดระดับนัยสำคัญ (α)

3️⃣ เลือกสถิติทดสอบที่เหมาะสม

4️⃣ คำนวณค่าสถิติทดสอบ

5️⃣ แปลงเป็นค่า p-value

6️⃣ สรุปผลและตัดสินใจ


##### 7. ❓ P-value: ความหมายและข้อควรระวัง


##### 8. ⚖️ ตัวอย่างประยุกต์: โปรแกรมลดน้ำหนัก (แสดงความสำคัญของการเลือกสถิติให้ถูกวิธี)


#### 📚 บันทึกการสอนเพิ่มเติม (Teaching Notes)


##### 🔹 H₀, Hₐ, p-value และ Type I / Type II Error

H₀ (Null Hypothesis)  

สมมติฐานว่างที่กล่าวว่า “ไม่มีความแตกต่าง” หรือ “ไม่มีความสัมพันธ์” หรือ “ผลที่เกิดขึ้นเกิดจากโอกาสเพียงอย่างเดียว”

Hₐ (Alternative Hypothesis)  

สมมติฐานทางเลือกที่ตรงข้ามกับ H₀ กล่าวว่า “มีความแตกต่าง” หรือ “มีความสัมพันธ์”

p-value  

คือความน่าจะเป็นที่จะได้ผลลัพธ์ที่สุดขั้วเท่ากับหรือมากกว่าที่สังเกตได้จากข้อมูล ภายใต้สมมติฐานว่า H₀ เป็นจริง

- หาก p-value < α (โดยทั่วไป α = 0.05) → ปฏิเสธ H₀ และยอมรับ Hₐ → มีนัยสำคัญทางสถิติ
- หาก p-value ≥ α → ไม่ปฏิเสธ H₀ → ยังไม่มีหลักฐานเพียงพอ
Type I Error (α)  

ปฏิเสธ H₀ ทั้งที่ H₀ เป็นจริง (False Positive) — สรุปว่า “มีผล” ทั้งที่จริงแล้ว “ไม่มีผล”

Type II Error (β)  

โดย Odds = จำนวนที่เกิดเหตุการณ์ / จำนวนที่ไม่เกิดเหตุการณ์

หลักการจำ:  

“แถวเป็นปัจจัย (Exposed/Non-exposed) — คอลัมน์เป็นผลลัพธ์ (Disease/No Disease)”  

เริ่มจากมุมซ้ายบนเป็นตัว a เสมอ

สูตรสำคัญที่ผูกกับ a, b, c, d

- Risk Exposed = a / (a+b)
- Risk Non-exposed = c / (c+d)
- Risk Ratio (RR) = [a/(a+b)] / [c/(c+d)]
- Odds Exposed = a/b

##### 🔹 สูตรและการทำความเข้าใจ Odds

Odds = จำนวนที่เกิดเหตุการณ์ ÷ จำนวนที่ไม่เกิดเหตุการณ์

Odds ใช้เมื่อคำนวณ Risk โดยตรงไม่ได้ (โดยเฉพาะ Case-control study) และเป็นพื้นฐานของ Odds Ratio รวมถึง Logistic Regression

หลักการเลือกใช้สั้น ๆ

- เริ่มจากปัจจัยเสี่ยง → ติดตามผลลัพธ์ = นิยมใช้ RR
- เริ่มจากผลลัพธ์ → ย้อนดูปัจจัยเสี่ยง = นิยมใช้ OR

##### 🔹 หลักการทำความเข้าใจและจำแนวคิดสถิติ


#### 📖 รายละเอียดเพิ่มเติมจาก Handout ต้นฉบับ (Chaiyawat Suppasilp, 09.2026)

เนื้อหาด้านล่างขยายจากเอกสารต้นฉบับ เพื่อลดความกระชับเกินไปของสรุปเดิม


##### 1. Clinical Epidemiology และการวิจัยทางการแพทย์

Clinical Epidemiology คือศาสตร์ที่ใช้การนับเหตุการณ์ทางคลินิก (the 5 Ds) ในกลุ่มผู้ป่วยที่คล้ายกัน แล้วใช้วิธีการทางวิทยาศาสตร์ที่เข้มงวดเพื่อทำนายผลลัพธ์ในผู้ป่วยแต่ละราย

5 Ds ของผลลัพธ์ทางคลินิก:

- Death
- Disease
- Discomfort
- Disability
- Dissatisfaction
(บางครั้งรวม Destitution)

กระบวนการวิจัยที่ John Snow ใช้กับอหิวาตกโรค แสดงให้เห็น Research flow มาตรฐาน:

Question (with Hypothesis) → Study design → Data collection → Data Analysis → Results and Discussion

Clinical Epidemiology = Clinical Medicine + Epidemiology


##### 2. ตาราง 2×2 และสูตร Odds / Risk อย่างละเอียด

โครงสร้างมาตรฐาน:

สูตร Risk

- Risk in Exposed = a / (a+b)
- Risk in Non-exposed = c / (c+d)
- Risk Ratio (RR) = [a/(a+b)] ÷ [c/(c+d)]
สูตร Odds

- Odds in Exposed = a / b
- Odds in Non-exposed = c / d
- Odds Ratio (OR) = (a/b) ÷ (c/d) = (a × d) / (b × c)
ตัวอย่างจาก Handout (ตาราง Smoking)

- Risk Exposed = 100/2000 = 0.05
- Risk Non-exposed = 80/8000 = 0.01
- RR = 5  
- Odds Exposed = 100/1900 ≈ 0.0526
- Odds Non-exposed = 80/7920 ≈ 0.0101
- OR ≈ 5.21

##### 3. ทำไมต้องใช้ Odds และความแตกต่าง RR กับ OR (จากต้นฉบับ)

- หากเหตุการณ์ที่สนใจพบได้น้อยมาก (rare event) → OR ≈ RR
- Logistic regression คำนวณ adjusted OR ไม่ใช่ RR
- ใน Meta-analysis แต่ละการศึกษาอาจมีความชุกต่างกัน การใช้ OR จึงเหมาะสมกว่า
- Case-control study (retrospective) ไม่สามารถคำนวณ RR ได้โดยตรง เพราะไม่ทราบจำนวนผู้สัมผัสทั้งหมด → ใช้ OR
- Cohort study (prospective) สามารถคำนวณได้ทั้ง RR และ OR

##### 4. Measure of Potential Impact

Attributable Risk (AR) หรือ Risk Difference

- บอกว่าความเสี่ยงส่วนเกินในกลุ่มที่สัมผัสปัจจัย เกิดจากปัจจัยนั้นมากน้อยเพียงใด
- AR = Risk_exposed − Risk_non-exposed
Population Attributable Risk (PAR)

- ความเสี่ยงส่วนเกินในประชากรทั้งหมดที่เกิดจากปัจจัยนั้น
- PAR = AR × ความชุกของปัจจัยในประชากร
- บอกว่าหากกำจัดปัจจัยนี้ออกไปได้ จะลดโรคในประชากรได้มากน้อยเพียงใด

##### 5. Hypothesis Testing (รายละเอียดจากต้นฉบับ)

ประเภทของ Hypothesis

- Clinical / Research Hypothesis → มักตรงกับ Alternative Hypothesis (Hₐ)
- Statistical Hypothesis:
6 ขั้นตอนของ Hypothesis Testing

- Generate null and alternative hypotheses
- Determine the significance level (α)
- Select an appropriate test statistic
- Calculate the test statistic
- Convert the test statistic to p-value
- Draw a conclusion
Type of Error

Interval Estimate = Point estimate ± (Reliability coefficient × Standard Error)

ตัวอย่าง 95% CI ของค่าเฉลี่ย:

หากทราบ variance ของประชากรหรือกลุ่มตัวอย่างใหญ่พอ ใช้ Z  

หากไม่ทราบและกลุ่มตัวอย่างเล็ก ใช้ t

> เนื้อหาส่วนนี้เพิ่มเติมโดยตรงจาก Handout ต้นฉบับ เพื่อให้รายละเอียดครบถ้วนมากขึ้น ลดความสรุปเกินไปของเวอร์ชันก่อนหน้า


#### 📊 Epidemiological Measures — รายละเอียดเพิ่มเติมจาก Handout

- สะท้อนทั้งการเกิดโรคใหม่และการคงอยู่ของโรค
ความสัมพันธ์ระหว่าง Incidence กับ Prevalence

ในโรคที่ค่อนข้างคงที่ (steady state):

Prevalence ≈ Incidence × Duration of disease

- Cox Proportional Hazards Model ตั้งสมมติฐานว่า HR คงที่ตลอดเวลา

##### 3. Measures of Potential Impact

Attributable Risk (AR) หรือ Risk Difference

- สูตร: Risk_exposed − Risk_non-exposed
- บอกว่าความเสี่ยงส่วนเกินในกลุ่มที่สัมผัสปัจจัย เกิดจากปัจจัยนั้นมากน้อยเพียงใด
- ตอบคำถาม: “ถ้าไม่มีปัจจัยนี้ ความเสี่ยงในกลุ่มที่สัมผัสจะลดลงเท่าไร?”
Attributable Risk Percent (AR%) หรือ Attributable Fraction among Exposed

- หรือ (Risk_total − Risk_non-exposed)

##### 4. ตัวอย่างจาก Handout (Ischemic Stroke และ Atrial Fibrillation)

ข้อมูล:

- กลุ่ม No AF 500 คน → เป็น ischemic stroke 1 คน
- ความชุกของ AF ในประชากร = 30%
การคำนวณโดยสรุป:

- Risk in AF = 2/500 = 0.004
- Risk in No AF = 1/500 = 0.002
- AR = 0.004 − 0.002 = 0.002
⚖️ Measures of Association

- Risk = จำนวนเคส ÷ จำนวนผู้ที่เสี่ยง  
- Odds = จำนวนที่เกิดเหตุการณ์ ÷ จำนวนที่ไม่เกิดเหตุการณ์  
- หากโรคพบได้น้อยมาก (rare event) → OR ≈ RR  
- เหตุผลที่นิยมใช้ Odds: logistic regression คำนวณ adjusted OR เป็นหลัก, meta-analysis ใช้ได้ดีแม้ความชุกต่างกัน, และ case-control ไม่ทราบจำนวนผู้สัมผัสทั้งหมดจึงใช้ OR แทน RR  
- Absolute measures ที่เกี่ยวข้อง: Risk Difference (RD) / Attributable Risk (AR), Number Needed to Treat (NNT), Number Needed to Harm (NNH)
📊 Measures of Potential Impact

- Attributable Risk (AR) = Risk difference  
- Population Attributable Risk (PAR) = AR × ความชุกของการสัมผัสในประชากร  
- Attributable Risk Fraction  

##### 🟡 ชุดที่ 2: การวัดทางระบาดวิทยาและการควบคุมตัวแปรกวน (ระดับง่าย-ปานกลาง)


##### 🟠 ชุดที่ 3: การทดสอบสมมติฐานและการเลือกสถิติ (ระดับปานกลาง)


##### 🔴 ชุดที่ 4: การประมาณค่าและการวิเคราะห์การรอดชีพ (ระดับปานกลาง-ยาก)


##### ⬛ ชุดที่ 5: การตีความเชิงวิพากษ์และสถิติขั้นสูง (ระดับยาก)


#### Session 3

Date: 3 Sep 2026  

Time: 17:00 – 20:00

Title (EN): Data Collection, Cleaning, and Preparation for Healthcare Analysis  

Title (TH): การรวบรวมข้อมูล การทำความสะอาด และการเตรียมการสำหรับการวิเคราะห์การดูแลสุขภาพ

Instructor: ดร.นพ. เสริมเกียรติ หล่อลักษณ์


##### 2. Bias และการควบคุม Confounding


##### 3. การวัดทางระบาดวิทยา (Epidemiological Measures)

Disease frequency

- Incidence = เคสใหม่ในช่วงเวลาหนึ่ง (Cumulative incidence / Incidence rate)
- Prevalence = เคสที่มีอยู่ทั้งหมด ณ จุดเวลาหนึ่ง
- ความสัมพันธ์: Prevalence ≈ Incidence × Duration (ในโรคเรื้อรังที่ค่อนข้างคงที่)
Measures of association

- ถ้าโรคพบได้น้อยมาก (rare event) ค่า OR ≈ RR
- Attributable Risk (AR) = Risk difference — ความเสี่ยงส่วนเกินที่เกิดจากการสัมผัสปัจจัยนั้นในกลุ่มที่สัมผัส
- Population Attributable Risk (PAR) = AR × ความชุกของการสัมผัสในประชากร — บอกว่าปัจจัยนี้สำคัญแค่ไหนในระดับสาธารณสุข

##### 4. Survival Analysis

- องค์ประกอบหลัก: Event vs Non-event, Time-to-event, แนวคิดการ censor (loss to follow-up, death, right censor)
- Hazard = อัตราการเกิดเหตุการณ์ ณ ช่วงเวลาหนึ่ง ๆ (ต่างจาก cumulative incidence ที่นับสะสม)
- Hazard Ratio (HR) เช่น HR = 2 หมายถึงกลุ่มเสี่ยงมีอัตราการเกิดเหตุการณ์เป็น 2 เท่าของกลุ่มไม่เสี่ยง ณ ช่วงเวลานั้น
- Cox proportional hazards model ตั้งสมมติฐานว่า HR คงที่ตลอดเวลาระหว่างสองกลุ่ม

##### 5. สถิติเชิงพรรณนา vs สถิติเชิงอนุมาน

- Descriptive statistics สรุปข้อมูล ใช้ได้ทั้งกับ sample หรือ population
- Inferential statistics ประมาณค่าพารามิเตอร์ของประชากร + ทดสอบสมมติฐาน + ช่วยตัดสินใจเกี่ยวกับประชากร
- Point estimate เช่น ค่าเฉลี่ยอายุจากกลุ่มตัวอย่าง แต่จะแตกต่างกันไปในแต่ละกลุ่มตัวอย่าง จึงต้องรายงานเป็นช่วง (Interval estimate)
- Confidence Interval (CI) = Point estimate ± (Reliability coefficient × Standard error); ยิ่งกลุ่มตัวอย่างใหญ่ขึ้น CI ยิ่งแคบลง (แม่นยำขึ้น)
- SD vs SE: SD วัดการกระจายของข้อมูลดิบ (ใช้บรรยายข้อมูล) ส่วน SE วัดความแม่นยำของค่าเฉลี่ยตัวอย่างในการประมาณค่าเฉลี่ยประชากร (ใช้คำนวณ CI และทดสอบสมมติฐาน)

##### 6. Hypothesis Testing

6 ขั้นตอน: (1) ตั้ง H0/Ha (2) กำหนดระดับนัยสำคัญ α (3) เลือกสถิติทดสอบที่เหมาะสม (4) คำนวณค่าสถิติทดสอบ (5) แปลงเป็นค่า p-value (6) สรุปผล

- Type I error (α): ปฏิเสธ H0 ทั้งที่จริง H0 ถูกต้อง (มักตั้งไว้ที่ 0.05)
- Type II error (β): ไม่ปฏิเสธ H0 ทั้งที่จริง H0 ผิด (มักตั้งไว้ที่ 0.20) → Power of test = 1-β
- ตารางเลือกสถิติทดสอบ (ตัวแปรผลลัพธ์ x ตัวแปรทำนาย):

##### 7. P-value: ความหมายและข้อควรระวัง

- P-value = ความน่าจะเป็นที่จะได้ผลลัพธ์ที่สุดขั้วเท่ากับหรือมากกว่าที่สังเกตได้ ภายใต้สมมติฐานว่า H0 เป็นจริง
- ถ้า P-value < α → ปฏิเสธ H0 → มีนัยสำคัญทางสถิติ (statistical significance)
- P-value สูง = ข้อมูลสอดคล้องกับ H0 มาก (ความต่างที่เห็นน่าจะเกิดจากโอกาส); P-value ต่ำ = ข้อมูลขัดกับ H0 มาก

##### 8. ตัวอย่างประยุกต์: โปรแกรมลดน้ำหนัก (แสดงความสำคัญของการเลือกสถิติให้ถูกวิธี)

- คำถามวิจัย: "น้ำหนักหลังใช้โปรแกรมลดลงอย่างมีนัยสำคัญหรือไม่"
- ถ้าใช้ Independent t-test (เปรียบเทียบค่าเฉลี่ยก่อน-หลังแบบไม่จับคู่ — วิธีที่ไม่เหมาะสม): P-value = 0.284 → ไม่ปฏิเสธ H0 (สรุปว่าไม่ต่าง)
- ถ้าใช้ Paired/Dependent t-test (วิธีที่ถูกต้องสำหรับข้อมูลคนเดียวกันวัดซ้ำ): ค่าเฉลี่ยผลต่าง = -4.43 กก. (95% CI: -8.63 ถึง -0.23), P-value = 0.042 → ปฏิเสธ H0 (สรุปว่าน้ำหนักลดลงจริงอย่างมีนัยสำคัญ)
- บทเรียน: การเลือกสถิติทดสอบผิดประเภท (ไม่จับคู่ข้อมูลที่จริงเป็น paired) เปลี่ยนข้อสรุปของงานวิจัยได้ทั้งหมด

##### 9. ข้อคิดสำคัญ (A Little Note)

- เพิ่มขนาดตัวอย่าง (n) มากพอ → มักจะปฏิเสธ H0 ได้เสมอ (CI แคบลง) แม้ความแตกต่างจะเล็กน้อยในทางคลินิก
- P-value ≠ ขนาดของความสัมพันธ์ (magnitude of association) — เช่น OR = 1.02 (P<0.001, 95%CI 1.01–1.03) มีนัยสำคัญทางสถิติ แต่ต้องถามต่อว่ามีนัยสำคัญทางคลินิกหรือไม่
- Statistical significance ≠ Clinical significance — ตัวอย่าง RCT มะเร็งตับอ่อนระยะลุกลาม (Erlotinib+Gemcitabine vs Gemcitabine) พบ P-value นัยสำคัญ แต่ overall survival ต่างกันเพียง 6.24 vs 5.91 เดือน
- การรายงาน P-value ที่ดี: รายงานค่าจริงแทนการเขียนแค่ "<0.05", ถ้า p=0 ให้เขียนเป็น <0.001 หรือ <0.01, ควรรายงานคู่กับ effect size เช่น OR (95%CI) เสมอ ไม่ใช่รายงานแค่ p-value โดด ๆ
- Association ไม่ใช่ Correlation — ผล Chi-square ที่ไม่มีนัยสำคัญ (p>0.05) บอกได้แค่ว่า "ไม่มีความสัมพันธ์" แต่บอกไม่ได้ว่าปัจจัยไหนสำคัญน้อยที่สุด ต้องดูขนาดความสัมพันธ์ (RR, OR, Spearman's/Pearson's correlation) เพิ่มเติม
> ที่มา: Statistical Inference and its Application in Clinical Research — Chaiyawat Suppasilp, 09.2026

สรุปจากไฟล์ handout "Statistical Inference and its Application in Clinical Research" โดย Chaiyawat Suppasilp (09.2026) — เอกสาร 127 หน้า ครอบคลุมตั้งแต่หลักระบาดวิทยาคลินิกไปจนถึงการทดสอบสมมติฐานทางสถิติ พร้อมบันทึกเพิ่มเติมจากการทบทวนด้วย Feynman Technique เมื่อวันที่ 3 กันยายน 2026 — จัดหน้าใหม่ให้เป็นลำดับเดียวตามหัวข้อ ไม่มีการตัดเนื้อหาออก

Statistical_Inference_and_its_Application_in_Clinical_Research_handout2026-1565848-17884010493646.pdf

- ช่วงออกแบบ: Exclusion/Restriction, Matching, Randomization
- ช่วงวิเคราะห์: Adjustment, Stratification, Multivariate analysis
- Cumulative incidence (Incidence proportion) = สัดส่วนของคนที่เคยไม่มีโรค แล้วกลายเป็นมีโรคในช่วงเวลาที่ติดตาม = จำนวนเคสใหม่ ÷ จำนวนประชากรที่เสี่ยงเมื่อเริ่มต้น
- Incidence rate (Incidence density / Hazard rate) = จำนวนเคสใหม่ ÷ person-time ที่เสี่ยง เหมาะเมื่อระยะเวลาติดตามของแต่ละคนไม่เท่ากัน
- ตัวอย่าง: หญิงอาชีพบริการ 5,572 คน พบ HIV ใหม่ 45 ราย ใน 4 ปี → Cumulative incidence = 45/5,572 = 0.8%
- ตัวอย่าง: สตรีคลอด 1,150 คน รับประทานวิตามินรวมบ่อย 468 คน → Prevalence = 468/1,150 = 40.7%
- Point prevalence / Period prevalence
ความสัมพันธ์ระหว่าง Incidence กับ Prevalence (ในโรคที่ค่อนข้างคงที่ / steady state)

Prevalence ≈ Incidence × Duration of disease

- Incidence วัด "NEW" (การปรากฏของโรค) / Prevalence วัด "ALL" (การมีอยู่ของโรค)
- โรคเรื้อรังที่มีระยะเวลานาน → Prevalence สูงแม้ Incidence ไม่สูงมาก
- โรคเฉียบพลันที่หายเร็วหรือเสียชีวิตเร็ว → Prevalence ต่ำแม้ Incidence สูง
ความสัมพันธ์หลัก  

- RR = 1 → ไม่มีความสัมพันธ์ / RR > 1 → เพิ่มความเสี่ยง / RR < 1 → ลดความเสี่ยง (protective)
บอกว่าความเสี่ยงส่วนเกินในกลุ่มที่สัมผัสปัจจัย เกิดจากปัจจัยนั้นมากน้อยเพียงใด (excess risk due to the exposure) — ตอบคำถาม "ถ้าไม่มีปัจจัยนี้ ความเสี่ยงในกลุ่มที่สัมผัสจะลดลงเท่าไร?"

บอกสัดส่วนของโรคในกลุ่มที่สัมผัส ซึ่งอธิบายได้ด้วยปัจจัยนั้น

บอกว่าปัจจัยนี้สำคัญแค่ไหนในระดับสาธารณสุข และหากกำจัดปัจจัยออกไป ความเสี่ยงในประชากรจะลดลงเท่าใด

บอกสัดส่วนของโรคทั้งหมดในประชากร ที่สามารถป้องกันได้หากกำจัดปัจจัยนั้นออกไป — มีประโยชน์ต่อการวางแผนสาธารณสุข

ตัวอย่างจาก handout — Ischemic Stroke และ Atrial Fibrillation (AF)

Cohort 1 ปี: กลุ่ม AF 500 คน vs ไม่มี AF 500 คน (ความชุก AF ในประชากร = 30%)

การคำนวณ: Risk in AF = 2/500 = 0.004 / Risk in No AF = 1/500 = 0.002 / AR = 0.004 − 0.002 = 0.002 / PAR = 0.002 × 0.30 = 0.0006

- มันเปรียบเทียบอะไรกับอะไร?  
- มันตอบว่า “มากกว่า/น้อยกว่า” หรือ “เกิดจากความบังเอิญ”?  
- ผลลัพธ์มีความหมายกับผู้ป่วยจริงหรือไม่?
- H₀ ↔ Hₐ  
- Type I Error (α) ↔ Type II Error (β)  
- Statistical Significance ↔ Clinical Significance  
- RR ↔ OR
- RR/OR = ตาชั่งเปรียบเทียบ  
- Type I/II = ผู้พิพากษาตัดสินคดี  
- Statistical vs Clinical = เข็มวัดขยับ vs คนไข้ดีขึ้นจริง
Confidence Interval (CI) = Point estimate ± (Reliability coefficient × Standard Error)

ยิ่งกลุ่มตัวอย่างใหญ่ขึ้น → CI ยิ่งแคบลง (แม่นยำขึ้น)

ตัวอย่าง 95% CI ของค่าเฉลี่ย: หากทราบ variance ของประชากรหรือกลุ่มตัวอย่างใหญ่พอ ใช้ Z / หากไม่ทราบและกลุ่มตัวอย่างเล็ก ใช้ t

- Null Hypothesis (H₀): สมมติฐานว่างที่กล่าวว่า "ไม่มีความแตกต่าง" หรือ "ไม่มีความสัมพันธ์" หรือ "ผลที่เกิดขึ้นเกิดจากโอกาสเพียงอย่างเดียว" (assumed to be true until proven otherwise)
- Alternative Hypothesis (Hₐ หรือ H₁): สมมติฐานทางเลือกที่ตรงข้ามกับ H₀ กล่าวว่า "มีความแตกต่าง" หรือ "มีความสัมพันธ์"
Sample size effect: เพิ่มขนาดตัวอย่าง (n) มากพอ → มักจะปฏิเสธ H0 ได้เสมอ (CI แคบลง) แม้ความแตกต่างจะเล็กน้อยในทางคลินิก

P-value ≠ ขนาดของความสัมพันธ์ (magnitude of association) — เช่น OR = 1.02 (P<0.001, 95%CI 1.01–1.03) มีนัยสำคัญทางสถิติ แต่ต้องถามต่อว่ามีนัยสำคัญทางคลินิกหรือไม่

Statistical significance ≠ Clinical significance — ตัวอย่าง RCT มะเร็งตับอ่อนระยะลุกลาม (Erlotinib+Gemcitabine vs Gemcitabine) พบ P-value นัยสำคัญ แต่ overall survival ต่างกันเพียง 6.24 vs 5.91 เดือน

การรายงาน P-value ที่ดี: รายงานค่าจริงแทนการเขียนแค่ "<0.05", ถ้า p=0 ให้เขียนเป็น <0.001 หรือ <0.01, ควรรายงานคู่กับ effect size เช่น OR (95%CI) เสมอ ไม่ใช่รายงานแค่ p-value โดด ๆ

Association ไม่ใช่ Correlation — ผล Chi-square ที่ไม่มีนัยสำคัญ (p>0.05) บอกได้แค่ว่า "ไม่มีความสัมพันธ์" แต่บอกไม่ได้ว่าปัจจัยไหนสำคัญน้อยที่สุด ต้องดูขนาดความสัมพันธ์ (RR, OR, Spearman's/Pearson's correlation) เพิ่มเติม

- มันเปรียบเทียบอะไรกับอะไร?
- มันตอบว่า "มากกว่า/น้อยกว่า" หรือ "เกิดจากความบังเอิญ"?
- ผลลัพธ์มีความหมายกับผู้ป่วยจริงหรือไม่?
- H₀ ↔ Hₐ
- Type I Error (α) ↔ Type II Error (β)
- Statistical Significance ↔ Clinical Significance
- RR ↔ OR
- RR/OR = ตาชั่งเปรียบเทียบ
- Type I/II = ผู้พิพากษาตัดสินคดี
- Statistical vs Clinical = เข็มวัดขยับ vs คนไข้ดีขึ้นจริง
ศูนย์รวมแบบทดสอบ Mock Test: Statistical Inference & Clinical Research (150 ข้อ)
แบบทดสอบวัดผลสัมฤทธิ์ทางการศึกษา เรียบเรียงจากเอกสารสรุปบรรยายด้านล่าง จัดแบ่งระดับความยากออกเป็น 5 ชุด (ง่าย → ยาก) ชุดละ 30 ข้อ เพื่อฝึกฝนการจดจำนิยาม, การคำนวณสถิติระบาดวิทยาคลินิก, และการคิดวิเคราะห์เชิงวิพากษ์ (Critical Appraisal)

- ก) ความน่าจะเป็นที่จะปฏิเสธ H0 อย่างถูกต้องเมื่อ H0 เป็นเท็จจริง
- ข) ความน่าจะเป็นที่จะยอมรับ H0 อย่างถูกต้อง
- ค) ระดับนัยสำคัญที่ตั้งไว้
- ง) ค่า p-value ของการทดสอบ
👀 เฉลย

- ก) Death
- ข) Disease
- ค) Diagnosis
- ง) Disability
👀 เฉลย

- ก) จำนวนผู้ป่วยรายใหม่ในช่วงเวลาหนึ่ง
- ข) จำนวนผู้ป่วยที่มีอยู่ทั้งหมด ณ จุดเวลาหนึ่งหรือช่วงเวลาหนึ่ง
- ค) อัตราการเสียชีวิตในกลุ่มประชากร
- ง) ความเสี่ยงสัมพัทธ์ระหว่างกลุ่มสัมผัสกับกลุ่มไม่สัมผัส
👀 เฉลย

- ก) Selection bias
- ข) Measurement bias
- ค) Confounding
- ง) Lead-time bias
👀 เฉลย

- ก) Random error
- ข) Systematic error (Bias)
- ค) Sampling error
- ง) Type I error
👀 เฉลย

- ก) ผลการศึกษาสามารถนำไปใช้ได้กับประชากรกลุ่มอื่น
- ข) ผลการศึกษาถูกต้องสำหรับกลุ่มตัวอย่างที่ศึกษาโดยเฉพาะ
- ค) ความแม่นยำของเครื่องมือวัด
- ง) ขนาดของกลุ่มตัวอย่างที่เพียงพอ
👀 เฉลย

- ก) ตัวแปรที่เป็นผลลัพธ์ของการศึกษา
- ข) ตัวแปรที่เป็นตัวทำนายหลักที่สนใจ
- ค) ตัวแปรกวนที่อาจส่งผลต่อความสัมพันธ์ระหว่างตัวแปรต้นและตัวแปรตาม
- ง) ตัวแปรที่ใช้วัด outcome เท่านั้น
👀 เฉลย

- ก) Incidence
- ข) Prevalence
- ค) Risk Ratio
- ง) Attributable Risk
👀 เฉลย

- ก) 1
- ข) 2.5
- ค) 5
- ง) 10
👀 เฉลย

- ก) OR คำนวณง่ายกว่า
- ข) ไม่ทราบจำนวนประชากรทั้งหมดที่มีความเสี่ยง (total at risk) จึงคำนวณ RR ไม่ได้
- ค) OR ให้ค่าที่แม่นยำกว่าเสมอ
- ง) RR ใช้ได้เฉพาะกับโรคเรื้อรังเท่านั้น
👀 เฉลย

- ก) OR จะสูงกว่า RR มาก
- ข) OR จะมีค่าใกล้เคียงกับ RR
- ค) OR จะต่ำกว่า RR เสมอ
- ง) ไม่มีความสัมพันธ์กัน
👀 เฉลย

- ก) RR x ความชุกของโรค
- ข) AR (Attributable Risk) x ความชุกของการสัมผัสปัจจัยเสี่ยงในประชากร
- ค) Incidence x Duration
- ง) OR ÷ RR
👀 เฉลย

- ก) เป็นตัวแปรที่อยู่ตรงกลางในสายโซ่เหตุ-ผล (intermediate) ระหว่าง exposure กับ outcome
- ข) สัมพันธ์กับ exposure และส่งผลต่อ outcome แต่ไม่ใช่ตัวแปรกลางในสายโซ่เหตุ-ผล
- ค) ไม่มีความสัมพันธ์กับทั้ง exposure และ outcome
- ง) เป็นตัวแปรตามเท่านั้น
👀 เฉลย

- ก) คำนวณค่าสถิติทดสอบ
- ข) กำหนดระดับนัยสำคัญ
- ค) ตั้งสมมติฐานว่าง (H0) และสมมติฐานทางเลือก (Ha)
- ง) แปลงเป็นค่า p-value
👀 เฉลย

- ก) ยอมรับ H0 ทั้งที่ H0 ผิด
- ข) ปฏิเสธ H0 ทั้งที่ H0 ถูกต้องจริง (ในประชากร)
- ค) เลือกใช้สถิติทดสอบผิดประเภท
- ง) เก็บข้อมูลผิดพลาด
👀 เฉลย

- ก) Independent t-test
- ข) Paired (Dependent) t-test
- ค) Pearson's Chi-square
- ง) One-way ANOVA
👀 เฉลย

- ก) Fisher's exact test
- ข) Mann-Whitney test
- ค) Kruskal-Wallis test
- ง) McNemar's test
👀 เฉลย

- ก) เพราะ SD ของข้อมูลลดลง
- ข) เพราะ Standard Error ลดลง ทำให้ CI แคบลงและตรวจจับความแตกต่างเล็กน้อยได้ง่ายขึ้น
- ค) เพราะระดับนัยสำคัญ (α) เปลี่ยนไปตามขนาดตัวอย่าง
- ง) เพราะ Type II error เพิ่มขึ้น
👀 เฉลย

- ก) SD ใช้วัดความแม่นยำของค่าเฉลี่ยตัวอย่างในการประมาณค่าเฉลี่ยประชากร ส่วน SE ใช้บรรยายการกระจายของข้อมูล
- ข) SD ใช้บรรยายการกระจายของข้อมูลดิบ ส่วน SE ใช้วัดความแม่นยำของค่าเฉลี่ยตัวอย่างในการประมาณค่าเฉลี่ยประชากร (ใช้คำนวณ CI)
- ค) SD และ SE เป็นค่าเดียวกันแต่เรียกชื่อต่างกัน
- ง) SE มีหน่วยเป็นหน่วยกำลังสองของ SD เสมอ
👀 เฉลย

- ก) ผู้ป่วยเข้าร่วมการศึกษาก่อนเวลาที่กำหนด
- ข) ผู้ป่วยหลุดจากการติดตาม (loss to follow-up) หรือสิ้นสุดการศึกษาก่อนเกิด event
- ค) ผู้ป่วยเสียชีวิตจาก event ที่สนใจศึกษา
- ง) ผู้ป่วยมี event เกิดขึ้นก่อนเริ่มการศึกษา
👀 เฉลย

- ก) กลุ่มเสี่ยงมีอัตราการเกิด event เป็น 2 เท่าของกลุ่มไม่เสี่ยง ณ ช่วงเวลานั้น
- ข) กลุ่มเสี่ยงมีโอกาสรอดชีวิตมากกว่ากลุ่มไม่เสี่ยง 2 เท่า
- ค) กลุ่มเสี่ยงมี cumulative incidence สูงกว่า 2%
- ง) ไม่สามารถแปลผลได้หากไม่ทราบ p-value
👀 เฉลย

- ก) ข้อมูลต้องมีการกระจายแบบปกติ (normal distribution)
- ข) Hazard Ratio คงที่ตลอดช่วงเวลาระหว่างสองกลุ่มที่เปรียบเทียบ
- ค) ต้องไม่มีการ censor ข้อมูลเลย
- ง) กลุ่มตัวอย่างต้องมีขนาดเท่ากันทั้งสองกลุ่ม
👀 เฉลย

- ก) 0.35
- ข) 0.47
- ค) 1.29
- ง) 12.93
👀 เฉลย

- ก) CI กว้างขึ้น เพราะมีความแปรปรวนมากขึ้น
- ข) CI แคบลง เพราะความแม่นยำของค่าประมาณเพิ่มขึ้น
- ค) CI ไม่เปลี่ยนแปลง
- ง) ไม่สามารถสรุปได้หากไม่ทราบค่า α
👀 เฉลย

- ก) ยา A ดีกว่ายา B อย่างมีนัยสำคัญทางคลินิก
- ข) ผลต่างมีนัยสำคัญทางสถิติ แต่ขนาดผลต่าง (effect size) เล็กมาก อาจไม่มีนัยสำคัญทางคลินิก
- ค) p-value ต่ำมากแสดงว่าขนาดความสัมพันธ์สูงมาก
- ง) ผลลัพธ์นี้ไม่น่าเชื่อถือเพราะ CI แคบเกินไป
👀 เฉลย

- ก) ไม่มีหลักฐานเพียงพอที่จะสรุปว่าปัจจัยเหล่านี้สัมพันธ์กับ CKD ในข้อมูลชุดนี้
- ข) การสูบบุหรี่เป็นปัจจัยที่สำคัญน้อยที่สุดในบรรดาสามปัจจัยนี้ เพราะมี p-value สูงสุด
- ค) ควรพิจารณาขนาดกลุ่มตัวอย่างและ power ของการศึกษาประกอบการแปลผล
- ง) การไม่มีนัยสำคัญทางสถิติไม่ได้แปลว่าไม่มีความสัมพันธ์กันจริงในประชากร (อาจเป็น Type II error)
👀 เฉลย

- ก) ผลต่าง 0.33 เดือนมีนัยสำคัญทางสถิติ แต่ควรพิจารณาว่ามีนัยสำคัญทางคลินิกเพียงพอหรือไม่ เมื่อเทียบกับผลข้างเคียงและค่าใช้จ่าย
- ข) เนื่องจาก p<0.05 จึงควรใช้ยาสูตรผสมนี้กับผู้ป่วยทุกราย
- ค) p-value บอกได้ว่ายาสูตรผสมนี้ปลอดภัยกว่า
- ง) ผลการศึกษานี้ไม่น่าเชื่อถือเพราะผลต่างน้อยเกินไป
👀 เฉลย

- ก) ผลลัพธ์จะเหมือนกันเสมอไม่ว่าจะใช้สถิติแบบใด
- ข) อาจได้ p-value ที่สูงกว่าความเป็นจริง ทำให้สรุปผิดว่าไม่มีนัยสำคัญ ทั้งที่จริงมีความแตกต่าง (เพิ่ม Type II error)
- ค) จะได้ค่า power ของการทดสอบสูงขึ้นเสมอ
- ง) ไม่มีผลกระทบเพราะเป็นข้อมูลเดียวกัน
👀 เฉลย

- ก) คำนวณ RR ก่อน แล้วคูณด้วยความชุกของโรคในกลุ่ม AF
- ข) คำนวณ Attributable Risk (risk difference ระหว่างกลุ่ม AF และไม่มี AF) ก่อน แล้วคูณด้วยความชุกของ AF ในประชากร (30%)
- ค) คำนวณ Odds Ratio แล้วหารด้วย Risk Ratio
- ง) ใช้ค่า Incidence rate แทน Cumulative incidence เสมอ
👀 เฉลย

- ก) เป็นคำที่ใช้แทนกันได้เสมอ ไม่มีความแตกต่าง
- ข) Chi-square บอกได้แค่ว่ามี/ไม่มีความสัมพันธ์เชิงหมวดหมู่ แต่ไม่ได้บอกขนาดหรือทิศทางของความสัมพันธ์ ต้องใช้ RR, OR หรือค่าสหสัมพันธ์เพิ่มเติม
- ค) Correlation ใช้ได้เฉพาะกับข้อมูล categorical เท่านั้น
- ง) Association หมายถึงความสัมพันธ์เชิงเหตุ-ผล (causation) เสมอ
👀 เฉลย

- ก) เพราะโมเดล logistic regression คำนวณ adjusted OR โดยธรรมชาติของโมเดลทางคณิตศาสตร์ ไม่ใช่ adjusted RR โดยตรง
- ข) เพราะ OR คำนวณง่ายกว่าเสมอในทุกสถานการณ์
- ค) เพราะ RR ใช้ไม่ได้กับข้อมูลที่มีตัวแปรกวนหลายตัว
- ง) เพราะ OR ให้ค่าที่ตรงกับความเสี่ยงจริงมากกว่า RR เสมอ
👀 เฉลย

- ก) Randomization ในขั้นตอนออกแบบการศึกษา
- ข) Stratification ในขั้นตอนวิเคราะห์ข้อมูล
- ค) เพิ่มขนาดกลุ่มตัวอย่างให้มากขึ้นเพื่อลด confounding โดยอัตโนมัติ
- ง) Matching ในขั้นตอนออกแบบการศึกษา
👀 เฉลย

ขอบเขตเนื้อหา: ความหมายของ Clinical Epidemiology, ผลลัพธ์ทางคลินิก 5Ds, ประเภทตัวแปร (Independent, Dependent, Extraneous), Population vs Sample, Random vs Systematic Error, Internal & External Validity, และ Confounding เบื้องต้น

ขอบเขตเนื้อหา: ความแตกต่างระหว่าง Standard Deviation (SD) และ Standard Error (SE), Point Estimate vs Interval Estimate, การคำนวณและแปลผล 95% Confidence Interval (CI), และหลักการ Survival Analysis (Event, Right Censoring, Hazard Rate, Hazard Ratio, Kaplan-Meier Curve, Log-Rank Test, Cox Proportional Hazards Model)

- Cumulative Incidence (Incidence Proportion): สัดส่วนของคนที่เคยไม่มีโรค แล้วกลายเป็นมีโรคในช่วงเวลาที่ติดตาม
- Incidence Rate (Incidence Density): จำนวนเคสใหม่ต่อหน่วยเวลาคน (person-time) เหมาะเมื่อระยะเวลาติดตามของแต่ละคนไม่เท่ากัน
Confidence Interval (CI) = Point estimate ± (Reliability coefficient × Standard error)

ยิ่งกลุ่มตัวอย่างใหญ่ขึ้น → CI ยิ่งแคบลง (แม่นยำขึ้น)

Sample size effect: เพิ่มขนาดตัวอย่าง (n) มากพอ → มักจะปฏิเสธ H0 ได้เสมอ (CI แคบลง) แม้ความแตกต่างจะเล็กน้อยในทางคลินิก

P-value ≠ ขนาดของความสัมพันธ์ (magnitude of association) — เช่น OR = 1.02 (P<0.001, 95%CI 1.01–1.03) มีนัยสำคัญทางสถิติ แต่ต้องถามต่อว่ามีนัยสำคัญทางคลินิกหรือไม่

Statistical significance ≠ Clinical significance — ตัวอย่าง RCT มะเร็งตับอ่อนระยะลุกลาม (Erlotinib+Gemcitabine vs Gemcitabine) พบ P-value นัยสำคัญ แต่ overall survival ต่างกันเพียง 6.24 vs 5.91 เดือน

การรายงาน P-value ที่ดี: รายงานค่าจริงแทนการเขียนแค่ "<0.05", ถ้า p=0 ให้เขียนเป็น <0.001 หรือ <0.01, ควรรายงานคู่กับ effect size เช่น OR (95%CI) เสมอ ไม่ใช่รายงานแค่ p-value โดด ๆ

Association ไม่ใช่ Correlation — ผล Chi-square ที่ไม่มีนัยสำคัญ (p>0.05) บอกได้แค่ว่า "ไม่มีความสัมพันธ์" แต่บอกไม่ได้ว่าปัจจัยไหนสำคัญน้อยที่สุด ต้องดูขนาดความสัมพันธ์ (RR, OR, Spearman's/Pearson's correlation) เพิ่มเติม

ความหมาย: ความเสี่ยงของกลุ่มสูบบุหรี่เป็น 5 เท่าของกลุ่มไม่สูบ หรือสูงกว่า 4 เท่า

- Null Hypothesis (H₀): มักเป็น “ไม่มีความแตกต่าง” หรือ “ไม่มีความสัมพันธ์” (assumed to be true until proven otherwise)
- Alternative Hypothesis (Hₐ หรือ H₁): ข้อความที่ตรงข้ามกับ H₀
ความเสี่ยงส่วนเกินที่เกิดจากการสัมผัสปัจจัยนั้นในกลุ่มที่สัมผัส (excess risk due to the exposure)

บอกว่าปัจจัยนี้สำคัญแค่ไหนในระดับสาธารณสุข และหากกำจัดปัจจัยออกไป ความเสี่ยงในประชากรจะลดลงเท่าใด

สัดส่วนของเคสในกลุ่มที่สัมผัสซึ่งอธิบายได้ด้วยปัจจัยนั้น

ตัวอย่างจาก handout  

Cohort 1 ปี: กลุ่ม AF 500 คน vs ไม่มี AF 500 คน (ความชุก AF ในประชากร = 30%)

สามารถคำนวณ Risk, RR, AR และ PAR ได้จากตารางนี้ตามสูตรข้างต้น

ขอบเขตเนื้อหา: การคำนวณ Incidence และ Prevalence, การเลือกใช้ Risk Ratio (RR) และ Odds Ratio (OR), การคำนวณ Attributable Risk (AR) และ Population Attributable Risk (PAR), การควบคุม Confounding ใน Design Phase vs Analysis Phase, และความเข้าใจเรื่อง Mediator vs Effect Modifier

ขอบเขตเนื้อหา: 6 ขั้นตอนของ Hypothesis Testing, Type I Error (α) และ Type II Error (β), กำลังการทดสอบ (Power = 1-β), ผลกระทบของ Sample Size ต่อ p-value, Multiple Comparisons Problem, และการเลือกสถิติทดสอบ (t-test, ANOVA, Chi-square, Fisher's Exact, Mann-Whitney, Kruskal-Wallis, McNemar, Logistic/Linear Regression)

ขอบเขตเนื้อหา: การประเมิน Statistical Significance เทียบกับ Clinical Significance, กับดักการแปลผล p-value (p-hacking, data dredging, post-hoc power), ข้อควรระวังใน Logistic Regression, ปัญหา Berkson Bias และ Lead-Time Bias เชิงลึก, และการบูรณาการสถิติร่วมกับการตัดสินใจทางคลินิก (EBM Decision Making)

🎯 ช่วงออกแบบ (Design Phase)

- Exclusion / Restriction
- Matching
- Randomization
🔍 ช่วงวิเคราะห์ (Analysis Phase)

- Adjustment (Standardization)
- Stratification
- Multivariate Analysis
เฉลย: ก) ความน่าจะเป็นที่จะปฏิเสธ H0 อย่างถูกต้องเมื่อ H0 เป็นเท็จจริง

Power = 1-β คือความสามารถของการทดสอบในการตรวจจับความแตกต่างที่มีอยู่จริง

เฉลย: ค) Diagnosis

5Ds ที่แท้จริงคือ Death, Disease, Discomfort, Disability, Dissatisfaction (และ Destitution) — ไม่มี Diagnosis

เฉลย: ข) จำนวนผู้ป่วยที่มีอยู่ทั้งหมด ณ จุดเวลาหนึ่งหรือช่วงเวลาหนึ่ง

Prevalence วัดผู้ป่วยที่มีอยู่ทั้งหมด (existing cases) ส่วน Incidence วัดผู้ป่วยรายใหม่ (new cases)

เฉลย: ข) Measurement bias

Measurement bias เกิดจากวิธีวัดที่ไม่เหมือนกันระหว่างกลุ่ม เช่น เครื่องมือ หรือผู้ประเมินต่างกัน

เฉลย: ข) Systematic error (Bias)

Systematic error (Bias) คือกระบวนการที่ทำให้ผลเบี่ยงเบนจากค่าจริงอย่างสม่ำเสมอ ต่างจาก Random error ที่เกิดจากโอกาส

เฉลย: ข) ผลการศึกษาถูกต้องสำหรับกลุ่มตัวอย่างที่ศึกษาโดยเฉพาะ

Internal validity = ผลถูกต้องสำหรับกลุ่มตัวอย่างที่ศึกษา ส่วน External validity (generalizability) คือนำไปใช้กับบริบทอื่นได้

เฉลย: ค) ตัวแปรกวนที่อาจส่งผลต่อความสัมพันธ์ระหว่างตัวแปรต้นและตัวแปรตาม

Extraneous variable = covariate/ตัวแปรกวน ที่อาจกระทบความสัมพันธ์ระหว่าง independent และ dependent variable

เฉลย: ข) Prevalence

เป็นสัดส่วนของผู้ที่มีพฤติกรรมนี้อยู่ ณ ช่วงเวลาที่สำรวจ จึงเป็น Prevalence ไม่ใช่ผู้ป่วยรายใหม่

เฉลย: ค) 5

Risk exposed = 100/2000 = 0.05, Risk unexposed = 80/8000 = 0.01, RR = 0.05/0.01 = 5

เฉลย: ข) ไม่ทราบจำนวนประชากรทั้งหมดที่มีความเสี่ยง (total at risk) จึงคำนวณ RR ไม่ได้

ใน case-control study เลือกกลุ่มจากสถานะโรค ไม่ทราบจำนวนผู้มีความเสี่ยงทั้งหมด จึงคำนวณ RR ไม่ได้ ต้องใช้ OR แทน

เฉลย: ข) OR จะมีค่าใกล้เคียงกับ RR

เมื่อ event พบได้น้อยมาก ค่า OR จะประมาณใกล้เคียงกับ RR

เฉลย: ข) AR (Attributable Risk) x ความชุกของการสัมผัสปัจจัยเสี่ยงในประชากร

PAR = AR × Prevalence of exposure ในประชากร ใช้บอกภาระโรคระดับสาธารณสุขที่เกิดจากปัจจัยนั้น

เฉลย: ข) สัมพันธ์กับ exposure และส่งผลต่อ outcome แต่ไม่ใช่ตัวแปรกลางในสายโซ่เหตุ-ผล

Confounder ต้องสัมพันธ์กับทั้ง exposure และ outcome แต่ต้องไม่ใช่ intermediate variable ในสายโซ่เหตุ-ผล

เฉลย: ค) ตั้งสมมติฐานว่าง (H0) และสมมติฐานทางเลือก (Ha)

ลำดับ 6 ขั้นตอนคือ: ตั้ง H0/Ha → กำหนด α → เลือกสถิติทดสอบ → คำนวณค่าสถิติ → แปลงเป็น p-value → สรุปผล

เฉลย: ข) ปฏิเสธ H0 ทั้งที่ H0 ถูกต้องจริง (ในประชากร)

Type I error (α) = ปฏิเสธ H0 ที่จริงเป็นจริง (false positive) ส่วน Type II error (β) = ไม่ปฏิเสธ H0 ที่จริงเป็นเท็จ

เฉลย: ข) Paired (Dependent) t-test

ข้อมูลก่อน-หลังในคนเดียวกันคือ paired/dependent samples จึงต้องใช้ Paired t-test

เฉลย: ก) Fisher's exact test

Fisher's exact test เหมาะกับตารางที่มี expected cell count น้อย ซึ่ง Chi-square อาจไม่แม่นยำ

เฉลย: ข) เพราะ Standard Error ลดลง ทำให้ CI แคบลงและตรวจจับความแตกต่างเล็กน้อยได้ง่ายขึ้น

n มากขึ้น → SE ลดลง (SE = SD/√n) → CI แคบลง → มีโอกาสตรวจพบความแตกต่างแม้เพียงเล็กน้อยทางคลินิก

เฉลย: ข) SD ใช้บรรยายการกระจายของข้อมูลดิบ ส่วน SE ใช้วัดความแม่นยำของค่าเฉลี่ยตัวอย่างในการประมาณค่าเฉลี่ยประชากร (ใช้คำนวณ CI)

SD บรรยายการกระจายของข้อมูล ส่วน SE บอกความแม่นยำของค่าประมาณค่าเฉลี่ย และใช้คำนวณ CI/ทดสอบสมมติฐาน

เฉลย: ข) ผู้ป่วยหลุดจากการติดตาม (loss to follow-up) หรือสิ้นสุดการศึกษาก่อนเกิด event

Right censoring คือกรณีที่ไม่ทราบว่า event จะเกิดขึ้นเมื่อใดเพราะข้อมูลถูกตัดที่ปลายด้าน follow-up (loss to follow-up หรือจบการศึกษาก่อน)

เฉลย: ก) กลุ่มเสี่ยงมีอัตราการเกิด event เป็น 2 เท่าของกลุ่มไม่เสี่ยง ณ ช่วงเวลานั้น

HR เปรียบเทียบ 'อัตรา' การเกิด event ณ จุดเวลาหนึ่ง ไม่ใช่ความน่าจะเป็นสะสมหรือการรอดชีวิตโดยตรง

เฉลย: ข) Hazard Ratio คงที่ตลอดช่วงเวลาระหว่างสองกลุ่มที่เปรียบเทียบ

Cox model ตั้งสมมติฐาน proportional hazards คือ HR คงที่ (constant) ตลอดเวลาระหว่างกลุ่มที่เปรียบเทียบ

เฉลย: ข) 0.47

SE = 12.93 / √750 ≈ 12.93 / 27.4 ≈ 0.47

เฉลย: ข) CI แคบลง เพราะความแม่นยำของค่าประมาณเพิ่มขึ้น

n มากขึ้น → SE เล็กลง → CI แคบลง (เหมือนตัวอย่างในเอกสาร: n=30 ได้ CI 15-80, n=500 ได้ CI 50-58)

เฉลย: ข) ผลต่างมีนัยสำคัญทางสถิติ แต่ขนาดผลต่าง (effect size) เล็กมาก อาจไม่มีนัยสำคัญทางคลินิก

P-value บอกความน่าเชื่อถือทางสถิติ ไม่ใช่ขนาดของความสัมพันธ์ — ต้องพิจารณา effect size (OR ใกล้ 1) ควบคู่กันเสมอ

เฉลย: ข) การสูบบุหรี่เป็นปัจจัยที่สำคัญน้อยที่สุดในบรรดาสามปัจจัยนี้ เพราะมี p-value สูงสุด

P-value ใช้เปรียบเทียบ 'ความสำคัญ' ของปัจจัยต่าง ๆ ไม่ได้ — ต้องดูขนาดความสัมพันธ์ (RR/OR/correlation) แทน (Association ไม่ใช่ Correlation)

เฉลย: ก) ผลต่าง 0.33 เดือนมีนัยสำคัญทางสถิติ แต่ควรพิจารณาว่ามีนัยสำคัญทางคลินิกเพียงพอหรือไม่ เมื่อเทียบกับผลข้างเคียงและค่าใช้จ่าย

นี่คือตัวอย่างคลาสสิกของ Statistical significance ≠ Clinical significance ต้องชั่งน้ำหนักกับ risk-benefit และบริบททางคลินิกจริง

เฉลย: ข) อาจได้ p-value ที่สูงกว่าความเป็นจริง ทำให้สรุปผิดว่าไม่มีนัยสำคัญ ทั้งที่จริงมีความแตกต่าง (เพิ่ม Type II error)

ตามตัวอย่างในเอกสาร: Independent t-test ให้ p=0.284 (ไม่มีนัยสำคัญ) แต่ Paired t-test ที่ถูกต้องให้ p=0.042 (มีนัยสำคัญ) — เลือกสถิติผิดเปลี่ยนข้อสรุปได้ทั้งหมด

เฉลย: ข) คำนวณ Attributable Risk (risk difference ระหว่างกลุ่ม AF และไม่มี AF) ก่อน แล้วคูณด้วยความชุกของ AF ในประชากร (30%)

PAR = AR × Prevalence of exposure โดย AR ต้องคำนวณจาก risk difference ระหว่างกลุ่มสัมผัสกับกลุ่มไม่สัมผัสก่อนเสมอ

เฉลย: ข) Chi-square บอกได้แค่ว่ามี/ไม่มีความสัมพันธ์เชิงหมวดหมู่ แต่ไม่ได้บอกขนาดหรือทิศทางของความสัมพันธ์ ต้องใช้ RR, OR หรือค่าสหสัมพันธ์เพิ่มเติม

Chi-square ตอบแค่คำถาม yes/no ว่ามี association หรือไม่ ส่วนขนาด/ทิศทางของความสัมพันธ์ต้องดู RR, OR, Spearman's หรือ Pearson's correlation

เฉลย: ก) เพราะโมเดล logistic regression คำนวณ adjusted OR โดยธรรมชาติของโมเดลทางคณิตศาสตร์ ไม่ใช่ adjusted RR โดยตรง

Logistic regression สร้างแบบจำลองบน log-odds จึงให้ผลลัพธ์เป็น adjusted OR โดยธรรมชาติ นี่คือเหตุผลหลักที่งานวิจัยแบบ multivariate มักรายงาน OR

เฉลย: ค) เพิ่มขนาดกลุ่มตัวอย่างให้มากขึ้นเพื่อลด confounding โดยอัตโนมัติ

การเพิ่ม n ช่วยลด random error และเพิ่ม power แต่ไม่ได้แก้ปัญหา confounding ซึ่งเป็น systematic error ต้องใช้ design/analysis phase methods แทน



## Topic 4: Research Methodology & Appraisal (ID: 3cc0abc4-4cc7-81ae-81d1-e23367a5fc7c)

4. Research Methodology and medical paper appraisal


#### 📖 สรุปเนื้อหาจากสไลด์

> ผู้บรรยาย: Amarit Tansawet, M.D., LL.B., Ph.D. (Clinical Epidemiology), Dip. Thai Board of Surgery, Dip. Thai Subspecialty Board of Endo-lap Surgery

> Data Management, AI and Biostatistics (DAB) Unit, Research Affairs, Faculty of Medicine, Chulalongkorn University

> 📄 ไฟล์สไลด์ต้นฉบับ

โครงสร้างการบรรยาย: Part I – Research Methodology · Part II – Article Appraisal

🟢 ชุดที่ 1 — Mock Test ระดับง่าย (30 ข้อ)

🟡 ชุดที่ 2 — Mock Test ระดับง่าย-ปานกลาง (30 ข้อ)

🟠 ชุดที่ 3 — Mock Test ระดับปานกลาง (30 ข้อ)

🔴 ชุดที่ 4 — Mock Test ระดับปานกลาง-ยาก (30 ข้อ)

🟣 ชุดที่ 5 — Mock Test ระดับยาก / บูรณาการและสถานการณ์ทางคลินิก (30 ข้อ)


### Part I — Research Methodology


#### 1. Epidemiology & Clinical Epidemiology

Epidemiology — การศึกษา distribution (การกระจาย) และ determinants (ปัจจัยกำหนด) ของภาวะหรือเหตุการณ์ที่เกี่ยวข้องกับสุขภาพ ในประชากรที่ระบุไว้ และการนำผลการศึกษานั้นไปใช้ควบคุมปัญหาสุขภาพ

วัตถุประสงค์ของ Epidemiology

- ระบุสาเหตุ (etiology) ของโรคและปัจจัยเสี่ยงที่เกี่ยวข้อง
- ประเมินขนาดของปัญหาโรคในชุมชน
- ศึกษา natural history และ prognosis ของโรค
- ประเมินมาตรการป้องกันและรักษา ทั้งที่มีอยู่เดิมและที่พัฒนาขึ้นใหม่ รวมถึงรูปแบบการให้บริการสุขภาพ
- เป็นพื้นฐานของการกำหนดนโยบายสาธารณะ ทั้งด้านสิ่งแวดล้อม พันธุกรรม และปัจจัยทางสังคม-พฤติกรรม
Clinical Epidemiology — ศาสตร์ของการ ทำนาย ผลลัพธ์ในผู้ป่วยรายบุคคล โดยการนับเหตุการณ์ทางคลินิกในกลุ่มผู้ป่วยที่มีลักษณะคล้ายกัน และใช้ระเบียบวิธีทางวิทยาศาสตร์ที่รัดกุมเพื่อให้การทำนายนั้นแม่นยำ


#### 2. กระบวนการวิจัย (Research process)

```
Research question → Available evidence → มีคำตอบที่ดีแล้ว?
   ├─ Yes → Stop
   └─ No (มี GAP) → Design → Population → Methodology → Measurement → Statistics → Conclusion
```

หัวใจคือการเริ่มจาก คำถามวิจัย แล้วทบทวนหลักฐานที่มีอยู่ก่อนเสมอ ถ้าหลักฐานเดิมดีพออยู่แล้วก็ไม่จำเป็นต้องทำวิจัยซ้ำ — ต้องหา gap ให้เจอ


#### 3. คำถามวิจัยทางคลินิก & PICO

ตัวอย่างคำถามจาก background → foreground:

การตั้งคำถามด้วย PICO ตามชนิดของคำถาม

- Therapy / Harm: Patient or Population – Intervention or Exposure – Comparator – Outcome
- Prognosis: Patient – Exposure – Comparator – Outcome หรือ Patient – Exposure (time) – Outcome
- Diagnostic test: Patient – Exposure (test) – Outcome (criterion/gold standard)
5 ชนิดของ foreground clinical question

- Therapy — ผลของ intervention ต่อ patient-important outcomes (อาการ, function, morbidity, mortality, ค่าใช้จ่าย)
- Harm — ผลของสิ่งที่อาจเป็นอันตราย (รวมถึงการรักษาในข้อ 1) ต่อ patient-important outcomes
- Differential diagnosis — ความถี่ของโรคที่เป็นสาเหตุ ในผู้ป่วยที่มา present ด้วยลักษณะทางคลินิกแบบหนึ่ง
- Diagnosis — ความสามารถของ test ในการแยกคนที่เป็นและไม่เป็นโรคเป้าหมาย
- Prognosis — การประเมินการดำเนินโรคของผู้ป่วยในอนาคต

#### 4. การสืบค้นหลักฐาน (EBM resources)

ลำดับชั้นการค้นหา — ไล่จากบนลงล่าง:

- Summaries and Guidelines
- Pre-appraised research — Synopses และ Systematic reviews
- Non-preappraised research และ Clinical queries

#### 5. Population & Conceptual framework

- Population → (sampling) → Sample; Sample statistic → (inference) → Population parameter
- ต้องมี conceptual framework ที่แสดงความสัมพันธ์เชิงเหตุผลระหว่างตัวแปร — ไม่ใช่แค่ผังขั้นตอนการทำงาน (flowchart การดำเนินงานไม่ใช่ conceptual framework)

#### 6. Study designs

Clinical trial — งานวิจัยที่ผู้วิจัย กำหนด ให้ผู้เข้าร่วมได้รับ intervention ตั้งแต่หนึ่งอย่างขึ้นไป เพื่อดูว่าเกิดอะไรขึ้นในคน (RCT เป็น subset ของ clinical trial)

การเลือก design ให้เหมาะกับคำถาม


##### 6.1 RCT — gold standard ของ therapeutic study

- วิธีสุ่ม: simple randomization, block randomization
- สิ่งที่บั่นทอนความน่าเชื่อถือ (possible underminers)
- ต้องวางแผน การวิเคราะห์เมื่อมี protocol deviation (ITT vs per-protocol)

##### 6.2 Cohort study

- เริ่มจาก defined population → แบ่งเป็น exposed / not exposed → ตามไปดู cases / noncases
- ทิศทางเวลา: Prospective (exposure และ disease ยังไม่เกิด ณ ปัจจุบัน) · Retrospective (เกิดไปแล้วทั้งคู่) · Ambidirectional (ผสม)
- ใช้สร้าง prediction model ได้ (Risk 1, 2, 3 → Outcome)

##### 6.3 Case-control study

เริ่มจาก cases และ controls แล้วย้อนดู exposure

แหล่งของ cases

- โรงพยาบาลเดียว vs หลายโรงพยาบาล — โรงพยาบาลเดียว exposure อาจจำเพาะกับที่นั่น
- Tertiary care center vs General hospital — tertiary อาจสัมพันธ์กับโรครุนแรงเท่านั้น → healthcare access / referral bias
Prevalent vs incident cases

- ถ้าใช้ prevalent cases จะเกิด Prevalence-Incidence (Neyman) bias — exposure ที่พบอาจสัมพันธ์กับ การรอดชีวิต มากกว่า การเกิดโรค (เพราะคนที่ตายหรือหายไปแล้วไม่ถูกนับ)
การเลือก controls — ต้องมีอัตรา exposure ที่เป็นตัวแทนประชากรจริง มิฉะนั้นความต่างที่เห็นจะไม่ใช่ของจริง

แหล่งของ controls

- Hospitalized patients — ง่าย แต่อาจไม่เป็นตัวแทนประชากรที่ cases มา; เลือกได้ว่าจะใช้ diagnosis เฉพาะบางโรค หรือผู้ป่วยอื่นทั้งหมด
- Non-hospitalized controls
Multiple controls

- ชนิดเดียวกันหลายคน (เช่น case:control = 1:4) → เพิ่ม power ของการทดสอบ
- ต่างชนิดกัน → ช่วยตีความ เช่น การได้รับรังสี: ถ้าเทียบกับ cancer control แล้วต่าง = ความเสี่ยงจำเพาะต่อ brain tumor (recall bias ไม่น่าเกิด); ถ้าเทียบกับ normal control แล้วต่าง = ความเสี่ยงต่อมะเร็งโดยรวม (recall bias เป็นไปได้)
Matching

- ทำเพื่อให้ cases และ controls คล้ายกัน
- ข้อควรระวัง: จับคู่หลายลักษณะพร้อมกันทำได้ยากมาก · ไม่สามารถประเมินผลของลักษณะที่นำมา match ได้ · ระวัง unplanned matching

##### 6.4 เปรียบเทียบ Cohort vs Case-control


#### 7. Measurement — Reliability vs Validity

- Reliability (Precision) — วัดซ้ำแล้วได้ค่าใกล้เคียงกัน (กระจุกตัว)
- Validity (Accuracy) — ค่าที่วัดได้ตรงกับค่าจริง (เข้าเป้า)
- ทั้งสองอย่างเป็นอิสระต่อกัน: สูง/ต่ำสลับกันได้ 4 แบบ (แม่นและตรง / แม่นแต่ไม่ตรง / ไม่แม่นแต่เฉลี่ยตรง / ทั้งไม่แม่นไม่ตรง)

#### 8. Error

ความคลาดเคลื่อนในงานวิจัยแบ่งออกเป็น 2 กลุ่มใหญ่ ตามธรรมชาติว่าเกิดขึ้นโดยบังเอิญหรือเกิดจากข้อบกพร่องเชิงระบบ


##### 8.1 Random error (ความคลาดเคลื่อนแบบสุ่ม)

เกิดจากความผันแปรตามธรรมชาติของการสุ่มตัวอย่าง — ลดได้ด้วยการเพิ่มขนาดตัวอย่าง (sample size) แต่ไม่มีทางกำจัดให้หมดไปได้

> 🔎 ความสัมพันธ์กับ sample size: ยิ่งขนาดตัวอย่างเล็ก ยิ่งเสี่ยง Type II error สูง (power ต่ำ) — การคำนวณ sample size ล่วงหน้าคือการควบคุม random error ทั้งสองชนิดให้อยู่ในระดับที่ยอมรับได้


##### 8.2 Systematic error (ความคลาดเคลื่อนเชิงระบบ / Bias)

เกิดจากข้อบกพร่องในการออกแบบ ดำเนินการ หรือวิเคราะห์งานวิจัย — เพิ่ม sample size ไม่ช่วยลด ต้องแก้ที่การออกแบบเท่านั้น แบ่งเป็น 3 กลุ่มหลัก:

(1) Selection bias — อคติจากการคัดเลือก/ติดตามกลุ่มตัวอย่างที่ไม่เป็นตัวแทนที่แท้จริง เกิดขึ้นได้ 3 จังหวะตลอดกระบวนการวิจัย

จังหวะที่ 1 — ตอนคัดเข้า (Enrollment)

- Neyman (prevalence-incidence) bias, Referral/healthcare access bias, การเลือก controls ที่ไม่เหมาะสม — รายละเอียดและตัวอย่างเต็มอยู่ในหัวข้อ 6.3 Case-control study ด้านบน
- Berkson's bias — เกิดเมื่อใช้ผู้ป่วยในโรงพยาบาลเป็นทั้ง cases และ controls คนที่มีทั้ง exposure และ disease พร้อมกันมีโอกาสถูกรับเข้าโรงพยาบาลสูงกว่าคนที่มีอย่างใดอย่างหนึ่ง ทำให้ความสัมพันธ์ที่เห็นในกลุ่มผู้ป่วยโรงพยาบาลสูงเกินจริงหรือกลับทิศทาง
- Volunteer (self-selection) bias — คนที่สมัครใจเข้าร่วมวิจัยมักมีลักษณะต่างจากประชากรทั่วไป (ใส่ใจสุขภาพกว่า, มีแรงจูงใจเฉพาะ)
- Healthy worker effect — คนทำงานมีสุขภาพดีกว่าประชากรทั่วไปโดยธรรมชาติ (คนป่วยหนักออกจากงานหรือไม่ได้เข้าทำงานตั้งแต่แรก) ทำให้เปรียบเทียบกับประชากรทั่วไปแล้วดูปลอดภัยเกินจริง
- Ascertainment bias — เกิดเมื่อวิธีการค้นหา/ระบุตัวผู้เข้าร่วมงานวิจัย (หรือการตรวจหา exposure/disease) ไม่เท่ากันระหว่างกลุ่มที่เปรียบเทียบ ส่งผลให้กลุ่มหนึ่งมีโอกาสถูกระบุเข้ามาอยู่ในกลุ่มตัวอย่างมากกว่าอีกกลุ่ม — เป็นคนละกันกับ Detection bias แต่เน้นที่ขั้นตอนคัดเข้า/ระบุตัว ไม่ใช่ขั้นวัดผล outcome ซ้ำ
จังหวะที่ 2 — ระหว่างติดตาม (Follow-up)

- Loss to follow-up / Attrition bias — การถอนตัวออกจากการศึกษาไม่ได้เกิดแบบสุ่ม แต่สัมพันธ์กับ exposure หรือ outcome (เช่น คนที่ทนผลข้างเคียงของยาไม่ไหวถอนตัวออกจากกลุ่มทดลองมากกว่ากลุ่มควบคุม) เกณฑ์ที่ยอมรับได้คือไม่ควรเกิน ~20% และใกล้เคียงกันระหว่างกลุ่ม
จังหวะที่ 3 — ตอนวิเคราะห์ (Analysis)

- Per-protocol analysis bias — วิเคราะห์เฉพาะคนที่ทำตาม protocol ครบแทนที่จะวิเคราะห์ตามกลุ่มที่ถูกสุ่มไว้ (ITT) คน compliance ดีมักมีลักษณะพื้นฐานต่างจากคนที่ไม่ทำตาม — นี่คือเหตุผลที่ ITT เป็นมาตรฐานทองในการวิเคราะห์ RCT
> 🔎 วิธีแยก Selection bias จาก Confounding และ Random error: ถาม "เกิดจากวิธีคัดเลือก/ติดตามคนหรือไม่" → selection bias · ถาม "มีตัวแปรที่สามสัมพันธ์กับทั้งคู่หรือไม่" → confounding (ปรับด้วยสถิติทีหลังได้) · ถาม "เกิดจากขนาดตัวอย่างเล็กเกินไปหรือไม่" → random error (เพิ่ม sample size แก้ได้) — selection bias ส่วนใหญ่แก้ทีหลังด้วยสถิติไม่ได้ ต้องป้องกันตั้งแต่ขั้นออกแบบเท่านั้น

(2) Information bias — อคติที่เกิดจากการวัดผลหรือเก็บข้อมูลผิดพลาด หลังจากคัดเลือกกลุ่มตัวอย่างมาแล้ว แบ่งย่อยได้เป็น:

> ⚠️ การป้องกัน Information bias หลัก: ใช้ blinding (single/double-blind), ใช้เกณฑ์วินิจฉัย/เครื่องมือวัดที่เป็นมาตรฐานเดียวกันทุกกลุ่ม, ใช้ข้อมูลจากแหล่งที่บันทึกไว้ก่อนเกิด outcome (เช่น เวชระเบียนที่บันทึกล่วงหน้า) แทนการถามย้อนหลัง

(3) Confounding — ดูรายละเอียดเต็มในหัวข้อ 9 ด้านล่าง (นิยาม 3 เงื่อนไข, ตัวอย่าง, และวิธีจัดการทั้งระดับ design และ statistics)


##### 8.3 สรุปความต่างที่มักสับสน


#### 9. Confounding

นิยาม: ตัวแปรที่สัมพันธ์กับ ทั้ง outcome และ exposure แต่ ไม่อยู่บน causal pathway ระหว่างทั้งสอง

ตัวอย่างคลาสสิก: ยอดขายไอศกรีม ↔ อาชญากรรมรุนแรง โดยมี อุณหภูมิ เป็น confounder → เป็นแค่ spurious association

> ⚠️ ASSOCIATION ≠ CAUSATION

การกำจัด confounding

ทำไม RCT ถึงดี? เพราะการสุ่มตัดความสัมพันธ์ระหว่าง exposure กับ confounder ทั้งที่รู้จักและไม่รู้จัก

ขั้นตอนปฏิบัติเพื่อจัดการ confounder

- Recognize — รู้ว่ามีอะไรบ้าง
- ทบทวนวรรณกรรม และปรึกษาผู้เชี่ยวชาญเนื้อหา (content expert)
- คิดและวาด causal diagram
- ออกแบบการศึกษา และ/หรือ เลือกวิธี statistical adjustment ที่เหมาะสม

#### 10. Bradford Hill criteria (เกณฑ์ประเมินความเป็นเหตุเป็นผล)

ใช้ประเมินว่าความสัมพันธ์ที่พบ (association) จะนำไปสู่การสรุปเรื่องความเป็นเหตุเป็นผล (causation) ได้หนักแน่นเพียงใด — ไม่จำเป็นต้องครบทุกข้อจึงจะสรุปว่าเป็นเหตุเป็นผล เป็นเครื่องมือช่วยคิดมากกว่าเกณฑ์ตายตัว

> ⚠️ ข้อสำคัญที่มักออกข้อสอบ:

> - Bradford Hill ไม่ได้เสนอว่าต้องครบทุกข้อ — เขาเสนอว่านี่คือ มุมมอง (viewpoints) สำหรับช่วยพิจารณา ไม่ใช่ checklist ที่ต้องผ่านครบทุกข้อ

> - ข้อที่จำเป็นจริง ๆ มีเพียงข้อเดียว — Temporality เพราะนิยามของเหตุผลกำหนดไว้เลยว่าเหตุต้องเกิดก่อนผล

> - Specificity อ่อนที่สุดในปัจจุบัน — โรคหลายชนิด (เช่น มะเร็ง) เกิดจากหลาย exposure ได้ และ 1 exposure ก็อาจก่อหลายโรคได้

> - Association ≠ Causation เสมอ 9 ข้อนี้เป็นเพียงเครื่องมือช่วยพิจารณา ไม่ใช่สูตรคณิตศาสตร์ตายตัวที่พิสูจน์ความเป็นเหตุเป็นผลได้โดยสมบูรณ์


#### 11. Ethics

การวิจัยในคนต้องผ่านการพิจารณาด้านจริยธรรมเสมอ เพราะงานวิจัยทางการแพทย์มีความเสี่ยงต่อผู้เข้าร่วมโดยตรง ทั้งทางกายภาพและจิตใจ


##### 11.1 หลักจริยธรรมหลัก (Belmont Report / CIOMS)


##### 11.2 กระบวนการก่อนทำวิจัย

- เสนอโครงการต่อ Ethics Committee / IRB (Institutional Review Board) ก่อนเริ่มเก็บข้อมูลเสมอ 2. รอการอนุมัติเป็นลายลักษณ์อักษร 3. จดทะเบียนงานวิจัย (เช่น ClinicalTrials.gov, Thai Clinical Trials Registry) โดยเฉพาะ clinical trial

##### 11.3 กลุ่มเปราะบาง (Vulnerable populations)

ต้องการการปกป้องเพิ่มเติมเนื่องจากมีความสามารถในการตัดสินใจจำกัด หรือเสี่ยงต่อการถูกชักจูง (coercion) เช่น:

- เด็ก, ผู้ป่วยจิตเวช, หญิงตั้งครรภ์ — ต้องมี consent จากผู้แทนโดยชอบธรรม/ผู้ปกครองร่วมด้วย
- นักโทษ, ทหาร — มีความสัมพันธ์เชิงอำนาจกับผู้เชิญชวน อาจเกิดการกดดันให้เข้าร่วมโดยไม่ชัดเจน
- ลูกศิษย์/ผู้ใต้บังคับบัชาของผู้วิจัย — อาจกลัวผลกระทบต่อเกรด/ความสัมพันธ์หากปฏิเสธเข้าร่วม

##### 11.4 การออกแบบที่เกี่ยวข้องกับจริยธรรมโดยตรง


##### 11.5 เอกสาร/มาตรฐานสากลที่เกี่ยวข้อง

- Declaration of Helsinki — หลักจริยธรรมสากลสำหรับการวิจัยทางการแพทย์ที่เกี่ยวข้องกับมนุษย์
- ICH-GCP (Good Clinical Practice) — มาตรฐานการดำเนินการศึกษาทางคลินิกที่โลกยอมรับ
- พ.ร.บ. สุขภาพแห่งชาติ และกฎหมายสาธารณสุขผู้รับสาร (ประเทศไทย) — คุ้มครองข้อมูลส่วนบุคคลของผู้เข้าร่วมวิจัย

### Part II — Article Appraisal


#### 1. EBM คืออะไร

EBM คือการทำงานร่วมกับผู้ป่วยอย่างใส่ใจ เพื่อช่วยแก้ไขหรือรับมือกับปัญหาด้านสุขภาพกาย ใจ และสังคม โดยต้องรู้และเข้าใจหลักฐานจากงานวิจัยทางคลินิก พร้อมทั้งสร้างกลยุทธ์ในการนำหลักฐานที่ดีที่สุดไปใช้จริงในเวชปฏิบัติ

3 เสาหลักของ EBM

- Best research evidence
- Patient preference
- Clinical circumstance

#### 2. การปฏิบัติ EBM — 5A

- Ask — ตั้งคำถามที่ตอบได้
- Acquire — ค้นหาบทความ
- Appraise — ประเมินคุณภาพหลักฐาน
- Apply — นำไปใช้ในเวชปฏิบัติ
- Assess — ประเมินผลการนำไปใช้

#### 3. กรอบการ appraise บทความ


#### 4. Checklist ตามชนิดของการศึกษา


##### 4.1 Therapy

Risk of bias — กลุ่มเริ่มต้นด้วย prognosis เท่ากันหรือไม่?

- ผู้ป่วยถูก randomize หรือไม่?
- Randomization ถูก conceal หรือไม่?
- กลุ่มต่าง ๆ คล้ายกันในแง่ prognostic factors ที่รู้จักหรือไม่?
Prognostic balance ยังคงอยู่ตลอดการศึกษาหรือไม่?

- มีการ blind มากน้อยเพียงใด?
กลุ่มยัง balance ตอนจบการศึกษาหรือไม่?

- Follow-up ครบถ้วนหรือไม่?
- วิเคราะห์ผู้ป่วยตามกลุ่มที่ถูกสุ่มไว้หรือไม่ (ITT)?
- การทดลองถูกหยุดก่อนกำหนดหรือไม่?
What are the results?

- ขนาดของผลการรักษาเป็นอย่างไร — ARR vs RRR, NNT
- ค่าประมาณแม่นยำแค่ไหน (precision / CI)
Applicability

- ผู้ป่วยในงานวิจัยคล้ายผู้ป่วยของเราหรือไม่?
- พิจารณา patient-important outcomes ครบหรือไม่?
- ประโยชน์ที่คาดว่าจะได้คุ้มกับอันตรายและค่าใช้จ่ายหรือไม่?

##### 4.2 Harm

Risk of bias — ถ้าเป็น Cohort

- ผู้ป่วยคล้ายกันในแง่ prognostic factors ที่สัมพันธ์กับ outcome หรือไม่ (หรือมี statistical adjustment แก้ความไม่สมดุล)?
- วิธีและสถานการณ์ในการตรวจหา outcome เหมือนกันทั้งสองกลุ่มหรือไม่?
- Follow-up ครบถ้วนพอหรือไม่?
Risk of bias — ถ้าเป็น Case-control

- Cases และ controls คล้ายกันในแง่ข้อบ่งชี้/สถานการณ์ที่นำไปสู่การได้รับ exposure หรือไม่ (หรือมี statistical adjustment)?
- วิธีและสถานการณ์ในการระบุ exposure เหมือนกันทั้งสองกลุ่มหรือไม่?
What are the results? — ความสัมพันธ์ระหว่าง exposure กับ outcome แข็งแรงแค่ไหน · ค่าประมาณความเสี่ยงแม่นยำแค่ไหน

Applicability — ผู้ป่วยคล้ายกันหรือไม่ · follow-up นานพอหรือไม่ · exposure คล้ายกับที่ผู้ป่วยเราเจอหรือไม่ · ขนาดของความเสี่ยงเท่าใด · exposure นั้นมีประโยชน์อะไรบ้างหรือไม่


##### 4.3 Prognosis

Risk of bias

- กลุ่มตัวอย่างเป็นตัวแทนหรือไม่?
- แบ่งผู้ป่วยเป็นกลุ่มที่ homogeneous ทาง prognosis หรือไม่?
- Follow-up ครบถ้วนพอหรือไม่?
- เกณฑ์ outcome เป็นปรนัยและไม่มีอคติหรือไม่?
What are the results? — โอกาสเกิด outcome ตามเวลาเป็นเท่าใด (survival curve) · ค่าประมาณแม่นยำแค่ไหน

Applicability — ผู้ป่วยและการดูแลคล้ายของเราหรือไม่ · follow-up นานพอหรือไม่ · ใช้ผลนี้จัดการผู้ป่วยได้จริงหรือไม่


##### 4.4 Diagnostic test

Risk of bias

- ผู้เข้าร่วมเป็นตัวแทนของผู้ที่มา present ด้วย diagnostic dilemma หรือไม่?
- เปรียบเทียบกับ reference standard ที่เหมาะสมและเป็นอิสระหรือไม่?
- ผู้แปลผล test และ reference standard blind ต่อกันหรือไม่?
- ผู้ป่วยทุกคนได้รับ reference standard เดียวกันไม่ว่าผล test จะออกมาอย่างไรหรือไม่?
What are the results? — Likelihood ratio (LR) ของผลตรวจในแต่ละช่วงเป็นเท่าใด

Applicability

- ความทำซ้ำได้ของผลและการแปลผลจะดีพอในสถานพยาบาลของเราหรือไม่?
- ผลการศึกษาใช้กับผู้ป่วยของเราได้หรือไม่?
- ผลตรวจจะเปลี่ยนแผนการรักษาหรือไม่?
- ผู้ป่วยจะได้ประโยชน์จากการตรวจนี้จริงหรือไม่?

#### 5. เครื่องมือช่วยประเมิน

แยกให้ชัดว่าเป็นเครื่องมือคนละประเภทกัน:

- Appraisal tool — ประเมินคุณภาพงานวิจัยโดยรวม (เช่น CASP)
- Reporting checklist — ตรวจความครบถ้วนของการรายงาน (เช่น CONSORT, STROBE, PRISMA)
- Risk of bias assessment tool — ประเมินความเสี่ยงต่ออคติอย่างเป็นระบบ (เช่น RoB 2 สำหรับ RCT)

##### 5.1 CASP (Critical Appraisal Skills Programme) — เจาะลึก

CASP เป็นองค์กรจากสหราชอาณาจักรที่พัฒนา checklist สำหรับการทำ critical appraisal โดยเฉพาะ ออกแบบมาเพื่อใช้ในการสอน/อภิปรายกลุ่ม (journal club) เป็นหลัก ภาษาที่ใช้เข้าใจง่าย ไม่ซับซ้อนเท่า risk-of-bias tool เชิงโครงสร้างสูงอย่าง RoB 2 หรือ AMSTAR 2

โครงสร้างหลัก: 3 ส่วน (ตรงกับกรอบการ appraise ที่อยู่ในหน้านี้เลย)

> โครงนี้สอดคล้องกับกรอบการ appraise ในหัวข้อ 3 ของหน้านี้ (Validity · Result · Applicability) โดยตรง

Checklist ที่ CASP มีให้ (แยกตามชนิดการศึกษา):

- Systematic Reviews (ทั้งแบบมี meta-analysis ของ RCT และของ observational studies)
- Randomised Controlled Trials (RCT)
- Cohort Studies
- Case Control Studies
- Diagnostic Studies
- Qualitative Studies
- Economic Evaluations
- Clinical Prediction Rule
ข้อควรระวังเวลาใช้:

- ต้องเลือก checklist ให้ตรงกับ study design — เช่น ห้ามนำ checklist ของ RCT ไปใช้กับงาน qualitative
- ข้อคำถามใน CASP ออกแบบมาเพื่อกระตุ้นการอภิปราย ไม่ใช่ signalling questions แบบ RoB 2/AMSTAR 2 จึงไม่ได้ให้คะแนนหรือเกณฑ์การเข้า/ออกที่เคร่งครัดเท่ากัน
- หากตอบ"Can't tell" จำนวนมาก อาจสะท้อนว่างานวิจัยนั้นรายงานไม่โปร่งใสพอ 4 การอนุมานว่าทำจริง (ไม่ใช่เกณฑ์ที่เคร่งครัดเท่า RoB 2 ที่มี domain ชัดเจน)
- ใช้เป็นจุดเริ่มต้นสำหรับนักศึกษา/มือใหม่ หากงานสำคัญ (เช่น systematic review, dissertation) อาจต้องใช้ formal tool เช่น RoB 2, ROBINS-I, AMSTAR 2 หรือ JBI เพิ่มเติม

#### 6. Resources

- Catalogue of Bias — https://catalogofbias.org/biases/
- CASP tools & checklists — https://casp-uk.net/casp-tools-checklists/

#### 🎯 ประเด็นสำคัญสำหรับทบทวน

- ความต่างระหว่าง random error (type I/II) กับ systematic error (bias, confounding) — และวิธีจัดการแต่ละแบบ
- นิยาม confounder 3 เงื่อนไข: สัมพันธ์กับ exposure · สัมพันธ์กับ outcome · ไม่อยู่บน causal pathway
- Bias ใน case-control: Neyman bias, referral/healthcare access bias, การเลือก control ที่ทำให้ exposure rate เพี้ยน
- ตารางเปรียบเทียบ cohort vs case-control (โดยเฉพาะ case-control เหมาะกับ rare disease, cohort เหมาะกับ rare exposure)
- Reliability ≠ Validity
- ARR vs RRR vs NNT และการแปลผล likelihood ratio
- Bradford Hill criteria ทั้ง 9 ข้อ

#### Session 4

Date: 4 Sep 2026  

Time: 09:00 – 12:00

Title (EN): Research Methodology and medical paper appraisal  

Title (TH): ระเบียบวิธีวิจัยและการพิจารณาวารสารงานวิจัย

Instructor: ดร.นพ. อมฤต ดาลเหวด

- Compliance — ผู้ป่วยไม่ทำตามที่กำหนด
- Co-intervention — ได้รับการรักษาอื่นเพิ่มเติมไม่เท่ากันระหว่างกลุ่ม
- Contamination — กลุ่มควบคุมได้รับ intervention ไปด้วย
- Neighborhood controls — ไม่ดี เพราะมีปัจจัยด้านสิ่งแวดล้อมร่วมกัน
- Best friend controls — ไม่ดี เพราะมีปัจจัยด้านพฤติกรรมร่วมกัน
- Type I error (alpha)
- Type II error (beta)
- Confounding
- Bias — Selection bias, Information bias
- ตัวอย่างที่ 1 (เวชพันธุศาสตร์): ครอบครัวที่มีสมาชิกเป็นโรคทางพันธุกรรมอยู่แล้วมักถูกส่งตรวจคัดกรองหรือมาสมัครเข้าร่วมงานวิจัยมากกว่าครอบครัวทั่วไป ทำให้ประมาณการถ่ายทอดทางพันธุกรรมดูสูงเกินจริง
- ตัวอย่างที่ 2 (การเฝ้าระวังทางการแพทย์): กลุ่มที่ได้รับการตรวจคัดกรองถี่หรือติดตามใกล้ชิดกว่า (เช่น เพราะอยู่ในโครงการ screening) จะตรวจเจอ disease ได้มากกว่ากลุ่มที่ไม่ได้เฝ้าระวังเพิ่ม → ทำให้ดูเหมือนมีความสัมพันธ์กับ exposure สูงเกินจริง ทั้งที่อัตรา disease จริงอาจเท่ากันทั้งสองกลุ่ม
- วิธีป้องกัน: ใช้เกณฑ์การค้นหา/วินิจฉัยเดียวกันทุกกลุ่ม หรือเก็บข้อมูลจากแหล่งที่มีความเข้มงวด (surveillance intensity) ใกล้เคียงกันระหว่างกลุ่ม


## Topic 5: Basic SQL (ID: 3cc0abc4-4cc7-810d-82b7-c10b4ee9ff67)

5. Data Collection, Cleaning, and Preparation — Basic SQL

🎯 6.1 SELECT / FROM — เลือกข้อมูล / ระบุตาราง

✨ 6.2 DISTINCT — ขจัดข้อมูลที่ซ้ำกัน

🔍 6.3 WHERE — กำหนดเงื่อนไขในการเลือกข้อมูล

↕️ 6.4 ORDER BY — เรียงลำดับข้อมูล

🔢 6.5 COUNT — นับจำนวนข้อมูลของคอลัมน์

➕ 6.6 ฟังก์ชันการคำนวณ (Aggregate Functions)

📊 6.7 GROUP BY — จัดกลุ่มข้อมูลตามคอลัมน์ที่กำหนด

🔗 6.8 JOIN — เชื่อมโยงข้อมูลระหว่างตาราง


#### Session 5

Date: 6 Sep 2026  

Time: 09:00 – 12:00

Title (EN): Data Collection, Cleaning, and Preparation for Healthcare Analysis — Basic SQL  

Title (TH): การรวบรวมข้อมูล การทำความสะอาด และการเตรียมการสำหรับการวิเคราะห์การดูแลสุขภาพ — Basic SQL

Instructor: ดร.นพ. เสริมเกียรติ / ฝ่ายข้อมูล รพ. จุฬาฯ


#### สรุปเนื้อหา: Structured Query Language (SQL)

- SQL (Structured Query Language) คือภาษาคอมพิวเตอร์ที่ใช้สำหรับจัดการฐานข้อมูลโดยเฉพาะ เช่น การสร้างฐานข้อมูล การเพิ่มข้อมูล การแก้ไขข้อมูล และการลบข้อมูล

##### 1. ภาษา SQL คืออะไร

- มักใช้ร่วมกับระบบจัดการฐานข้อมูลเชิงสัมพันธ์ (RDBMS) ที่นิยม เช่น MS Access, MS SQL Server, Oracle, MySQL
- ดาวน์โหลดโปรแกรม DB Browser for SQLite: https://sqlitebrowser.org/dl/
- เป็นภาษามาตรฐานสำหรับจัดการและเรียกดูข้อมูลในฐานข้อมูล มีจุดเริ่มต้นจากการพัฒนาโดยบริษัท IBM
- ใช้กันอย่างแพร่หลาย เพราะเรียนรู้และใช้งานได้ไม่ยาก คำสั่งส่วนใหญ่ใช้คำภาษาอังกฤษที่เข้าใจง่าย

##### 2. เครื่องมือที่ใช้ในคลาส

- ดาวน์โหลดชุดข้อมูลสำหรับฝึก (QR code ที่ 2)
มี 3 ตาราง เชื่อมกันด้วย key (🔑):


##### 3. โครงสร้างสำหรับเก็บข้อมูล (Table)

ตาราง CLINICLCT

- CLINICLCT 🔑
- CLINICTYPENAME
- HN_CODE
ตาราง DIAG

- CLINICLCT 🔑
- NAME

### 📖 1. ภาษา SQL คืออะไร

- VSTDATE
ดาวน์โหลดโปรแกรม DB Browser for SQLite: https://sqlitebrowser.org/dl/

ดาวน์โหลด ชุดข้อมูลสำหรับฝึก (QR code ที่ 2 ในสไลด์)


### 🛠️ 2. เครื่องมือที่ใช้ในคลาส

มี 3 ตาราง เชื่อมกันด้วย key 🔑:


### 🗂️ 3. โครงสร้างสำหรับเก็บข้อมูล (Table)

- THAINAME

### 📥 4. การนำเข้าไฟล์ฐานข้อมูล (Import CSV)

ใน DB Browser for SQLite: ลากไฟล์ CSV วางในโปรแกรม → เลือก "Import CSV file(s)" → ตั้งชื่อตาราง (Table name) → กำหนด Column names in first line, Field separator, Quote character, Encoding (UTF-8), Trim fields → กด OK


### 🔢 5. ลำดับคำสั่ง SQL (Syntax Order)


##### 6. เรียนรู้คำสั่งพื้นฐาน SQL

6.1 SELECT / FROM — เลือกข้อมูลที่ต้องการจากตาราง / ระบุตารางที่ต้องการดึงข้อมูล

6.2 DISTINCT — ขจัดรายการข้อมูลที่ซ้ำกัน

แบบฝึก: (1) แสดงข้อมูลทุกคอลัมน์จากตาราง CLINICLCT ด้วย SELECT * FROM CLINICLCT; (2) แสดงเฉพาะคอลัมน์ CLINICLCT, NAME, CLINICTYPENAME (3) ตั้งชื่อคอลัมน์ใหม่ด้วย AS

```
SELECT column_name(s)
FROM table_name
```

แบบฝึก: (4) แสดง HN_CODE โดยไม่ให้ซ้ำ ตาราง DIAG (5) แสดงรหัสคลินิกโดยไม่ให้ซ้ำ ตาราง DIAG

```
SELECT DISTINCT column_name(s)
FROM table_name
```

6.3 WHERE — ใช้กำหนดเงื่อนไขในการเลือกข้อมูล

```
SELECT column_name(s)
FROM table_name
WHERE condition
```

- IN — กรองข้อมูลแบบหลายค่าตามรายการที่ระบุ
- AND — เชื่อมเงื่อนไขที่ต้องเป็นจริงพร้อมกัน
ตัวดำเนินการที่ใช้กับ WHERE:

- ASC (Ascending) = จัดเรียงจากน้อยไปมาก
- BETWEEN…AND… — กรองข้อมูลที่อยู่ในช่วงระหว่างสองค่า
```
SELECT column_name(s)
FROM table_name
ORDER BY column_name(s) DESC
```

- OR — แสดงข้อมูลเมื่อเงื่อนไขใดเงื่อนไขหนึ่งเป็นจริง
6.4 ORDER BY — ใช้เรียงลำดับข้อมูล

แบบฝึก: (6) แสดง HN, รหัสคลินิก, ICD10 ของผู้ป่วยที่เข้ารับบริการในคลินิกรหัส 101101 ตาราง DIAG (7) เพิ่มเงื่อนไข ICD10 = 'I10' (8) แสดง HN_CODE, CLINICLCT, ICD10 โดยเลือก ICD10 เป็น I10 หรือ E119 (9) ทำข้อ 8 ด้วย IN แทน (10) แสดงข้อมูลที่ ICD10 ขึ้นต้นด้วยตัวอักษร I

- LIKE — ค้นหาคำหรือตัวอักษรที่ต้องการ เช่น LIKE 'J%'
แบบฝึก: (11) แสดง HN_CODE, CLINICLCT, ICD10 ที่ ICD10 เป็น I10 หรือ E119 เรียง CLINICLCT จากน้อยไปมาก (12) เรียง CLINICLCT น้อยไปมาก และ ICD10 มากไปน้อย

- DESC (Descending) = จัดเรียงจากมากไปน้อย
ประเภทของ JOIN (SQL JOINS):

6.5 COUNT — นับจำนวนข้อมูลของคอลัมน์ที่ระบุ

- MAX — ค่ามากที่สุด เช่น MAX(HEIGHT) AS MAX_HEIGHT
- FULL OUTER JOIN — ข้อมูลทั้งหมดจากทั้งสองตาราง (รวมถึงแบบเฉพาะส่วนที่ไม่ตรงกันทั้งสองฝั่ง โดยเพิ่ม WHERE a.KEY IS NULL OR b.KEY IS NULL)
6.6 ฟังก์ชันการคำนวณ (Aggregate Functions)

```
SELECT COUNT(column_name(s))
FROM table_name
```

แบบฝึก: (13) นับจำนวนรายการทั้งหมดในตาราง DIAG (14) นับจำนวนผู้ป่วยที่ไม่ซ้ำกันจาก HN_CODE

- SUM — ผลรวม เช่น SUM(WEIGHT) AS TOTAL_WEIGHT
- AVG — ค่าเฉลี่ย เช่น AVG(WEIGHT) AS AVG_WEIGHT
- MIN — ค่าน้อยที่สุด เช่น MIN(HEIGHT) AS MIN_HEIGHT
6.7 GROUP BY — ใช้จัดกลุ่มข้อมูลตามคอลัมน์ที่กำหนด (มักใช้ร่วมกับฟังก์ชันการคำนวณ)

แบบฝึก: (15) หาค่าเฉลี่ยน้ำหนัก ตาราง DIAG (16) นับจำนวนแถวทั้งหมด (17) แสดง ICD10 และนับจำนวนรายการวินิจฉัยแยกตามรหัส ICD10 เรียงจำนวนมากไปน้อย (18) แสดง CLINICLCT และนับจำนวนครั้งแยกตามคลินิก (19) แสดง CLINICLCT และนับจำนวนผู้ป่วยไม่ซ้ำแยกตามคลินิก เรียงมากไปน้อย (20) แสดง CLINICLCT และผลรวมน้ำหนักแยกตามคลินิก เรียงมากไปน้อย (21) แสดง CLINICLCT และค่าเฉลี่ยน้ำหนักแยกตามคลินิก เรียงมากไปน้อย (22) แสดง CLINICLCT และส่วนสูงสูงสุดแยกตามคลินิก เรียงมากไปน้อย (23) แสดง CLINICLCT และส่วนสูงต่ำสุดแยกตามคลินิก เรียงมากไปน้อย

- เชื่อม DIAG กับ CLINICLCT แสดง HN_CODE, รหัสคลินิก, ชื่อคลินิก, ประเภทคลินิก และ ICD10 เฉพาะประเภท "คลินิกพิเศษนอกเวลาราชการ" เรียงตามรหัสคลินิกและ HN_CODE จากน้อยไปมาก
```
SELECT column_name(s), SUM(column_name(s))
FROM table_name
GROUP BY column_name(s)
```


##### 7. แบบฝึกหัดท้ายบท (Exercises 1–15)

6.8 JOIN — การเชื่อมโยงข้อมูลระหว่างตาราง

```
SELECT column_name(s)
FROM table_nameA AS a
LEFT JOIN table_nameB AS b ON a.KEY = b.KEY
```

- INNER JOIN — เฉพาะข้อมูลที่ตรงกันทั้งสองตาราง (A ∩ B)
แบบฝึก: (24) เชื่อม DIAG กับ CLINICLCT แสดง HN_CODE, รหัสคลินิก, ชื่อคลินิก, รหัสวินิจฉัย (25) เชื่อม DIAG กับ ICD10 แสดง HN_CODE, รหัสวินิจฉัย, ชื่อโรคอังกฤษ, ชื่อโรคไทย (26) เชื่อม DIAG, CLINICLCT, ICD10 ทั้ง 3 ตาราง แสดง HN_CODE, รหัสคลินิก, ชื่อคลินิก, รหัสวินิจฉัย, ชื่อโรคอังกฤษ, ชื่อโรคไทย (27) เชื่อม DIAG กับ CLINICLCT สรุปจำนวนรายการวินิจฉัยแยกตามรหัสคลินิกและชื่อคลินิก เรียงจำนวนมากไปน้อย

- LEFT OUTER JOIN — ข้อมูลทั้งหมดจากตาราง A + ข้อมูลที่ตรงกันจาก B (และแบบเฉพาะที่มีเฉพาะใน A โดยเพิ่ม WHERE b.KEY IS NULL)
- แสดง HN_CODE, CLINICLCT และ ICD10 เฉพาะคลินิกรหัส 105101
- แสดงรหัส ICD10, จำนวนรายการวินิจฉัย และจำนวนผู้ป่วยไม่ซ้ำ จากตาราง DIAG เฉพาะรหัส ICD10 I10, E119, N185 เรียงจำนวนรายการวินิจฉัยจากมากไปน้อย
- แสดง HN_CODE, CLINICLCT และ ICD10 เฉพาะรหัสวินิจฉัยที่ขึ้นต้นด้วยตัวอักษร J เรียงตาม ICD10 และ HN_CODE จากน้อยไปมาก
- สรุปข้อมูลได้ง่าย
- เชื่อม DIAG, CLINICLCT, ICD10 แสดง HN_CODE, รหัสคลินิก, ชื่อคลินิก, รหัสวินิจฉัย, ชื่อโรคอังกฤษ, ชื่อโรคไทย เฉพาะรหัสวินิจฉัย E119
- นับจำนวนผู้ป่วยไม่ซ้ำที่มีรหัสวินิจฉัย I10
- นับจำนวนรายการวินิจฉัยของผู้ป่วยแต่ละ HN_CODE ตั้งชื่อว่า COUNT_DIAG เรียงจากจำนวนมากไปน้อย หากเท่ากันเรียง HN_CODE จากน้อยไปมาก
- เชื่อมทั้ง 3 ตาราง แสดง HN_CODE, รหัสคลินิก, ชื่อคลินิก, ICD10, ชื่อโรคอังกฤษ, ชื่อโรคไทย เฉพาะรหัสวินิจฉัย I10 หรือ E119 โดยใช้ IN เรียงตาม ICD10 และรหัสคลินิกจากน้อยไปมาก
- RIGHT OUTER JOIN — ข้อมูลทั้งหมดจากตาราง B + ข้อมูลที่ตรงกันจาก A (และแบบเฉพาะที่มีเฉพาะใน B โดยเพิ่ม WHERE a.KEY IS NULL)
- นับจำนวนรายการวินิจฉัยแยกตามคลินิก และเรียงจากมากไปน้อย
- เชื่อม DIAG กับ CLINICLCT สรุปแยกตามคลินิก แสดงรหัสคลินิก, ชื่อคลินิก, จำนวนรายการวินิจฉัย (COUNT_DIAG) และจำนวนผู้ป่วยไม่ซ้ำ (COUNT_PATIENTS) เรียงตามจำนวนผู้ป่วยจากมากไปน้อย หากเท่ากันเรียงรหัสคลินิกจากน้อยไปมาก
ข้อดี

- เชื่อมข้อมูลหลายตารางได้
- นับจำนวนรายการวินิจฉัยทั้งหมดที่รหัส ICD10 ขึ้นต้นด้วยตัวอักษร C ตั้งชื่อผลลัพธ์ว่า COUNT_DIAG
- แสดง CLINICLCT, NAME และ CLINICTYPENAME เฉพาะคลินิกประเภท "คลินิกพิเศษนอกเวลาราชการ" เรียงตามรหัสคลินิกจากน้อยไปมาก
- แสดงผู้ป่วยที่มีรหัสวินิจฉัย M170 หรือ M171 โดยใช้ IN
- เฉพาะคลินิกรหัส 101101 นับจำนวนรายการวินิจฉัยแยกตาม ICD10 ตั้งชื่อว่า COUNT_DIAG เรียงจำนวนมากไปน้อย และเรียง ICD10 น้อยไปมากเมื่อจำนวนเท่ากัน
- กรองข้อมูลได้ละเอียด
- เชื่อม DIAG กับ ICD10 แสดง HN_CODE, ICD10, ชื่อโรคอังกฤษ, ชื่อโรคไทย เฉพาะรหัสวินิจฉัยที่ขึ้นต้นด้วย M17 เรียงตาม ICD10 และ HN_CODE จากน้อยไปมาก

### 📚 6. เรียนรู้คำสั่งพื้นฐาน SQL

- ช่วยจัดการข้อมูลขนาดใหญ่ก่อนนำไปวิเคราะห์

##### 8. สรุป: ข้อดี / ข้อเสีย-ข้อจำกัดของ SQL

- ต่อยอด Data Analysis ได้ดี
ข้อเสีย/ข้อจำกัด

- ไม่สามารถนำไปวิเคราะห์ (ขั้นสูง) ได้ในตัวเอง
- เขียนผิดแล้วผลลัพธ์อาจผิดโดยไม่รู้ตัว

### 📝 7. แบบฝึกหัดท้ายบท (Exercises 1–15)


### ⚖️ 8. สรุป: ข้อดี / ข้อเสีย-ข้อจำกัดของ SQL

```
SELECT column_name(s)
FROM table_name
```

แบบฝึก: (1) แสดงข้อมูลทุกคอลัมน์จากตาราง CLINICLCT ด้วย SELECT * FROM CLINICLCT; (2) แสดงเฉพาะคอลัมน์ CLINICLCT, NAME, CLINICTYPENAME (3) ตั้งชื่อคอลัมน์ใหม่ด้วย AS

6.1 SELECT / FROM — เลือกข้อมูลที่ต้องการจากตาราง / ระบุตารางที่ต้องการดึงข้อมูล

```
SELECT column_name(s)
FROM table_name
WHERE condition
```

6.3 WHERE — ใช้กำหนดเงื่อนไขในการเลือกข้อมูล

แบบฝึก: (6) แสดง HN, รหัสคลินิก, ICD10 ของผู้ป่วยที่เข้ารับบริการในคลินิกรหัส 101101 ตาราง DIAG (7) เพิ่มเงื่อนไข ICD10 = 'I10' (8) แสดง HN_CODE, CLINICLCT, ICD10 โดยเลือก ICD10 เป็น I10 หรือ E119 (9) ทำข้อ 8 ด้วย IN แทน (10) แสดงข้อมูลที่ ICD10 ขึ้นต้นด้วยตัวอักษร I

6.2 DISTINCT — ขจัดรายการข้อมูลที่ซ้ำกัน

```
SELECT column_name(s)
FROM table_name
ORDER BY column_name(s) DESC
```

- ASC (Ascending) = จัดเรียงจากน้อยไปมาก
- AND — เชื่อมเงื่อนไขที่ต้องเป็นจริงพร้อมกัน
- OR — แสดงข้อมูลเมื่อเงื่อนไขใดเงื่อนไขหนึ่งเป็นจริง
6.4 ORDER BY — ใช้เรียงลำดับข้อมูล

```
SELECT DISTINCT column_name(s)
FROM table_name
```

แบบฝึก: (4) แสดง HN_CODE โดยไม่ให้ซ้ำ ตาราง DIAG (5) แสดงรหัสคลินิกโดยไม่ให้ซ้ำ ตาราง DIAG

- IN — กรองข้อมูลแบบหลายค่าตามรายการที่ระบุ
ตัวดำเนินการที่ใช้กับ WHERE:

- BETWEEN…AND… — กรองข้อมูลที่อยู่ในช่วงระหว่างสองค่า
6.5 COUNT — นับจำนวนข้อมูลของคอลัมน์ที่ระบุ

- DESC (Descending) = จัดเรียงจากมากไปน้อย
- MAX — ค่ามากที่สุด เช่น MAX(HEIGHT) AS MAX_HEIGHT
- LIKE — ค้นหาคำหรือตัวอักษรที่ต้องการ เช่น LIKE 'J%'
6.7 GROUP BY — ใช้จัดกลุ่มข้อมูลตามคอลัมน์ที่กำหนด (มักใช้ร่วมกับฟังก์ชันการคำนวณ)

แบบฝึก: (11) แสดง HN_CODE, CLINICLCT, ICD10 ที่ ICD10 เป็น I10 หรือ E119 เรียง CLINICLCT จากน้อยไปมาก (12) เรียง CLINICLCT น้อยไปมาก และ ICD10 มากไปน้อย

- SUM — ผลรวม เช่น SUM(WEIGHT) AS TOTAL_WEIGHT
แบบฝึก: (13) นับจำนวนรายการทั้งหมดในตาราง DIAG (14) นับจำนวนผู้ป่วยที่ไม่ซ้ำกันจาก HN_CODE

- AVG — ค่าเฉลี่ย เช่น AVG(WEIGHT) AS AVG_WEIGHT
แบบฝึก: (15) หาค่าเฉลี่ยน้ำหนัก ตาราง DIAG (16) นับจำนวนแถวทั้งหมด (17) แสดง ICD10 และนับจำนวนรายการวินิจฉัยแยกตามรหัส ICD10 เรียงจำนวนมากไปน้อย (18) แสดง CLINICLCT และนับจำนวนครั้งแยกตามคลินิก (19) แสดง CLINICLCT และนับจำนวนผู้ป่วยไม่ซ้ำแยกตามคลินิก เรียงมากไปน้อย (20) แสดง CLINICLCT และผลรวมน้ำหนักแยกตามคลินิก เรียงมากไปน้อย (21) แสดง CLINICLCT และค่าเฉลี่ยน้ำหนักแยกตามคลินิก เรียงมากไปน้อย (22) แสดง CLINICLCT และส่วนสูงสูงสุดแยกตามคลินิก เรียงมากไปน้อย (23) แสดง CLINICLCT และส่วนสูงต่ำสุดแยกตามคลินิก เรียงมากไปน้อย

แบบฝึก: (24) เชื่อม DIAG กับ CLINICLCT แสดง HN_CODE, รหัสคลินิก, ชื่อคลินิก, รหัสวินิจฉัย (25) เชื่อม DIAG กับ ICD10 แสดง HN_CODE, รหัสวินิจฉัย, ชื่อโรคอังกฤษ, ชื่อโรคไทย (26) เชื่อม DIAG, CLINICLCT, ICD10 ทั้ง 3 ตาราง แสดง HN_CODE, รหัสคลินิก, ชื่อคลินิก, รหัสวินิจฉัย, ชื่อโรคอังกฤษ, ชื่อโรคไทย (27) เชื่อม DIAG กับ CLINICLCT สรุปจำนวนรายการวินิจฉัยแยกตามรหัสคลินิกและชื่อคลินิก เรียงจำนวนมากไปน้อย

```
SELECT COUNT(column_name(s))
FROM table_name
```

- แสดง HN_CODE, CLINICLCT และ ICD10 เฉพาะคลินิกรหัส 105101
```
SELECT column_name(s), SUM(column_name(s))
FROM table_name
GROUP BY column_name(s)
```

6.6 ฟังก์ชันการคำนวณ (Aggregate Functions)

- MIN — ค่าน้อยที่สุด เช่น MIN(HEIGHT) AS MIN_HEIGHT
- FULL OUTER JOIN — ข้อมูลทั้งหมดจากทั้งสองตาราง (รวมถึงแบบเฉพาะส่วนที่ไม่ตรงกันทั้งสองฝั่ง โดยเพิ่ม WHERE a.KEY IS NULL OR b.KEY IS NULL)
6.8 JOIN — การเชื่อมโยงข้อมูลระหว่างตาราง

- แสดง CLINICLCT, NAME และ CLINICTYPENAME เฉพาะคลินิกประเภท "คลินิกพิเศษนอกเวลาราชการ" เรียงตามรหัสคลินิกจากน้อยไปมาก
```
SELECT column_name(s)
FROM table_nameA AS a
LEFT JOIN table_nameB AS b ON a.KEY = b.KEY
```

ประเภทของ JOIN (SQL JOINS):

- แสดง HN_CODE, CLINICLCT และ ICD10 เฉพาะรหัสวินิจฉัยที่ขึ้นต้นด้วยตัวอักษร J เรียงตาม ICD10 และ HN_CODE จากน้อยไปมาก
- LEFT OUTER JOIN — ข้อมูลทั้งหมดจากตาราง A + ข้อมูลที่ตรงกันจาก B (และแบบเฉพาะที่มีเฉพาะใน A โดยเพิ่ม WHERE b.KEY IS NULL)
- INNER JOIN — เฉพาะข้อมูลที่ตรงกันทั้งสองตาราง (A ∩ B)

##### 7. แบบฝึกหัดท้ายบท (Exercises 1–15)

- RIGHT OUTER JOIN — ข้อมูลทั้งหมดจากตาราง B + ข้อมูลที่ตรงกันจาก A (และแบบเฉพาะที่มีเฉพาะใน B โดยเพิ่ม WHERE a.KEY IS NULL)
- แสดงผู้ป่วยที่มีรหัสวินิจฉัย M170 หรือ M171 โดยใช้ IN
- นับจำนวนรายการวินิจฉัยของผู้ป่วยแต่ละ HN_CODE ตั้งชื่อว่า COUNT_DIAG เรียงจากจำนวนมากไปน้อย หากเท่ากันเรียง HN_CODE จากน้อยไปมาก
- นับจำนวนผู้ป่วยไม่ซ้ำที่มีรหัสวินิจฉัย I10

##### 8. สรุป: ข้อดี / ข้อเสีย-ข้อจำกัดของ SQL

- นับจำนวนรายการวินิจฉัยแยกตามคลินิก และเรียงจากมากไปน้อย
- นับจำนวนรายการวินิจฉัยทั้งหมดที่รหัส ICD10 ขึ้นต้นด้วยตัวอักษร C ตั้งชื่อผลลัพธ์ว่า COUNT_DIAG
- เฉพาะคลินิกรหัส 101101 นับจำนวนรายการวินิจฉัยแยกตาม ICD10 ตั้งชื่อว่า COUNT_DIAG เรียงจำนวนมากไปน้อย และเรียง ICD10 น้อยไปมากเมื่อจำนวนเท่ากัน
- แสดงรหัส ICD10, จำนวนรายการวินิจฉัย และจำนวนผู้ป่วยไม่ซ้ำ จากตาราง DIAG เฉพาะรหัส ICD10 I10, E119, N185 เรียงจำนวนรายการวินิจฉัยจากมากไปน้อย
- เชื่อม DIAG, CLINICLCT, ICD10 แสดง HN_CODE, รหัสคลินิก, ชื่อคลินิก, รหัสวินิจฉัย, ชื่อโรคอังกฤษ, ชื่อโรคไทย เฉพาะรหัสวินิจฉัย E119
- เชื่อมทั้ง 3 ตาราง แสดง HN_CODE, รหัสคลินิก, ชื่อคลินิก, ICD10, ชื่อโรคอังกฤษ, ชื่อโรคไทย เฉพาะรหัสวินิจฉัย I10 หรือ E119 โดยใช้ IN เรียงตาม ICD10 และรหัสคลินิกจากน้อยไปมาก
- เชื่อม DIAG กับ CLINICLCT แสดง HN_CODE, รหัสคลินิก, ชื่อคลินิก, ประเภทคลินิก และ ICD10 เฉพาะประเภท "คลินิกพิเศษนอกเวลาราชการ" เรียงตามรหัสคลินิกและ HN_CODE จากน้อยไปมาก
- เชื่อมข้อมูลหลายตารางได้
- กรองข้อมูลได้ละเอียด
- เชื่อม DIAG กับ ICD10 แสดง HN_CODE, ICD10, ชื่อโรคอังกฤษ, ชื่อโรคไทย เฉพาะรหัสวินิจฉัยที่ขึ้นต้นด้วย M17 เรียงตาม ICD10 และ HN_CODE จากน้อยไปมาก
- Query ที่เขียนไม่ดีอาจทำงานช้ามาก
- ต้องเข้าใจโครงสร้าง Database
- ไม่สามารถนำไปวิเคราะห์ (ขั้นสูง) ได้ในตัวเอง
ข้อดี

- เชื่อม DIAG กับ CLINICLCT สรุปแยกตามคลินิก แสดงรหัสคลินิก, ชื่อคลินิก, จำนวนรายการวินิจฉัย (COUNT_DIAG) และจำนวนผู้ป่วยไม่ซ้ำ (COUNT_PATIENTS) เรียงตามจำนวนผู้ป่วยจากมากไปน้อย หากเท่ากันเรียงรหัสคลินิกจากน้อยไปมาก
- สรุปข้อมูลได้ง่าย
ข้อเสีย/ข้อจำกัด

- ต่อยอด Data Analysis ได้ดี
- ช่วยจัดการข้อมูลขนาดใหญ่ก่อนนำไปวิเคราะห์
- เขียนผิดแล้วผลลัพธ์อาจผิดโดยไม่รู้ตัว
```
SELECT DISTINCT column_name(s)
FROM table_name
```

แบบฝึก: (4) แสดง HN_CODE โดยไม่ให้ซ้ำ ตาราง DIAG (5) แสดงรหัสคลินิกโดยไม่ให้ซ้ำ ตาราง DIAG

```
SELECT column_name(s)
FROM table_name
WHERE condition
```

ตัวดำเนินการที่ใช้กับ WHERE:

- AND — เชื่อมเงื่อนไขที่ต้องเป็นจริงพร้อมกัน
- OR — แสดงข้อมูลเมื่อเงื่อนไขใดเงื่อนไขหนึ่งเป็นจริง
- IN — กรองข้อมูลแบบหลายค่าตามรายการที่ระบุ
- LIKE — ค้นหาคำหรือตัวอักษรที่ต้องการ เช่น LIKE 'J%'
- BETWEEN…AND… — กรองข้อมูลที่อยู่ในช่วงระหว่างสองค่า
แบบฝึก: (6) แสดง HN, รหัสคลินิก, ICD10 ของผู้ป่วยที่เข้ารับบริการในคลินิกรหัส 101101 ตาราง DIAG (7) เพิ่มเงื่อนไข ICD10 = 'I10' (8) แสดง HN_CODE, CLINICLCT, ICD10 โดยเลือก ICD10 เป็น I10 หรือ E119 (9) ทำข้อ 8 ด้วย IN แทน (10) แสดงข้อมูลที่ ICD10 ขึ้นต้นด้วยตัวอักษร I

```
SELECT column_name(s)
FROM table_name
ORDER BY column_name(s) DESC
```

- ASC (Ascending) = จัดเรียงจากน้อยไปมาก
- DESC (Descending) = จัดเรียงจากมากไปน้อย
แบบฝึก: (11) แสดง HN_CODE, CLINICLCT, ICD10 ที่ ICD10 เป็น I10 หรือ E119 เรียง CLINICLCT จากน้อยไปมาก (12) เรียง CLINICLCT น้อยไปมาก และ ICD10 มากไปน้อย

```
SELECT COUNT(column_name(s))
FROM table_name
```

แบบฝึก: (13) นับจำนวนรายการทั้งหมดในตาราง DIAG (14) นับจำนวนผู้ป่วยที่ไม่ซ้ำกันจาก HN_CODE

- SUM — ผลรวม เช่น SUM(WEIGHT) AS TOTAL_WEIGHT
- AVG — ค่าเฉลี่ย เช่น AVG(WEIGHT) AS AVG_WEIGHT
- MAX — ค่ามากที่สุด เช่น MAX(HEIGHT) AS MAX_HEIGHT
- MIN — ค่าน้อยที่สุด เช่น MIN(HEIGHT) AS MIN_HEIGHT
```
SELECT column_name(s), SUM(column_name(s))
FROM table_name
GROUP BY column_name(s)
```

แบบฝึก: (15) หาค่าเฉลี่ยน้ำหนัก ตาราง DIAG (16) นับจำนวนแถวทั้งหมด (17) แสดง ICD10 และนับจำนวนรายการวินิจฉัยแยกตามรหัส ICD10 เรียงจำนวนมากไปน้อย (18) แสดง CLINICLCT และนับจำนวนครั้งแยกตามคลินิก (19) แสดง CLINICLCT และนับจำนวนผู้ป่วยไม่ซ้ำแยกตามคลินิก เรียงมากไปน้อย (20) แสดง CLINICLCT และผลรวมน้ำหนักแยกตามคลินิก เรียงมากไปน้อย (21) แสดง CLINICLCT และค่าเฉลี่ยน้ำหนักแยกตามคลินิก เรียงมากไปน้อย (22) แสดง CLINICLCT และส่วนสูงสูงสุดแยกตามคลินิก เรียงมากไปน้อย (23) แสดง CLINICLCT และส่วนสูงต่ำสุดแยกตามคลินิก เรียงมากไปน้อย

```
SELECT column_name(s)
FROM table_nameA AS a
LEFT JOIN table_nameB AS b ON a.KEY = b.KEY
```

ประเภทของ JOIN (SQL JOINS):

- LEFT OUTER JOIN — ข้อมูลทั้งหมดจากตาราง A + ข้อมูลที่ตรงกันจาก B (เฉพาะที่มีเฉพาะใน A: เพิ่ม WHERE b.KEY IS NULL)
- INNER JOIN — เฉพาะข้อมูลที่ตรงกันทั้งสองตาราง (A ∩ B)
- RIGHT OUTER JOIN — ข้อมูลทั้งหมดจากตาราง B + ข้อมูลที่ตรงกันจาก A (เฉพาะที่มีเฉพาะใน B: เพิ่ม WHERE a.KEY IS NULL)
- FULL OUTER JOIN — ข้อมูลทั้งหมดจากทั้งสองตาราง (เฉพาะส่วนที่ไม่ตรงกันทั้งสองฝั่ง: เพิ่ม WHERE a.KEY IS NULL OR b.KEY IS NULL)
แบบฝึก: (24) เชื่อม DIAG กับ CLINICLCT แสดง HN_CODE, รหัสคลินิก, ชื่อคลินิก, รหัสวินิจฉัย (25) เชื่อม DIAG กับ ICD10 แสดง HN_CODE, รหัสวินิจฉัย, ชื่อโรคอังกฤษ, ชื่อโรคไทย (26) เชื่อม DIAG, CLINICLCT, ICD10 ทั้ง 3 ตาราง แสดง HN_CODE, รหัสคลินิก, ชื่อคลินิก, รหัสวินิจฉัย, ชื่อโรคอังกฤษ, ชื่อโรคไทย (27) เชื่อม DIAG กับ CLINICLCT สรุปจำนวนรายการวินิจฉัยแยกตามรหัสคลินิกและชื่อคลินิก เรียงจำนวนมากไปน้อย

สรุปเนื้อหา: Structured Query Language (SQL)

สรุปย่อจากสไลด์ประกอบการสอน พร้อมโจทย์ฝึกหัดทั้งหมด สำหรับทบทวนก่อน/หลังคลาส

- SQL (Structured Query Language) คือภาษาคอมพิวเตอร์ที่ใช้สำหรับ จัดการฐานข้อมูล โดยเฉพาะ เช่น การสร้างฐานข้อมูล การเพิ่มข้อมูล การแก้ไขข้อมูล และการลบข้อมูล
- เป็นภาษามาตรฐานสำหรับจัดการและเรียกดูข้อมูลในฐานข้อมูล มีจุดเริ่มต้นจากการพัฒนาโดยบริษัท IBM
- ใช้กันอย่างแพร่หลาย เพราะเรียนรู้และใช้งานได้ไม่ยาก คำสั่งส่วนใหญ่ใช้คำภาษาอังกฤษที่เข้าใจง่าย
- มักใช้ร่วมกับระบบจัดการฐานข้อมูลเชิงสัมพันธ์ (RDBMS) ที่นิยม เช่น 🗄️ MS Access, MS SQL Server, Oracle และ 🐬 MySQL
ใน DB Browser for SQLite: ลากไฟล์ CSV วางในโปรแกรม → เลือก "Import CSV file(s)" → ตั้งชื่อตาราง (Table name) → กำหนด Column names in first line, Field separator, Quote character, Encoding (UTF-8), Trim fields → กด OK

- แสดง HN_CODE, CLINICLCT และ ICD10 เฉพาะคลินิกรหัส 105101
- แสดงผู้ป่วยที่มีรหัสวินิจฉัย M170 หรือ M171 โดยใช้ IN
- นับจำนวนผู้ป่วยไม่ซ้ำที่มีรหัสวินิจฉัย I10
- นับจำนวนรายการวินิจฉัยแยกตามคลินิก และเรียงจากมากไปน้อย
- แสดง CLINICLCT, NAME และ CLINICTYPENAME เฉพาะคลินิกประเภท "คลินิกพิเศษนอกเวลาราชการ" เรียงตามรหัสคลินิกจากน้อยไปมาก
- แสดง HN_CODE, CLINICLCT และ ICD10 เฉพาะรหัสวินิจฉัยที่ขึ้นต้นด้วยตัวอักษร J เรียงตาม ICD10 และ HN_CODE จากน้อยไปมาก
- นับจำนวนรายการวินิจฉัยทั้งหมดที่รหัส ICD10 ขึ้นต้นด้วยตัวอักษร C ตั้งชื่อผลลัพธ์ว่า COUNT_DIAG
- แสดงรหัส ICD10, จำนวนรายการวินิจฉัย และจำนวนผู้ป่วยไม่ซ้ำ จากตาราง DIAG เฉพาะรหัส ICD10 I10, E119, N185 เรียงจำนวนรายการวินิจฉัยจากมากไปน้อย
- นับจำนวนรายการวินิจฉัยของผู้ป่วยแต่ละ HN_CODE ตั้งชื่อว่า COUNT_DIAG เรียงจากจำนวนมากไปน้อย หากเท่ากันเรียง HN_CODE จากน้อยไปมาก
- เฉพาะคลินิกรหัส 101101 นับจำนวนรายการวินิจฉัยแยกตาม ICD10 ตั้งชื่อว่า COUNT_DIAG เรียงจำนวนมากไปน้อย และเรียง ICD10 น้อยไปมากเมื่อจำนวนเท่ากัน
- เชื่อม DIAG กับ CLINICLCT แสดง HN_CODE, รหัสคลินิก, ชื่อคลินิก, ประเภทคลินิก และ ICD10 เฉพาะประเภท "คลินิกพิเศษนอกเวลาราชการ" เรียงตามรหัสคลินิกและ HN_CODE จากน้อยไปมาก
- เชื่อม DIAG กับ ICD10 แสดง HN_CODE, ICD10, ชื่อโรคอังกฤษ, ชื่อโรคไทย เฉพาะรหัสวินิจฉัยที่ขึ้นต้นด้วย M17 เรียงตาม ICD10 และ HN_CODE จากน้อยไปมาก
- เชื่อม DIAG, CLINICLCT, ICD10 แสดง HN_CODE, รหัสคลินิก, ชื่อคลินิก, รหัสวินิจฉัย, ชื่อโรคอังกฤษ, ชื่อโรคไทย เฉพาะรหัสวินิจฉัย E119
- เชื่อมทั้ง 3 ตาราง แสดง HN_CODE, รหัสคลินิก, ชื่อคลินิก, ICD10, ชื่อโรคอังกฤษ, ชื่อโรคไทย เฉพาะรหัสวินิจฉัย I10 หรือ E119 โดยใช้ IN เรียงตาม ICD10 และรหัสคลินิกจากน้อยไปมาก
- เชื่อม DIAG กับ CLINICLCT สรุปแยกตามคลินิก แสดงรหัสคลินิก, ชื่อคลินิก, จำนวนรายการวินิจฉัย (COUNT_DIAG) และจำนวนผู้ป่วยไม่ซ้ำ (COUNT_PATIENTS) เรียงตามจำนวนผู้ป่วยจากมากไปน้อย หากเท่ากันเรียงรหัสคลินิกจากน้อยไปมาก
CLINICLCT

- CLINICLCT 🔑
- NAME
- CLINICTYPENAME
DIAG

- HN_CODE
- CLINICLCT 🔑
- ICD10 🔑
- VSTDATE
- WEIGHT
- HEIGHT
ICD10

- ICD10 🔑
- NAME
- THAINAME
ข้อดี

- ช่วยจัดการข้อมูลขนาดใหญ่ก่อนนำไปวิเคราะห์
- เชื่อมข้อมูลหลายตารางได้
- กรองข้อมูลได้ละเอียด
- สรุปข้อมูลได้ง่าย
- ต่อยอด Data Analysis ได้ดี
ข้อเสีย/ข้อจำกัด

- ไม่สามารถนำไปวิเคราะห์ (ขั้นสูง) ได้ในตัวเอง
- เขียนผิดแล้วผลลัพธ์อาจผิดโดยไม่รู้ตัว
- ต้องเข้าใจโครงสร้าง Database
- Query ที่เขียนไม่ดีอาจทำงานช้ามาก


## Topic 5b: Excel & Power BI (ID: 3d20abc4-4cc7-80c5-900f-ec217310adf5)

5. Data Collection, Cleaning, and Preparation for Healthcare Analysis by Excel


### 🏥 1. แหล่งข้อมูลทางการแพทย์ (Data Sources in Medicine)


### 🗄️ 2. Data Warehouse: Structured vs Unstructured Data


### 📥 3. Data Collection — การเก็บข้อมูล


### 📊 4. Excel Overview (พื้นฐาน)


### 🧹 5. Data Preparation (เชิงลึก) — Data Matters: How We Collect, Clean, and Prepare for AI

ใช้ตัวอย่างชุดข้อมูล: ID, Day, Male, HT, Weight, Height, Number of medication used

(ค่า 999 หมายถึงค่าที่ขาดหายหรือผิดปกติ)


### ⚡ 6. Data Analytics with Introduction to Power BI


##### 🔷 Power BI คืออะไร

Power BI เป็นแพลตฟอร์ม self-service และ enterprise BI ที่เป็น unified และ scalable สามารถเชื่อมต่อและแสดงผล (visualize) ข้อมูลได้ทุกประเภท และผสานภาพ visual เข้ากับแอปที่ใช้งานประจำวันได้อย่างไร้รอยต่อ (Self-Service BI)


##### 🔄 How Business Intelligence Works (4 ขั้นตอน)

- Collect and transform data from multiple sources — Data Preparation, Extract-Transform-Load (ETL)
- Uncover trends and inconsistencies — Exploratory Data Analysis (EDA)
- Use data visualization to present findings — Create Visualization
- Take action on insights in real time — Create Dashboard
อ้างอิง: blog.bismart.com/en/excel-vs-power-bi-which-one-is-better (เปรียบเทียบ Power BI vs Excel)


##### 🧱 องค์ประกอบหลักของ Power BI (3 ส่วน)

อ้างอิง: learn.microsoft.com/en-us/power-bi/fundamentals/


##### 🗺️ Workflow ของ Power BI

อ้างอิงภาพ: yoadministrador.com/en/what-is-power-bi


##### 💰 Pricing (ราคา)

อ้างอิง: monsterconnect.co.th/power-bi-free-vs-pro-vs-premium

- Power BI Service (Free)
- Power BI Service (Pro)
- Power BI Premium
🏆 ตัวอย่างงาน Power BI จาก Community


##### ⬇️ การติดตั้ง Power BI

- ดาวน์โหลด: https://powerbi.microsoft.com/en-us/desktop/
- Sign In/Sign up โดยใช้ Organization/University Email

### Data Collection, Cleaning, and Preparation for Healthcare Analysis by Excel


#### หัวข้อ (Topics)

- Data Preparation (Excel)
- Data Sources
- Prospective data collection (Excel)

##### ระบบข้อมูลในโรงพยาบาล

- Introduction to Power BI

#### 1. แหล่งข้อมูลทางการแพทย์ (Data Sources in Medicine)

- ICD-10 / ICD-9CM: International Classification of Diseases ใช้จัดหมวดหมู่โรคและหัตถการ
- ตัวอย่างข้อมูล Billing/Admission: มีคอลัมน์ En_HN, เพศ, วันที่ชำระค่าบริการ, ประเภทผู้ป่วย, Product code, Product name, Product type (LAB/SUPPLY), จำนวน, ค่ารักษา
โดย Chaiyawat Suppasilp | 09.2026


##### แหล่งข้อมูลระดับประเทศ/องค์กร

- ตัวอย่างข้อมูล Medication: รหัสยา, ยาและความแรง, ชื่อสามัญ, รูปแบบยา (Inj/Tab/Cap), จำนวน, หน่วยการจ่าย
- Government organization: GISTDA (Geo-Informatics and Space Technology Development Agency)
- Public Data ตัวอย่างงานวิจัย: "Association between Wildfire area and PM2.5 levels on the Prevalence of Mental disorders in Thailand"
- Ministry of Public Health: 43-file Data, Strategy and Planning Division
- Administrative claim data:

##### Real World Data (RWD)

อ้างอิง: J Am Coll Surg. 2017;224:1-7; Nat Rev Clin Oncol. 2019 May;16:312-325

ข้อมูลจากการปฏิบัติงานทางคลินิกตามปกติ (ไม่ได้วางแผนเพื่อการวิจัยแต่แรก)


##### Structured Data — ประเภทข้อมูล

- Categorical

#### 2. Data Warehouse: Structured vs Unstructured Data

- Numeric
- Boolean
- Date time
> Check point: Pain Score 0–10 และการแบ่งระดับการศึกษา เป็นตัวอย่างการแยกแยะ Nominal vs Ordinal

ได้แก่ Image, Signal, Text


##### Unstructured Data


##### ตารางเปรียบเทียบ Excel vs CSV vs JSON


##### รูปแบบไฟล์ (Data Format)

- Structured data: Excel, CSV, JSON
- Unstructured data: PDF, Signal (ECG, EEG, Voice/Audiogram), Image (DICOM = Digital Imaging and Communications in Medicine)

#### 3. การเตรียมฟอร์มเก็บข้อมูล (Data Preparation) — หลักการออกแบบตาราง

ตัวอย่างข้อมูลที่ใช้อธิบายตลอดเซกชันนี้ (ติดตามผู้ป่วยหลายครั้ง — ID, Day, Gender, HT, Weight, Height, Number of medication used) ใช้แสดงข้อผิดพลาดที่พบบ่อย:

Header ควรมีแถวเดียวชัดเจน ไม่ควรแยกเป็น 2 แถวซ้อนกัน (เช่น แถวบนเป็นหมวดใหญ่ "For BMI calculation" แถวล่างเป็น Male/Female/Weight/Height)


##### 3.3 ห้ามมี Summary Row ปนอยู่ในข้อมูลดิบ


##### 3.2 ไม่เว้นแถวว่าง และไม่ merge cell


##### 3.1 หลีกเลี่ยง Header สองแถว

เช่น คอลัมน์ ID ไม่ควรเว้นว่างในแถวถัดไปของผู้ป่วยคนเดิม (ต้องกรอกซ้ำทุกแถว ไม่ merge cell ข้าม row)

เช่น แถวสรุปอย่าง "2 pts, 82.5 days" ไม่ควรอยู่ปนกับแถวข้อมูลรายบุคคล


##### รูปแบบฟอร์มเก็บข้อมูล


##### 3.4 หลักสำคัญที่สุด

1 คอลัมน์ = 1 ข้อมูล (variable/concept) เท่านั้น

- Data collection form
- Case record form

#### 4. Excel Overview (พื้นฐาน)

อ้างอิง: w3schools.com/excel/excel_overview.php

- ส่วนประกอบหน้าจอ: Name Box, Formula Bar, Cell, Status Bar
- Cell ประกอบด้วย:

##### การตรวจสอบและแปลง Data Type

- ISNUMBER
- ISTEXT
- ISERROR
- ISBLANK
- ISNONTEXT
การแปลงชนิดข้อมูล:

- Logic → Number: ใช้ *1, --
- Text → Number: ใช้ *1, +0, /1, --
- Number → Text: ใช้เครื่องหมาย ' นำหน้า หรือใช้ &""
- Default Date format กำหนดที่ Date Format ใน Control Panel > Region

##### Date Format

- ควรใช้ปี ค.ศ. ทั้งหมด (All way ค.ศ.)
- วันที่ในระบบคือตัวเลข (Is Number) โดย Reference Date คือ 01/01/1900
- goskills.com/excel/resources/excel-date-functions (Date Function)
- Data collection form: worksheet — ตัวอย่างสร้างฟอร์มเก็บข้อมูล Age, Sex, Height, Weight, Birth date, Income level
ตรวจสอบชนิดข้อมูล ด้วยฟังก์ชัน IS:

อ้างอิงเพิ่มเติม:

- ตัวอย่างการตรวจสอบ: 01/03/2027 = 29 กุมภาพันธ์ 2560 (ต้องเช็ค Data format > Calendar Type: Thai Buddhist ให้ถูกต้อง เพราะอาจทำให้ตีความวันที่ผิดพลาดได้)
- xfanatical.com/blog/how-to-format-a-date-time-in-excel
- excelexperttraining.com (Date Function, Fix cell reference)

##### เครื่องมือช่วยวิเคราะห์ใน Excel

- Conditional Formatting: data bars, color scale, icon set (อ้างอิง: support.microsoft.com)
- Sort and Filter
ใช้ตัวอย่างชุดข้อมูล: ID, Day, Male, HT, Weight, Height, Number of medication used


#### 5. Data Preparation (เชิงลึก) — Data Matters: How We Collect, Clean, and Prepare for AI


##### 5.1 Data Verification (ตรวจสอบข้อมูล)

(ค่า 999 หมายถึงค่าที่ขาดหายหรือผิดปกติ)

- Outliers (ค่าผิดปกติ)
- Missing value (ค่าที่หายไป)
ตรวจสอบ 3 เรื่องหลัก:

- ลบข้อมูลที่ขาด/ผิดปกติออกทั้งหมด (remove all missing/abnormal records)

##### 5.2 Complete Case Analysis


##### 5.3 Data Imputation (การแทนค่าที่ขาดหาย)

- Data Unit (หน่วยข้อมูลไม่สอดคล้องกัน เช่น Height บางแถวเป็น cm บางแถวเป็น m — เช่น 158 vs 1.72)
- แทนที่ด้วยค่า 0 (Replace with 0)
- หลักการ: ควรลบออกไม่เกิน 5% ของข้อมูลทั้งหมด
- Mean/Mode/Median Filling
- อาจส่งผลกระทบต่อผลการวิเคราะห์
วิธีการ:

- Interpolation/Extrapolation
- Forward/Backward Filling

##### Business Intelligence (BI) คืออะไร


#### 6. Data Analytics with Introduction to Power BI

BI คือชุดของ methodologies, processes, architectures และ technologies ที่แปลงข้อมูลดิบให้กลายเป็นข้อมูลที่มีความหมายและมีประโยชน์ เพื่อสนับสนุนการตัดสินใจเชิงกลยุทธ์ (strategic), เชิงยุทธวิธี (tactical) และเชิงปฏิบัติการ (operational) อย่างมีประสิทธิภาพ

- Data gathering
ระบบ BI ประกอบด้วยการรวมกันของ:

- Data storage
- Knowledge management
Power BI เป็นแพลตฟอร์ม self-service และ enterprise BI ที่เป็น unified และ scalable สามารถเชื่อมต่อและแสดงผล (visualize) ข้อมูลได้ทุกประเภท และผสานภาพ visual เข้ากับแอปที่ใช้งานประจำวันได้อย่างไร้รอยต่อ (Self-Service BI)


##### How Business Intelligence Works (4 ขั้นตอน)


##### Power BI คืออะไร

- Collect and transform data from multiple sources — Data Preparation, Extract-Transform-Load (ETL)
- Uncover trends and inconsistencies — Exploratory Data Analysis (EDA)
อ้างอิง: blog.bismart.com/en/excel-vs-power-bi-which-one-is-better (เปรียบเทียบ Power BI vs Excel)

- Use data visualization to present findings — Create Visualization
- Take action on insights in real time — Create Dashboard

##### องค์ประกอบหลักของ Power BI (3 ส่วน)

- แปลงและทำความสะอาดข้อมูลเพื่อสร้าง data model
อ้างอิง: learn.microsoft.com/en-us/power-bi/fundamentals/

1. Power BI Desktop (Windows desktop application)

- สร้าง visuals เช่น charts/graphs
- เชื่อมต่อข้อมูล (Connect to data)
- สร้าง reports (รวม visuals หลายหน้า)
- License กำหนดสิ่งที่ทำได้
- ดู/สร้าง reports และ dashboards ที่สร้างจาก Desktop/Service
- โต้ตอบกับรายงานผ่านมือถือได้
- แชร์ reports ผ่าน Power BI service (ต้องมี license)
2. Power BI Service (คลาวด์/SaaS — Power BI online)

- รองรับ Paginated reports
- เชื่อมต่อ data source ได้ แต่ modeling มีข้อจำกัด
อ้างอิงภาพ: yoadministrador.com/en/what-is-power-bi

- งานตัวอย่าง: สร้าง dashboards, สร้าง/แชร์ apps, วิเคราะห์ข้อมูลเพื่อหา business insights
- Power BI Service (Pro)
- ใช้งานได้ทั้ง on-premises และ cloud
3. Power BI Mobile apps (Windows, iOS, Android)


##### Workflow ของ Power BI

อ้างอิง: monsterconnect.co.th/power-bi-free-vs-pro-vs-premium

- Power BI Service (Free)

##### Pricing (ราคา)

- Power BI Premium
- Covid World Wide Report — community.powerbi.com

##### ตัวอย่างงาน Power BI จาก Community

- Financial Performance Overview — community.powerbi.com
- MLB Baseball Batting Stats — community.powerbi.com
- ดาวน์โหลด: https://powerbi.microsoft.com/en-us/desktop/

#### สรุปกระบวนการทั้งหมด (End-to-end flow)

Data Sources (LIS/HIS/PACS/Billing, NHSO, 43-file ฯลฯ) → Data Collection (ออกแบบฟอร์มใน Excel ให้ถูกหลัก: 1 คอลัมน์ = 1 ตัวแปร) → Data Preparation (ตรวจสอบ missing/outlier/unit → Complete Case Analysis หรือ Imputation) → Power BI: ETL → EDA → Visualization → Dashboard

Data Collection, Cleaning, and Preparation for Healthcare Analysis by Excel

โดย Chaiyawat Suppasilp | 09.2026

หัวข้อ (Topics)

- Data Sources
- Prospective data collection (Excel)
- Data Preparation (Excel)
- Introduction to Power BI

##### ระบบข้อมูลในโรงพยาบาล

- ICD-10 / ICD-9CM: International Classification of Diseases ใช้จัดหมวดหมู่โรคและหัตถการ
📋 ตัวอย่างข้อมูล Billing/Admission

💊 ตัวอย่างข้อมูล Medication


##### 🌏 แหล่งข้อมูลระดับประเทศ/องค์กร

- Administrative claim data:
- Ministry of Public Health: 43-file Data, Strategy and Planning Division
- Government organization: GISTDA (Geo-Informatics and Space Technology Development Agency)
- Public Data ตัวอย่างงานวิจัย: "Association between Wildfire area and PM2.5 levels on the Prevalence of Mental disorders in Thailand"

##### 🔬 Real World Data (RWD)


##### 📁 รูปแบบไฟล์ (Data Format)

- Structured data: Excel, CSV, JSON
- Unstructured data: PDF, Signal (ECG, EEG, Voice/Audiogram), Image (DICOM = Digital Imaging and Communications in Medicine)

##### ⚖️ ตารางเปรียบเทียบ Excel vs CSV vs JSON


##### 🔎 Prospective Data Collection คืออะไร

การเก็บข้อมูลไปข้างหน้า (เก็บข้อมูลใหม่ ตั้งแต่ตอนนี้เป็นต้นไป) ตรงข้ามกับการดึงข้อมูลย้อนหลังจากระบบที่มีอยู่แล้ว (เช่น LIS, HIS, PACS, Billing ที่กล่าวถึงในหัวข้อ Data Sources)


##### 🧰 เครื่องมือที่ใช้เก็บข้อมูล

- Data collection form — แบบฟอร์มสำหรับกรอกข้อมูล
- Case record form (CRF) — แบบบันทึกข้อมูลผู้ป่วยรายเคส (นิยมใช้ในงานวิจัยทางคลินิก)
- ตัวแปรที่มักเก็บ: Age, Sex, Height, Weight, Birth date, Income level (แบ่งช่วง เช่น <15,000 / 15,000–30,000 / 30,000–50,000 / >50,000)

##### 📐 หลักการออกแบบฟอร์มเก็บข้อมูลใน Excel ให้ถูกต้อง

ตัวอย่างข้อมูลที่ใช้อธิบายตลอดเซกชันนี้ (ติดตามผู้ป่วยหลายครั้ง — ID, Day, Gender, HT, Weight, Height, Number of medication used) ใช้แสดงข้อผิดพลาดที่พบบ่อย:

⚠️ 3.1 หลีกเลี่ยง Header สองแถว — Header ควรมีแถวเดียวชัดเจน ไม่ควรแยกเป็น 2 แถวซ้อนกัน (เช่น แถวบนเป็นหมวดใหญ่ "For BMI calculation" แถวล่างเป็น Male/Female/Weight/Height)

⚠️ 3.2 ไม่เว้นแถวว่าง และไม่ merge cell — เช่น คอลัมน์ ID ไม่ควรเว้นว่างในแถวถัดไปของผู้ป่วยคนเดิม (ต้องกรอกซ้ำทุกแถว ไม่ merge cell ข้าม row)

⚠️ 3.3 ห้ามมี Summary Row ปนอยู่ในข้อมูลดิบ — เช่น แถวสรุปอย่าง "2 pts, 82.5 days" ไม่ควรอยู่ปนกับแถวข้อมูลรายบุคคล


##### 📋 รูปแบบฟอร์มเก็บข้อมูล

- Data collection form
- Case record form
- ตัวอย่าง: ฟอร์มเก็บข้อมูล Age, Sex, Height, Weight, Birth date, Income level (แบ่งช่วง เช่น <15,000 / 15,000–30,000 / 30,000–50,000 / >50,000)
อ้างอิง: w3schools.com/excel/excel_overview.php

- ส่วนประกอบหน้าจอ: Name Box, Formula Bar, Cell, Status Bar
- Cell ประกอบด้วย:
🔍 การตรวจสอบและแปลง Data Type

📅 Date Format


##### 🛠️ เครื่องมือช่วยวิเคราะห์ใน Excel

- Data collection form: worksheet — ตัวอย่างสร้างฟอร์มเก็บข้อมูล Age, Sex, Height, Weight, Birth date, Income level
- Conditional Formatting: data bars, color scale, icon set (อ้างอิง: support.microsoft.com)
- Sort and Filter
- Flash Fill (อ้างอิง: softwarekeep.com)
5.1 Data Verification

5.2 Complete Case Analysis

5.3 Data Imputation

Business Intelligence (BI) คือชุดของ methodologies, processes, architectures และ technologies ที่แปลงข้อมูลดิบให้กลายเป็นข้อมูลที่มีความหมายและมีประโยชน์ เพื่อสนับสนุนการตัดสินใจเชิงกลยุทธ์ (strategic), เชิงยุทธวิธี (tactical) และเชิงปฏิบัติการ (operational) อย่างมีประสิทธิภาพ

ระบบ BI ประกอบด้วยการรวมกันของ: Data gathering, Data storage, Knowledge management

- Financial Performance Overview — community.powerbi.com
- Covid World Wide Report — community.powerbi.com
- MLB Baseball Batting Stats — community.powerbi.com
สรุปกระบวนการทั้งหมด (End-to-end flow)

Data Sources (LIS/HIS/PACS/Billing, NHSO, 43-file ฯลฯ) → Data Collection (ออกแบบฟอร์มใน Excel ให้ถูกหลัก: 1 คอลัมน์ = 1 ตัวแปร) → Data Preparation (ตรวจสอบ missing/outlier/unit → Complete Case Analysis หรือ Imputation) → Power BI: ETL → EDA → Visualization → Dashboard

- Thai Universal Health Coverage — National Health Security Office (NHSO)
- Government Service — Comptroller General's Department (กรมบัญชีกลาง)
- Social Security (ประกันสังคม)
- Nominal (ไม่มีลำดับ) เช่น เพศ, กรุ๊ปเลือด
- Ordinal (มีลำดับ) เช่น Tumor staging, ระดับการศึกษา, Pain Score (0–10)
- Value
- Format
มีคอลัมน์ En_HN, เพศ, วันที่ชำระค่าบริการ, ประเภทผู้ป่วย, Product code, Product name, Product type (LAB/SUPPLY), จำนวน, ค่ารักษา

รหัสยา, ยาและความแรง, ชื่อสามัญ, รูปแบบยา (Inj/Tab/Cap), จำนวน, หน่วยการจ่าย

- Thai Universal Health Coverage — National Health Security Office (NHSO)
- Government Service — Comptroller General's Department (กรมบัญชีกลาง)
- Social Security (ประกันสังคม)
ข้อมูลจากการปฏิบัติงานทางคลินิกตามปกติ (ไม่ได้วางแผนเพื่อการวิจัยแต่แรก)

อ้างอิง: J Am Coll Surg. 2017;224:1-7; Nat Rev Clin Oncol. 2019 May;16:312-325

Check point: Pain Score 0–10 และการแบ่งระดับการศึกษา เป็นตัวอย่างการแยกแยะ Nominal vs Ordinal

อ้างอิงภาพ: sqlservercentral.com, Luís A. Bastião Silva (2024) — Day 1: Foundations & the AI Pipeline: Data Matters: How We Collect, Clean, and Prepare for AI

ทำไมต้องเน้นเรื่องการออกแบบฟอร์มเก็บข้อมูล: ถ้าเก็บข้อมูลผิดรูปแบบตั้งแต่ต้น (header ซ้อน, merge cell, มี summary row ปน) จะทำให้โปรแกรมวิเคราะห์ข้อมูล (Excel, Power BI, R, Python) อ่านข้อมูลผิดพลาด หรือประมวลผลอัตโนมัติไม่ได้ ต้องมาแก้ไขทีหลัง (data cleaning) ซึ่งเสียเวลาและเสี่ยงผิดพลาดมากกว่า

พูดง่ายๆ คือ Data Collection ที่ดี = ออกแบบตารางให้ "machine-readable" ตั้งแต่แรก ไม่ใช่แค่ให้มนุษย์อ่านสวยงาม

หลักสำคัญที่สุด: 1 คอลัมน์ = 1 ข้อมูล (variable/concept) เท่านั้น

- Value
- Format
ตรวจสอบชนิดข้อมูล ด้วยฟังก์ชัน IS:

- ISNUMBER
- ISTEXT
- ISBLANK
- ISERROR
- ISNONTEXT
การแปลงชนิดข้อมูล:

- Number → Text: ใช้เครื่องหมาย ' นำหน้า หรือใช้ &""
- Text → Number: ใช้ *1, +0, /1, --
- Logic → Number: ใช้ *1, --
- Default Date format กำหนดที่ Date Format ใน Control Panel > Region
- วันที่ในระบบคือตัวเลข (Is Number) โดย Reference Date คือ 01/01/1900
- ควรใช้ปี ค.ศ. ทั้งหมด (All way ค.ศ.)
อ้างอิงเพิ่มเติม:

- xfanatical.com/blog/how-to-format-a-date-time-in-excel
- goskills.com/excel/resources/excel-date-functions (Date Function)
- excelexperttraining.com (Date Function, Fix cell reference)
Conditional Formatting

Sort and Filter

Flash Fill

ตรวจสอบ 3 เรื่องหลัก:

- Missing value (ค่าที่หายไป)
- Outliers (ค่าผิดปกติ)
- Data Unit (หน่วยข้อมูลไม่สอดคล้องกัน เช่น Height บางแถวเป็น cm บางแถวเป็น m — เช่น 158 vs 1.72)
- ลบข้อมูลที่ขาด/ผิดปกติออกทั้งหมด (remove all missing/abnormal records)
- อาจส่งผลกระทบต่อผลการวิเคราะห์
วิธีการแทนค่าที่ขาดหาย:

- แทนที่ด้วยค่า 0 (Replace with 0)
- Forward/Backward Filling
- Mean/Mode/Median Filling
- Interpolation/Extrapolation
อ้างอิงภาพ: airbyte.com

🖥️ Power BI Desktop

(Windows desktop application)

- เชื่อมต่อข้อมูล (Connect to data)
- แปลงและทำความสะอาดข้อมูลเพื่อสร้าง data model
- สร้าง visuals เช่น charts/graphs
- สร้าง reports (รวม visuals หลายหน้า)
- แชร์ reports ผ่าน Power BI service (ต้องมี license)
☁️ Power BI Service

(คลาวด์/SaaS — Power BI online)

- เชื่อมต่อ data source ได้ แต่ modeling มีข้อจำกัด
- License กำหนดสิ่งที่ทำได้
- งานตัวอย่าง: สร้าง dashboards, สร้าง/แชร์ apps, วิเคราะห์ข้อมูลเพื่อหา business insights
- รองรับ Paginated reports
📱 Power BI Mobile apps

(Windows, iOS, Android)

- ดู/สร้าง reports และ dashboards ที่สร้างจาก Desktop/Service
- ใช้งานได้ทั้ง on-premises และ cloud
- โต้ตอบกับรายงานผ่านมือถือได้
- Data Types: Number, Formula
- Number Format: Percentage, Decimal/whole number, Date, Time
- Cell format: Colour, Protection

##### 📊 Structured Data — ประเภทข้อมูล

- Categorical
- Numeric
- Boolean
- Date time

##### 🖼️ Unstructured Data

ได้แก่ Image, Signal, Text

- Data Types: Number, Formula
- Number Format: Percentage, Decimal/whole number, Date, Time
- Cell format: Colour, Protection
ตัวอย่างการตรวจสอบ: 01/03/2027 = 29 กุมภาพันธ์ 2560 (ต้องเช็ค Data format > Calendar Type: Thai Buddhist ให้ถูกต้อง เพราะอาจทำให้ตีความวันที่ผิดพลาดได้)

การจัดรูปแบบ cell โดยอัตโนมัติตามเงื่อนไขที่กำหนด ช่วยให้เห็นค่าผิดปกติ/แนวโน้มของข้อมูลได้ทันทีโดยไม่ต้องคำนวณเอง

- Data Bars — แสดงแท่งสีในเซลล์เทียบเท่าสัดส่วนกับค่า เหมาะกับการดูขนาด/เปรียบเทียบเชิงปริมาณ เช่น ดูค่ารักษาพยาบาลเปรียบเทียบระหว่างแผนกงาน
- Color Scale — ไล่ระดับสี (เช่น เขียว→เหลือง→แดง) ตามค่าตัวเลข เหมาะกับการสแกนหาค่าผิดปกติ/แนวโน้มอย่างรวดเร็ว เช่น ค่า Lab สูง/ต่ำในตารางเดียว
- Icon Set — ใส่ไอคอน (ลูกศร, ธง, สัญลักษณ์) กำกับค่าตามเกณฑ์ เหมาะกับการจัดกลุ่มสถานะ เช่น ปกติ/เสี่ยง/อันตราย
อ้างอิง: support.microsoft.com

- Sort — เรียงลำดับข้อมูลจากน้อย→มาก หรือ A→Z (หรือกลับกัน) เช่น เรียงผู้ป่วยตามอายุ หรือเรียงค่า Lab จากสูงสุดไปต่ำสุด
- Filter — ซ่อน/แสดงเฉพาะแถวที่ตรงตามเงื่อนไข เช่น ดูเฉพาะผู้ป่วยเพศหญิงที่อายุ > 60 ปี
- Custom Sort/Filter — จัดเรียง/กรองหลายเงื่อนไขพร้อมกัน เช่น เรียงตาม ID ก่อน แล้วค่อยเรียงตาม Day
เครื่องมือที่ Excel คาดเดารูปแบบจากตัวอย่างที่ผู้ใช้พิมพ์ไว้ใน 1–2 แถวแรก แล้วเติมข้อมูลที่เหลือให้อัตโนมัติตามรูปแบบนั้น โดยไม่ต้องเขียนสูตร

ตัวอย่างการใช้งาน

- แยกชื่อ-นามสกุลจากชื่อ-สกุลเต็มที่อยู่คอลัมน์เดียวกัน
- แก้ไขรูปแบบเบอร์โทรศัพท์ให้เป็นรูปแบบเดียวกัน (เช่น 081-234-5678)
- ดึงปี/เดือน/วันออกจากคอลัมน์ Birth date
อ้างอิง: softwarekeep.com

หลักการ: ควรลบออกไม่เกิน 5% ของข้อมูลทั้งหมด

- Nominal (ไม่มีลำดับ) เช่น เพศ, กรุ๊ปเลือด
- Ordinal (มีลำดับ) เช่น Tumor staging, ระดับการศึกษา, Pain Score (0–10)
ประโยชน์ในงาน Healthcare: ช่วยสแกนหาค่าผิดปกติ (เช่น 999 หรือค่า outlier) ด้วยสายตาก่อนทำ Data Verification ด้วยหน้าตาเปล่า โดยไม่ต้องเขียนสูตรแยก

มีประโยชน์มากในขั้นตอน Data Verification เพราะช่วย sort ค่าสูง/ต่ำสุดขึ้นมาดูได้ง่าย เห็น outlier ได้ทันที โดยไม่ต้องไลตาทีละแถว

ข้อควรระวัง: Flash Fill เดารูปแบบจากตัวอย่างที่ให้เท่านั้น ควรตรวจสอบผลลัพธ์ซ้ำอีกครั้งก่อนนำไปใช้จริง โดยเฉพาะข้อมูลที่มีรูปแบบไม่สม่ำเสมอ



## Topic 8: Diagnostic Studies & Performance (ID: 3cc0abc4-4cc7-8156-82ab-e8054a75e77d)

8. Statistical Inference and its Application in Clinical Research 2


### 1. Concept


#### การตรวจวินิจฉัยในเวชปฏิบัติ

- ตัวอย่าง: ผู้ป่วยมาด้วย RLQ pain — เริ่มต้นมี pre-test probability ของโรคต่างๆ ตาม differential diagnosis:
- เมื่อได้ประวัติ + ตรวจร่างกายเพิ่ม (ชาย + RLQ pain 3 วัน on-off + ไม่มี localizing sign + ไม่มีการอักเสบ) → probability เปลี่ยนไป (GI disturbance ขึ้นเป็น 50%, Ureteric stone 10%, Appendicitis เหลือ 5% ฯลฯ)
- เมื่อทำ Lab + CT เพิ่ม และผล CT ปกติ → probability เปลี่ยนอีกครั้ง (เช่น GI disturbance ขึ้นเป็น 90%)
🧠 อธิบายง่ายๆ: Pre-test → Post-test probability คืออะไร


#### Diagnostic Studies

เปรียบเทียบ diagnostic test 2 ชนิด: Gold standard (Reference test) vs Study test

🧠 อธิบายง่ายๆ: ทำไมต้องมี Gold standard


### 2. Performance Matrices


#### Classification (2×2 Table)

🧠 อธิบายง่ายๆ: Sensitivity/Specificity vs PPV/NPV ต่างกันอย่างไร


#### Accuracy vs F1-score

🧠 อธิบายง่ายๆ: ทำไม Accuracy ถึงหลอกตาได้ (Accuracy Paradox)


#### Case study: หา cutoff จากค่าต่อเนื่อง (เช่น ML score)

ข้อมูลตัวอย่าง 10 ราย:

แสดงให้เห็นว่า cutoff ต่างกัน ให้ Sensitivity/Specificity ต่างกัน (trade-off)

🧠 อธิบายง่ายๆ: ทำไม cutoff ยิ่งต่ำ Sensitivity ยิ่งสูง


#### ROC Curve (Receiver Operator Characteristic)

Plot ระหว่าง True positive rate (sensitivity) แกน y กับ False positive rate (1−specificity) แกน x ที่ cutoff ต่างๆ

🧠 อธิบายง่ายๆ: ROC curve และ AUC คืออะไรกันแน่


#### การเลือกจุดตัด (Cutoff)

- Test ที่แยกโรคได้ดี → ROC curve โค้งเข้าใกล้มุมบนซ้าย (least distance method)
- เมื่อ sensitivity เพิ่มขึ้น จะสูญเสีย specificity เพียงเล็กน้อย จนกระทั่งถึงระดับ sensitivity ที่สูงมาก
- วิธีเลือก cutoff:
🧠 อธิบายง่ายๆ: Youden's index เหมือน "จุดสมดุลบนไม้กระดก"


#### การใช้ Test ตาม Sensitivity/Specificity

🧠 อธิบายง่ายๆ: จำง่ายๆ ด้วย SnNout / SpPin


#### Likelihood Ratio (LR)

บอกว่า test มีประโยชน์เพียงใดในการเปลี่ยนแปลงการวินิจฉัย

🧠 อธิบายง่ายๆ: LR คือ "ตัวคูณความเชื่อ"


#### วิธีนำ LR ไปใช้ (Pre-test → Post-test probability)

pretest\ odds = \frac{pretest\ probability}{1 - pretest\ probability}

posttest\ probability = \frac{posttest\ odds}{1 + posttest\ odds}

🧠 อธิบายง่ายๆ: "Probability" กับ "Odds" ต่างกันยังไง


#### ตัวอย่างกรณีศึกษา

Chest radiograph (PA/Lat) วินิจฉัย Parapneumonic effusion เทียบกับ Chest CT (reference standard):


#### การแปลผล LR


#### Fagan's Nomogram

เครื่องมือกราฟิกแปลง pre-test probability → post-test probability โดยใช้ LR โดยไม่ต้องคำนวณ odds เอง (ลากเส้นตรงจาก pre-test probability ผ่านค่า LR ไปยัง post-test probability)

ตัวอย่างในเอกสาร (LR+ = 11, LR− = 0.40):

🧠 อธิบายง่ายๆ: Fagan's nomogram คือ "ไม้บรรทัดคำนวณลัด"


### 3. ปัจจัยที่มีผลต่อประสิทธิภาพของโมเดล

🧠 อธิบายง่ายๆ: ทำไมต้องเช็ค 5 ข้อนี้ทั้งหมด


#### ข้อ 1: Spectrum ของผู้ป่วย

- ผู้ป่วยมี diagnostic dilemma หรือไม่? — ควรเป็นกลุ่มที่ผู้ทำการรักษาไม่แน่ใจในการวินิจฉัย และจะใช้ test นี้ในเวชปฏิบัติจริงเพื่อคลี่คลายความไม่แน่ใจนั้น
- Spectrum Bias: หาก spectrum ของโรค/ไม่เป็นโรคในกลุ่มตัวอย่างต่างจากในเวชปฏิบัติจริง
- ประเด็นที่ทำให้เกิด spectrum bias:
🧠 อธิบายง่ายๆ: Spectrum bias เหมือนอะไร

Sample size สำหรับ Machine Learning

🧠 อธิบายง่ายๆ: ทำไมโมเดลซับซ้อนขึ้นต้องการข้อมูลมากขึ้น


#### ข้อ 2: Validation set ที่เป็นอิสระ

ประเภทของการแบ่งข้อมูล (Data splitting)

🧠 อธิบายง่ายๆ: ทำไม validation set ต้อง "เป็นอิสระ"


#### ข้อ 3: Independent & blind comparison กับ reference standard

- เลือก reference standard เหมาะสมหรือไม่? ตัดสินโดย Domain experts, ควรแทนความจริง และนำไปใช้กับผู้ป่วยทุกรายที่ตรวจด้วย index test
- เปรียบเทียบกับ reference standard ที่เป็นอิสระเหมาะสมหรือไม่? Index test (เช่น ML Model) ไม่ควรเป็นส่วนหนึ่งของ reference standard เอง — มิฉะนั้นจะได้ performance สูงเกินจริงอย่างผิดพลาด (falsely high)
- ผู้แปลผล test และ reference standard ปิดบัง (blind) ต่อกันหรือไม่?
🧠 อธิบายง่ายๆ: ทำไมต้อง "ปิดตา" ผู้แปลผล


#### ข้อ 4: Verification / Work-up Bias

คำถามสำคัญ: มีผลต่อความ valid ของผลการศึกษาหรือไม่? มีผลต่อ performance ของโมเดลหรือไม่?

🧠 อธิบายง่ายๆ: Verification bias เหมือนอะไร


#### ข้อ 5: รายละเอียดวิธีการที่เพียงพอให้ทำซ้ำได้

- มีแนวทางการรายงาน (Reporting guideline) ที่ควรอ้างอิง
- คุณภาพและขนาดของภาพ (Image size/quality) มีผลต่อ performance ของโมเดล — ตัวอย่าง: เปรียบเทียบ chest radiograph ที่ resolution ต่างกันของผู้ป่วยชาย 60 ปีที่มี thoracic mass; ทุก network และทุกระดับ distortion ค่า confidence จาก soft-max unit ลดลงเมื่อคุณภาพภาพลดลง
🧠 อธิบายง่ายๆ: ทำไมคุณภาพภาพถึงมีผลต่อโมเดล

Key issues ที่ควรระบุ


### 4. หัวข้ออื่นๆ


#### Multiple Tests

การใช้ test เดียวมักให้ผลความน่าจะเป็นที่ยังไม่ชัดเจน (inconclusive) โดยทั่วไปจึงไม่ควรหยุดกระบวนการวินิจฉัยแค่จุดนั้น

🧠 อธิบายง่ายๆ: Parallel = ประตู OR, Serial = ประตู AND

🧠 อธิบายง่ายๆ: ทำไมสมมติฐาน independence อาจไม่จริง


#### Clinical Prediction Rules

- ดัดแปลงจาก parallel testing โดยผสมผสานทั้งผลบวกและผลลบของหลายปัจจัยเพื่อพิจารณาการวินิจฉัย
- มักรวม history + physical examination + laboratory tests เข้าด้วยกัน
- แบ่งผู้ป่วยออกเป็นกลุ่มที่มี prevalence ของโรคแตกต่างกัน
🧠 อธิบายง่ายๆ: Clinical Prediction Rule คือ "ใบให้คะแนนสะสม"

คำนวณ Positive LR และ Negative LR จากตารางนี้ได้ตามสูตรข้างต้น

Diagnostic study & Model performance measures

อ.Chaiyawat Suppasilp (Chaiyawat.sup@mahidol.edu) · Ramathibodi CEB · 2026.09.09

เอกสารนี้สรุปจาก handout ต้นฉบับ + เพิ่มคำอธิบายแบบ Feynman Technique (อธิบายด้วยภาษาง่ายๆ/เปรียบเทียบ เหมือนสอนคนไม่มีพื้นฐาน) ไว้ในกล่อง 🧠 ใต้แต่ละหัวข้อ

Diagnostic test ครอบคลุม: History · Laboratory tests · Physical examination · Imaging procedures · Combination of tests · Clinical Prediction Rules

แนวคิดหลัก: การตรวจแต่ละครั้ง (Index test) เปลี่ยน Pre-test Probability ให้กลายเป็น Post-test Probability

ลองนึกภาพว่าคุณเป็นนักสืบ กำลังสืบคดี

- ตอนเริ่มต้น คุณมี "ผู้ต้องสงสัย" หลายคน แต่ละคนมีโอกาสเป็นคนร้ายไม่เท่ากัน (นี่คือ pre-test probability — ความน่าจะเป็นตั้งต้น ก่อนมีเบาะแสใดๆ เพิ่ม)
- ทุกครั้งที่คุณได้ เบาะแสใหม่ (= ผลตรวจ/ผล lab/ผล imaging หนึ่งอย่าง) ความสงสัยของคุณต่อผู้ต้องสงสัยแต่ละคนจะเปลี่ยนไป — บางคนน่าสงสัยขึ้น บางคนตัดออกไปเลย
- ความสงสัยที่ปรับใหม่นี้คือ post-test probability ซึ่งจะกลายเป็น "pre-test probability" ของรอบถัดไป เมื่อคุณหาเบาะแสเพิ่มอีก
ทุก diagnostic test ที่เราสั่ง (history, lab, imaging) ก็ทำหน้าที่แบบเดียวกัน คือ ปรับความเชื่อ (belief) ของเราทีละขั้น ไม่ใช่บอกคำตอบ "ใช่/ไม่ใช่" แบบเบ็ดเสร็จในทีเดียว

Gold standard เหมือน ไม้บรรทัดมาตรฐานที่ทุกคนยอมรับว่าแม่นที่สุด — ถ้าคุณอยากรู้ว่า "ไม้บรรทัดอันใหม่" (study test) วัดแม่นแค่ไหน คุณต้องเอาไปเทียบกับไม้บรรทัดมาตรฐานอันนี้

ปัญหาคือ: ไม่มีไม้บรรทัดไหนสมบูรณ์แบบ 100% — gold standard บางอย่างก็ยังมีข้อจำกัด (เช่น เจ็บตัว, แพง, ทำไม่ได้ในทุกคน) นี่คือเหตุผลที่เราต้องหา study test ที่ทำง่ายกว่า ถูกกว่า ปลอดภัยกว่า มาทดแทน — แต่ก็ต้องรู้ว่ามันเบี่ยงเบนจาก "ความจริง" ไปมากแค่ไหน

Check point ในเอกสาร: ลองนึกว่าอะไรคือ gold standard ของ Acute appendicitis และ Alzheimer's disease

(ตัวอย่างคำตอบทั่วไปทางคลินิก — ไม่ได้ระบุไว้ใน slide ต้นฉบับ): Acute appendicitis → surgical pathology ของชิ้นเนื้อไส้ติ่งที่ตัดออก; Alzheimer's disease → neuropathological examination ของสมอง (มักทำได้หลังเสียชีวิตเท่านั้น จึงต้องใช้เกณฑ์ทางคลินิก เช่น NINCDS-ADRDA แทนในทางปฏิบัติ)

PPV/NPV ขึ้นกับ prevalence ของโรค — prevalence เพิ่มขึ้น → PPV เพิ่มขึ้น, NPV ลดลง

Sensitivity/Specificity — คุณสมบัติของ "เครื่องตรวจจับควันไฟ"

ลองนึกถึงเครื่องตรวจจับควัน (smoke detector):

- Sensitivity สูง = ไวมาก จับควันได้แม้นิดเดียว → ถ้ามีไฟไหม้จริง มันแทบไม่พลาดแน่นอน (ดีสำหรับ "ไม่อยากพลาดเคสจริง") แต่ข้อเสียคือ อาจร้องเตือนตอนแค่ทอดไข่ควันขึ้นนิดหน่อย (false alarm)
- Specificity สูง = ไม่ค่อยร้องมั่ว จะร้องเมื่อมีไฟจริงๆ เท่านั้น (ดีสำหรับ "ไม่อยากตกใจเล่นๆ") แต่ข้อเสียคือ อาจไม่ทันร้องเตือนตอนไฟเพิ่งเริ่มไหม้เล็กๆ
สิ่งสำคัญ: Sensitivity/Specificity เป็น "คุณสมบัติของตัวเครื่องตรวจจับเอง" — ไม่เปลี่ยนไปตามว่าบ้านคุณมีโอกาสไฟไหม้บ่อยแค่ไหน

PPV/NPV — คำถามที่คุณอยากรู้จริงๆ ตอนเครื่องมันร้อง

พอเครื่องร้องเตือนขึ้นมา คำถามที่คุณสนใจจริงๆ คือ "เครื่องร้อง แปลว่าไฟไหม้จริงแค่ไหน" (=PPV) — และคำตอบนี้ ขึ้นกับว่าบ้านคุณมีโอกาสไฟไหม้บ่อยแค่ไหนด้วย (prevalence)

เปรียบเทียบ: เครื่องตรวจจับควันตัวเดียวกันเป๊ะๆ

- ติดในโรงงานที่เสี่ยงไฟไหม้บ่อย (prevalence สูง) → เครื่องร้อง มักจะไฟไหม้จริง (PPV สูง)
- ติดในบ้านที่แทบไม่เคยไฟไหม้เลย (prevalence ต่ำ) → เครื่องร้อง ส่วนใหญ่กลับเป็น false alarm (PPV ต่ำ) แม้เครื่องจะเป็นตัวเดียวกัน ไวเท่าเดิมทุกอย่าง!
นี่คือเหตุผลที่ PPV/NPV เปลี่ยนตาม prevalence แต่ Sensitivity/Specificity ไม่เปลี่ยน

ในปัญหาจริงส่วนใหญ่ class มักไม่สมดุล → F1-score มักเป็น metric ที่ดีกว่า Accuracy

สมมติมีโรคหายากมาก พบแค่ 1 ใน 1,000 คน ถ้าสร้างโมเดลโง่ๆ ที่ ทายว่า "ไม่มีใครเป็นโรค" ทุกคนเลย โดยไม่ตรวจอะไรเลย —

โมเดลนี้จะได้ Accuracy = 99.9% ทันที! (เพราะทายถูก 999 คนจาก 1,000 คน) แต่โมเดลนี้ไร้ประโยชน์อย่างสิ้นเชิง เพราะจับคนป่วยจริงไม่ได้แม้แต่คนเดียว (Sensitivity = 0%)

นี่คือเหตุผลที่เวลา class ไม่สมดุล (คนป่วยน้อยกว่าคนไม่ป่วยมาก) เราไม่ควรดู Accuracy อย่างเดียว — F1-score จะจับความล้มเหลวแบบนี้ได้ เพราะมันคำนึงถึงทั้ง Sensitivity (จับคนป่วยได้ไหม) และ PPV (จับแล้วแม่นไหม) ไปพร้อมกัน

ลองนึกภาพ ด่านตรวจคนเข้าเมือง ที่ใช้คะแนนความน่าสงสัยตัดสินใจ (ML score)

- ถ้าตั้ง cutoff ต่ำมาก (เช่น ≥2 = "แค่ดูน่าสงสัยนิดหน่อยก็เรียกตรวจ") → คุณจะจับผู้ต้องสงสัยจริงได้เกือบหมด (sensitivity สูง) แต่ก็จะเรียกตรวจคนบริสุทธิ์เยอะไปด้วย (specificity ต่ำ)
- ถ้าตั้ง cutoff สูงมาก (เช่น ≥5 = "ต้องน่าสงสัยมากๆ ถึงจะเรียกตรวจ") → คุณจะรบกวนคนบริสุทธิ์น้อยลง (specificity สูง) แต่ก็เสี่ยงปล่อยผู้ต้องสงสัยจริงหลุดไปด้วย (sensitivity ต่ำ)
ไม่มี cutoff ไหน "ถูกที่สุด" ในตัวเอง — ขึ้นกับว่าคุณกลัว การจับพลาด (miss) มากกว่า หรือกลัว การรบกวนคนที่ไม่ผิด (false alarm) มากกว่า

Area Under ROC Curve (AUC) ตัวอย่าง = 0.8400 (Asymptotic normal 95% CI ≈ 0.5546–1.0000)

เส้นทแยงมุม (diagonal) = test ที่ไม่ให้ข้อมูลอะไรเลย (เทียบเท่าการโยนเหรียญ)

ลองนึกภาพคุณกำลังหมุนปุ่มปรับความไวของสัญญาณกันขโมย ไปเรื่อยๆ ตั้งแต่ไวสุด (จับทุกความเคลื่อนไหว) ไปจนถึงไม่ไวเลย (ไม่จับอะไรเลย) — ทุกจุดที่คุณหมุนปุ่ม จะได้ค่า sensitivity/specificity คู่หนึ่งเสมอ

ROC curve คือการเอาทุกจุดที่หมุนปุ่มได้ มาลากเป็นเส้นกราฟ — แสดงให้เห็น "trade-off" ทั้งหมดที่เป็นไปได้ ณ ทุกระดับความไว ไม่ใช่แค่จุดใดจุดหนึ่ง

AUC (พื้นที่ใต้กราฟ) คือการสรุปทั้งเส้นกราฟให้เหลือ "เลขตัวเดียว" ที่บอกว่า test นี้ แยกคนป่วยกับคนไม่ป่วยได้เก่งแค่ไหนโดยรวม ไม่ขึ้นกับว่าจะเลือก cutoff ตรงไหน:

- AUC = 1.0 → แยกได้สมบูรณ์แบบ (perfect test)
- AUC = 0.5 → แยกไม่ได้เลย เหมือนโยนเหรียญทาย (เส้นทแยงมุม)
- AUC = 0.84 (ตัวอย่างในเอกสาร) → ค่อนข้างดี (โดยทั่วไป >0.8 ถือว่าดี)
ข้อดีของ AUC คือช่วยเปรียบเทียบ "ตัว test สองตัว" ได้อย่างยุติธรรม โดยยังไม่ต้องตัดสินใจว่าจะใช้ cutoff ไหน

- พิจารณาจากบริบททางคลินิก (clinical application)
- ใช้ Accuracy สูงสุด
- ใช้ Youden's index = Sensitivity + Specificity − 1 (จุดสูงสุด อยู่บริเวณ "shoulder" ของ ROC curve)
ตัวอย่างจากตาราง: Youden's index สูงสุด (60%) เกิดที่ cutoff ≥3 และ ≥4

นึกถึง ไม้กระดก (see-saw) ที่ด้านหนึ่งคือ Sensitivity อีกด้านคือ Specificity — เวลาคุณขยับ cutoff ด้านหนึ่งจะสูงขึ้น อีกด้านจะต่ำลงเสมอ (trade-off)

Youden's index (Sn+Sp−1) คือการหา จุดที่ผลรวมของทั้งสองด้านมากที่สุด — ไม่ใช่จุดที่ด้านใดด้านหนึ่งสูงสุดโดยไม่สนอีกด้าน แต่เป็นจุดที่ "สมดุลรวม" ดีที่สุด เหมือนหาจุดวางตุ้มน้ำหนักที่ทำให้ไม้กระดกสมดุลมากที่สุดนั่นเอง — ในทางกราฟ จุดนี้จะอยู่แถว "ไหล่ (shoulder)" ของ ROC curve ที่โค้งเข้าใกล้มุมบนซ้ายที่สุด

นี่คือ mnemonic ที่ใช้กันทั่วไปในวงการแพทย์ (ไม่ได้อยู่ใน slide แต่ช่วยจำหลักการเดียวกัน):

- SnNout: Sensitivity สูง (Sn) + ผลเป็น Negative (N) → ใช้ "out" คัดโรคออกได้ค่อนข้างมั่นใจ (เพราะ test ไวมาก ถ้าเป็นโรคจริงมันแทบไม่พลาด ดังนั้นถ้าผลลบ ก็ไม่น่าจะเป็นโรค)
- SpPin: Specificity สูง (Sp) + ผลเป็น Positive (P) → ใช้ "in" ยืนยันว่าเป็นโรคได้ค่อนข้างมั่นใจ (เพราะ test แม่นมาก ไม่ค่อย false positive ดังนั้นถ้าผลบวก ก็น่าจะเป็นโรคจริง)
Likelihood Ratio ตอบคำถามว่า "ผลตรวจนี้ ควรทำให้ฉันเชื่อว่าเป็นโรคมากขึ้นกี่เท่า"

- LR+ = 10 แปลว่า ผลบวกนี้ น่าจะพบในคนที่เป็นโรคมากกว่าคนไม่เป็นโรคถึง 10 เท่า — ดังนั้นเมื่อเจอผลบวก ควรจะ "เชื่อมากขึ้นอย่างมีนัยสำคัญ" ว่าเป็นโรค
- LR− = 0.1 แปลว่า ผลลบนี้ พบในคนเป็นโรคน้อยกว่าคนไม่เป็นโรคมาก (เพียง 1 ใน 10 ของอัตราปกติ) — ดังนั้นผลลบนี้ช่วย "ตัดออก" ได้ค่อนข้างมั่นใจ
ข้อดีของ LR เหนือ Sensitivity/Specificity: LR สามารถเอาไป "คูณ" กับความเชื่อตั้งต้น (pretest odds) ของผู้ป่วยแต่ละคนได้โดยตรง — ทำให้เราปรับความน่าจะเป็นเฉพาะบุคคลได้ ไม่ใช่แค่บอกคุณสมบัติรวมของ test เฉยๆ

- Probability = สัดส่วนของ "เหตุการณ์ที่เกิด" เทียบกับ "เหตุการณ์ทั้งหมด" (เช่น เป็นโรค 3 ใน 10 คน = probability 30%)
- Odds = สัดส่วนของ "เหตุการณ์ที่เกิด" เทียบกับ "เหตุการณ์ที่ไม่เกิด" (เช่น เป็นโรค 3 คน ไม่เป็น 7 คน = odds 3:7 หรือ 0.43)
เหตุผลที่ต้องแปลงเป็น odds ก่อนคูณด้วย LR คือ odds คูณกันได้ตรงไปตรงมา (multiplicative) ในขณะที่ probability คูณตรงๆ ไม่ได้ (เพราะ probability ต้องอยู่ระหว่าง 0-1 เสมอ ถ้าคูณตรงๆ อาจเกิน 1 ซึ่งไม่มีความหมาย) จึงต้องแปลงไป-กลับระหว่าง probability ↔ odds ทุกครั้งที่ใช้ LR

คำนวณจากตาราง (เพิ่มเติมจาก slide ต้นฉบับ ซึ่งเว้นให้ผู้เรียนคิดเอง):

- Sensitivity = 40/64 = 62.5%
- Specificity = 48/51 = 94.1%
- PPV = 40/43 = 93.0%
- NPV = 48/72 = 66.7%
- LR+ = 0.625 / (1−0.941) = 0.625/0.0588 ≈ 10.6
- LR− = (1−0.625) / 0.941 = 0.375/0.941 ≈ 0.40
ค่า LR+ ≈ 11 และ LR− ≈ 0.40 ที่ได้นี้ ตรงกับตัวเลขที่ใช้สาธิตใน Fagan's nomogram ด้านล่าง — เป็นกรณีศึกษาเดียวกัน

แม้ LR จะคงที่ prior probability (prevalence/pretest) มีผลอย่างมากต่อ post-test probability

Fagan's nomogram เปรียบเหมือน slide rule (ไม้คำนวณโบราณก่อนมีเครื่องคิดเลข) — แทนที่จะต้องนั่งคำนวณสูตร odds ↔ probability ทุกครั้ง คุณแค่:

- หาจุด pre-test probability บนเส้นซ้าย
- ลากเส้นตรงผ่านค่า LR ตรงกลาง
- เส้นจะไปตัดกับ post-test probability บนเส้นขวาโดยอัตโนมัติ
จากตัวอย่างในตาราง จะเห็นว่า ค่า LR เท่ากันเป๊ะ แต่ post-test probability ต่างกันมาก ขึ้นอยู่กับว่า prior probability (ความชุกของโรค/ความสงสัยตั้งต้น) เริ่มต้นสูงหรือต่ำ — นี่คือเหตุผลว่าทำไมแพทย์คนเดียวกัน ใช้ test เดียวกัน แต่แปลผลไม่เหมือนกันในผู้ป่วยแต่ละราย เพราะ pretest probability ของแต่ละคนไม่เท่ากัน

คำถามหลัก 5 ข้อ สำหรับประเมินความ valid ของ diagnostic study:

- กลุ่มตัวอย่างมี spectrum ของผู้ป่วยที่เหมาะสมกับการใช้ test ในเวชปฏิบัติจริงหรือไม่?
- มี validation set ที่เป็นอิสระอย่างสมบูรณ์หรือไม่?
- มีการเปรียบเทียบแบบ independent และ blind กับ reference standard หรือไม่?
- ผลของ test ที่ประเมินมีผลต่อการตัดสินใจทำ reference standard หรือไม่?
- อธิบายวิธีการทำ test ไว้ละเอียดเพียงพอให้ทำซ้ำได้หรือไม่?
ลองนึกภาพว่าคุณกำลังจะซื้อรถมือสอง — ต่อให้ผู้ขายบอกตัวเลขสวยหรูแค่ไหน (เช่น "sensitivity 99%!") คุณก็ยังต้องเช็คว่า:

- เขาทดสอบรถกับ "สภาพถนนแบบไหน" (spectrum ของผู้ป่วย — ตรงกับที่คุณจะใช้จริงไหม)
- เขาทดสอบกับรถ "คันเดียวกับที่ปรับแต่งเครื่อง" หรือรถคันอื่นที่เป็นอิสระ (independent validation set)
- คนตรวจสภาพรถ รู้หรือเปล่าว่าเป็นรถของผู้ขายเอง (blind comparison)
- เขาเลือกทดสอบเฉพาะรถที่ผ่านด่านแรกมาแล้วหรือเปล่า (verification bias)
- เขาบอกรายละเอียดวิธีทดสอบครบไหม ให้คนอื่นไปทดสอบซ้ำได้ (reproducibility)
ถ้าข้อใดข้อหนึ่งมีปัญหา ตัวเลข performance ที่ได้ก็ ไม่น่าเชื่อถือเท่าที่ตัวเลขบอก แม้ตัวเลขจะดูสวยแค่ไหนก็ตาม

- Sensitivity ขึ้นกับ spectrum ของกลุ่มที่เป็นโรค
- Specificity ขึ้นกับ spectrum ของกลุ่มที่ไม่เป็นโรค (หรือโรคอื่นที่อาการคล้ายกัน)
ตัวอย่าง: งานวิจัยใช้ BNP แยก dyspnea จาก CHF กับ acute asthma แต่คัดเฉพาะผู้ป่วยอาการหนัก (severe cases) เท่านั้น → sensitivity สูงเกินจริง และ cutoff ที่ได้จะสูงกว่าที่ควรจะเป็น

- บริบทโรงพยาบาลตติยภูมิ vs หน่วยปฐมภูมิ (Primary care)
- การออกแบบ Case-control vs Cross-sectional/Cohort
- disease spectrum ที่แตกต่างกัน
เหมือนการทดสอบยาแก้ปวดหัวโดยเอาไปลองกับ คนที่ปวดหัวรุนแรงระดับ "จะเป็นลม" เท่านั้น (ไม่รวมคนปวดหัวเบาๆ) — พอเทียบกับยาหลอก ยาตัวนี้อาจดูเหมือน "ได้ผลชัดเจนมาก" เพราะกลุ่มทดสอบมีแต่เคสรุนแรงที่เห็นความแตกต่างง่าย

แต่พอเอายาตัวนี้ไปใช้จริงกับคนทั่วไปที่ปวดหัวธรรมดาๆ (ซึ่งเป็นกลุ่มส่วนใหญ่ที่จะเจอในชีวิตจริง) ผลอาจไม่ได้ดีขนาดที่ทดสอบมา เพราะกลุ่มตัวอย่างตอนทดสอบ "ไม่ตรงกับสเปกตรัมของคนที่จะใช้จริง"

หลักคิดง่ายๆ: ทดสอบกับใคร ก็ควรใช้กับคนแบบนั้น ถ้าทดสอบกับกลุ่มที่ต่างจากการใช้งานจริงมาก ตัวเลข performance ที่ได้ก็เชื่อถือไม่ได้เต็มที่

ลองนึกถึงการเรียนรู้จำหน้าคน:

- ถ้าให้กฎง่ายๆ แค่ "คนผมยาว = ผู้หญิง คนผมสั้น = ผู้ชาย" (โมเดลง่าย เหมือน linear regression) — คุณอาจเรียนรู้กฎนี้จากตัวอย่างแค่ไม่กี่สิบคนก็พอเดาได้ประมาณหนึ่ง
- แต่ถ้าอยากให้แยกแยะใบหน้าคนได้แม่นยำจริงๆ ทุกมุม ทุกแสง ทุกอายุ (โมเดลซับซ้อน เหมือน deep learning) — คุณต้องเห็นตัวอย่างนับหมื่นนับแสนใบหน้า ถึงจะเรียนรู้ "รูปแบบที่ซับซ้อน" ได้จริงโดยไม่ใช่แค่จำตัวอย่างที่เคยเห็น (memorize) เฉยๆ
ยิ่งโมเดลมี "พารามิเตอร์" ให้ปรับเยอะเท่าไร (ยิ่งซับซ้อน) ก็ยิ่งต้องการข้อมูลตัวอย่างมากขึ้นเพื่อป้องกันไม่ให้โมเดล "จำ" ข้อมูล training แทนที่จะ "เข้าใจรูปแบบ" จริงๆ (= overfitting)

คำศัพท์

- Development set = Training set + Tuning set
- Tuning set = Validation set (เรียก Development set ในวงการ engineering) = Test set (ถ้าไม่มี Validation set แยก)
- Validation Set = Test set = Holdout set = Evaluation set
หาก validation set ไม่เป็นอิสระอย่างสมบูรณ์ → ประเมิน performance สูงเกินจริง (overestimate) เมื่อนำไปใช้จริง; วิธีแบ่งข้อมูลก็มีผล (เช่น training set >60% อาจทำให้เกิด overfitting)

ไม่มีสัดส่วนการแบ่งที่เหมาะสมที่สุดตายตัว — หลักสำคัญคือ Training, Tuning, Test set ต้องเป็นตัวแทนของการกระจายตัว (distribution) ของข้อมูลจริง เพียงพอที่จะสะท้อนความแปรปรวนของข้อมูล

เปรียบเหมือนนักเรียนที่แอบได้โจทย์ข้อสอบล่วงหน้า — ถ้าครูให้นักเรียนอ่านโจทย์ข้อสอบก่อนสอบจริง แล้วนักเรียนทำข้อสอบได้ 100% คะแนนนี้ไม่ได้บอกว่านักเรียนเข้าใจเนื้อหาจริง มันแค่บอกว่า "จำโจทย์ได้"

โมเดล ML ก็เหมือนกัน — ถ้า validation set (ข้อสอบ) ไปปนกับ training set (สิ่งที่ใช้สอน) ไม่ว่าจะโดยตั้งใจหรือไม่ตั้งใจ (เช่น มีข้อมูลผู้ป่วยคนเดียวกันอยู่ทั้งสองชุด = data leakage) → ผลที่วัดได้จะ "สวยเกินจริง" และพอเอาโมเดลไปใช้กับผู้ป่วยจริงที่ไม่เคยเห็นมาก่อน ผลจะแย่กว่าที่ตัวเลขบอกไว้มาก

ตัวอย่าง: เป้าหมายคือหา pulmonary nodule บน CT แต่ผลแสดงใน study ก่อนหน้าแล้ว; หรือประเมิน BIRAD score โดยรู้อยู่แล้วว่าผู้ป่วยได้ทำ breast biopsy มาก่อน (BIRAD ต้องอย่างน้อย 4)

เนื่องจากกระบวนการพัฒนา machine learning มักไม่ค่อยมีปัญหาเรื่อง independency และ blinding เท่า diagnostic study แบบดั้งเดิม

เหมือนกรรมการตัดสินกีฬาที่รู้ล่วงหน้าว่าใครเป็นทีมโปรด — ต่อให้กรรมการตั้งใจจะตัดสินอย่างเป็นธรรม แต่การรู้ข้อมูลล่วงหน้าอาจทำให้ "โน้มเอียง" การตัดสินโดยไม่รู้ตัว (unconscious bias)

ในทางการแพทย์ก็เช่นกัน — ถ้าคนอ่าน CT รู้อยู่แล้วว่าผู้ป่วยเคยตรวจพบอะไรมาก่อน (เช่น รู้ว่ามี biopsy ยืนยันมะเร็งแล้ว) การอ่านผล CT ครั้งใหม่อาจ "โน้มเอียง" ไปทางเดียวกับที่รู้มาก่อน ทำให้ผลที่ได้ดูแม่นยำกว่าความเป็นจริง — การ blind จึงช่วยให้มั่นใจว่าผลที่ได้มาจาก "ตัว test เอง" ไม่ใช่จากอคติของผู้อ่านผล

Verification bias (Work-up bias) เกิดขึ้นเมื่อ:

- มีเพียงผู้เข้าร่วมบางส่วนที่ได้รับ index test แล้วได้ไปตรวจ reference standard ต่อ (ไม่ใช่ทุกคน)
- ผู้เข้าร่วมบางคนได้รับ reference standard test หนึ่ง ขณะที่บางคนได้รับ reference standard test อื่นที่แตกต่างกัน
เหมือนครูที่ตรวจการบ้านซ้ำเฉพาะนักเรียนที่ได้คะแนนสอบต่ำ (ไม่ตรวจซ้ำนักเรียนที่คะแนนดีอยู่แล้ว) — ถ้าครูสรุปว่า "การบ้านช่วยพัฒนาการเรียน" จากการตรวจซ้ำเฉพาะกลุ่มนี้ ข้อสรุปจะเอนเอียงเพราะไม่ได้เห็นข้อมูลของนักเรียนกลุ่มที่ไม่ถูกตรวจซ้ำเลย

ในทางการแพทย์ — ถ้า test ให้ผลบวก แพทย์มักส่งตรวจ reference standard ต่อ (เช่น biopsy) แต่ถ้า test ให้ผลลบ อาจไม่ส่งตรวจต่อเพราะคิดว่าไม่จำเป็น → ทำให้ข้อมูลที่ได้เอนเอียงไปทางกลุ่ม "test บวก" มากกว่า ซึ่งอาจทำให้ตัวเลข sensitivity/specificity ที่คำนวณได้ผิดเพี้ยนจากความเป็นจริง

เหมือนการให้คนอ่านเอกสารที่ถ่ายเอกสารซ้ำมาหลายรอบจนเบลอ — ต่อให้เนื้อหาเหมือนเดิมทุกตัวอักษร แต่ถ้าภาพเบลอ ตัวหนังสือบิดเบี้ยว คนอ่านก็จะอ่านผิดหรือไม่มั่นใจมากขึ้น

โมเดล deep learning ที่เรียนรู้จากภาพก็เช่นกัน — มันเรียนรู้ "ลวดลาย/พิกเซล" ในระดับละเอียดมาก ถ้าภาพตอนใช้งานจริง (เช่น จากเครื่อง X-ray รุ่นเก่า, บีบอัดไฟล์จนภาพแตก) มีคุณภาพต่ำกว่าภาพที่ใช้ตอน train โมเดลจะ "มั่นใจน้อยลง" หรือทำนายผิดพลาดมากขึ้น — นี่คือเหตุผลที่ต้องรายงานรายละเอียดของภาพที่ใช้ให้ครบ เพื่อให้คนอื่นรู้ว่าโมเดลนี้ใช้ได้ดีกับภาพคุณภาพระดับไหน

งานวิจัยด้าน ML ต้องอธิบายทั้งระเบียบวิธีดั้งเดิมและส่วน Data handling กับ Modeling ไม่ใช่แค่อย่างใดอย่างหนึ่ง

ลองนึกภาพระบบล็อกบ้าน:

- Parallel testing เหมือนบ้านที่มีหลายประตู เข้าทางไหนก็ได้ถือว่าเข้าบ้านได้ (= "OR": test A บวก หรือ test B บวก ก็ถือว่าเป็นโรค) → เพิ่มโอกาส "จับโรคได้" (sensitivity สูงขึ้น) เพราะมีหลายช่องทางที่จะตรวจพบ แต่ก็เพิ่มโอกาส "เข้าใจผิดคิดว่าเป็นโรค" (false positive) มากขึ้นด้วย เพราะแค่ประตูเดียวหลุดก็นับว่าเข้าได้แล้ว
- Serial testing เหมือนบ้านที่ต้องผ่านทุกด่านตามลำดับ (ประตูรั้ว → ประตูบ้าน → ตู้เซฟ) ถ้าด่านไหนผ่านไม่ได้ก็จบเลย (= "AND": ต้อง test A บวก และ test B บวก จึงจะสรุปว่าเป็นโรค) → มั่นใจได้มากขึ้นว่าถ้าสรุปว่าเป็นโรค คือเป็นโรคจริง (specificity สูงขึ้น) แต่ก็เสี่ยง "พลาดเคสจริง" มากขึ้น เพราะแค่ด่านเดียวไม่ผ่านก็ตกไปแล้ว
สมมติฐาน Independence: การรวม multiple tests อาศัยสมมติฐานว่าแต่ละ test เป็นอิสระต่อกัน

ตัวอย่าง: Test A sensitivity 80%, Test B sensitivity 60% → parallel testing รวมกัน = 80% + (60%×(100%−80%)) = 80% + 12% = 92%

แต่หาก test แรกตรวจพบ case ทั้งหมดที่ควรพบไปแล้ว test ถัดไปจะไม่ช่วยเพิ่มอะไรในกลุ่ม 20% ที่เหลือ (สมมติฐาน independence อาจไม่จริงในทางปฏิบัติ)

เหมือนการถามเพื่อนสองคนที่ดูหนังเรื่องเดียวกันมาด้วยกัน ว่าหนังสนุกไหม — แม้จะถามสองคน แต่ความเห็นของพวกเขาไม่ได้เป็นอิสระต่อกันจริงๆ เพราะดูมาด้วยกัน คุยกันมาก่อน อาจมีอิทธิพลต่อกัน คำตอบที่ได้จึงให้ข้อมูลใหม่น้อยกว่าที่ควรจะเป็นถ้าถามคนแปลกหน้าสองคนที่ไม่รู้จักกัน

ในทางการแพทย์ — ถ้า Test A และ Test B ต่างก็ตรวจจับ "กลไกทางชีวภาพเดียวกัน" (เช่น สองตัวชี้วัดที่สัมพันธ์กับการอักเสบแบบเดียวกัน) การรวมสอง test นี้เข้าด้วยกันอาจไม่ได้เพิ่ม sensitivity มากเท่าที่สูตรคำนวณบอกไว้ เพราะคนที่ Test A ตรวจพบ มักจะเป็นคนกลุ่มเดียวกับที่ Test B ตรวจพบด้วยอยู่แล้ว (ไม่ใช่กลุ่มใหม่ทั้งหมด)

ตัวอย่างในเอกสาร: Alvarado Score สำหรับวินิจฉัย acute appendicitis

ลองนึกถึง แบบทดสอบให้คะแนนสะสม เช่น แบบประเมินความเสี่ยงโรคหัวใจที่ให้คะแนนตามอายุ, ความดัน, การสูบบุหรี่ ฯลฯ แล้วรวมคะแนนทั้งหมดเป็นตัวเลขเดียว

Alvarado Score ก็ทำงานแบบเดียวกัน — แทนที่จะดูอาการทีละอย่างแยกกัน (ปวดท้อง, ไข้, เม็ดเลือดขาวสูง ฯลฯ) มันให้ คะแนนแต่ละอาการ แล้วรวมกันเป็นคะแนนรวม เพื่อแบ่งผู้ป่วยเป็นกลุ่มความเสี่ยงต่ำ/กลาง/สูง ต่อการเป็น acute appendicitis

ข้อดีคือช่วยให้แพทย์ (โดยเฉพาะมือใหม่) มี "เกณฑ์ที่เป็นระบบ" แทนที่จะอาศัยความรู้สึก/ประสบการณ์ส่วนตัวเพียงอย่างเดียวในการตัดสินใจ

เอกสารต้นฉบับ: Chaiyawat Suppasilp (Chaiyawat.sup@mahidol.edu) — Ramathibodi CEB

คำอธิบายในกล่อง 🧠 "Feynman" เป็นการเปรียบเทียบเพิ่มเติมเพื่อช่วยความเข้าใจ ไม่ได้อยู่ใน slide ต้นฉบับ

Gold standard / Reference test / Criterion standard

- คือการทดสอบที่บ่งบอก "ความจริง" ว่ามีโรคหรือไม่ (เช่น Tissue pathology, Physiologic studies เช่น cardiac catheterization)
- สำหรับโรคที่ไม่ใช่ self-limited และแสดงอาการชัดเจนขึ้นตามเวลา → follow-up ใช้เป็น gold standard ได้ (ระยะเวลาต้องนานพอ แต่ไม่นานเกินจนมีผู้ป่วยรายใหม่ปนเข้ามา)
- อาจเปลี่ยนแปลงได้ตามการยอมรับของผู้เชี่ยวชาญในสาขา
Study test

- พยายามประมาณผลของ reference test
- พิจารณาด้าน:
Cutoff ≥2

→ Sensitivity = 100%, Specificity = 60%

Cutoff ≥5

→ Sensitivity = 60%, Specificity = 80%

- Feasibility
- Cost
- Safety
Sensitivity (True positive rate)

= TP / (TP+FN)

ในกลุ่มที่เป็นโรคจริง มีสัดส่วนเท่าไรที่ test ให้ผลบวก

Specificity (True negative rate)

= TN / (FP+TN)

ในกลุ่มที่ไม่เป็นโรค มีสัดส่วนเท่าไรที่ test ให้ผลลบ

PPV (Positive Predictive Value)

= TP / (TP+FP)

ถ้า test บวก มีโอกาสเป็นโรคเท่าไร

NPV (Negative Predictive Value)

= TN / (FN+TN)

ถ้า test ลบ มีโอกาสไม่เป็นโรคเท่าไร

Positive LR (LR+)

= Sensitivity / (1−Specificity)

= [a/(a+c)] / [b/(b+d)]

ผลบวกพบในกลุ่มเป็นโรคบ่อยกว่ากลุ่มไม่เป็นโรคกี่เท่า

Negative LR (LR−)

= (1−Sensitivity) / Specificity

= False Negative rate / True Negative rate

ผลลบพบในกลุ่มเป็นโรคบ่อยกว่ากลุ่มไม่เป็นโรคกี่เท่า

Parallel testing

- ทำ test ทั้งหมดพร้อมกัน
- ถือว่าเป็นโรคหาก test ใด test หนึ่งบวก
- เพิ่ม Sensitivity
Serial testing

- สั่ง test ถัดไปตามผล test ก่อนหน้า
- ต้องบวกทุก test จึงสรุปว่าเป็นโรค
- เพิ่ม Specificity


## Topic 9: RWD & RWE Causal Inference (ID: 3cc0abc4-4cc7-816e-add3-fd479ea7f5c8)

9. Real-World Data (RWD) and Real-World Evidence (RWE) in Healthcare

📝 Mock Test 1

📝 Mock Test 2

📝 Mock Test 3

📝 Mock Test 4

📝 Mock Test 5


### 🎲 1. พื้นฐานความน่าจะเป็น

✅ สัจพจน์ของความน่าจะเป็น (Axioms)

➕ Probability of OR

🔗 Conditional Probability & Independence


#### 🧮 Bayes' Theorem


#### 🎯 ทำความเข้าใจง่าย: Bayes' Theorem คืออะไรกันแน่

🏒 ตัวอย่างจำง่ายสุด: กระเป๋าลูกบอล

🐶 ตัวอย่างจำง่าย: เสียงหมาเห่า

🧮 ที่มาของสูตร — มาจาก Conditional Probability ธรรมดา


##### 🦠 ตัวอย่างประยุกต์: COVID Rapid Test


##### ⚖️ Frequentist vs Bayesian

P(θ|D) = P(D|θ)P(θ) / P(D) — เมื่อ P(D) ไม่มี analytical form ใช้ MCMC หรือ Variational inference


### 🔀 2. Causality พื้นฐาน

🔺 Reichenbach's Common Cause Principle (RCCP)


##### 🪨 Simpson's Paradox (ตัวอย่างนิ่วในไต)

⚠️ A ชนะทุกกลุ่มย่อยแต่แพ้เมื่อรวมข้อมูล เพราะสัดส่วนผู้ป่วยแต่ละกลุ่มไม่เท่ากัน


#### 🕸️ Causal Graph / DAG

- Node = ตัวแปร, Arc = ความสัมพันธ์เชิงสาเหตุโดยตรง (Vⱼ → Vᵢ)
- DAG ไม่มี directed cycle
🧩 Four Elemental Confounds

🚦 D-Separation


#### 🧭 จะรู้ได้ยังไงว่าตัวแปรไหนเป็นเหตุ ไหนเป็นผล

🕒 1. ลำดับเวลา (Temporal Order) — เกณฑ์ที่แข็งแรงที่สุด

🧬 2. กลไกทางชีวภาพ/ฟิสิกส์ที่รู้จักอยู่แล้ว

🧪 3. หลักฐานจาก RCT ที่เคยทำมาก่อน

👨‍⚕️ 4. ความเห็นผู้เชี่ยวชาญ (Domain Expert)

🧠 5. Logic และ Common Sense

✅ ขั้นตอนปฏิบัติเวลาสร้าง DAG จริง


##### 🩺 ตัวอย่างไดอะแกรมทางการแพทย์: Diet/Disease และ Smoking/Cancer


##### 🎛️ Confounding vs RCT vs Observational Study


### 🪜 3. Pearl Causal Hierarchy (บันได 3 ขั้น)

- ML อยู่ที่ Rung 1: fit curve หา pattern จาก observational data (P(Y|X))
- Causal Inference อยู่ที่ Rung 2-3: ต้องระบุสมมติฐานเชิงสาเหตุ มักเป็นทางการในรูป causal model
📊 ตารางขยาย: Association is Insufficient (พร้อม Data Type และ ML Status)


### 🧪 4. RCT และความท้าทายของ RWD

🚧 ข้อจำกัดของ RCT

📐 นิยาม RWD Challenge อย่างเป็นทางการ (3 ข้อ)


### 🌗 5. Potential Outcomes Framework (POF)

Causal effect = E(Y¹ − Y⁰) — สองสำนักหลัก: Potential Outcome (D. Rubin) และ Structural Causal Model (SCM)

- Yᵢ¹ = ผลลัพธ์ของหน่วย i ถ้าได้รับ treatment (T=1)
- Yᵢ⁰ = ผลลัพธ์ของหน่วย i ถ้าไม่ได้รับ treatment (T=0)
📏 Average Treatment Effect (ATE)

📋 สมมติฐานของ POF


#### 🛠️ วิธีประมาณค่า


### 🏗️ 6. Structural Causal Model (SCM)

ตัวอย่าง X→M→Y พร้อม X→Y:

```
Y := f_Y(X, M) + U_Y
M := f_M(X) + U_M
X := U_X
```

Regression ในมุมมอง SCM: y := αX + ε โดย α = ∂/∂x E[Y|do(x)], ε = y − E[Y|do(x)]

🔁 Mediation Analysis


### 🎯 7. ATE / CATE / ITE


##### 🧠 Causal Graph สำหรับ personalized stroke prevention

- C = Individual characteristic (พันธุกรรม, adherence, socioeconomic)
- t = Treatment/Risk (เช่น antiplatelets)
- X = Features (age, gender, DM, HT, DLP, AF)
- Y = Outcome (Stroke)
- ITE: P(Y|X=x,t=1,C_ind) − P(Y|X=x,t=0,C_ind)
🩺 ตัวอย่างงานวิจัยจริง: DAG of Stroke


### 🕳️ 8. หัวข้อขยาย: Missingness และ Transportability

🧩 DAG of Missingness

✈️ Causal Transportability


### 🌟 แก่นของบทเรียน


### 🍎 สรุปแบบง่าย (Feynman Technique)


##### 🔧 ทางแก้ 2 แบบ


##### 🍦 ตัวอย่างจำง่าย: ไอศกรีมกับคนจมน้ำ

> สรุปประโยคเดียว: "เห็นสองสิ่งไปด้วยกัน" ไม่เท่ากับ "สิ่งหนึ่งทำให้อีกสิ่งเกิด" — ต้องมีลูกศรจริงจากสาเหตุไปผล และต้องระวังทั้งตัวกวนใจ (confounder) กับกับดักการเลือกกลุ่มตัวอย่าง (collider)

Q1. ข้อใดคือนิยามของ Sample Space ที่ถูกต้อง

- A) เซตของผลลัพธ์ที่เป็นไปได้ทั้งหมดของการทดลอง
- B) ค่าเฉลี่ยของข้อมูลทั้งหมด
- C) จำนวนตัวแปรอิสระ
- D) ผลลัพธ์ที่เกิดขึ้นบ่อยที่สุด
<details><summary>🔑 เฉลย</summary>ตอบ A)</details>

Q2. สูตรใดถูกต้องสำหรับ Conditional Probability

- A) P(E|F) = P(F)/P(E)
- B) P(E|F) = P(E and F)/P(F)
- C) P(E|F) = P(E) + P(F)
- D) P(E|F) = P(E) − P(F)
<details><summary>🔑 เฉลย</summary>ตอบ B)</details>

Q3. ในบริบทของ Bayesian หากเราสังเกตหลักฐานใหม่ (E) ค่าที่เปลี่ยนจาก Prior ไปเป็นอะไร

- A) Likelihood
- B) Marginal
- C) Posterior
- D) Normalization constant
<details><summary>🔑 เฉลย</summary>ตอบ C)</details>

Q4. ในกราฟ DAG ลูกศร Vⱼ → Vᵢ มีความหมายว่าอย่างไรตามนิยาม SCM

- A) Vⱼ เป็น argument ในฟังก์ชัน fᵢ ที่สร้าง Vᵢ
- B) Vᵢ และ Vⱼ ไม่มีความเกี่ยวข้องกัน
- C) Vᵢ เกิดก่อน Vⱼ เสมอ
- D) Vⱼ ต้องเป็นตัวแปร exogenous เสมอ
<details><summary>🔑 เฉลย</summary>ตอบ A)</details>

Q5. ในบันได Pearl Causal Hierarchy เหตุใดคำถาม "Was it the aspirin that stopped my headache?" จึงจัดอยู่ใน Rung 3 ไม่ใช่ Rung 2

- A) เพราะเป็นการย้อนถามถึงเหตุการณ์ที่เกิดขึ้นแล้วจริง (factual) เทียบกับสิ่งที่อาจเกิดขึ้นถ้าทำต่างไป (counterfactual) ซึ่งต่างจาก Rung 2 ที่ถามล่วงหน้าว่า "ถ้าทำ X จะเกิดอะไร"
- B) เพราะเกี่ยวกับยาแอสไพรินเท่านั้น
- C) เพราะ Rung 2 ใช้ไม่ได้กับคำถามทางการแพทย์
- D) เพราะไม่มีความแตกต่างระหว่าง Rung 2 และ 3 เลย
<details><summary>🔑 เฉลย</summary>ตอบ A)</details>

Q6. เหตุใด RCT จึงถูกเรียกว่า "Magical" ในการแก้ปัญหา confounding

- A) เพราะการสุ่มทำให้ทั้ง confounder ที่วัดได้และวัดไม่ได้ (unmeasured) กระจายสมดุลกันในทุกกลุ่ม ทำให้ P(Y|X) = P(Y|do(X))
- B) เพราะ RCT ใช้เทคโนโลยี AI ขั้นสูง
- C) เพราะ RCT ไม่ต้องมีกลุ่มควบคุม
- D) เพราะ RCT รับประกันว่าไม่มีค่าใช้จ่ายใดๆ
<details><summary>🔑 เฉลย</summary>ตอบ A) — จุดเด่นที่สำคัญที่สุดคือแก้ได้ทั้ง confounder ที่วัดไม่ได้ด้วย ซึ่งวิธีเชิงสถิติอื่นทำไม่ได้</details>

Q7. ในกรณีที่ RWD มี confounder ที่ "วัดไม่ได้" (unmeasured confounder, U) เทคนิคอย่าง PSM หรือ IPW จะยังคงให้ผลถูกต้องหรือไม่ เพราะเหตุใด

- A) ยังคงถูกต้องเสมอเพราะ ML ที่ใช้ทำนาย propensity score แก้ปัญหานี้ได้
- B) ไม่ถูกต้อง เพราะ PSM/IPW ปรับได้เฉพาะ confounder ที่วัดได้และรวมอยู่ในโมเดลเท่านั้น ส่วน U ที่วัดไม่ได้ยังคงสร้าง bias อยู่
- C) ถูกต้องถ้าใช้ deep learning เท่านั้น
- D) ไม่เกี่ยวข้องกับความถูกต้องของผลลัพธ์เลย
<details><summary>🔑 เฉลย</summary>ตอบ B) — นี่คือข้อจำกัดสำคัญที่สุดของวิธีเชิงสาเหตุบน RWD เมื่อเทียบกับ RCT</details>

Q8. พิจารณากราฟ: GPA → เข้าโปรแกรมท็อป ← เรียงความ หากนักวิจัยศึกษาความสัมพันธ์ระหว่าง GPA กับคุณภาพเรียงความ "เฉพาะในกลุ่มนักเรียนที่เข้าโปรแกรมท็อปได้" จะเกิดปัญหาใด

- A) ไม่มีปัญหาใดๆ เพราะ GPA และเรียงความเป็นตัวแปรอิสระอยู่แล้ว
- B) เกิด collider bias — การเลือกดูเฉพาะกลุ่มที่เข้าได้ (condition บน collider) จะสร้างความสัมพันธ์ผกผันเทียมระหว่าง GPA กับเรียงความ ทั้งที่จริงไม่เกี่ยวกัน
- C) เกิดปัญหาขนาดตัวอย่างเล็กเกินไปเท่านั้น
- D) เป็นปัญหาการวัดตัวแปร (measurement error) เท่านั้น
<details><summary>🔑 เฉลย</summary>ตอบ B)</details>

Q9. ในสมมติฐาน POF ข้อใด "Consistency" (A=a ⟹ Y=Y(a)) มีความสำคัญอย่างไรต่อการตีความ ATE ที่ประมาณได้จากข้อมูลจริง

- A) รับรองว่า outcome ที่สังเกตได้จริงตรงกับ potential outcome ภายใต้ treatment ที่หน่วยนั้นได้รับจริง ซึ่งเป็นสะพานเชื่อมระหว่างกรอบทฤษฎี (potential outcomes) กับข้อมูลที่สังเกตได้จริง
- B) รับประกันว่าไม่มี confounder ในข้อมูล
- C) รับประกันว่าตัวอย่างมีขนาดใหญ่พอ
- D) ไม่มีความสำคัญต่อการวิเคราะห์เลย
<details><summary>🔑 เฉลย</summary>ตอบ A)</details>

Q10. เหตุใด ATE เพียงตัวเดียวจึงอาจ "ปิดบัง" อันตรายของการรักษาต่อ subpopulation บางกลุ่มได้ ตามที่แสดงในตัวอย่าง antiplatelets กับกลุ่ม DLP

- A) เพราะ ATE เป็นค่าเฉลี่ยถ่วงน้ำหนักของ ITE ทั่วทั้งประชากร ทำให้ผลบวกในกลุ่มใหญ่ (เช่น HT, DM) สามารถหักล้างผลลบในกลุ่มย่อย (DLP) จนดูเหมือนโดยรวมยาได้ผลดี
- B) เพราะ ATE คำนวณผิดพลาดเสมอ
- C) เพราะ DLP ไม่ใช่ปัจจัยเสี่ยงของ stroke
- D) เพราะ ATE ใช้ได้เฉพาะกับ RCT เท่านั้น
<details><summary>🔑 เฉลย</summary>ตอบ A) — นี่คือเหตุผลหลักที่ต้องดู CATE/ITE เพิ่มเติมใน personalized medicine</details>

Q11. ในบริบท SCM ของ Mediation Analysis กรณี non-linear (ผ่าน ReLU) เพราะเหตุใดการแยก Direct Effect และ Indirect Effect แบบเส้นตรง (linear decomposition) จึงอาจนำไปสู่ข้อสรุปที่ผิดพลาด

- A) เพราะฟังก์ชัน non-linear ทำให้ effect ของ mediator ขึ้นกับค่าของตัวแปรอื่นร่วมด้วย (interaction) การบวก DE+IE แบบตรงไปตรงมาจึงไม่สะท้อน causal effect ที่แท้จริงซึ่งต้องคำนวณผ่าน NDE และ NIER แยกกัน
- B) เพราะ Mediation Analysis ใช้ไม่ได้กับข้อมูลทางการแพทย์
- C) เพราะ ReLU ทำให้ mediator ไม่มีผลเลย
- D) เพราะ Direct Effect ต้องมีค่าเป็นลบเสมอ
<details><summary>🔑 เฉลย</summary>ตอบ A)</details>

Q12. พิจารณา MNAR (Missing Not At Random) ในบริบทข้อมูล Obesity ที่ค่าซึ่งหายไปมักเป็นคนอ้วนที่ไม่อยากเปิดเผยน้ำหนัก เหตุใดการวิเคราะห์แบบ complete-case (ตัดข้อมูลที่หายทิ้ง) จึงให้ผลลัพธ์ที่มี bias

- A) เพราะกลไกการหายไปของข้อมูล (R_O) สัมพันธ์กับค่าจริงของ Obesity เอง การตัดทิ้งจึงทำให้ตัวอย่างที่เหลือไม่ใช่ตัวแทนของประชากรจริง (เอนเอียงไปทางคนที่ไม่อ้วนหรือยอมเปิดเผย)
- B) เพราะขนาดตัวอย่างเล็กลงเท่านั้นไม่มีผลต่อทิศทางของผล
- C) เพราะ MNAR ไม่มีผลต่อการวิเคราะห์เลย
- D) เพราะต้องใช้ MCAR เท่านั้นในการวิเคราะห์ทุกกรณี
<details><summary>🔑 เฉลย</summary>ตอบ A)</details>

Q13. ในการทำ Causal Transportability หากพบว่า Y ไม่ d-separated จาก S แม้ intervene บน X แล้ว (มีเส้นทางเปิดอยู่) ข้อสรุปที่ถูกต้องคือข้อใด

- A) Effect ยัง directly transportable ได้เหมือนเดิม
- B) Effect ไม่ transportable โดยตรง อาจต้องหาสูตรปรับเพิ่มเติม (เช่น ปรับผ่านตัวแปรอื่นที่บล็อกเส้นทางที่เหลือ) หรือสรุปว่า transport ไม่ได้เลยถ้าไม่มีเงื่อนไขเพิ่มเติม
- C) ต้องทิ้งข้อมูลจาก target domain ทั้งหมด
- D) S ไม่มีผลต่อการวิเคราะห์อีกต่อไป
<details><summary>🔑 เฉลย</summary>ตอบ B)</details>

Q14. พิจารณาสถานการณ์: ทีมวิจัยพบว่า "คนที่ใช้ LINE แจ้งเตือนนัดหมายของคลินิก มาตามนัดมากกว่าคนที่ไม่ใช้" หากสรุปทันทีว่า LINE ทำให้มาตามนัดมากขึ้น อาจเข้าข่ายความผิดพลาดใด และควรแก้ไขอย่างไร

- A) ไม่มีความผิดพลาดใดๆ เพราะข้อมูลแสดงความสัมพันธ์ชัดเจนแล้ว
- B) อาจเป็น confounding — คนที่ add LINE คลินิกอยู่แล้วอาจเป็นคนที่ engaged สูงตั้งแต่แรก (U → add LINE, U → มาตามนัด) ควรแก้ด้วยการทำ RCT ขนาดเล็ก สุ่มว่าใครได้รับ/ไม่ได้รับการแจ้งเตือน แล้วเปรียบเทียบ
- C) ควรเพิ่มจำนวนคนที่ใช้ LINE ให้มากขึ้นเพื่อยืนยันผล
- D) ควรใช้เฉพาะข้อมูลจากคนที่ไม่ใช้ LINE เท่านั้น
<details><summary>🔑 เฉลย</summary>ตอบ B) — ตัวอย่างคลาสสิกของ confounding by engagement ซึ่งแก้ได้ดีที่สุดด้วยการสุ่มทดลองเล็กๆ เองแม้ในบริบทธุรกิจขนาดเล็ก</details>

Q15. ในงานวิจัย DAG of Stroke การใช้ทั้ง Conventional estimator (Stratification, IPW, Doubly Robust, SCM), Mediation Analysis, Double ML และ Dragonnet ร่วมกัน สะท้อนหลักการใดของ Causal Inference ที่ดี

- A) Triangulation — การใช้หลายวิธีที่มีสมมติฐานและจุดอ่อนต่างกัน เพื่อตรวจสอบว่าผลสรุปมีความคงทน (robust) ไม่ได้ขึ้นกับข้อสมมติของวิธีใดวิธีหนึ่งเพียงอย่างเดียว
- B) การเลือกใช้เฉพาะวิธีที่ให้ผลตามที่ต้องการ (cherry-picking)
- C) การใช้ ML ที่ซับซ้อนที่สุดเสมอโดยไม่ต้องเปรียบเทียบ
- D) ไม่มีหลักการใดเป็นพิเศษ เป็นเพียงการทำซ้ำโดยไม่จำเป็น
<details><summary>🔑 เฉลย</summary>ตอบ A)</details>

Q16. หากต้องออกแบบงานวิจัยเพื่อพิสูจน์ประสิทธิภาพของภูมิปัญญาแพทย์แผนไทยโดยใช้ RWD จากคลินิก ข้อใดคือขั้นตอนที่ควรทำเป็นลำดับแรกตามหลัก Causal Inference ก่อนจะเลือกใช้เทคนิคทางสถิติใดๆ

- A) รันโมเดล ML ที่แม่นยำที่สุดก่อนแล้วค่อยตีความ
- B) วาด DAG ระบุ treatment, outcome และ confounder ที่เป็นไปได้ทั้งหมด (เช่น เหตุผลที่คนไข้เลือกมารักษาแบบนี้) เพื่อกำหนดว่าต้องเก็บ/ปรับตัวแปรใดบ้าง ก่อนเลือกเทคนิคประมาณค่า
- C) เก็บข้อมูลให้มากที่สุดโดยไม่ต้องวางแผนล่วงหน้า
- D) ข้ามขั้นตอนนี้ไปเลยเพราะไม่จำเป็น
<details><summary>🔑 เฉลย</summary>ตอบ B) — การวาด DAG ก่อนเป็นขั้นตอนพื้นฐานที่สุดที่กำหนดทิศทางการวิเคราะห์ทั้งหมด</details>

Q17. ในบริบทของ collider bias เหตุใดการที่ผู้ป่วยที่มาหาหมอพื้นบ้านมักเป็นผู้ที่ "การรักษาแผนปัจจุบันไม่ได้ผล" จึงเป็นความเสี่ยงสำคัญเมื่อวิเคราะห์ RWD จากกลุ่มนี้

- A) การเลือกกลุ่มตัวอย่างแบบนี้อาจเป็นการ condition บน collider (Treatment แผนปัจจุบัน → มาหาหมอพื้นบ้าน ← ความรุนแรงของโรค) ซึ่งอาจสร้างความสัมพันธ์เทียมระหว่างตัวแปรที่ไม่เกี่ยวข้องกันจริง
- B) ไม่มีความเสี่ยงใดๆ เพราะเป็นกลุ่มตัวอย่างที่ใหญ่พอ
- C) เป็นปัญหาด้านจริยธรรมเท่านั้นไม่เกี่ยวกับสถิติ
- D) แก้ได้ด้วยการเพิ่มขนาดตัวอย่างเพียงอย่างเดียว
<details><summary>🔑 เฉลย</summary>ตอบ A)</details>

Q18. พิจารณา: หากพบว่า Doubly Robust Estimation ให้ผลใกล้เคียงกับทั้ง IPW และ Regression-based method มาก ข้อใดอธิบายจุดแข็งของ Doubly Robust ได้ถูกต้องที่สุด

- A) Doubly Robust ให้ผลถูกต้องแม้เพียงหนึ่งในสองโมเดล (propensity model หรือ outcome model) ถูกระบุอย่างถูกต้องเท่านั้น ทำให้ทนทานต่อการระบุโมเดลผิดพลาดมากกว่าการใช้ IPW หรือ regression เพียงอย่างเดียว
- B) Doubly Robust ต้องการข้อมูลน้อยกว่าวิธีอื่นเสมอ
- C) Doubly Robust ใช้ได้เฉพาะกับ RCT เท่านั้น
- D) Doubly Robust ไม่ต้องมีสมมติฐาน ignorability เลย
<details><summary>🔑 เฉลย</summary>ตอบ A)</details>

Q19. สมมติทีมพัฒนาแอปการศึกษาทางการแพทย์ต้องการวัดว่า "การจำลองสถานการณ์คลินิกเสมือนจริง (clinical simulation)" ช่วยพัฒนาทักษะการตัดสินใจของนักศึกษาได้จริงหรือไม่ (Rung 2) ไม่ใช่แค่ว่านักศึกษาที่เก่งอยู่แล้วเลือกใช้ฟีเจอร์นี้บ่อยกว่า (Rung 1) ควรออกแบบการประเมินผลอย่างไรให้สอดคล้องกับหลักการที่เรียนมาทั้งหมด

- A) วัด correlation ระหว่างความถี่การใช้ฟีเจอร์กับคะแนนสอบปลายภาคเพียงอย่างเดียว
- B) ออกแบบ intervention จริง เช่น สุ่มแบ่งนักศึกษาเป็นกลุ่มที่ได้ใช้ฟีเจอร์ก่อน/หลัง (stepped-wedge) หรือถ้าทำ RCT ไม่ได้ ให้เก็บ RWD พร้อมวาด DAG ระบุ confounder (เช่น พื้นฐานความรู้เดิม, ความขยัน) แล้วใช้ PSM/IPW หรือ mediation analysis เพื่อแยก direct effect ของฟีเจอร์ออกจาก confounder เหล่านั้น
- C) ถามความพึงพอใจของนักศึกษาเพียงอย่างเดียวแล้วสรุปผล
- D) ใช้เฉพาะข้อมูลจากนักศึกษาที่ใช้ฟีเจอร์นี้เท่านั้นโดยไม่มีกลุ่มเปรียบเทียบ
<details><summary>🔑 เฉลย</summary>ตอบ B) — คำตอบนี้ผสมผสานทั้งแนวคิด Rung 2 (intervention design) และเทคนิคเชิงสาเหตุสำหรับ RWD เมื่อ RCT ทำไม่ได้เต็มรูปแบบ</details>

Q20. สรุปภาพรวมทั้งหมดของวิชานี้ ข้อใดอธิบาย "เหตุผลที่ RWD เพียงอย่างเดียวไม่เพียงพอสำหรับการตัดสินใจทางคลินิก" ได้ครบถ้วนและถูกต้องที่สุด

- A) เพราะ RWD มีขนาดเล็กเกินไปเสมอ
- B) เพราะ RWD ให้ข้อมูลเพียงระดับ Association (Rung 1, P(Y|X)) ซึ่งอาจถูกบิดเบือนด้วย confounding และ collider bias ในขณะที่การตัดสินใจทางคลินิกต้องการคำตอบระดับ Intervention/Counterfactual (Rung 2-3) จึงต้องอาศัยกรอบ Causal Inference (DAG, POF, SCM) ร่วมกับเทคนิคปรับ confounder เพื่อประมาณ effect ที่ใกล้เคียงความจริงมากที่สุด แม้จะไม่สมบูรณ์แบบเท่า RCT
- C) เพราะ RWD ไม่มีตัวแปร outcome ให้วิเคราะห์
- D) เพราะกฎหมายห้ามใช้ RWD ในการวิจัยทางคลินิก
<details><summary>🔑 เฉลย</summary>ตอบ B) — นี่คือสรุปแก่นของทั้งวิชา: ช่องว่างระหว่าง Rung 1 และ Rung 2-3 คือเหตุผลที่ต้องมี Causal Inference framework</details>

สรุปเนื้อหา: Causal Inference for Digital Health (RWD & RWE)

เนื้อหาครอบคลุมตั้งแต่พื้นฐานความน่าจะเป็น → Causality → Pearl Causal Hierarchy → RCT vs RWD → Potential Outcomes → SCM → ATE/CATE/ITE → Missingness & Transportability

Sample Space (S) คือเซตของผลลัพธ์ที่เป็นไปได้ทั้งหมด

Event (E) คือสับเซตของ S ที่เราให้ความหมาย

- 0 ≤ P(E) ≤ 1
- P(S) = 1
- ถ้า E, F ไม่เกิดร่วมกัน: P(E or F) = P(E) + P(F)
- Mutually exclusive: P(E or F) = P(E) + P(F)
- Non-mutually exclusive: P(E or F) = P(E) + P(F) − P(E and F)
Conditional Probability: P(E|F) = P(E and F) / P(F)

Independence: P(E|F) = P(E) — เหตุการณ์หนึ่งไม่ให้ข้อมูลเกี่ยวกับอีกเหตุการณ์

Probability of AND

- อิสระ: P(E,F) = P(E)·P(F)
- ไม่อิสระ (chain rule): P(E,F) = P(E|F)P(F)
Law of Total Probability: P(E) = P(E|F)P(F) + P(E|Fᶜ)P(Fᶜ) = Σ P(E|Bᵢ)P(Bᵢ)

Conditional Independence: P(A∩B|C) = P(A|C)·P(B|C)

P(B|E) = P(E|B)·P(B) / P(E)

- Posterior P(B|E) = ความเชื่อหลังเห็นหลักฐาน
- Prior P(B) = ความเชื่อก่อนเห็นหลักฐาน
- Likelihood P(E|B) = สิ่งที่สังเกตได้
- Marginal P(E) = normalization constant
เมื่อไม่รู้ P(E) ใช้ law of total probability ขยาย:

P(B|E) = P(E|B)P(B) / [P(E|B)P(B) + P(E|Bᶜ)P(Bᶜ)]

แนวคิดหลัก: เชื่ออะไรอยู่ก่อน (Prior) + เจอหลักฐานที่เข้ากับสมมติฐานนั้นแค่ไหน (Likelihood) = เชื่อใหม่หลังเห็นหลักฐาน (Posterior)

ทุกครั้งที่คุณ "เปลี่ยนใจ" เพราะเจอข้อมูลใหม่ๆ ในชีวิตจริง — สมองคุณกำลังทำ Bayes' Theorem อยู่โดยไม่รู้ตัว

มีกระเป๋า 2 ใบ วางปนกันแบบมองไม่เห็นว่าใบไหน

- กระเป๋า A: ลูกบอล 9 แดง 1 ขาว
- กระเป๋า B: ลูกบอล 1 แดง 9 ขาว
หยิบกระเป๋ามา 1 ใบแบบสุ่ม (Prior = 50-50) แล้วล้วงมือหยิบลูกบอลออกมา 1 ลูก ได้ ลูกแดง — กระเป๋าที่ถืออยู่น่าจะเป็น A มากแค่ไหน?

คิดง่ายๆ:

- ถ้าเป็น A → โอกาสหยิบได้แดง = 9/10
- ถ้าเป็น B → โอกาสหยิบได้แดง = 1/10
เอาสองค่านี้มาเทียบสัดส่วนกัน:

⁍

แค่นี้เอง! พอเห็นลูกแดง ความเชื่อเปลี่ยนจาก "50-50" เป็น "90% น่าจะเป็นกระเป๋า A"

คุณได้ยินเสียงเห่าดังจากหลังบ้าน

- Prior = ก่อนได้ยินเสียง คุณคิดว่าน่าจะมีหมาแถวนั้นอยู่แล้วสัก 30%
- Likelihood = ถ้ามีหมาจริง โอกาสได้ยินเสียงเห่าแบบนี้สูงมาก (90%)
- Posterior = พอได้ยินเสียงเห่า คุณมั่นใจขึ้นเยอะว่ามีหมาอยู่จริง (อาจขึ้นเป็น 80-90%)
จุดสำคัญที่สุดของสูตร: สังเกตตำแหน่งของ B กับ E สลับกัน — P(B|E) ขณะที่ P(E|B) อยู่คนละตำแหน่ง

Bayes' Theorem คือเครื่องมือสำหรับ "กลับทิศทาง" ของ conditional probability

- P(E|B) = สิ่งที่เราคำนวณง่ายกว่า (เช่น "ถ้าเป็นกระเป๋า A จะหยิบได้แดงกี่%" — รู้อยู่แล้วจากจำนวนลูกบอลในกระเป๋า)
- P(B|E) = สิ่งที่เราอยากรู้ (เช่น "หยิบได้แดงแล้ว น่าจะเป็นกระเป๋า A กี่%") — คำนวณตรงๆ ไม่ได้ ต้องใช้ Bayes ช่วยกลับทิศ
มี 2 สมการที่มี P(B และ E) เหมือนกัน:

⁍

จัดรูปสมการที่สองใหม่: P(B และ E) = P(E|B) × P(B) แล้วแทนกลับเข้าสมการแรก จะได้ Bayes' Theorem ทันที

สรุป: Bayes ไม่ใช่สูตรใหม่ที่ผุดขึ้นมาลอยๆ แต่เป็นการเอาสูตร conditional probability สองอันที่มี "ตัวร่วม" เดียวกันมาเชื่อมกันเท่านั้น

"Correlation doesn't imply causation"

Causal Inference คืออะไร (นิยามง่ายๆ): ศาสตร์ที่พยายามตอบคำถาม "อะไรเป็นสาเหตุของอะไร" — ไม่ใช่แค่ "อะไรมักเกิดพร้อมกับอะไร" (เช่นไอศกรีมกับคนจมน้ำ — ทั้งสองเกิดจาก "หน้าร้อน" เหมือนกัน ไม่ได้เกี่ยวข้องกันโดยตรง)

ทำไมต้องมีศาสตร์นี้แยกจาก ML: ML ตอบได้แค่ "เห็น X แล้วบอกอะไรเกี่ยวกับ Y" แต่การตัดสินจริง (เช่นจะให้ยาหรือไม่, จะทำนโยบายหรือไม่) ต้องการคำตอบเชิงสาเหตุ ซึ่งต้องการเทียบกับ "โลกสมมติที่ไม่เคยเกิด" (counterfactual) — นี่คือเหตุผลที่ต้องแยกเป็นศาสตร์ต่างหากจาก ML ธรรมดา

ถ้าสองเหตุการณ์สัมพันธ์กันและไม่มีอันไหนเป็นสาเหตุของอีกอัน ต้องมี "สาเหตุร่วม" ตัวที่สาม (A ← C → B)

No causation without manipulation: Causality ต้องมี agent + intervention (do) — causality ไม่ใช่สิ่งพื้นฐาน (not fundamental)

Agent ในที่นี้คือ "ผู้กระทำ" อะไรก็ได้ในระดับ macroscopic ที่เข้าไป intervene ตัวแปร — แนวคิดนี้เชื่อมโยงกับกฎข้อที่ 2 ของอุณหพลศาสตร์ (2nd Law of Thermodynamics) ที่ให้ "ทิศทางของเวลา" ที่ชัดเจน (entropy เพิ่มขึ้นเสมอ) ซึ่งเป็นสิ่งที่ทำให้แนวคิดเรื่อง "เหตุเกิดก่อนผล" มีความหมายตั้งแต่แรก: Causality = Agent ทำ intervention (do) ต่อ X → ส่งผลไปยัง Z

- Fork: X ← Z → Y
- Pipe: X → Z → Y
- Collider: X → Z ← Y
- Descendant: X → Z → D, Z → Y
- Chain/Fork ถูกบล็อกเมื่อ middle node ถูก condition
- Collider ถูกบล็อกโดยธรรมชาติ การ condition บน collider (หรือลูกหลาน) จะเปิดเส้นทาง — ตัวอย่าง GPA → เข้าโปรแกรมท็อป ← เรียงความ
ข้อมูลเพียงอย่างเดียวบอกไม่ได้ทั้งหมด — หลักการเชิงสาเหตุอีกข้อ: DAG ไม่ได้มาจากข้อมูล แต่มาจาก "สมมติฐาน" ที่เราใส่เข้าไปเอง

เหตุต้องเกิดก่อนผลเสมอ 

ถ้ารู้ว่า X เกิดก่อน Y ตามเวลา Y จะเป็นเหตุของ X ไม่ได้เด็ดขาด

ตัวอย่าง: Age → Hypertension → Stroke — อายุมาก่อนความดันสูง ความดันสูงมาก่อน stroke — ลำดับเวลาบังคับทิศทางลูกศรชัดเจน

ในทางการแพทย์ มีความรู้ทาง pathophysiology รองรับอยู่แล้วว่าอะไรทำให้เกิดอะไร เช่น สูบบุหรี่ → เยื่อบุหลอดลมอักเสบ → มะเร็งปอด (มีกลไกชีวเคมีรองรับ) ไม่มีทางที่มะเร็งปอดจะ "ทำให้" คนไปสูบบุหรี่ย้อนกลับได้

ถ้าเคยมี RCT ยืนยันแล้วว่า "ยา X ลดความดัน" นั่นคือหลักฐานเชิงสาเหตุที่แน่นหนาที่สุด เพราะ RCT ตัดปัญหาเรื่องทิศทางออกไปแล้วโดยธรรมชาติของการสุ่ม — เอามาใช้เป็นฐานวาด DAG ต่อได้เลย

คนที่รู้กลไกจริงในสนามจะบอกได้ว่าอะไรเป็นเหตุอะไรเป็นผลในบริบทที่ข้อมูลอย่างเดียวบอกไม่ได้ เช่น การสัมภาษณ์หมอแผนไทยเรื่องกลไกการรักษาแบบพื้นบ้าน ช่วยกำหนด confounder ที่ข้อมูลมองไม่เห็น

ตัวแปรประเภท "ลักษณะประจำตัวที่กำหนดแต่เกิด" (เช่น เพศ) เป็นผลจากโรคไม่ได้เด็ดขาด มักถูกกำหนดให้อยู่ต้นๆ ของ DAG เสมอ

สิ่งที่ข้อมูลอย่างเดียวบอกได้: แยก Collider ออกจาก Fork/Chain

- Fork (X ← Z → Y) และ Chain (X → Z → Y): X กับ Y สัมพันธ์กันตอนไม่ควบคุม Z แต่พอควบคุม Z แล้ว หมดความสัมพันธ์
- Collider (X → Z ← Y): X กับ Y ไม่สัมพันธ์กันตอนไม่ควบคุม Z แต่พอควบคุมกลับเกิดความสัมพันธ์ขึ้นมา
Algorithm จำพวก Causal Discovery (เช่น PC algorithm, FCI) ใช้ pattern นี้เดา skeleton ของ DAG จากข้อมูลได้บางส่วน — แต่ยังแยก fork กับ chain ไม่ได้ ต้องพึ่งลำดับเวลาหรือความรู้ภายนอกเสมอ

ทำไมเรื่องนี้สำคัญมาก: ทุกการคำนวณ (PSM, IPW, SCM) ล้วนพึ่งพา DAG ที่วาดไว้ ถ้า DAG ผิด ทุกอย่างที่คำนวณตามมาก็ผิดหมด แม้สูตรจะถูกต้อง 100% ก็ตาม เช่น ถ้าเข้าใจผิดว่าตัวแปรหนึ่งเป็น confounder ทั้งที่จริงเป็น mediator แล้วไปควบคุมมัน จะเผลอ effect ที่แท้จริงทิ้งโดยไม่รู้ตัว

- เริ่มจากลำดับเวลาก่อนเสมอ 
- ทบทวนวรรณกรรม/ความรู้ทางวิชาชีพว่ามีกลไกอะไรรองรับความสัมพันธ์นี้บ้าง 
- ปรึกษาผู้เชี่ยวชาญในสาขานั้นๆ โดยเฉพาะเรื่องที่ไม่ชัดเจน 
- วาด DAG ออกมาให้ชัด แล้วลองอธิบายทุกลูกศรว่า "ทำไมถึงคิดว่าเป็นแบบนี้" 
- ทำ Sensitivity Analysis — ลองวาด DAG แบบอื่นที่เป็นไปได้ แล้วดูว่าผลลัพธ์เปลี่ยนไปมากไหม ถ้าเปลี่ยนมากแปลว่าข้อสรุปยังไม่แน่นพอ
Confounding: Diet → Disease โดยมี U ชี้เข้าทั้งคู่ (U → Diet, U → Disease) — ตัวอย่าง U คือ Hypertension, Age

คนอายุมากมักเลือกกิน Diet บางแบบ และ มีความเสี่ยง Disease สูงกว่าอยู่แล้วจาก Age เอง — ถ้าไม่คุม Age ความสัมพันธ์ Diet-Disease ที่เห็นจะ "ปนเปื้อน" จาก U

RCT: สุ่ม assign diet → ตัดลูกศร U → Diet ออก เหลือ do(diet) → Disease กับ U → Disease เท่านั้น — เพราะเหรียญสุ่มไม่สนใจว่าใครอายุเท่าไหร่ ความสัมพันธ์ที่เหลือจึงเป็นเชิงสาเหตุแท้

ตัวอย่าง Intervention ที่ทำจริงไม่ได้: Smoking → Cancer

do(smoke?) → Cancer พร้อมเครื่องหมาย "?" กำกับ — สื่อว่าการบังคับสุ่มให้คนสูบบุหรี่เป็น RCT ผิดจริยธรรม ทำไม่ได้จริง ต้องอาศัย Observational Study/RWD แทน (Smoking → Cancer ที่ยังมี U → Smoking, U → Cancer อยู่ครบ เพราะคนสูบเลือกสูบเอง มีลักษณะพื้นฐาน เช่น stress หรือสังคม ต่างจากคนไม่สูบ)

The Confounding Problem: Confounding เป็นแนวคิดเชิงสาเหตุล้วนๆ นิยาม/แก้ไขด้วยภาษาสถิติเพียงอย่างเดียวไม่ได้ การใส่ feature มั่วใน ML อาจเพิ่ม predictive power แต่เสี่ยงทำให้ estimate เชิงสาเหตุ bias

ตัวอย่างที่จับต้องได้ในแต่ละ Rung (ปวดหัว + aspirin):

- Rung 1 (Association): "อาการปวดหัวบอกอะไรเราเกี่ยวกับการมีโรคอยู่หรือไม่" — เป็นการวินิจฉัยเชิงสังเกตการณ์ ไม่มีการแทรกแซงใดๆ
- Rung 2 (Intervention): "ถ้าฉันกินยา aspirin อาการปวดหัวจะหายไหม" — P(Y|do(X)) ต้องมี Experimental Design หรือ Reinforcement Learning
- Rung 3 (Counterfactual): "อาการปวดหัวที่หายไปนั้น เป็นเพราะ aspirin จริงหรือเปล่า" — ใช้อธิบายเหตุการณ์รายบุคคล/หาผู้รับผิดชอบ (explaining, attributing blame)
💡 จุดสำคัญคือคำว่า "identified" observational data ใน Rung 2 — RWD จะขยับขึ้นไปตอบคำถามระดับ intervention ได้ ถ้า effect นั้น identifiable จาก DAG ที่ถูกต้อง (เช่นผ่าน backdoor criterion, matching, PSM, IPW) — นี่คือเหตุผลที่ต้องเรียนเครื่องมือเหล่านี้ เพื่อ "เลื่อน" ข้อมูลสังเกตจาก Rung 1 ขึ้นไปตอบคำถาม Rung 2 ได้อย่างมีหลักการ

สรุป: Predictive ML ตอบ "อะไรน่าจะเกิดขึ้น" — Causal Inference ตอบ "เราจะทำให้มันเกิด (หรือป้องกัน) ได้อย่างไร" เป้าหมายต่างกันโดยพื้นฐาน

สรุปแบบตาราง (จำง่าย):

จุดสำคัญ: ยิ่งขึ้นบันไดสูง คำถามยิ่งลึกและมีประโยชน์ต่อการตัดสินใจมากขึ้น แต่ก็ต้องการ "สมมติฐานเชิงสาเหตุ" ที่แน่นหนากว่าเดิมเสมอ 2 ข้อมูลเยอะอย่างเดียวไม่พอที่จะขึ้นบันได

RCT คือ Gold Standard เพราะขจัด confounding ได้หมด

- Exchangeability: P(U|X=1) = P(U|X=0)
- Identification: P(Y|X) = P(Y|do(X))
- Estimation: ATE = Ȳ(T=1) − Ȳ(T=0)
- Ethical Constraints — ทดลองที่อาจก่ออันตรายทำไม่ได้
- Feasibility/Cost — แพงหรือทำไม่ได้ทางเทคนิค
- Generalizability (External Validity) — ผลจาก lab อาจไม่ transport สู่โลกจริง
- Data Scarcity — ข้อมูล RCT อาจจำกัด ต้องพึ่ง observational data
ความท้าทายของ RWD: RWD มาจากการ "มอง" โลก (Layer 1) แต่ผู้ตัดสินใจต้องการคำตอบเรื่อง intervention (Layer 2) และ counterfactual (Layer 3) → RWD ต้องใช้วิธีเชิงสาเหตุแก้ปัญหา counterfactual

- Observational Studies — ข้อมูลถูกเก็บมาโดยไม่มีการควบคุมหรือทดลอง (manipulation) ใดๆ
- The Goal Mismatch — RWD มาจากการสังเกตโลก (Layer 1: Association) แต่ผู้ตัดสินใจต้องการคำตอบเรื่อง intervention (Layer 2) และสถานการณ์สมมติ (Layer 3: Counterfactuals)
- The Central Dilemma — เราจะใช้ข้อมูลที่เก็บมาแบบ passive ไปสร้างข้อสรุปเชิงสาเหตุเกี่ยวกับ intervention ที่หนักแน่นพอนำไปปฏิบัติได้อย่างไร
ตัวอย่าง: ยาแก้ปวดหัว

ถ้ากินยา (Y¹ = 0 คือไม่ปวดหัว) และถ้าไม่กินยา (Y⁰ = 1 คือปวดหัว) แสดงว่ายาตัวนี้น่าจะมี causal effect (แม้จะสังเกตทั้งสองสถานการณ์พร้อมกันไม่ได้จริงก็ตาม)

The Fundamental Problem of Causal Inference: สำหรับหน่วย i ใดๆ สังเกตได้เพียง potential outcome เดียว (factual) — อีกอันเป็น counterfactual ที่ไม่มีวันสังเกตได้ → causal inference คือปัญหา missing data

💡 มองเป็นตาราง (matrix) ของ potential outcomes ก็ได้: แต่ละหน่วย (แถว) จะมีคอลัมน์ผลลัพธ์หนึ่งอัน "หายไปเสมอ" (คือ potential outcome ของ treatment ที่ไม่ได้รับ) — เป้าหมายของ causal inference คือการประมาณค่าที่หายไปเหล่านี้ให้แม่นยำที่สุด

ตัวอย่างคำนวณ ITE (ยาแก้ปวดหัว): สมมติ ปวดหัว = 1, ไม่ปวดหัว = 0

- Yᵢ⁰ = 1 (ถ้าไม่กินยา ยังปวดหัวอยู่)
- Yᵢ¹ = 0 (ถ้ากินยา หายปวดหัว)
- ITE = Yᵢ¹ − Yᵢ⁰ = 0 − 1 = −1 → ค่าติดลบหมายถึงยาช่วยลดอาการปวดหัวได้จริงสำหรับหน่วยนี้
สรุปง่ายๆ ว่าทำไม POF ถึงสำคัญ: การหาสาเหตุ = การเดาสิ่งที่ไม่เคยเกิดขึ้น (counterfactual) — เพราะคนคนเดียวเลือกได้แค่ทางเดียว จึงต้อง "หาคนอื่นที่คล้ายกันมากที่สุด" มาแทน — นี่คือที่มาของเครื่องมือทั้งหมดที่เรียนต่อจากนี้ (matching, PSM, IPW, SCM) ซึ่งล้วนมีเป้าหมายเดียวกันคือพยายามเดาสิ่งที่หายไปนี้ให้แม่นที่สุด

- ATE = E(Y¹ − Y⁰)
- ATE = E(Y¹) − E(Y⁰)
- ATE ≠ E(Y¹|A=1) − E(Y⁰|A=0) ← จุดสำคัญ
- ATE = E(Y¹|do(A=1)) − E(Y⁰|do(A=0))
- Ignorability: Y¹,Y⁰ ⊥ A
- Conditional Exchangeability: Y¹,Y⁰ ⊥ A | Z
- Positivity: 0 < P(A=1|Z=z) < 1
- No interference: Y(a₁,...,aₙ) = Y(aᵢ)
- Consistency: A=a ⟹ Y=Y(a)
ต้องระบุ GLM ถูกต้อง แม้ใช้ ML แทน GLM ได้ แต่ยังไม่มีทฤษฎีสถิติรองรับ CI/p-value ที่ชัดเจน

นิยาม SCM ประกอบด้วย

- V = endogenous variables (สังเกตได้ เช่น treatment, outcome, confounder)
- U = exogenous variables (noise, มักอิสระ)
- F = structural equations (Vᵢ = fᵢ(Paᵢ, Uᵢ))
IV →(a)→ Mediator →(b)→ DV

- c' = Direct Effect (มี mediator ในโมเดล)
- c = Total Effect (ไม่มี mediator ในโมเดล)
ตัวอย่าง non-linear causal diagram (ผ่าน ReLU):

```
Naive TE = DE + IE = 2 + 0 = 2
NDE = 2, NIER = 2
Causal Effect = NDE − NIER = 2 − 2 = 0
```

บทเรียน: ในระบบ non-linear การบวก direct+indirect effect ตรงๆ ให้คำตอบผิด

CATE สำคัญกับ Personalized Medicine: ยาอาจมีประโยชน์เฉลี่ย (ATE บวก) แต่ เป็นอันตรายกับ subpopulation บางกลุ่ม (CATE ติดลบ)

สรุปเปรียบเทียบ ATE / CATE / ITE (จำง่าย):

สรุปประโยคเดียว: ATE บอกภาพรวม, CATE บอกว่ากลุ่มไหนได้/เสียประโยชน์ต่างกัน, ITE คือเป้าหมายสูงสุด (รักษาเจาะจงรายคน) แต่คำนวณตรงๆไม่ได้ ต้องอาศัยโมเดล (เช่น Dragonnet) มาประมาณแทน

"Application of Dragonnet and Conformal Inference for Estimating Individualized Treatment Effects for Personalized Stroke Prevention" (JMIR, Vol 9, 2025)

เปรียบเทียบ estimator หลายวิธี (Stratification, IPW, Doubly Robust, SCM, Mediation Analysis, Double ML, Dragonnet) กับ Epidemiological Case-Control (OR) — พบว่า Atrial Fibrillation มีผลเชิงสาเหตุสูงสุด (~0.075–0.097 ratio 4.56) รองมา Hypertension (~0.017–0.025) แล้ว Diabetes (~0.006–0.010) ส่วน Dyslipidemia แทบไม่มีผล

ITE ของ antiplatelets แยกตามกลุ่มเสี่ยง (box plot) — ค่าติดลบ = ลดความเสี่ยง stroke:

- HT: ~−0.007 (ได้ประโยชน์)
- DM: ~−0.015 (ได้ประโยชน์ชัดสุด)
- DLP: ~+0.027 (เป็นโทษ)
- HT+DM: ~−0.016, HT+DLP: ~+0.016, DM+DLP: ~+0.010
- HT+DM+DLP: ~0 (กระจายกว้างมาก)
→ หัวใจของ personalized medicine: ยาตัวเดียวกันให้ผลตรงข้ามในกลุ่มเสี่ยงต่างกัน ซึ่ง ATE เดียวมองไม่เห็น

R_O = ตัวควบคุมการปิดบัง/เปิดเผยค่า

- Complete: สังเกต O ได้ตรงๆ
- MCAR (Missing Completely At Random): R_O เป็นอิสระจากทุกอย่าง
- MAR (Missing At Random): R_O ขึ้นกับตัวแปรที่สังเกตได้
- MNAR (Missing Not At Random): R_O ขึ้นกับ O เอง (ค่าที่หายกำหนดว่ามันจะหาย)
ตัวอย่างประกอบ: ตัวแปร Age (A), Gender (G), Obesity (O) — R_O คือตัวควบคุมการปิดบัง/เปิดเผยค่าของ Obesity โดยเฉพาะ เมื่อ R_O = 1 ค่า Obesity จะถูกซ่อนไว้ (ไม่ถูกบันทึก) ส่วนกลไกว่า R_O ขึ้นกับอะไรบ้าง (ไม่มีเลย / ขึ้นกับ A,G ที่สังเกตได้ / ขึ้นกับ O เอง) จะกำหนดว่าข้อมูลที่หายไปเป็นแบบ Complete, MCAR, MAR หรือ MNAR

- P*(Y|do(X)) = causal effect ใน target domain
- P(Y|do(X)) = effect เดียวกันใน source domain
- เป้าหมาย: หาสูตรคำนวณ P*(Y|do(X)) จากข้อมูล source + target
Generalizability vs Transportability

- Generalizability: อนุมานจาก source sample กลับไปหา source population
- Transportability: ขยายผลจาก source sample ไปยัง target population ภายนอก
d-Separation ของ transportability: ถ้า (Y ⊥ S | do(X), Z) แล้ว

P*(Y|do(X),Z) = P(Y|do(X),Z) — effect นั้น directly transportable

Selection Diagram: ใช้ S = selection variable แทนปัจจัยที่ต่างกันระหว่างโดเมน ตำแหน่งของ S ในกราฟชี้ว่า effect transport ได้หรือไม่และต้องปรับสูตรแบบใด

- ความน่าจะเป็นและ Bayes เป็นภาษาพื้นฐาน แต่ไม่พอตอบคำถามเชิงสาเหตุ
- Confounding เป็นแนวคิดเชิงสาเหตุ ไม่ใช่เชิงสถิติ
- ML อยู่ที่ Rung 1 (P(Y|X)) แต่การตัดสินใจทางคลินิกต้องการ Rung 2-3 (do และ counterfactual)
- RCT แก้ confounding ได้หมดแต่มีข้อจำกัด (จริยธรรม/ต้นทุน/generalizability/ขนาดข้อมูล)
- RWD จำเป็น แต่ต้องใช้เครื่องมือเชิงสาเหตุ (POF+SCM, DAG, d-separation, matching/PSM/IPW/DML/Dragonnet) เติม counterfactual ที่หายไป
- ATE เดียวไม่พอ ต้องลงถึง CATE/ITE เพื่อ personalized medicine
- ปัญหาปลายทาง: missingness และ transportability — ผลที่ได้ขนไปใช้กับประชากรอื่นได้แค่ไหน
ปัญหาหลัก: เราไม่มีทางย้อนเวลากลับไปดูว่าถ้าไม่ทำ X จะเกิดอะไรขึ้น — เห็นได้แค่โลกที่เกิดขึ้นจริง 1 เส้นทาง (fundamental problem of causal inference)

ไอศกรีมกับคนจมน้ำสัมพันธ์กัน ไม่ใช่เพราะไอศกรีมทำให้จมน้ำ แต่เพราะ "หน้าร้อน" เป็นสาเหตุร่วมของทั้งคู่

```
    หน้าร้อน
    ↙        ↘
ไอศกรีม     จมน้ำ
```

กับดักที่กลับหัว — Collider: บางทีควบคุมตัวแปรมากไปกลับทำให้เกิดความสัมพันธ์เทียม เช่น เกรด กับ เรียงความ ไม่เกี่ยวกันเลย แต่พอดูเฉพาะคนที่ "เข้ามหาลัยได้" (ซึ่งรับจากเกรดดีหรือเรียงความดี) จะเห็นว่าเกรดต่ำมักเรียงความเก่ง (ภาพลวงจากการเลือกกลุ่มตัวอย่าง)

ถ้าไม่มี RCT: เลียนแบบการสุ่มด้วยข้อมูลจริง เช่น จับคู่คนไข้ที่ลักษณะคล้ายกันมาก (matching / PSM) เหมือนสร้าง "ฝาแฝดเทียม" เปรียบเทียบกัน แทนที่จะเทียบทั้งกลุ่มที่ไม่เหมือนกันเลย

- P(A) = prevalence = 0.1%
- P(B|A) = sensitivity = 85%
- P(B|not A) = false positive = 1%
P(A|B) = (0.85×0.001) / [(0.85×0.001)+(0.01×0.999)] = 0.078

→ ในประชากรทั่วไป (ไม่ใช่ close contact) test positive มีโอกาสเป็นโรคจริงแค่ 7.8%

Confounding

U → Treatment

U → Outcome

Treatment → Outcome

RCT

ตัด U → Treatment (randomization)

เหลือ do(Treatment) → Outcome

Observational/RWD

ลูกศร U → Treatment ยังอยู่ครบ

Matching

จับคู่หน่วย treat/control ที่ลักษณะคล้ายกัน

PSM

ใช้ π = P(assigned to treatment) จับคู่

IPW

- ประมาณ propensity score ด้วย GLM: P[A=1|W]
- Weight = I[A=1]/P̂[A=1|W] − I[A=0]/P̂[A=0|W]
- ATE = E[weight × Y]
1. สุ่มเหรียญ (RCT)

สุ่มแบ่งกลุ่ม ทำให้สองกลุ่ม "เหมือนกันโดยเฉลี่ย" ยกเว้นตัวแปรที่สนใจ — แต่บางทีทำไม่ได้ (แพง/ผิดจริยธรรม/ช้าเกิน)

2. ใช้ข้อมูลจริง (RWD)

ปัญหาคือคนที่เลือกรับ treatment เองมักไม่เหมือนคนที่ไม่รับ → เกิด confounder (ตัวกวนใจ)



## Clinical Epidemiology (Fletcher) (ID: 3d20abc4-4cc7-80c4-8fa1-f5ee2d8856fa)

Clinical Epidemiology: The Essentials

> สรุปเนื้อหาจากหนังสือ Clinical Epidemiology: The Essentials (5th ed.) โดย Robert H. Fletcher, Suzanne W. Fletcher และ Grant S. Fletcher — จัดทำเป็นสรุปรายบทเพื่อการทบทวน (ไม่ใช่การคัดลอกต้นฉบับ แต่เรียบเรียงใหม่โดยคงประเด็นสำคัญและตัวอย่างเชิงแนวคิดไว้ครบถ้วน)


#### ภาพรวมของหนังสือ

หนังสือเล่มนี้สอนให้บุคลากรทางการแพทย์ประเมิน "ความน่าเชื่อถือของหลักฐานทางคลินิก" ด้วยตนเอง แทนที่จะเชื่อคำแนะนำโดยไม่เข้าใจที่มา ระบาดวิทยาคลินิก (clinical epidemiology) ถูกนิยามว่าเป็น "วิทยาศาสตร์พื้นฐาน" อีกแขนงหนึ่งของการแพทย์คลินิก — เป็นศาสตร์ที่ใช้การนับเหตุการณ์ทางคลินิกในกลุ่มผู้ป่วยที่คล้ายกัน แล้วใช้วิธีวิจัยที่เข้มงวดเพื่อให้การทำนายเกี่ยวกับผู้ป่วยแต่ละรายมีความแม่นยำ โดยพยายามหลีกเลี่ยงความคลาดเคลื่อนเชิงระบบ (bias) และผลจากความบังเอิญ (chance)

โครงสร้างหนังสือมี 14 บท ครอบคลุมคำถามทางคลินิกหลัก ๆ ที่แพทย์ต้องเผชิญในการดูแลผู้ป่วย ได้แก่ ความถี่ของโรค ความผิดปกติ ความเสี่ยง การพยากรณ์โรค การวินิจฉัย การรักษา การป้องกัน บทบาทของโอกาสทางสถิติ สาเหตุของโรค การรวบรวมหลักฐาน และการจัดการความรู้ทางการแพทย์


#### สารบัญ (ลิงก์ไปยังแต่ละบท)

จะทยอยเพิ่มเนื้อหาแต่ละบทด้านล่างนี้ทีละบท


#### บทที่ 1: บทนำ (Introduction)

แนวคิดหลัก: หนังสือเปิดด้วยกรณีตัวอย่างผู้ป่วยชายอายุ 51 ปี มาด้วยอาการแน่นหน้าอก เพื่อชี้ให้เห็นว่าคำถามที่แพทย์ต้องตอบในชีวิตจริง (เป็นโรคหรือไม่ แม่นยำแค่ไหน พยากรณ์โรคเป็นอย่างไร รักษาอย่างไร ป้องกันได้ไหม สาเหตุคืออะไร) ล้วนเป็น "คำถามทางคลินิก" ที่ต้องอาศัยหลักระบาดวิทยาคลินิกในการตอบ โดยหนังสือได้จับคู่แต่ละคำถามกับบทต่าง ๆ ของหนังสือไว้อย่างชัดเจน (ความถี่→บทที่ 2, ความผิดปกติ→บทที่ 3, ความเสี่ยง→บทที่ 5-6, การพยากรณ์โรค→บทที่ 7, การวินิจฉัย→บทที่ 8, การรักษา→บทที่ 9, การป้องกัน→บทที่ 10, สาเหตุ→บทที่ 12)

ผลลัพธ์ทางสุขภาพ (Health Outcomes) — "5 Ds": สิ่งที่สำคัญที่สุดในเวชปฏิบัติคือผลลัพธ์ที่มีความหมายต่อผู้ป่วยจริง ๆ ไม่ใช่แค่ค่าตรวจแล็บที่ดีขึ้น ประกอบด้วย

- Death — การเสียชีวิตก่อนเวลาอันควร
- Disease — กลุ่มอาการ อาการแสดง และความผิดปกติทางแล็บ
- Discomfort — อาการไม่สบายตัว เช่น ปวด คลื่นไส้ หายใจลำบาก
- Disability — ความบกพร่องในการทำกิจวัตร
- Dissatisfaction — ปฏิกิริยาทางอารมณ์ต่อโรคและการรักษา
(บางครั้งเสริม D ที่ 6 คือ Destitution หรือภาระค่าใช้จ่าย) มีตัวอย่างสำคัญคือกรณียา rosiglitazone ที่ลดน้ำตาลในเลือดได้ดีแต่กลับเพิ่มความเสี่ยงโรคหัวใจ สะท้อนว่าการเปลี่ยนแปลงค่าตรวจแล็บไม่เท่ากับผลลัพธ์ทางคลินิกที่แท้จริง เว้นแต่จะมีหลักฐานที่เชื่อมโยงทั้งสองอย่างชัดเจน

รากฐานทางวิทยาศาสตร์ของการแพทย์คลินิก: ระบาดวิทยาคลินิกเป็นหนึ่งในหลายศาสตร์ที่ประกอบกันเป็นพื้นฐานของการดูแลผู้ป่วย ได้แก่ วิทยาศาสตร์ชีวภาพ (biologic sciences – เน้นเซลล์ ยีน กลไกโรค), วิทยาศาสตร์คลินิก (เน้นผู้ป่วยรายบุคคล), ระบาดวิทยา (เน้นประชากร) และการวิจัยระบบบริการสุขภาพ (health services research) โดยระบาดวิทยาคลินิกอยู่ตรงกลางระหว่างวิทยาศาสตร์คลินิกกับระบาดวิทยา — ใช้วิธีการเชิงประชากรมาตอบคำถามเกี่ยวกับผู้ป่วยรายบุคคล มีตัวอย่างประวัติศาสตร์ที่ดีคือการค้นพบโรคเอดส์ (AIDS) ในทศวรรษ 1980 ซึ่งอาศัยความร่วมมือของแพทย์ นักระบาดวิทยา นักวิทยาศาสตร์ห้องแล็บ และเจ้าหน้าที่สาธารณสุขร่วมกัน

Evidence-Based Medicine (EBM): คือการประยุกต์ใช้ระบาดวิทยาคลินิกในการดูแลผู้ป่วยจริง ประกอบด้วยการตั้งคำถามทางคลินิกที่ตอบได้ การค้นหาหลักฐานที่ดีที่สุด การประเมินความน่าเชื่อถือของหลักฐาน แล้วผสานเข้ากับความเชี่ยวชาญของแพทย์และค่านิยม/สถานการณ์ของผู้ป่วย หนังสือยังล้อเลียนถึง "ทางเลือกอื่นที่ไม่ใช่ EBM" ที่พบได้บ่อยในเวชปฏิบัติจริง เช่น การตัดสินใจตามอาวุโส (eminence-based) ตามความมั่นใจในน้ำเสียง (vehemence-based) ตามภาพลักษณ์ (eloquence-based) ตามความกลัวถูกฟ้อง (nervousness-based) ซึ่งล้วนเป็นทางลัดทางอารมณ์ที่ด้อยกว่าหลักฐานเชิงประจักษ์

หลักการพื้นฐาน (Basic Principles):

- ตัวแปร (Variables): แบ่งเป็นตัวแปรต้น/ตัวทำนาย (independent variable), ตัวแปรตาม/ผลลัพธ์ (dependent variable) และตัวแปรแทรกซ้อน (extraneous variables/covariates)
- ตัวเลขและความน่าจะเป็น: เนื่องจากผลลัพธ์ของผู้ป่วยแต่ละคนไม่แน่นอน การพยากรณ์ทางคลินิกจึงต้องแสดงเป็น "ความน่าจะเป็น" โดยอ้างอิงจากประสบการณ์ของกลุ่มผู้ป่วยที่คล้ายกันในอดีต
- ประชากรและกลุ่มตัวอย่าง (Populations & Samples): งานวิจัยทางคลินิกมักทำในกลุ่มตัวอย่าง (sample) แล้ว "อนุมาน (infer)" กลับไปยังประชากร (population) ความน่าเชื่อถือของการอนุมานขึ้นกับวิธีการสุ่มตัวอย่าง — การสุ่มที่ทุกคนมีโอกาสถูกเลือกเท่ากันจะให้กลุ่มตัวอย่างที่เป็นตัวแทนที่ดี ต่างจากการเลือกแบบสะดวก (convenience sample) ที่อาจทำให้ผลบิดเบือน
ความคลาดเคลื่อนเชิงระบบ (Bias): นิยามว่าเป็นกระบวนการใด ๆ ที่ทำให้ผลลัพธ์เบี่ยงเบนออกจากความจริงอย่างเป็นระบบ (ไม่ใช่แบบสุ่ม) แบ่งเป็น 3 กลุ่มหลัก

- Selection bias — เกิดเมื่อกลุ่มที่นำมาเปรียบเทียบแตกต่างกันในปัจจัยอื่นที่มีผลต่อผลลัพธ์ด้วย (ตัวอย่าง: การผ่าตัดไส้เลื่อนแบบส่องกล้อง vs. แบบเปิด — หากผู้ป่วยที่ได้รับการส่องกล้องมีสุขภาพดีกว่าอยู่แล้ว การเปรียบเทียบผลก็จะลำเอียง)
- Measurement bias — เกิดเมื่อวิธีวัดผลแตกต่างกันระหว่างกลุ่ม (ตัวอย่างคลาสสิก: "White coat hypertension" ความดันโลหิตสูงขึ้นเมื่อวัดโดยแพทย์เทียบกับพยาบาล เพราะความวิตกกังวลของผู้ป่วย และปัจจัยทางเทคนิค เช่น ขนาดผ้าพันแขนไม่เหมาะสม)
- Confounding — เกิดเมื่อปัจจัยสองอย่าง "เดินทางไปด้วยกัน" ทำให้ผลของปัจจัยหนึ่งถูกปนเปื้อนด้วยผลของอีกปัจจัย (ตัวอย่าง: การกินสารต้านอนุมูลอิสระดูเหมือนลดโรคหัวใจในการศึกษาเชิงสังเกต แต่เมื่อทำการทดลองแบบสุ่มที่ควบคุม confounding ได้ กลับไม่พบประโยชน์ เพราะคนที่กินอาหารเสริมเองมักมีพฤติกรรมสุขภาพดีอื่น ๆ ร่วมด้วย เช่น ออกกำลังกาย ไม่สูบบุหรี่)
โอกาส/ความบังเอิญ (Chance): ต่างจาก bias ตรงที่ chance ทำให้ผลเบี่ยงเบนได้ทั้งสองทิศทางแบบสุ่ม ไม่ใช่ไปทางใดทางหนึ่งเสมอ เรียกว่า "random variation" — สถิติสามารถช่วยประมาณว่าโอกาสมีผลต่อผลการศึกษามากน้อยเพียงใด แต่ไม่สามารถกำจัด bias ที่ซ่อนอยู่ได้

Bias และ Chance สะสมร่วมกัน: ตัวอย่างการวัดความดันโลหิตแสดงให้เห็นว่าความคลาดเคลื่อนจากทั้ง bias (เครื่องมือ/เทคนิคการวัด) และ chance (ความแปรปรวนสุ่ม) เกิดร่วมกันได้เสมอในการวัดทางคลินิก

ความตรงภายในและภายนอก (Internal & External Validity):

- Internal validity = ผลการศึกษาถูกต้องสำหรับกลุ่มตัวอย่างที่ศึกษาจริงหรือไม่ (ถูกคุกคามโดย bias และ chance ทั้งหมดข้างต้น)
- External validity (generalizability) = ผลที่ได้นำไปใช้กับผู้ป่วยกลุ่มอื่น/สถานที่อื่นได้หรือไม่
ตัวอย่างสำคัญ: อัตราตายจาก anorexia nervosa ที่รายงานจากศูนย์ส่งต่อผู้ป่วยหนัก (referral center) สูงถึง 15% ใน 30 ปี แต่เมื่อศึกษาประชากรทั้งหมดในเมือง Rochester กลับพบเพียง 7% ใกล้เคียงกับคนทั่วไป สะท้อนปัญหา sampling bias ที่ทำให้ผลจากศูนย์ส่งต่อไม่สามารถ generalize ไปยังผู้ป่วยทั่วไปได้

ข้อมูลและการตัดสินใจ: การตัดสินใจทางคลินิกที่ดีต้องอาศัยทั้งหลักฐาน ความเชี่ยวชาญทางคลินิก และคุณค่า/ความต้องการของผู้ป่วย ซึ่งนำไปสู่แนวคิด shared decision making (การตัดสินใจร่วมกันระหว่างแพทย์กับผู้ป่วย) โดยแพทย์เป็นผู้เชี่ยวชาญด้านหลักฐาน ส่วนผู้ป่วยเป็นผู้เชี่ยวชาญด้านคุณค่าและความต้องการของตนเอง


#### บทที่ 2: ความถี่ (Frequency)

คำ vs. ตัวเลข: งานวิจัยพบว่าแพทย์และผู้ป่วยตีความคำบอกความน่าจะเป็น เช่น "มักจะ" "บางครั้ง" "นาน ๆ ครั้ง" แตกต่างกันมาก (เช่น "มักจะ" ถูกตีความได้ตั้งแต่ 60–90% หรือกว้างกว่านั้น) หนังสือจึงเน้นย้ำว่าควรใช้ตัวเลขแทนคำเชิงคุณภาพเสมอที่ทำได้ เพื่อสื่อสารได้แม่นยำและตรวจสอบได้

Prevalence กับ Incidence — หัวใจของบทนี้

- Prevalence (ความชุก) = สัดส่วนของคนที่ "มี" ภาวะนั้น ณ จุดเวลาหนึ่ง (point prevalence) หรือช่วงเวลาหนึ่ง (period prevalence) — เปรียบเหมือนภาพนิ่งหนึ่งเฟรม
- Incidence (อุบัติการณ์) = สัดส่วนของคนที่ "ยังไม่เป็น" แล้วเกิดภาวะนั้นขึ้นใหม่ในช่วงเวลาที่กำหนด — วัดจาก cohort (กลุ่มคนที่ติดตามไปข้างหน้า)
ทั้งสองตอบคำถามคนละแบบ: prevalence ตอบว่า "ตอนนี้มีกี่คนที่เป็น" ส่วน incidence ตอบว่า "อัตราการเกิดผู้ป่วยใหม่เป็นเท่าไร" — ตัวอย่างตัวเลขจากมะเร็งปอดในประชากร 10,000 คนแสดงวิธีคำนวณทั้งสองค่าอย่างละเอียด

ความสัมพันธ์ระหว่าง Prevalence, Incidence และระยะเวลาของโรค (ในภาวะคงตัว/steady state):

> Prevalence = Incidence × ระยะเวลาเฉลี่ยของโรค

ตัวอย่าง: ulcerative colitis มี incidence 8.3/100,000 คน-ปี และ prevalence 229/100,000 คน → ระยะเวลาเฉลี่ยของโรค ≈ 28 ปี (สอดคล้องกับการเป็นโรคเรื้อรัง) โรคที่ระยะสั้น (เช่น หัวใจวายเฉียบพลันที่ตายเร็ว) จะถูกมองข้ามได้ง่ายจาก prevalence study แม้จะมี incidence สูงก็ตาม ตรงข้ามกับโรคเรื้อรังที่ prevalence สูงแม้ incidence ต่ำ (เช่น inflammatory bowel disease)

อัตราอื่น ๆ ที่ใช้บ่อย: case fatality rate/survival rate (สัดส่วนที่ตาย/รอดจากโรค), complication rate, infant mortality rate, perinatal mortality rate, maternal mortality rate — ซึ่งบางอัตรา (เช่น infant mortality rate) เป็นเพียง "การประมาณ" ของ incidence เพราะตัวเศษกับตัวส่วนไม่ได้มาจากกลุ่มคนเดียวกันเป๊ะ

รูปแบบการศึกษา:

- Prevalence/cross-sectional studies (surveys) — ตรวจสอบประชากร ณ จุดเวลาหนึ่ง เช่น การศึกษาความชุกของโรคซึมเศร้าในหลายประเทศของ WHO
- Incidence/cohort studies — ติดตามกลุ่มคน (cohort) ไปข้างหน้าเพื่อดูการเกิดเหตุการณ์ แบ่งเป็น
องค์ประกอบพื้นฐานของการศึกษาความถี่:

- นิยาม "case" (ตัวเศษ): จุดตัด (cutoff) ที่ใช้นิยามว่าเป็นโรคมีผลอย่างมากต่อความชุกที่วัดได้ (ตัวอย่าง: โรคหืดที่เกิดจากแอสไพรินมีความชุก 3% ถ้าถามอาการ แต่สูงถึง 21% ถ้าทดสอบจริงด้วยการให้แอสไพริน) และความไวของการตรวจหาโรคก็มีผลมาก เช่น การตรวจ PSA ทำให้ incidence ของมะเร็งต่อมลูกหมากพุ่งสูงขึ้นอย่างรวดเร็วโดยไม่ได้แปลว่าโรคเพิ่มขึ้นจริง
- นิยามประชากร (ตัวส่วน): ต้องเป็น "population at risk" ที่มีโอกาสเกิดเหตุการณ์นั้นได้จริง (เช่น อัตรามะเร็งปากมดลูกต้องคำนวณเฉพาะในผู้หญิงที่ยังมีมดลูก) ต้องตรงกับคำถามวิจัย และต้องอธิบายรายละเอียดพอที่จะบอกได้ว่า generalize ไปใช้กับใครได้บ้าง
- กลุ่มตัวอย่างเป็นตัวแทนประชากรหรือไม่: random/probability sample (ทุกคนมีโอกาสถูกเลือกเท่ากันหรือรู้ค่าความน่าจะเป็น) ให้ผลใกล้เคียงประชากรจริงมากกว่า convenience/grab sample (สุ่มแบบสะดวก) ซึ่งพบได้บ่อยในงานวิจัยทางคลินิกและมักทำให้เกิดปัญหาการ generalize ผลไปยังผู้ป่วยกลุ่มอื่น
การกระจายตัวของโรคตามเวลา สถานที่ บุคคล (Time, Place, Person): เป็นเบาะแสสำคัญสู่สาเหตุของโรค

- เวลา: epidemic (การระบาดเพิ่มขึ้นเฉียบพลัน) เช่น SARS ที่ปักกิ่งปี 2003 ซึ่งกราฟ epidemic curve แสดงจำนวนผู้ป่วยลดลงหลังมีมาตรการกักตัว, pandemic (ระบาดทั่วโลก) เช่น ไข้หวัดใหญ่ 1918, endemic (จำกัดอยู่เฉพาะพื้นที่) เช่น โรคคอพอกจากขาดไอโอดีน
- สถานที่: เช่น อุบัติการณ์มะเร็งลำไส้ใหญ่สูงในอเมริกาเหนือ/ยุโรป/ออสเตรเลีย แต่ต่ำในแอฟริกา/เอเชีย ชี้ไปที่ปัจจัยสิ่งแวดล้อม
- บุคคล: เช่น กรณี AIDS ในระยะแรกพบมากในกลุ่มชายรักชายและผู้ใช้ยาเสพติดทางหลอดเลือด ซึ่งนำไปสู่สมมติฐานเรื่องการติดต่อทางเพศสัมพันธ์/เลือด
ประโยชน์และข้อจำกัดของ Prevalence Studies:

- ประโยชน์: ช่วยวางแผนบริการสุขภาพ ช่วยประเมิน pretest probability ในการวินิจฉัย (เช่น ต่อมน้ำเหลืองโตในเด็กที่คลินิกทั่วไปมีโอกาสเป็นมะเร็งเพียง 0.4% แต่ในผู้ใหญ่ที่ศูนย์ส่งต่อสูงถึง 60%)
- ข้อจำกัด: ให้หลักฐานเชิงสาเหตุที่อ่อนมาก เพราะวัดตัวแปรเหตุและผลพร้อมกันในเวลาเดียว ทำให้ไม่รู้ว่าอะไรเกิดก่อนเกิดหลัง (เช่น ภาวะน้ำตาลสูงทำให้ติดเชื้อ หรือติดเชื้อทำให้น้ำตาลสูง) และไม่สามารถแยกได้ว่า prevalence ที่สูงมาจาก incidence สูงหรือระยะเวลาโรคนาน

#### บทที่ 3: ความผิดปกติ (Abnormality)

ประเด็นตั้งต้น: การแยก "ปกติ" กับ "ผิดปกติ" คืองานประจำวันของแพทย์ แต่ในความเป็นจริงกรณีชัดเจนสุดขั้ว (เช่น ตับม้ามโตมาก) พบน้อย ส่วนใหญ่ต้องตัดสินใจในจุดที่ก้ำกึ่ง โดยเฉพาะในผู้ป่วยที่ยังไม่ถูกคัดกรองมาก่อน (เวชปฏิบัติทั่วไป/ห้องฉุกเฉิน) ซึ่งยากกว่าศูนย์ส่งต่อที่รู้อยู่แล้วว่ามีบางอย่างผิดปกติ

ประเภทของข้อมูล (Types of Data):

- Nominal data — ข้อมูลเป็นหมวดหมู่ไม่มีลำดับ เช่น หมู่เลือด เพศ (ถ้ามี 2 หมวดเรียกว่า dichotomous)
- Ordinal data — มีลำดับแต่ช่วงห่างไม่เท่ากัน เช่น อาการบวมขา 1+ ถึง 4+, เกรดเสียงหัวใจ I–VI, ระดับความเสี่ยงยาต่อทารกในครรภ์ของ FDA (A ถึง X)
- Interval data — มีลำดับและช่วงห่างเท่ากันจริง แบ่งเป็น continuous (ต่อเนื่อง เช่น ความดันโลหิต ค่าเคมีเลือด) และ discrete (นับได้เป็นจำนวนเต็ม เช่น จำนวนครั้งตั้งครรภ์)
คุณภาพของการวัดผล (Performance of Measurements):

- Validity (ความตรง/ความแม่นยำ) — วัดได้ตรงกับสิ่งที่ต้องการวัดจริงหรือไม่ สำหรับสิ่งที่วัดทางกายภาพได้ตรง ๆ (เช่น โซเดียมในเลือด) ตรวจสอบได้ง่ายโดยเทียบกับมาตรฐาน แต่สำหรับสิ่งที่วัดทางกายภาพไม่ได้ (เช่น ปวด คลื่นไส้ ซึมเศร้า) ต้องอาศัย 3 แนวทาง คือ content validity (ครอบคลุมทุกมิติของสิ่งที่วัดและไม่เกินขอบเขต) criterion validity (ทำนายปรากฏการณ์ที่สังเกตได้จริง) และ construct validity (สอดคล้องกับตัวชี้วัดอื่นที่เชื่อว่าเกี่ยวข้องกัน) ตัวอย่างเครื่องมือ เช่น แบบทดสอบ CAGE สำหรับคัดกรองการติดสุรา
- Reliability (ความเที่ยง/reproducibility/precision) — วัดซ้ำ ๆ ด้วยคนละคนคนละเครื่องมือแล้วได้ผลใกล้เคียงกันหรือไม่ (ตัวอย่าง: ผู้เชี่ยวชาญ 21 คนอ่านฟิล์มเอกซเรย์ปอดผู้ป่วย ARDS ชุดเดียวกัน แต่ให้ผล "positive" ตั้งแต่ 36% ถึง 71% แสดงถึงความแปรปรวนระหว่างผู้สังเกตที่สูงมาก) ความสัมพันธ์ระหว่าง validity กับ reliability: การวัดที่ไม่เที่ยงมักไม่แม่นยำไปด้วย แต่การวัดที่แม่นยำ (เที่ยง) อาจยังไม่ตรง (ถ้ามี bias เป็นระบบ)
- Range — เครื่องมือบางชนิดวัดค่าสุดขั้วไม่ได้ (เช่น Basic ADL scale ไม่วัดความสามารถอ่านเขียนหรือเล่นเปียโน)
- Responsiveness — ตรวจจับการเปลี่ยนแปลงตามอาการที่เปลี่ยนไปได้ดีแค่ไหน
- Interpretability — ค่าตัวเลขมีความหมายเข้าใจง่ายหรือไม่ (นิยมใช้วิธี "anchor" ค่ากับสภาพที่คุ้นเคย เช่น Karnofsky Performance Status Scale)
แหล่งที่มาของความแปรปรวน (Variation): แบ่งเป็น variation จากการวัด (เครื่องมือ/ผู้สังเกต) และ variation ทางชีวภาพ (ภายในคนเดียวกันตามเวลา เช่น จำนวน VPBs ต่อชั่วโมงที่ผันผวนมากในผู้ป่วยรายเดียวใน 3 วัน, และระหว่างคนต่างกัน) ทั้งสองแหล่งสะสมรวมกันได้ ตัวอย่างคลาสสิกคือความดันโลหิต ซึ่งความแปรปรวนจากการวัดมีน้อย (~12 mmHg) แต่ความแปรปรวนทางชีวภาพระหว่างการมาตรวจแต่ละครั้งมีมาก จึงต้องวัดหลายครั้งเพื่อให้ได้ค่าที่เป็นตัวแทนจริง

การอธิบายการกระจายตัวของข้อมูล (Distributions): ใช้ central tendency (mean, median, mode) และ dispersion (range, SD, percentile) ในการสรุป ข้อมูลทางคลินิกส่วนใหญ่มีรูปทรงคล้าย unimodal แต่ เบ้ (skewed) ไม่สมมาตร ต่างจาก normal/Gaussian distribution ที่เป็นทฤษฎีสมมาตรสมบูรณ์ (68% อยู่ใน 1 SD, 95% ใน 2 SD) — ข้อควรระวังคือข้อมูลทางคลินิกจริงมักไม่ได้กระจายแบบปกติ การสมมติเช่นนั้นเพียงเพื่อความสะดวกทางคณิตศาสตร์อาจทำให้ตีความผิด

เกณฑ์ตัดสินความผิดปกติ 3 แบบ (แต่ละแบบอาจให้คำตอบไม่ตรงกัน):

- ผิดปกติ = ไม่ธรรมดา (Unusual) — นิยามตามสถิติ เช่น เกิน 2 SD จากค่าเฉลี่ย ข้อเสียคือ (ก) ทำให้ทุกโรคมีความชุก "เท่ากัน" โดยไม่สอดคล้องความจริง (ข) ความไม่ธรรมดาทางสถิติไม่ได้แปลว่าเป็นโรคเสมอไป และ (ค) บางค่าที่ผิดปกติทางสถิติกลับดีต่อสุขภาพ เช่น ความดันต่ำผิดปกติ หรือความหนาแน่นกระดูกสูงผิดปกติ กลับสัมพันธ์กับความเสี่ยงต่ำกว่า
- ผิดปกติ = สัมพันธ์กับโรค (Associated with Disease) — แนวทางที่แข็งแรงกว่า เช่น ความดันซิสโตลิกสัมพันธ์กับอัตราตายจากโรคหัวใจแบบต่อเนื่องไม่มีจุดตัดชัดเจน (no threshold) ตั้งแต่ 115 mmHg ขึ้นไป, หรือดัชนีมวลกาย (BMI) ในผู้สูงอายุ — จุดตัดที่ "ผิดปกติ" ต่างกันไปตามผลลัพธ์ที่สนใจ (BMI ต่ำมากถึงเพิ่มอัตราตาย แต่ BMI ที่เพิ่มความเสี่ยงเสื่อมสมรรถภาพกลับเพิ่มขึ้นตลอดช่วง) — ตัวอย่างสำคัญอีกอันคือการตรวจคัดกรอง PKU ในทารกแรกเกิด ซึ่งค่า phenylalanine ของทารกปกติกับทารกป่วยซ้อนทับกัน (overlap) ทำให้ผลบวกจากการคัดกรอง 10 คน มีเพียง 1 คนที่เป็นโรคจริง
- ผิดปกติ = รักษาแล้วผลลัพธ์ดีขึ้น (Treating leads to better outcome) — เหมาะกับภาวะไม่มีอาการ เช่น กรณีกรดโฟลิก ที่แต่เดิมกำหนด "ปริมาณปกติ" จากปริมาณที่ป้องกันโลหิตจาง แต่ภายหลังพบว่าต้องการปริมาณสูงกว่าเดิม 2-8 เท่าเพื่อป้องกันความพิการท่อประสาทในทารก — หรือกรณี MRI เข่าพบ meniscal tear ในคนไม่มีอาการปวดพอ ๆ กับคนมีอาการ ทำให้ตัดสินใจยากว่าพยาธิสภาพที่พบเกี่ยวข้องกับอาการจริงหรือไม่
Regression to the Mean: เมื่อคัดเลือกผู้ป่วยที่มีค่าตรวจสุดโต่ง (เช่น สูงผิดปกติมาก) แล้ววัดซ้ำ ค่าที่วัดครั้งที่สองมักเข้าใกล้ค่าเฉลี่ยมากขึ้น โดยไม่ได้เกิดจากการรักษาหรือการดีขึ้นจริง แต่เป็นปรากฏการณ์ทางสถิติล้วน ๆ (เพราะค่าที่สูงมากครั้งแรกส่วนหนึ่งมาจากความแปรปรวนสุ่มที่บังเอิญสูง) แพทย์จึงต้องระวังไม่ตีความการดีขึ้นของค่าตรวจซ้ำว่าเป็นผลของการรักษาเสมอไป


#### บทที่ 4: ความเสี่ยง — หลักการพื้นฐาน (Risk: Basic Principles)

นิยาม: Risk factor คือลักษณะที่สัมพันธ์กับความเสี่ยงเป็นโรคที่เพิ่มขึ้น อาจเป็นพันธุกรรม (เช่น HLA-B27 กับกลุ่มโรค spondyloarthropathy) สิ่งแวดล้อมทางกายภาพ (เชื้อโรค สารพิษ) สิ่งแวดล้อมทางสังคม (การสูญเสียคู่สมรส ความแออัด) หรือพฤติกรรม (สูบบุหรี่ ดื่มแอลกอฮอล์ ขับรถไม่คาดเข็มขัด) Exposure คือการได้สัมผัส/ปัจจัยเสี่ยงนั้นก่อนป่วย ซึ่งวัดได้หลายแบบ (เคยสัมผัสหรือไม่ ปริมาณปัจจุบัน ปริมาณสะสม ระยะเวลาที่สัมผัส) — การเลือกตัวชี้วัดที่ไม่เหมาะสมอาจทำให้มองไม่เห็นความสัมพันธ์จริง (เช่น ปริมาณแดดสะสมสัมพันธ์กับมะเร็งผิวหนังชนิด non-melanoma แต่การถูกแดดเผารุนแรงเป็นครั้ง ๆ ต่างหากที่ทำนาย melanoma ได้ดีกว่า)

เหตุใดแพทย์รายบุคคลจึงยากที่จะสังเกตความเสี่ยงของโรคเรื้อรังได้เอง:

- Long latency — ระยะฟักตัวยาวนาน (เช่น รังสีในวัยเด็ก → มะเร็งไทรอยด์ในผู้ใหญ่หลายสิบปีให้หลัง)
- Immediate vs. distant causes — แพทย์สนใจสาเหตุใกล้ตัว (เช่น เชื้อไวรัสก่อโรค) แต่สาเหตุที่อยู่ไกลออกไป (เช่น การศึกษาของมารดาต่ำ→ทารกน้ำหนักน้อย) ก็อยู่ในสายโซ่เหตุ-ผลด้วย
- Common exposure — เมื่อปัจจัยเสี่ยงพบได้ทั่วไปมาก (เช่น การสูบบุหรี่ อาหารเค็ม/หวาน/มัน) ความอันตรายมักถูกมองข้ามไปนาน จนกว่าจะเปรียบเทียบกับกลุ่มพิเศษที่ไม่สัมผัส (เช่น มอร์มอนที่ไม่สูบบุหรี่)
- Low incidence — แม้โรค "พบบ่อย" ในภาพรวม (เช่น มะเร็งปอด) แต่อัตราการเกิดผู้ป่วยใหม่ต่อปีในเวชปฏิบัติจริงยังน้อยมาก จนยากจะสรุปจากประสบการณ์ส่วนตัว
- Small risk — ผลของปัจจัยเสี่ยงหลายตัวมีขนาดเล็ก ต้องศึกษาคนจำนวนมากมหาศาลถึงจะตรวจพบได้ (เช่น ต้องใช้ข้อมูล 2.4 ล้านคน-ปี เพื่อพบว่าดื่มไวน์วันละแก้วเพิ่มความเสี่ยงมะเร็งเต้านม 15%)
- Multiple causes, multiple effects — ปัจจัยเสี่ยงหนึ่งอาจก่อหลายโรค และโรคหนึ่งมีหลายสาเหตุ (เช่น ความดันสูงเป็นสาเหตุอันดับ 3 ของหัวใจล้มเหลว แต่กว่าจะรู้ก็ต้องรอการศึกษาขนาดใหญ่หลายสิบปี)
Risk factor อาจไม่ใช่สาเหตุที่แท้จริง (may or may not be causal): ปัจจัยเสี่ยงที่ไม่ใช่สาเหตุแต่เพียงบ่งชี้ความเสี่ยง เรียกว่า marker — ตัวอย่างสำคัญคือ homocysteine ที่สัมพันธ์กับโรคหัวใจ แต่เมื่อทดลองลดระดับ homocysteine ด้วยวิตามินกลับไม่ลดความเสี่ยงโรคหัวใจจริง แสดงว่าเป็นเพียง marker ไม่ใช่สาเหตุ (การพิสูจน์ว่าเป็นสาเหตุจริงหรือไม่ อยู่ในบทที่ 5)

การทำนายความเสี่ยง (Predicting Risk): เนื่องจากปัจจัยเสี่ยงส่วนใหญ่อ่อนแรงเพียงลำพัง จึงนำหลายปัจจัยมารวมกันด้วยสถิติเป็น risk prediction model/tool เช่น Framingham Risk Score (โรคหัวใจ) หรือ NCI Breast Cancer Risk Assessment Tool (มะเร็งเต้านม) เพื่อช่วย risk stratification (แบ่งกลุ่มเสี่ยงต่ำ/กลาง/สูง)

การประเมินคุณภาพเครื่องมือทำนายความเสี่ยง:

- Calibration — ทำนาย "สัดส่วน" ของกลุ่มที่จะเป็นโรคได้ใกล้เคียงจริงแค่ไหน (เทียบค่า Expected/Observed ให้ใกล้ 1.0)
- Discrimination — แยกแยะ "รายบุคคล" ว่าใครจะเป็น/ไม่เป็นโรคได้ดีแค่ไหน วัดด้วย c-statistic (concordance statistic) — ค่า 0.5 = เท่ากับทายเหรียญ, 1.0 = แยกได้สมบูรณ์แบบ (ตัวอย่าง: เครื่องมือประเมินความเสี่ยงมะเร็งเต้านมของ NCI มี calibration ดีมาก แต่ discrimination ต่ำ ค่า c-statistic เพียง 0.58 เพราะคะแนนความเสี่ยงของคนที่เป็น/ไม่เป็นโรคทับซ้อนกันมาก)
ทำไม risk prediction tool ส่วนใหญ่แยกแยะรายบุคคลได้ไม่ดี: เพราะปัจจัยเสี่ยงส่วนใหญ่อ่อนเกินไป (ต้องมีความเสี่ยงสัมพัทธ์สูงมาก บางแหล่งเสนอว่าต้องมากกว่า 200 เท่า จึงจะแยกแยะรายบุคคลได้ดี) และปัจจัยเสี่ยงกระจายอยู่ทั่วประชากร ทำให้แม้แต่คนที่ "คะแนนความเสี่ยงต่ำ" ก็ยังมีจำนวนสัมบูรณ์ที่ป่วยมากกว่าคนกลุ่ม "คะแนนความเสี่ยงสูง" เพราะกลุ่มความเสี่ยงต่ำมีขนาดใหญ่กว่ามาก — ข้อคิดสำคัญ: สำหรับโรคส่วนใหญ่ คนส่วนใหญ่ที่จะป่วยไม่ได้อยู่ในกลุ่มความเสี่ยงสูง (ตามคำกล่าวของ Geoffrey Rose ที่เปิดบทนี้)

การใช้ปัจจัยเสี่ยงในทางคลินิก:

- ช่วยประเมิน pretest probability ในการวินิจฉัย — แม้ปัจจัยเสี่ยงจะเป็นตัวทำนายที่อ่อนกว่าอาการ/สิ่งตรวจพบทางคลินิกของโรคระยะเริ่มต้น (ตามหลักของ Geoffrey Rose ที่ว่า "ตัวทำนายโรคใหญ่ในอนาคตที่ดีที่สุด มักเป็นโรคเล็กที่มีอยู่แล้วในปัจจุบัน")
- ช่วยเลือกการรักษา — เช่น การตรวจ HER2 ในมะเร็งเต้านมเพื่อเลือกใช้ยาต้าน HER2 แบบมุ่งเป้า
- ช่วยคัดกรองกลุ่มเสี่ยงสูงในโปรแกรมตรวจคัดกรอง — เช่น การตรวจยีนมะเร็งเต้านมเฉพาะในผู้หญิงที่มีประวัติครอบครัวชัดเจน หรือเริ่มคัดกรองมะเร็งลำไส้ใหญ่เร็วขึ้นในผู้มีญาติสายตรงเป็นโรคนี้
- การกำจัดปัจจัยเสี่ยงเพื่อป้องกันโรค — ตัวอย่างคลาสสิกในประวัติศาสตร์ระบาดวิทยา คือ John Snow ที่ค้นพบว่าอหิวาตกโรคระบาดเกี่ยวข้องกับแหล่งน้ำปนเปื้อนในปี 1854 (ก่อนรู้จักเชื้อแบคทีเรียด้วยซ้ำ) และหยุดการระบาดได้โดยตัดแหล่งน้ำนั้น — แสดงว่าไม่จำเป็นต้องรู้กลไกทางชีววิทยาทั้งหมดก็สามารถป้องกันโรคได้ถ้ารู้ปัจจัยเสี่ยงที่แท้จริง

#### บทที่ 5: ความเสี่ยง — จากการสัมผัสไปสู่โรค (Risk: Exposure to Disease)

ทำไมต้องใช้ Observational Study แทนการทดลอง: วิธีที่ทรงพลังที่สุดในการพิสูจน์ความเสี่ยงคือการทดลอง (experiment) แต่คำถามความเสี่ยงส่วนใหญ่ในชีวิตจริง (เช่น มือถือทำให้เกิดมะเร็งสมองไหม การอ้วนเพิ่มความเสี่ยงมะเร็งไหม) ทำการทดลองไม่ได้ทั้งด้านจริยธรรมและทางปฏิบัติ จึงต้องใช้ observational study ซึ่งแบ่งเป็น cohort study (บทนี้) และ case-control study (บทที่ 6)

Cohort Study — หลักการออกแบบ: รวบรวมกลุ่มคน (cohort) ที่ยังไม่เป็นโรค แบ่งเป็นกลุ่ม exposed/unexposed ต่อปัจจัยเสี่ยง แล้วติดตามไปข้างหน้าดูว่าใครป่วยบ้าง เงื่อนไข 3 ข้อที่ cohort ต้องมี: (1) ไม่มีโรคนั้นตั้งแต่แรก (2) ติดตามนานพอให้ความเสี่ยงแสดงออกมาได้จริง (3) ติดตามครบถ้วน/จัดการ dropout อย่างเหมาะสม — ตัวอย่างคลาสสิกคือ Framingham Study (เริ่ม 1949 ติดตามคน 5,209 คน) ที่ค้นพบปัจจัยเสี่ยงโรคหัวใจอย่างความดันสูง คอเลสเตอรอลสูง สูบบุหรี่ ฯลฯ และกลายเป็นที่มาของ Framingham Risk Score

ประเภทของ Cohort Study:

- Prospective cohort — ประกอบกลุ่มปัจจุบันแล้วติดตามไปอนาคต (เช่น Framingham) — ข้อดี: เก็บข้อมูลได้มาตรฐาน วัดปัจจัยหลากหลาย (รวมพฤติกรรม/สังคม) ที่ไม่มีในเวชระเบียน — ข้อเสีย: ใช้เวลานาน แพงมาก และไม่มีประสิทธิภาพถ้าโรคพบน้อย
- Retrospective/Historical cohort — ใช้ฐานข้อมูลย้อนหลัง (เวชระเบียน ทะเบียนโรค) ประกอบ cohort จากอดีตแล้วติดตามมาถึงปัจจุบัน — เร็วกว่า ถูกกว่า แต่ถูกจำกัดด้วยข้อมูลที่มีอยู่แล้วเท่านั้น (ตัวอย่างสำคัญ: การศึกษาวัคซีน MMR กับออทิสติกในเด็กเดนมาร์กกว่า 537,000 คน ที่พบว่าอัตราออทิสติกในเด็กที่ได้วัคซีนไม่ต่างจากไม่ได้วัคซีน หักล้างงานวิจัยที่ก่อความตื่นตระหนกและภายหลังถูกถอนออกเพราะพบการปลอมแปลงข้อมูล)
- Case-cohort design — ดัดแปลง retrospective cohort โดยสุ่มตัวอย่างกลุ่ม unexposed มาเพียงบางส่วน (ไม่ใช่ทั้งหมด) เพื่อเพิ่มประสิทธิภาพ แล้วปรับด้วย sampling fraction ตอนวิเคราะห์ (ตัวอย่าง: การศึกษาผ่าตัดเต้านมป้องกันมะเร็งในผู้หญิงกลุ่มเสี่ยงสูง)
การวัดและเปรียบเทียบความเสี่ยง (Measures of Effect) — สำคัญมาก:

- Absolute risk = incidence ในกลุ่มที่ศึกษา — วิธีที่เข้าใจง่ายที่สุดสำหรับผู้ป่วย/แพทย์
- Attributable risk (risk difference) = Absolute risk กลุ่ม exposed ลบด้วยกลุ่ม unexposed — บอกว่า "ความเสี่ยงส่วนเกิน" จากการสัมผัสคือเท่าไร
- Relative risk (risk ratio) = Absolute risk กลุ่ม exposed หารด้วยกลุ่ม unexposed — บอกว่า "มากกว่ากี่เท่า" นิยมใช้รายงานมากที่สุดในวารสาร แต่ทำให้ตีความขนาดผลกระทบจริงผิดได้ เพราะไม่บอกขนาดสัมบูรณ์ (ตัวอย่าง: บุหรี่กับมะเร็งปอด RR=23.2 แต่ attributable risk =326.6/100,000/ปี เท่านั้น) — ตัวอย่างกระดูกพรุน: RR ของกระดูกความหนาแน่นต่ำต่อการหักคงที่ราว 2 เท่าตลอดทุกช่วงอายุ แต่ attributable risk เพิ่มขึ้นเกือบเท่าตัวตามอายุที่มากขึ้น เพราะความเสี่ยงพื้นฐานสูงขึ้น
- Population-attributable risk / fraction = คำนึงถึงความชุกของการสัมผัสในประชากรด้วย — ตัวอย่างสำคัญ "prevention paradox": ความดันสูงระดับปานกลาง (พบบ่อยกว่า) กลับก่อให้เกิดโรคหัวใจส่วนเกินในภาพรวมประชากรมากกว่าความดันสูงระดับรุนแรง (พบน้อยกว่า) แม้ attributable risk รายบุคคลจะต่ำกว่าก็ตาม — สะท้อนหลักการของ Geoffrey Rose ว่าปัจจัยเสี่ยงที่พบบ่อยแม้อ่อนแรงก็ส่งผลกระทบระดับประชากรได้มากกว่าปัจจัยเสี่ยงรุนแรงที่พบน้อย
Confounding — ภัยคุกคามหลักของ Observational Study: ตัวแปรกวนต้อง (1) สัมพันธ์กับ exposure (2) สัมพันธ์กับโรค และ (3) ไม่ได้อยู่ในสายโซ่เหตุ-ผลระหว่าง exposure กับโรค (ถ้าอยู่ในสายโซ่ เรียกว่า intermediate outcome ไม่ใช่ confounder) — ตัวอย่างสำคัญ: การศึกษาโฟเลตกับโรคหลอดเลือดสมอง เบื้องต้นดูเหมือนโฟเลตป้องกันได้ (RR=0.83) แต่เมื่อปรับตัวแปรกวน (ไขมันอิ่มตัว การสูบบุหรี่ การออกกำลังกาย ที่สัมพันธ์กับการกินโฟเลตด้วย) ผล RR เปลี่ยนเป็น 0.99 — แสดงว่าความสัมพันธ์เดิมเกิดจาก confounding ล้วน ๆ

วิธีควบคุม Confounding:

- Randomization — วิธีที่ดีที่สุด (ควบคุมได้ทั้งตัวแปรที่รู้และไม่รู้) แต่ทำไม่ได้ในการศึกษาความเสี่ยงส่วนใหญ่
- Restriction — จำกัดกลุ่มศึกษาให้มีลักษณะแคบลง (แลกกับ generalizability ที่ลดลง)
- Matching — จับคู่ผู้ป่วยที่มีลักษณะเดียวกัน (ควบคุมได้แค่ตัวแปรที่จับคู่)
- Stratification — วิเคราะห์แยกตามกลุ่มย่อยความเสี่ยงใกล้เคียงกัน (ตัวอย่างคลาสสิก: อัตราตายจากผ่าตัดบายพาสหัวใจของโรงพยาบาล A (4%) ดูสูงกว่า B (2.6%) แต่เมื่อแบ่งชั้นตามความเสี่ยงก่อนผ่าตัด อัตราตายในแต่ละชั้นความเสี่ยงกลับเท่ากันทุกประการ — เพราะ รพ. A รับผู้ป่วยเสี่ยงสูงมากกว่า)
- Standardization (adjustment) — ปรับถ่วงน้ำหนักให้กลุ่มเปรียบเทียบมีสัดส่วนความเสี่ยงเท่ากัน
- Multivariable adjustment — ใช้แบบจำลองทางสถิติ (logistic regression สำหรับผลลัพธ์แบบ dichotomous, Cox proportional hazard สำหรับข้อมูลเวลารอดชีวิต) ควบคุมหลายตัวแปรพร้อมกัน — ข้อจำกัดคือเป็น "black box" ที่ตรวจสอบความผิดพลาดยาก จึงควรใช้ร่วมกับวิธีอื่นเสมอ ไม่ใช้แทนกัน
- ทุกวิธี (ยกเว้น randomization) ควบคุมได้เฉพาะตัวแปรที่รู้จักและวัดได้เท่านั้น — ตัวแปรที่ไม่ได้วัดจะเหลือเป็น residual confounding เสมอ ด้วยเหตุนี้ผลจาก observational study เดี่ยว ๆ ควรตีความเป็น "ความสัมพันธ์อิสระ (independent association)" ไม่ใช่การพิสูจน์สาเหตุ
Effect Modification (Interaction): ต่างจาก confounding ตรงที่ ไม่ใช่ bias ที่ต้องกำจัด แต่เป็นข้อค้นพบที่ควรรายงาน — เกิดเมื่อขนาดผลของ exposure เปลี่ยนแปลงไปตามตัวแปรที่สาม เช่น ความเสี่ยงเลือดออกทางเดินอาหารส่วนบนจากแอสไพรินถูก "ปรับเปลี่ยน" โดยอายุและประวัติแผลในกระเพาะ — ในชายอายุ <50 ปีไม่มีประวัติแผล ความเสี่ยงเพิ่มจากแอสไพรินแทบไม่มี แต่ในชายอายุ >80 ปีที่มีประวัติแผล ความเสี่ยงเพิ่มขึ้นเป็นสองเท่า — ข้อมูลนี้ช่วยให้แพทย์ปรับคำแนะนำการใช้ยาให้เหมาะกับผู้ป่วยแต่ละราย ตัวแปรเดียวกันอาจเป็นได้ทั้ง confounder, effect modifier, ทั้งสอง หรือไม่เป็นทั้งคู่ ขึ้นกับคำถามวิจัยและข้อมูลที่ใช้


#### บทที่ 6: ความเสี่ยง — จากโรคย้อนกลับไปหาการสัมผัส (Risk: From Disease to Exposure)

เหตุผลที่ต้องมี Case-Control Study: cohort study แม่นยำแต่ใช้เวลานาน แพงมาก และไม่มีประสิทธิภาพเมื่อโรคพบน้อย (latency period ของโรคเรื้อรังมักยาวนับสิบปี) Case-control study แก้ปัญหานี้โดยเริ่มจาก "ผล" (โรค) แล้วย้อนไปดู "เหตุ" (การสัมผัส) — ข้อดีคือเร็วกว่า ประหยัดกว่า และเหมาะกับโรคหายากมาก แต่แลกมาด้วยการควบคุม bias ที่ยากกว่า และให้ได้แค่ "ค่าประมาณ" relative risk เท่านั้น ไม่สามารถคำนวณ absolute risk, attributable risk ได้โดยตรง (เพราะกลุ่มตัวอย่างถูกเลือกโดยผู้วิจัย ไม่ใช่เกิดขึ้นเองตามธรรมชาติ)

การออกแบบพื้นฐาน: เลือกกลุ่ม "cases" (มีโรค) และกลุ่ม "controls" (ไม่มีโรค) แล้วย้อนดูว่าในอดีตแต่ละกลุ่มเคยสัมผัสปัจจัยเสี่ยงมากน้อยแค่ไหน ตัวอย่างสำคัญ: การศึกษาว่า bisphosphonate (ยาป้องกันกระดูกพรุน) ทำให้เกิดกระดูกโคนขาหักแบบผิดปกติหรือไม่ — case-control study ในสวีเดนพบว่าผู้ที่ใช้ยานี้มีโอกาสเกิดกระดูกหักผิดปกติสูงกว่าถึง 33 เท่า และตัวอย่างเรื่องหมวกกันน็อคสกีที่ลดความเสี่ยงบาดเจ็บศีรษะได้ 60%

การเลือก Cases: ควรเป็น incident cases (ผู้ป่วยใหม่) ไม่ใช่ prevalent cases เพราะ prevalence ปนกันระหว่าง incidence กับ duration ของโรค (ถ้าใช้ prevalent cases ที่โรคทำให้ตายเร็ว จะทำให้ดูเหมือนปัจจัยเสี่ยงนั้นอันตรายน้อยกว่าความจริง) ควรเป็นตัวแทนของ "ทุก case ในประชากรที่กำหนด" ไม่ใช่เลือกจากศูนย์ส่งต่อที่มักดึงดูดเคสรุนแรง/ผิดปกติ (biased sample)

การเลือก Controls — หัวใจสำคัญของความสมเหตุสมผลของการศึกษา: ต้องมาจาก "ประชากรฐานเดียวกัน" กับ cases และมีโอกาสสัมผัสปัจจัยเสี่ยงเท่ากัน มี 2 แนวทางหลัก

- Population-based — สุ่ม controls จากประชากรทั้งหมดโดยตรง (ดีที่สุด)
- Cohort-based (nested case-control) — ดึง cases/controls มาจาก cohort เดียวกัน ทำให้ได้ทั้งข้อมูล crude incidence จาก cohort และ relative risk ที่ปรับตัวแปรกวนอย่างละเอียดจาก case-control analysis ในคราวเดียว
- ถ้าใช้ hospital/community controls ต้องระวังว่าผู้ป่วยในโรงพยาบาลมักเป็นกลุ่มตัวอย่างที่ลำเอียงอยู่แล้ว บางครั้งจึงใช้ multiple control groups เพื่อเช็คว่าผลลัพธ์สอดคล้องกันไหม (ถ้าค่า RR ใกล้เคียงกันในหลายกลุ่ม control แสดงว่าไม่น่าจะมี bias มาก)
Matching: ช่วยลด confounding แต่ระวัง overmatching — การจับคู่ตัวแปรที่สัมพันธ์ใกล้ชิดกับ exposure มากเกินไป (เช่น จับคู่ด้วยอาการข้ออักเสบในการศึกษายา NSAID กับไตวาย) จะทำให้ผลลัพธ์เพี้ยนเข้าใกล้ "ไม่มีผล" อย่างผิด ๆ และตัวแปรที่จับคู่แล้วจะไม่สามารถศึกษาผลของมันเองได้อีก Umbrella matching คือการจับคู่ด้วยตัวแปรตัวเดียว (เช่น โรงพยาบาล/ชุมชน) ที่เป็นตัวแทนของหลายปัจจัยกวนพร้อมกัน

การวัด Exposure และปัญหา Recall Bias: วิธีที่ปลอดภัยที่สุดคือใช้บันทึกที่เก็บไว้ก่อนเกิดโรค (เวชระเบียน ใบสั่งยา) แต่หลายปัจจัย (อาหาร การออกกำลังกาย) ต้องถามย้อนหลัง ซึ่งเสี่ยงต่อ recall bias — คนที่ป่วยแล้วมักจำการสัมผัสได้แม่นกว่า/มากกว่าคนที่ไม่ป่วย (เช่น พ่อแม่เด็กที่เป็น Reye syndrome มักจำได้แม่นว่าเคยให้แอสไพรินเพราะเป็นข่าวดัง) วิธีป้องกันคือไม่บอกสมมติฐานเฉพาะเจาะจงแก่ผู้เข้าร่วม ใช้แหล่งข้อมูลหลายแหล่ง และปกปิด (blind) ผู้เก็บข้อมูลจากสมมติฐานที่กำลังทดสอบ

Odds Ratio — ตัวประมาณของ Relative Risk: เนื่องจาก case-control study ไม่สามารถคำนวณ incidence ได้ตรง ๆ (เพราะผู้วิจัยเป็นผู้กำหนดสัดส่วน case:control เอง) จึงใช้ odds ratio (OR) = ad/bc (จากตาราง 2x2) แทน ซึ่งจะใกล้เคียงกับ relative risk มาก เมื่อโรคนั้นพบได้น้อยในประชากร (rare disease assumption) — ถ้า incidence สูงเกิน ~1-5% ค่า OR จะเริ่มบิดเบือนจาก RR จริง (OR จะประเมิน RR เกินจริงถ้า RR>1 และประเมินต่ำกว่าจริงถ้า RR<1) — crude OR คือค่าที่ยังไม่ปรับตัวแปรกวน ส่วน adjusted OR คือค่าที่ปรับด้วยแบบจำลองทางสถิติแล้ว

การควบคุมตัวแปรกวน: ใช้วิธีเดียวกับ cohort study ทั้งหมด (restriction, matching, stratification, multivariable modeling) — และเช่นเดียวกับ observational study ทุกชนิด ผลที่ได้ควรตีความเป็น "ความสัมพันธ์" ไม่ใช่ "การพิสูจน์สาเหตุ" เพราะยังมีโอกาสเกิด residual confounding จากตัวแปรที่ไม่ได้วัด

การใช้ Case-Control Study สืบสวนการระบาด: เป็นเครื่องมือสำคัญในการหาสาเหตุของ outbreak เฉียบพลัน เช่น กรณีการระบาดของเชื้อ E. coli สายพันธุ์ผลิตสารพิษ Shiga toxin ในเยอรมนีปี 2011 (ผู้ป่วยกว่า 3,816 ราย) ที่ทีมวิจัยใช้ case-control study เปรียบเทียบผู้ป่วย hemolytic-uremic syndrome กับ controls พบว่าการกินถั่วงอก (sprouts) สัมพันธ์กับโรค (OR=5.8) แล้วยืนยันด้วย cohort study ขนาดเล็กในร้านอาหารที่พบ relative risk สูงถึง 14.2 จนสามารถสืบย้อนไปถึงผู้ผลิตถั่วงอกรายเดียวและควบคุมการระบาดได้สำเร็จ — แสดงให้เห็นว่า case-control และ cohort study ทำงานร่วมกับการสอบสวนทางระบาดวิทยาภาคสนาม ("shoe-leather epidemiology") ได้อย่างมีพลัง


#### บทที่ 7: การพยากรณ์โรค (Prognosis)

นิยาม: Prognosis คือการทำนายการดำเนินโรคหลังเริ่มเป็นโรคแล้ว — คล้ายกับ cohort study ของความเสี่ยง แต่ต่างกันสำคัญ 4 ประการ:

- ผู้ป่วยต่างกัน — risk factor ศึกษาในคนสุขภาพดี, prognostic factor ศึกษาในคนที่ป่วยแล้ว
- ผลลัพธ์ต่างกัน — risk นับ "การเกิดโรค" ส่วน prognosis นับ "ผลลัพธ์ของโรคที่มีอยู่แล้ว" (ตาย ภาวะแทรกซ้อน ทุพพลภาพ)
- อัตราต่างกัน — เหตุการณ์ทาง risk มักหายาก (1/1,000 ถึง 1/100,000) แต่เหตุการณ์ทาง prognosis พบบ่อยกว่ามาก ทำให้แพทย์รายบุคคลพอจะสังเกตแนวโน้ม prognosis ระยะสั้นได้เองจากประสบการณ์
- ปัจจัยต่างกัน — ปัจจัยเสี่ยงกับปัจจัยพยากรณ์โรคอาจไม่ใช่ตัวเดียวกันเลย (เช่น ปัจจัยเสี่ยงโรคหัวใจแบบดั้งเดิม กลับสัมพันธ์ผกผันกับการเสียชีวิตในโรงพยาบาลหลังกล้ามเนื้อหัวใจตายครั้งแรก)
Clinical Course vs. Natural History: Clinical course = การดำเนินโรคหลังเข้ารับการรักษาแล้ว, Natural history = การดำเนินโรคถ้าไม่ได้รักษาอะไรเลย — โรคจำนวนมากไม่เคยเข้าสู่ระบบการรักษาเลยเพราะไม่มีอาการหรือถูกมองว่าเป็น "เรื่องปกติของชีวิต" (เช่น มีเพียง 17% ของผู้ป่วย irritable bowel syndrome ที่ไปพบแพทย์ในรอบ 10 ปี)

องค์ประกอบของการศึกษา Prognosis ที่ดี:

- Patient sample — ควรเป็นตัวแทนของประชากรที่กำหนดชัดเจน (คลินิก/ภูมิภาค) เพื่อ generalizability
- Zero time — จุดเริ่มต้นนับเวลาที่ชัดเจนและเดียวกันสำหรับทุกคน (เช่น วันวินิจฉัย) เรียกกลุ่มที่เริ่มนับจากจุดกำเนิดโรคว่า inception cohort — ถ้าจุดเริ่มต้นเปลี่ยนไปอย่างเป็นระบบ (เช่น เทคโนโลยีใหม่ตรวจพบการแพร่กระจายของมะเร็งได้ไวขึ้น) จะเกิด stage migration (หรือ "Will Rogers phenomenon") ที่ทำให้ผลการรักษาดูดีขึ้นทั้งที่จริง ๆ ไม่มีอะไรเปลี่ยนแปลง เพราะผู้ป่วยที่แย่ถูกย้ายไปอยู่ระยะที่สูงขึ้น ทำให้แต่ละระยะดูมี prognosis ดีขึ้นทั้งคู่
- Follow-up — ต้องนานพอให้เหตุการณ์สำคัญเกิดขึ้นครบถ้วน
- Outcomes — ควรครอบคลุม 5 Ds ไม่ใช่แค่ตัวชี้วัดทางเทคนิค (เช่น ขนาดก้อนเนื้องอกจากภาพเอกซเรย์) ที่ผู้ป่วยสัมผัสไม่ได้โดยตรง
การอธิบาย Prognosis:

- อัตราสรุปเดียว (เช่น 5-year survival rate) — เข้าใจง่ายแต่ซ่อนรายละเอียดสำคัญได้มาก ตัวอย่างคลาสสิก: 4 โรคที่มี 5-year survival rate เท่ากันที่ 10% แต่รูปแบบการดำเนินโรคต่างกันสิ้นเชิง (dissecting aneurysm ตายเร็วในช่วงแรกแล้วเสี่ยงลดลงมาก, มะเร็งปอดตายในอัตราคงที่ตลอด, ALS ค่อย ๆ แย่ลงจนตายช้า ๆ)
- Survival analysis (Kaplan-Meier) — วิธีมาตรฐานในการประมาณอัตราการรอดชีวิต ณ ทุกจุดเวลา โดยใช้ข้อมูลจากผู้ป่วยทุกคนอย่างมีประสิทธิภาพแม้บางคนจะ censored (ถูกตัดออกจากการติดตามก่อนสิ้นสุดการศึกษา เช่น ยังไม่ตายเมื่อสิ้นสุดการศึกษา หรือขาดการติดตาม) — ข้อควรระวัง: ค่าประมาณที่ปลายเส้นโค้ง (เมื่อเหลือผู้ป่วยน้อยราย) มีความไม่แม่นยำสูงมาก ควรตีความด้วยความระมัดระวัง และรูปร่างเส้นโค้งที่ดูเหมือนเหตุการณ์เกิดถี่ช่วงต้นแล้วราบลงปลาย อาจเป็นภาพลวงตาจากจำนวนผู้ป่วยที่เหลือน้อยลงเท่านั้น ไม่ใช่อัตราเหตุการณ์ที่เปลี่ยนจริง
- Case series/Case report — บรรยายการดำเนินโรคในผู้ป่วยจำนวนน้อย (case report <10 ราย) มีประโยชน์สำหรับโรคหายากหรือกลุ่มอาการใหม่ แต่ไม่ใช่ cohort ที่แท้จริง เพราะมักดึงเฉพาะผู้ป่วยที่มาถึงศูนย์รักษา (prevalent, ไม่ใช่ incident) ทำให้เป็น "false cohort" ที่ไม่สะท้อนภาพรวมของโรคทั้งหมด (ตัวอย่าง: รายงานเด็กถูกงูกัดที่โรงพยาบาลเดียว อาจพลาดเคสที่ดีมากจนไม่ถูกส่งต่อ หรือแย่มากจนตายก่อนถึงโรงพยาบาล)
- Clinical prediction rules — รวมหลายปัจจัยพยากรณ์เป็นคะแนนเดียว เช่น CHADS2 score สำหรับประเมินความเสี่ยงโรคหลอดเลือดสมองในผู้ป่วย atrial fibrillation ซึ่งแบ่งความเสี่ยงได้ต่างกันถึง 14 เท่าระหว่างกลุ่มคะแนนต่ำสุดกับสูงสุด — กติกาสำคัญ: ต้องพัฒนาใน training set แล้วนำไปทดสอบความแม่นยำใน test set ที่แยกต่างหาก (validation) ก่อนนำไปใช้จริงในวงกว้าง
อคติที่พบในการศึกษา Cohort ของ Prognosis:

- Sampling bias — ผู้ป่วยในการศึกษาไม่เป็นตัวแทนของผู้ป่วยทั่วไป (เช่น ศึกษาเฉพาะผู้ป่วยที่ถูกส่งต่อไปศูนย์เฉพาะทาง)
- Migration bias — ผู้ป่วยหลุดออกจากการติดตามอย่างไม่สุ่ม (เช่น คนที่อาการดีมาก/แย่มากมักหลุดออกจากการศึกษาบ่อยกว่า) ทำให้ผลลัพธ์ที่เหลือบิดเบือน
- Measurement bias — การตรวจหาผลลัพธ์ไม่เท่าเทียมกันระหว่างกลุ่ม ป้องกันได้ด้วยการตรวจทุกคนตามมาตรฐานเดียวกัน ปกปิดกลุ่มที่สังกัดจากผู้ประเมิน และตั้งเกณฑ์ชัดเจนล่วงหน้า
- Non-differential misclassification — การจำแนกผิดพลาดที่เกิดขึ้นเท่า ๆ กันทั้งสองกลุ่ม มักทำให้ผลลัพธ์ เอนเอียงไปทาง "ไม่มีผล" (null) ไม่ใช่ทำให้เห็นความแตกต่างที่ไม่มีจริง
Sensitivity Analysis: เมื่อสงสัยว่า bias (เช่น ข้อมูลขาดหาย) อาจมีผลต่อข้อสรุป ให้ทดลองคำนวณผลลัพธ์ภายใต้สมมติฐานต่าง ๆ ว่าข้อมูลที่ขาดหายไปมีลักษณะแตกต่างจากที่มีอยู่มากน้อยเพียงใด (เช่น สมมติว่าคนที่ขาดการติดตามมีอัตราเกิด post-polio syndrome สูง/ต่ำกว่าคนที่ติดตามได้ 2 เท่า) เพื่อดูว่าข้อสรุปยัง "ทนทาน (robust)" ต่อความไม่แน่นอนนั้นหรือไม่ — หลักการสำคัญปิดท้ายบทนี้: การพบว่างานวิจัยมี bias ที่เป็นไปได้ ไม่ได้แปลว่างานวิจัยนั้นใช้ไม่ได้เสมอไป ต้องประเมินต่อว่า bias นั้นมีอยู่จริงหรือไม่ และขนาดใหญ่พอจะเปลี่ยนข้อสรุปทางคลินิกหรือไม่


#### บทที่ 8: การวินิจฉัย (Diagnosis)

กรอบพื้นฐาน — ตาราง 2x2: ผลตรวจ (บวก/ลบ) เทียบกับความจริง (มี/ไม่มีโรค) ให้ผล 4 แบบ: true positive, true negative (ถูกต้อง) และ false positive, false negative (ผิดพลาด) ความแม่นยำของผลตรวจต้องเทียบกับ gold standard/reference standard ซึ่งบางครั้งเป็นการตรวจที่แพงกว่า/เสี่ยงกว่า (เช่น ชิ้นเนื้อ การผ่าตัดสำรวจ) หรือใช้ผลการติดตามในระยะยาวแทนก็ได้สำหรับโรคที่ค่อยๆ แสดงตัว — ปัญหาสำคัญคือบางโรคไม่มี gold standard ที่แท้จริง (เช่น angina pectoris, ลำไส้แปรปรวน) ทำให้เกิด circular reasoning ได้ และเมื่อเปรียบเทียบวิธีตรวจใหม่กับ standard เดิมที่ไม่สมบูรณ์แบบ วิธีใหม่ที่ดีกว่าจริงอาจดู "แย่กว่า" อย่างผิด ๆ เพราะเคสที่ตรวจพบเพิ่มถูกนับเป็น false positive เทียบกับ standard เดิม

Sensitivity และ Specificity:

- Sensitivity = สัดส่วนคนที่มีโรคจริงที่ตรวจได้ผลบวก — ทดสอบไวช่วย "rule out" โรค (ผลลบเชื่อถือได้มาก) เหมาะกับโรคอันตรายที่พลาดไม่ได้ หรือช่วงต้นของการวินิจฉัยที่ต้องการคัดกรองความเป็นไปได้จำนวนมาก
- Specificity = สัดส่วนคนที่ไม่มีโรคจริงที่ตรวจได้ผลลบ — ทดสอบที่จำเพาะช่วย "rule in" โรค (ผลบวกเชื่อถือได้มาก) เหมาะเมื่อผลบวกลวงจะสร้างความเสียหายสูง เช่น ก่อนให้เคมีบำบัด
- ทั้งสองมักแลกกันเสมอ (trade-off) เมื่อขยับจุดตัด (cutoff point) เช่น ตัวอย่าง BNP วินิจฉัยหัวใจล้มเหลว — คุมด้วย ROC curve (พล็อต sensitivity เทียบ 1-specificity) ยิ่งเส้นโค้งชิดมุมบนซ้ายยิ่งดี พื้นที่ใต้เส้นโค้ง (AUC) ใช้เปรียบเทียบว่าทดสอบไหนดีกว่ากัน
ปัจจัยที่ทำให้ค่า Sensitivity/Specificity คลาดเคลื่อนจากรายงานเดิม:

- Spectrum of patients — ทดสอบที่ประเมินในกลุ่มคนที่ป่วยชัดเจนสุดขั้วเทียบกับคนปกติสนิท จะดูมี sensitivity สูงเกินจริงเมื่อเทียบกับการใช้จริงในผู้ป่วยที่มีอาการไม่ชัดเจน (ตัวอย่าง: การตรวจเต้านมมี sensitivity 85% เมื่อใช้วินิจฉัยในคนมีอาการ แต่ลดเหลือ 36% เมื่อใช้เป็นการตรวจคัดกรองในคนไม่มีอาการ)
- Bias — ถ้าผลตรวจที่กำลังประเมินไปมีอิทธิพลต่อการตัดสิน gold standard (เช่น หมอเปลี่ยนใจตรวจเพิ่มเพราะเห็นผลตรวจเป็นบวกก่อน) จะทำให้ตัวเลขดูดีเกินจริงเสมอ ป้องกันด้วยการปิดบัง (blind) ผู้อ่านผล gold standard จากผลตรวจที่กำลังศึกษา
- Chance — กลุ่มตัวอย่างเล็กทำให้ค่า sensitivity/specificity ที่วัดได้มีช่วงความเชื่อมั่นกว้างมาก
Predictive Value — สิ่งที่แพทย์อยากรู้จริง ๆ:

- Positive predictive value (PPV) = ความน่าจะเป็นที่จะมีโรคจริง เมื่อผลตรวจเป็นบวก
- Negative predictive value (NPV) = ความน่าจะเป็นที่จะไม่มีโรคจริง เมื่อผลตรวจเป็นลบ
- กุญแจสำคัญที่สุด: PPV/NPV ไม่ใช่คุณสมบัติของตัวทดสอบเพียงอย่างเดียว แต่ขึ้นกับ "ความชุกของโรคในกลุ่มที่ตรวจ (prevalence/pretest probability)" ด้วยเสมอ — ทดสอบที่จำเพาะสูงมากแค่ไหนก็ตาม ถ้าใช้ในกลุ่มที่ความชุกโรคต่ำมาก (เช่น ตรวจคัดกรองในคนสุขภาพดี) ผลบวกส่วนใหญ่จะเป็น false positive แทบทั้งหมด (PPV เข้าใกล้ 0 เมื่อ prevalence เข้าใกล้ 0) — นี่คือเหตุผลที่การตรวจคัดกรองในกลุ่มความชุกต่ำต้องระวังผลบวกลวงมาก ในขณะที่การตรวจโรคเดียวกันในผู้ป่วยที่สงสัยจริง (ความชุกสูงกว่า) จะมี PPV ดีกว่ามาก — ตัวอย่าง D-dimer วินิจฉัย DVT: sensitivity 98% specificity 60% แต่ PPV เพียง 22% เพราะความชุก DVT ในกลุ่มศึกษาแค่ 10%
การประมาณ Pretest Probability และการใช้ในทางปฏิบัติ: แพทย์ควรประเมิน pretest probability ก่อนสั่งตรวจเสมอ โดยพิจารณาจากอาการ ปัจจัยเสี่ยง กลุ่มประชากร และบริบท (การส่งต่อไปศูนย์เฉพาะทางเพิ่ม pretest probability) — การตรวจวินิจฉัยมีประโยชน์สูงสุดเมื่อ pretest probability อยู่ระดับปานกลาง (ไม่สูงหรือต่ำเกินไป) ถ้า pretest probability ต่ำมากอยู่แล้ว ผลบวกก็ยังไม่น่าเชื่อ (ตรวจไปก็เปลี่ยนการตัดสินใจไม่มาก) ถ้าสูงมากอยู่แล้ว ผลลบก็ยังไม่อาจตัดโรคออกได้ (ตัวอย่างคลาสสิก: การตรวจ exercise stress test หาโรคหลอดเลือดหัวใจ — ในชายหนุ่มไม่มีปัจจัยเสี่ยง (pretest ต่ำมาก) ผลบวกก็ไม่ค่อยเปลี่ยนอะไร ในชายสูงอายุที่มี typical angina (pretest 93%) ผลลบก็ยังไม่ตัดโรคออกได้จริง)

Likelihood Ratio (LR) — ทางเลือกที่ทรงพลังกว่า: LR แสดงว่าผลตรวจแต่ละระดับ "เพิ่มหรือลด" ความน่าจะเป็นของโรคเท่าไร โดยไม่ต้องบีบผลลัพธ์ให้เป็นแค่ บวก/ลบ (LR+ = sensitivity/(1-specificity), LR- = (1-sensitivity)/specificity) ข้อดีคือใช้ได้กับผลตรวจแบบต่อเนื่องหลายระดับ (เช่น ค่า pleural fluid/serum protein ratio ที่ยิ่งสูงยิ่ง LR สูง) วิธีใช้: แปลง pretest probability → pretest odds → คูณด้วย LR → posttest odds → แปลงกลับเป็น posttest probability

การใช้หลายการทดสอบร่วมกัน:

- Parallel testing (ตรวจพร้อมกันทั้งหมด แล้วถือว่าผลบวกจากตัวใดตัวหนึ่งคือผิดปกติ) — เพิ่ม sensitivity/NPV แต่ลด specificity/PPV เหมาะกับสถานการณ์ฉุกเฉินที่ต้องการความไวสูงและมีเวลาจำกัด
- Serial testing (ตรวจทีละขั้น ตรวจต่อเมื่อผลก่อนหน้าเป็นบวก) — เพิ่ม specificity/PPV แต่ลด sensitivity/NPV เหมาะกับกรณีที่ไม่รีบและอยากลดการตรวจที่แพง/เสี่ยง เช่น การคัดกรองดาวน์ซินโดรมที่ตรวจซับซ้อนอย่าง chorionic villus sampling ต่อเมื่อการตรวจเบื้องต้นบ่งชี้ความเสี่ยงสูงเท่านั้น
- ข้อสมมติสำคัญคือการทดสอบแต่ละตัว "ให้ข้อมูลอิสระต่อกัน" — ถ้าไม่เป็นจริง (การทดสอบซ้ำซ้อนกัน) การคำนวณความน่าจะเป็นรวมจากหลายตัวจะประเมิน "คุณค่า" ของการตรวจเกินจริง
- Clinical prediction/decision rules — รวมประวัติ ตรวจร่างกาย และแล็บ เป็นคะแนนเดียวเพื่อแบ่งกลุ่มความชุกโรค เช่น Modified Centor Score สำหรับคอหอยอักเสบจากเชื้อ Group A Streptococcus ที่ช่วยลดการส่งเพาะเชื้อและใช้ยาปฏิชีวนะโดยไม่จำเป็น

#### บทที่ 9: การรักษา (Treatment)

ที่มาของแนวคิดการรักษาและความจำเป็นต้องทดสอบ: แนวคิดการรักษาใหม่มาจากหลายแหล่ง — กลไกโรคระดับโมเลกุล การสังเกตทางคลินิก อุบัติเหตุ (เช่น minoxidil ที่พัฒนาเพื่อรักษาความดันสูงแต่กลับพบว่าแก้ผมร่วงได้ หรือ tamoxifen ที่พัฒนาเป็นยาคุมกำเนิดแต่กลับป้องกันมะเร็งเต้านมได้) และการศึกษาทางระบาดวิทยา (เช่น Framingham Study นำไปสู่การทดลองลดความดัน/คอเลสเตอรอล) แต่แนวคิดที่ฟังดูสมเหตุสมผลทางชีววิทยาต้องถูกทดสอบอย่างเข้มงวดเสมอ — ตัวอย่างสำคัญคือการทดลอง ACCORD ที่คุมน้ำตาลอย่างเข้มงวดในผู้ป่วยเบาหวานชนิดที่ 2 กลับพบว่าอัตราตายเพิ่มขึ้น 21% ทั้งที่ตามทฤษฎีควรจะดีขึ้น หรือกรณีการนอนพักผ่อนบนเตียง (bed rest) ที่เชื่อกันมานานว่าช่วยรักษาหลายโรค แต่การทบทวน 39 การทดลองกลับพบว่าไม่ช่วยโรคใดเลย และแย่กว่าเดิมใน 17 การทดลอง

Randomized Controlled Trial (RCT) — มาตรฐานทองคำ: โครงสร้างเหมือน cohort study ทุกอย่าง ยกเว้นว่าการรักษาถูกสุ่มแทนที่จะให้แพทย์/ผู้ป่วยเลือกเอง ทำให้ตัวแปรกวนทุกตัว (ทั้งที่รู้และไม่รู้) กระจายเท่า ๆ กันในทั้งสองกลุ่มโดยเฉลี่ย

หลักจริยธรรม — Equipoise: การสุ่มจะทำได้อย่างมีจริยธรรมก็ต่อเมื่อยังไม่มีเหตุผลหนักแน่นที่จะเชื่อว่าการรักษาใดดีกว่ากัน และผู้เข้าร่วมต้องยินยอมโดยสมัครใจ สามารถถอนตัวได้ตลอดเวลา และการทดลองต้องหยุดทันทีเมื่อมีหลักฐานชัดเจนว่าได้ผล/เป็นอันตราย/ไร้ประโยชน์

การสุ่มตัวอย่าง (Sampling) — ปัญหา Generalizability: Inclusion/exclusion criteria ที่เข้มงวด (ไม่มีโรคร่วม อายุขัยยาวพอ ไม่มีข้อห้ามใช้ยา ยินยอมเข้าร่วม ให้ความร่วมมือ) ช่วยเพิ่ม internal validity แต่แลกมาด้วยการที่ผู้ป่วยในทดลองเป็นกลุ่มตัวอย่างที่คัดสรรมาก ไม่เหมือนผู้ป่วยทั่วไป (ตัวอย่าง: การทดลองโรคหืดในสก็อตแลนด์ ชวนคนไข้ 1,410 คน แต่สุดท้ายสุ่มได้เพียง 259 คน หรือ 18% เท่านั้น) — แนวทางแก้ปัญหานี้คือ large simple trials (ลดเกณฑ์คัดเข้าให้กว้าง) และ practical/pragmatic clinical trials (ออกแบบให้ตอบคำถามในสถานการณ์จริงของการดูแลผู้ป่วย)

กลุ่มเปรียบเทียบ (Comparison Groups): อาจเป็น (1) ไม่รักษาเลย (2) เพียงเข้าร่วมการศึกษา (Hawthorne effect — คนที่รู้ตัวว่าถูกจับตามองมักมีพฤติกรรม/ผลลัพธ์ดีขึ้นเอง) (3) การดูแลตามปกติ (usual care) (4) placebo (มีฤทธิ์ placebo effect ที่บรรเทาอาการได้จริงราว 1 ใน 3 ของผู้ป่วยแม้ไม่มีกลไกทางเภสัชวิทยา) หรือ (5) การรักษามาตรฐานปัจจุบัน (comparative effectiveness) — ผลรวมของการรักษาที่สังเกตได้ = natural history + Hawthorne effect + placebo effect + ผลจากการรักษาจริง สะสมรวมกันทั้งหมด

การจัดสรรการรักษาแบบสุ่ม: ทำให้ baseline characteristics ของทั้งสองกลุ่มใกล้เคียงกันโดยเฉลี่ย (ควรมีตารางเปรียบเทียบลักษณะพื้นฐานแสดงในรายงาน) — สำหรับการทดลองขนาดเล็กที่เสี่ยงต่อ "โชคร้าย" ทางสถิติ อาจใช้ stratified randomization (แบ่งชั้นตามปัจจัยพยากรณ์สำคัญก่อนสุ่มแยกในแต่ละชั้น)

สิ่งที่เกิดขึ้นหลังการสุ่ม (ที่บั่นทอนความสมบูรณ์ของการทดลอง):

- Compliance/Adherence — ผู้ป่วยไม่ทำตามคำแนะนำ (ลืมกินยา เข้าใจผิด ไม่มีเงินซื้อยา) ผู้ที่ปฏิบัติตามมักมี prognosis ดีกว่าอยู่แล้วไม่ว่าจะได้รับการรักษาจริงหรือ placebo — วิธีลดปัญหานี้คือใช้ run-in period (ให้ placebo ก่อนแล้วคัดคนไม่ให้ความร่วมมือออกก่อนสุ่มจริง)
- Cross-over — ผู้ป่วยย้ายข้ามกลุ่มระหว่างติดตาม ลดความแตกต่างที่สังเกตได้ระหว่างกลุ่ม
- Cointerventions — ได้รับการรักษาอื่นนอกเหนือจากที่ศึกษา ซึ่งถ้าไม่เท่ากันระหว่างกลุ่มจะกลายเป็นตัวแปรกวนใหม่
Blinding (Masking): ทำได้ 4 ระดับ — (1) ผู้จัดสรรการรักษา (allocation concealment) (2) ผู้ป่วย (3) แพทย์ผู้ดูแล (4) ผู้ประเมินผลลัพธ์ — คำว่า single/double-blind มีความหมายกำกวม ควรอธิบายให้ชัดเจนว่าใครถูกปิดบังบ้าง การทดลองที่ไม่ปิดบังเลยเรียก open-label trial — บางครั้งการปิดบังทำไม่สำเร็จจริงเพราะยามีผลข้างเคียงทางสรีรวิทยาที่สังเกตได้ (เช่น ยา beta-blocker ทำให้ชีพจรช้าลง)

การวัดผลลัพธ์: ใช้หลักการเดียวกับ cohort study — ระวังการใช้ intermediate outcome แทนผลลัพธ์ทางคลินิกจริง อาจใช้ composite outcome (รวมหลายผลลัพธ์เป็นตัวเดียว เพิ่มจำนวนเหตุการณ์ที่นับได้ แต่เสี่ยงบดบังความแตกต่างของผลแต่ละองค์ประกอบ — เช่น การเพิ่ม HDL ด้วยไนอาซินไม่ได้ลด composite cardiovascular event แม้ตัวชี้วัดทางแล็บดีขึ้นก็ตาม) และวัด health-related quality of life ควบคู่กับผลลัพธ์ "แข็ง" อย่างการตาย

การสรุปขนาดผล: relative risk reduction, absolute risk reduction, number needed to treat/harm (NNT/NNH)

Efficacy vs. Effectiveness: Efficacy trial ตอบคำถามว่า "รักษาได้ผลหรือไม่ภายใต้สภาวะอุดมคติ" (เน้น internal validity) ส่วน Effectiveness trial ตอบว่า "ได้ผลจริงหรือไม่ในสถานการณ์ปกติ" (เน้น generalizability) — ช่องว่างระหว่างสองสิ่งนี้เรียก "implementation gap"

Intention-to-Treat vs. Explanatory Analysis:

- Intention-to-treat — วิเคราะห์ตามกลุ่มที่ ถูกสุ่มไว้แต่แรก ไม่ว่าจะได้รับการรักษาจริงหรือไม่ — คงความแข็งแรงของการสุ่มไว้เต็มที่ ตอบคำถามเชิง effectiveness ("เสนอการรักษา" มีผลอย่างไร) แต่มีแนวโน้มลดขนาดผลที่สังเกตได้ (เพราะบางคนไม่ได้รับการรักษาจริง)
- Explanatory (per-protocol) — วิเคราะห์ตามการรักษาที่ได้รับจริง — ตอบคำถามเชิง efficacy แต่เสียความเป็น randomized trial ไปบางส่วน (กลายเป็นเหมือน cohort study ที่ต้องจัดการ confounding เอง)
- โดยทั่วไปควรรายงานทั้งสองแบบ แต่ intention-to-treat มักเป็นการวิเคราะห์หลัก
Superiority, Equivalence, Non-inferiority Trials: ปกติทดลองต้องการพิสูจน์ว่า "ดีกว่า" (superiority) แต่บางครั้งต้องการพิสูจน์แค่ว่า "ไม่ด้อยกว่า" (non-inferiority) เมื่อยาใหม่ปลอดภัยกว่า/ถูกกว่า/ใช้ง่ายกว่า — ต้องกำหนด inferiority margin (ค่าความแตกต่างสูงสุดที่ยังยอมรับได้ทางคลินิก) ล่วงหน้า (ตัวอย่าง: azithromycin ชนิดกินเทียบกับ penicillin ชนิดฉีดรักษาโรค yaws — ผลไม่ด้อยกว่าจริง ทำให้เปลี่ยนมาใช้ยากินที่สะดวกกว่าในพื้นที่ห่างไกลได้)

รูปแบบอื่นของ RCT:

- Cluster randomized trials — สุ่มเป็น "กลุ่ม" (โรงพยาบาล ชุมชน) แทนที่จะสุ่มรายบุคคล เหมาะเมื่อการรักษาสามารถ "ปนเปื้อน" ข้ามกลุ่มได้ง่ายถ้าสุ่มรายบุคคล
- Cross-over trials — ผู้ป่วยแต่ละคนได้รับทั้งสองการรักษาตามลำดับสุ่ม (ใช้ได้เมื่อผลของการรักษาไม่คงค้างข้ามช่วง)
- Trials of N=1 — ทดลองสลับการรักษาในผู้ป่วยรายเดียวซ้ำหลายรอบแบบสุ่มและปิดบัง เหมาะกับโรคที่อาการไม่แน่นอน ตอบสนองเร็ว ไม่มีผลตกค้าง (เช่น ไมเกรน หืด ไฟโบรมัยอัลเจีย)
การปรับผลการทดลองให้เข้ากับผู้ป่วยรายบุคคล: วิเคราะห์ subgroup (ระวัง: ยิ่งแบ่งย่อยมาก ตัวอย่างยิ่งเล็กลง ความแม่นยำยิ่งลดลง) และตั้งคำถาม 4 ข้อก่อนตัดสินใจรักษาผู้ป่วยแต่ละราย: การรักษามีประสิทธิภาพในคนบางกลุ่มหรือไม่ → มีผลโดยเฉลี่ยในคนที่คล้ายผู้ป่วยของเราหรือไม่ → กำลังได้ผลกับผู้ป่วยรายนี้จริงหรือไม่ → ประโยชน์คุ้มกับความเสี่ยง/ความไม่สบายตามค่านิยมผู้ป่วยหรือไม่

ทางเลือกเมื่อไม่มี RCT — Observational Studies of Treatment: มีข้อจำกัดสำคัญคือ confounding by indication (เหตุผลที่แพทย์เลือกให้การรักษานั้น ๆ เองที่สัมพันธ์กับผลลัพธ์ ไม่ใช่ตัวการรักษา) — ตัวอย่าง: วัคซีนไข้หวัดใหญ่ดูเหมือนทำให้หืดกำเริบมากขึ้นในการศึกษาเชิงสังเกตดิบ ๆ (เพราะเด็กที่หืดรุนแรงกว่ามักถูกฉีดวัคซีนมากกว่าด้วย) แต่เมื่อปรับตัวแปรกวนอย่างละเอียด (รวมถึงเปรียบเทียบในเด็กคนเดียวกันช่วงก่อน/หลังฉีด) กลับพบว่าวัคซีนป้องกันได้จริง — บทสรุปสำคัญ: การศึกษาเชิงสังเกตของการรักษาส่วนใหญ่ให้คำตอบตรงกับ RCT แต่ก็มีข้อยกเว้นที่ผิดพลาดชัดเจน (เช่น วิตามินต้านอนุมูลอิสระกับโรคหัวใจ) จึงควรใช้ด้วยความระมัดระวังเมื่อไม่มี RCT ให้อ้างอิง

Phases ของการทดลองยา: Phase I (หาขนาดยาที่ปลอดภัย คนไข้น้อยมาก ไม่มีกลุ่มควบคุม) → Phase II (ประเมินประสิทธิภาพเบื้องต้น ความสัมพันธ์ขนาดยา-ผล) → Phase III (RCT ขนาดใหญ่ ยืนยันประสิทธิภาพและผลข้างเคียงที่พบบ่อย) → Postmarketing surveillance (ติดตามผลข้างเคียงที่หายากหลังยาออกสู่ตลาดจริง เพราะ Phase III ไม่มีขนาดตัวอย่างมากพอตรวจจับผลข้างเคียงที่พบน้อยได้)


#### บทที่ 10: การป้องกันโรค (Prevention)

ประเภทของกิจกรรมป้องกันในคลินิก 4 แบบ: วัคซีน (immunizations), การคัดกรอง (screening), การให้คำปรึกษาปรับพฤติกรรม (behavioral counseling), และเคมีป้องกัน (chemoprevention เช่น กรดโฟลิกป้องกันความพิการท่อประสาท, แอสไพรินขนาดต่ำป้องกันหัวใจ)

ระดับการป้องกัน 3 ระดับ:

- Primary prevention — ป้องกันไม่ให้เกิดโรคเลยโดยกำจัดสาเหตุ (วัคซีน ยา การให้คำปรึกษา ผ่าตัดป้องกัน) — จุดเด่นคือการแทรกแซงเดียวอาจป้องกันได้หลายโรคพร้อมกัน (เช่น เลิกบุหรี่ลดทั้งมะเร็งปอด โรคปอดอื่น และหัวใจ) การป้องกันระดับชุมชน (เช่น กฎหมายคาดเข็มขัด การเติมฟลูออไรด์ในน้ำ) ก็นับเป็น primary prevention เช่นกัน
- Secondary prevention — ตรวจพบโรคระยะไม่มีอาการแล้วรักษาก่อนลุกลาม เป็นกระบวนการ 2 ขั้นตอน (ตรวจคัดกรอง → วินิจฉัยและรักษา)
- Tertiary prevention — ลดภาวะแทรกซ้อนหลังเป็นโรคแล้ว (จริง ๆ คือ "การรักษา" ที่เน้นผลระยะยาวเป็นเดือน/ปี เช่น การควบคุมปัจจัยเสี่ยงหัวใจในผู้ป่วยเบาหวานเพิ่มเติมจากคุมน้ำตาล)
- ขอบเขตทั้งสามระดับมักซ้อนทับกันในทางปฏิบัติ (เช่น colonoscopy ใช้ได้ทั้งวินิจฉัย, secondary prevention (พบมะเร็งระยะแรก), primary prevention (ตัดติ่งเนื้อที่เป็นปัจจัยเสี่ยง), และ tertiary prevention/surveillance)
3 เกณฑ์ตัดสินว่าควรทำกิจกรรมป้องกันหรือไม่:

- ภาระของโรค (Burden of suffering) — วัดจาก 5 Ds และความถี่ของโรค — โรคที่หายากเกินไปในกลุ่มอายุนั้นไม่ควรคัดกรอง (เช่น มะเร็งเต้านมในหญิงอายุ 20 มีอุบัติการณ์เพียง 1.6/100,000 ต่างจากหญิงอายุมากกว่า 50 ที่คัดกรองคุ้มค่ากว่ามาก)
- ประสิทธิภาพของการรักษา/แทรกแซง — วัคซีนส่วนใหญ่มีหลักฐานจาก RCT ที่ชัดเจน แต่การป้องกันขั้นต้น/ขั้นรองบางอย่าง (วิตามิน อาหารเสริม การให้คำปรึกษา) มักขาด RCT ที่เข้มงวด — ตัวอย่างสำคัญ: วัคซีนตับอักเสบบีในไต้หวันลดอุบัติการณ์มะเร็งตับได้ถึง 70% ในรอบ 20 ปี (จาก observational study เพราะรอ RCT นานหลายสิบปีไม่ได้ทางจริยธรรม) หรือกรณีวัคซีนไข้หวัดใหญ่ 2009 ที่ใช้ระบบเฝ้าระวังขนาดใหญ่ (9 ล้านคน) ตรวจพบความเสี่ยง Guillain-Barré syndrome เพิ่มขึ้นเพียง 5 รายต่อล้านโดส (ต่ำกว่าวัคซีนปี 1970 มาก)
- คุณภาพของ screening test — ต้อง sensitivity/specificity สูง เรียบง่าย ราคาถูก ปลอดภัย และเป็นที่ยอมรับของผู้ป่วยและแพทย์
คุณสมบัติพิเศษของ Screening Test (ต่างจาก diagnostic test ทั่วไป):

- ใช้ detection method (นับ interval cancer ที่ตรวจไม่พบเป็น false negative) หรือ incidence method (เทียบอัตราการเกิดโรคระหว่างกลุ่มคัดกรองกับกลุ่มควบคุม) ในการคำนวณ sensitivity ซึ่งให้ผลต่างกัน โดยเฉพาะกับมะเร็งที่โตช้ามาก เช่น มะเร็งต่อมลูกหมาก
- Positive predictive value ต่ำมาก เสมอเพราะความชุกของโรคในคนไม่มีอาการต่ำ (เช่น แมมโมแกรมในหญิงอายุ 40 ต้น ๆ มี PPV เพียง 1.7% — ต้องตรวจเพิ่มถึง 57 คนถึงจะเจอมะเร็งจริง 1 คน เทียบกับหญิงอายุ 80 ที่ PPV สูงขึ้นเป็น 9.5%)
อคติสำคัญที่ทำให้ screening ดูมีประโยชน์เกินจริง (Special Biases):

- Lead-time bias — การตรวจพบเร็วขึ้นทำให้ "เวลารอดชีวิตนับจากวินิจฉัย" ยาวขึ้นโดยที่ผู้ป่วยไม่ได้อยู่นานขึ้นจริง (แค่รู้ว่าป่วยนานขึ้น) วิธีแก้คือใช้ อัตราตาย (mortality rate) เทียบกันในกลุ่มที่คัดกรองกับไม่คัดกรอง แทนที่จะใช้ survival rate — ตัวอย่างคลาสสิก: การคัดกรองมะเร็งปอดด้วย chest x-ray รอบแรก ๆ (1970-80s) ไม่ลดอัตราตายเลยเพราะ lead time ของมะเร็งปอดสั้นมาก จนกระทั่งการทดลอง CT scan ขนาดต่ำในปี 2011 จึงพิสูจน์ได้ว่าลดอัตราตายจริง 20%
- Length-time bias — การคัดกรองมีแนวโน้มตรวจพบมะเร็งที่โตช้า (พยากรณ์โรคดีอยู่แล้ว) มากกว่ามะเร็งที่โตเร็ว (ซึ่งมักแสดงอาการและถูกวินิจฉัยระหว่างรอบคัดกรองไปแล้ว) ทำให้ผลลัพธ์ในกลุ่มคัดกรองดูดีกว่าความเป็นจริง
- Compliance bias — คนที่ให้ความร่วมมือกับการตรวจ/รักษา มักมีสุขภาพและพฤติกรรมดีกว่าอยู่แล้วโดยไม่เกี่ยวกับตัวการคัดกรองเอง (ปรากฏการณ์ placebo adherence — คนที่กินยาหลอกตามนัดครบมี prognosis ดีกว่าคนไม่กินตามนัด)
- วิธีหลีกเลี่ยงอคติทั้งสามคือใช้ randomized controlled trial เปรียบเทียบกลุ่มที่ได้รับการเสนอคัดกรองกับกลุ่มควบคุม แล้วนับผลลัพธ์ทุกคนไม่ว่าจะตรวจพบด้วยวิธีใดหรือให้ความร่วมมือแค่ไหน
ผลเสียที่ไม่ได้ตั้งใจของการคัดกรอง (Unintended Consequences):

- False-positive results — พบได้บ่อยกว่าที่คิดเมื่อสะสมจากการตรวจหลายอย่างและหลายรอบ (เช่น ผู้ชายที่ตรวจคัดกรองมะเร็งต่อมลูกหมาก รังไข่ ลำไส้ และปอด รวม 14 การตรวจใน 3 ปี มีโอกาสได้ผลบวกลวงอย่างน้อย 1 ครั้งสูงถึง 60.4%) นำไปสู่การตรวจเพิ่มเติมที่ไม่จำเป็น บางครั้งถึงขั้นผ่าตัด
- Labeling effect — ผลตรวจ (แม้จะเป็น false positive) ส่งผลกระทบทางจิตใจได้มาก คนที่ผล PSA ผิดปกติแต่สุดท้ายไม่เป็นมะเร็ง ยังคงกังวลเรื่องมะเร็งต่อมลูกหมากนานถึง 1 ปีหลังตรวจ (26% เทียบกับ 6% ในกลุ่มผลปกติ)
- Overdiagnosis (Pseudodisease) — ตรวจพบมะเร็งที่โตช้ามากหรือไม่ลุกลามเลย ซึ่งไม่มีวันก่อปัญหาต่อผู้ป่วยหากไม่ตรวจพบ ถือเป็น length-time bias ขั้นรุนแรง — ประมาณกันว่ามะเร็งต่อมลูกหมากที่ตรวจพบจากการคัดกรองสูงถึง 50% เป็น overdiagnosis — ตัวอย่างสำคัญ: การคัดกรอง neuroblastoma ในทารกด้วยปัสสาวะ พบว่าอุบัติการณ์เพิ่มเป็น 2 เท่าในกลุ่มคัดกรอง แต่อัตราตายไม่ต่างจากกลุ่มไม่คัดกรองเลย — แสดงว่าเป็น overdiagnosis ล้วน ๆ ไม่ได้ช่วยชีวิตเพิ่ม
- Incidentaloma — การตรวจด้วยเทคโนโลยีภาพ (เช่น CT) มักเห็นสิ่งผิดปกติที่ไม่เกี่ยวกับเป้าหมายเดิมโดยบังเอิญ นำไปสู่การตรวจต่อเนื่องที่ไม่จำเป็น
การชั่งน้ำหนักประโยชน์กับโทษ: ใช้การเปรียบเทียบตัวเลขสัมบูรณ์ (ไม่ใช่ relative risk) ของประโยชน์กับโทษอย่างตรงไปตรงมา หรือใช้แบบจำลอง Cost-effectiveness analysis ที่แปลงทั้งประโยชน์และโทษเป็นหน่วยเดียวกัน เช่น QALY (Quality-Adjusted Life Year) เพื่อเปรียบเทียบความคุ้มค่าระหว่างกิจกรรมป้องกันต่าง ๆ (ตัวอย่าง: การฉีดวัคซีน HPV ร่วมกับตรวจ Pap smear มีต้นทุนประมาณ 57,400-58,500 ดอลลาร์ต่อ QALY ซึ่งอยู่ในเกณฑ์ที่ยอมรับได้ในสหรัฐฯ ที่ ~50,000 ดอลลาร์ต่อ QALY) — ข้อควรระวัง: การป้องกันไม่ได้ "ประหยัดเงิน" เสมอไป อย่างที่มักเข้าใจกัน ส่วนใหญ่มีต้นทุนสุทธิ แต่ก็ยังคุ้มค่าเมื่อเทียบกับกิจกรรมทางการแพทย์อื่น ๆ


#### บทที่ 11: โอกาส (Chance)

สองแนวทางจัดการกับ Chance:

- Hypothesis testing — ถามว่ามีความแตกต่างหรือไม่ (ใช้ P value) ให้ข้อสรุปแบบ dichotomous (มี/ไม่มีผลต่างอย่างมีนัยสำคัญ)
- Estimation — ประมาณ "ช่วง" ของค่าจริงที่เป็นไปได้ (confidence interval) — เป็นที่นิยมมากขึ้นในปัจจุบันเพราะให้ข้อมูลมากกว่า
Type I (α) และ Type II (β) Error: เปรียบเทียบได้กับ false positive/negative ของการตรวจวินิจฉัย

- Type I error (α) — สรุปว่า "มีผลต่าง" ทั้งที่จริง ๆ ไม่มี (false positive) — ตามธรรมเนียมกำหนดไว้ที่ 0.05 (1 ใน 20)
- Type II error (β) — สรุปว่า "ไม่มีผลต่าง" ทั้งที่จริง ๆ มี (false negative) — ตามธรรมเนียมกำหนดไว้ที่ 0.20 (1 ใน 5) ซึ่งสูงกว่า α มาก สะท้อนว่าสังคมให้ความสำคัญกับการ "มั่นใจว่ามีผลจริง" มากกว่า "มั่นใจว่าไม่มีผลจริง"
P value คืออะไรกันแน่: เป็นความน่าจะเป็นที่ผลต่างที่สังเกตได้ (หรือมากกว่า) จะเกิดขึ้นได้ โดยบังเอิญล้วน ๆ ถ้าสมมติว่าจริง ๆ แล้วไม่มีผลต่างเลย (null hypothesis) — จุดตัด P≤0.05 เป็นเพียงธรรมเนียมปฏิบัติที่กำหนดเองตามอำเภอใจ ไม่ใช่กฎธรรมชาติ — ข้อควรระวังสำคัญที่สุด: นัยสำคัญทางสถิติ (statistical significance) ไม่เท่ากับความสำคัญทางคลินิก (clinical importance) ตัวอย่างคลาสสิก: ยา donepezil รักษาอัลไซเมอร์ให้ผล P<0.0001 (นัยสำคัญทางสถิติสูงมาก) แต่ขนาดผลต่างจริงเล็กน้อยมาก (0.8 จาก 30 คะแนน) จนสรุปได้ว่า "ประโยชน์ต่ำกว่าเกณฑ์ที่มีความหมายทางคลินิก" — ในทางกลับกัน การศึกษาที่มีผู้ป่วยน้อยอาจได้ P value ที่ไม่น่าประทับใจ แม้จะมีผลการรักษาที่แข็งแรงจริงก็ตาม

การคำนวณสถิติทดสอบ: ตัวอย่างการคำนวณ chi-square (χ²) เปรียบเทียบสัดส่วนระหว่างกลุ่ม โดยเทียบค่าที่สังเกตได้กับค่าที่คาดหวังถ้าไม่มีผลต่างจริง — มีสถิติทดสอบหลายแบบตามชนิดข้อมูล (chi-square/Fisher's exact สำหรับสัดส่วน, t-test/F-test สำหรับค่าเฉลี่ย, logistic regression/Cox proportional hazards สำหรับแบบจำลองหลายตัวแปร)

Statistical Power และการกำหนดขนาดตัวอย่าง: Power = 1-β คือความน่าจะเป็นที่การศึกษาจะตรวจพบความแตกต่างที่มีอยู่จริงได้สำเร็จ (เปรียบได้กับ sensitivity ของการทดสอบ) — ปัจจัยที่กำหนดขนาดตัวอย่างที่เพียงพอ ได้แก่ (1) ขนาดผลต่างที่ต้องการตรวจจับ — ยิ่งเล็กยิ่งต้องใช้ตัวอย่างมาก (2) α ที่ยอมรับได้ (3) β ที่ยอมรับได้ (4) อัตราการเกิดเหตุการณ์พื้นฐาน — หัวใจสำคัญ: จำนวน "เหตุการณ์" (เช่น การตาย) ที่เกิดขึ้นสำคัญกว่าจำนวนผู้ป่วยทั้งหมดที่เข้าร่วม (การศึกษา 100 คนที่มี 50 คนตาย ให้ความไวทางสถิติใกล้เคียงกับการศึกษา 1,000 คนที่มี 50 คนตายเช่นกัน) — ตัวอย่างประวัติศาสตร์ที่งดงาม: การทดลองของ James Lind ปี 1747 รักษาโรคลักปิดลักเปิดด้วยกลุ่มตัวอย่างเพียง 12 คน (2 คนต่อกลุ่ม) แต่ผลชัดเจนมากจนมีนัยสำคัญทางสถิติ (P=0.02) เพราะขนาดผลต่างใหญ่มาก — ตรงข้ามกับการศึกษาวิตามินดีกับมะเร็งลำไส้ใหญ่ที่ใช้คนถึง 29,133 คน แต่ก็ยังไม่มีนัยสำคัญทางสถิติเพราะขนาดผลต่างที่แท้จริงอาจเล็กมาก

Point Estimate และ Confidence Interval: ค่าที่วัดได้จากการศึกษา (เช่น relative risk) เป็นเพียง point estimate ซึ่งไม่ใช่ค่าจริงเป๊ะ — 95% confidence interval (CI) คือช่วงที่มีโอกาส 95% ที่จะครอบคลุมค่าจริง (ถ้าการศึกษาไม่มี bias) — ยิ่ง CI แคบยิ่งแม่นยำ ข้อดีของ CI เหนือ P value คือเน้นที่ "ขนาด" ของผลมากกว่าแค่ "มี/ไม่มี" ผล และบอกได้ว่าการศึกษา "ทรงพลัง" พอจะตัดความเป็นไปได้ที่มีความหมายทางคลินิกออกได้หรือไม่ (ตัวอย่าง: การศึกษา Women's Health Initiative พบ CI ของความเสี่ยงมะเร็งเยื่อบุโพรงมดลูกกว้างมากจนตัดทั้งความเสี่ยงสูงและประโยชน์มากไม่ได้เลย แสดงว่าการศึกษาให้ข้อมูลไม่เพียงพอสำหรับผลลัพธ์นี้) — ถ้าค่าที่แปลว่า "ไม่มีผล" (RR=1 หรือผลต่าง=0) อยู่นอกช่วง CI 95% แปลว่ามีนัยสำคัญทางสถิติที่ P≤0.05

Multiple Comparisons — กับดักสำคัญ: ยิ่งทำการเปรียบเทียบหลายครั้งในข้อมูลชุดเดียว (หลาย subgroup หลายผลลัพธ์) ยิ่งมีโอกาสพบผลที่ "มีนัยสำคัญทางสถิติ" โดยบังเอิญมากขึ้นเรื่อย ๆ (ถ้าเปรียบเทียบ 20 ครั้ง คาดว่าจะพบ 1 ครั้งที่ "มีนัยสำคัญ" แม้ไม่มีความสัมพันธ์จริงในธรรมชาติเลยก็ตาม) — สำนวนที่จำง่าย: "ถ้าทรมานข้อมูลนานพอ ข้อมูลจะสารภาพเอง" — ข้อควรระวังพิเศษ: subgroup analysis แม้มีประโยชน์ในการค้นหา effect modification แต่ก็เสี่ยงต่อ false-positive จาก multiple comparisons สูงมาก (แต่ละ subgroup มีขนาดตัวอย่างเล็กลง ยิ่งเพิ่มความเสี่ยง false-negative ด้วย) — เกณฑ์ตัดสินว่าผลใน subgroup "จริง" หรือไม่ ให้พิจารณา: ขนาดผลมีความหมายทางคลินิกไหม ตั้งสมมติฐานไว้ก่อนหรือมาอธิบายทีหลัง เป็นส่วนหนึ่งของสมมติฐานจำนวนน้อยที่ตั้งไว้แต่แรกหรือไม่ และผลสอดคล้องกับการศึกษาอื่นหรือไม่

Multivariable Modeling: ใช้จัดการผลของหลายตัวแปรพร้อมกันเมื่อ stratified analysis ไม่พอ (ข้อมูลไม่พอในแต่ละ stratum) — มีประโยชน์มากแต่เป็น "black box" ที่ตรวจสอบความถูกต้องยาก ผลลัพธ์ไวต่อ "ความเพี้ยน" ของข้อมูลตัวอย่าง (โมเดลเดียวกันอาจเลือกตัวแปรทำนายต่างกันเมื่อรันบนกลุ่มตัวอย่างสุ่มที่ต่างกันจากชุดข้อมูลเดียวกัน) จึงควรตรวจสอบผลด้วยชุดข้อมูลอิสระอื่น (validation) และเทียบกับความเป็นไปได้ทางชีววิทยาเสมอ

Bayesian Reasoning: แนวคิดทางเลือกที่เริ่มจาก "ความเชื่อก่อนหน้า (prior belief)" แล้วถามว่าผลการศึกษาใหม่เปลี่ยนความเชื่อนั้นไปมากแค่ไหน (คล้ายหลักการ pretest/posttest probability ในบทที่ 8) — จุดแข็งคือสะท้อนความจริงที่ว่าไม่มีการศึกษาใดเกิดขึ้นในสุญญากาศของความรู้ — แต่ในทางปฏิบัติยากที่จะกำหนดตัวเลขให้ "ความเชื่อก่อนหน้า" ได้ชัดเจน ยกเว้นในบริบทเฉพาะ เช่น การรวบรวมหลักฐานสะสม (systematic review) และการวินิจฉัยโรค


#### บทที่ 12: สาเหตุ (Cause)

ประเด็นตั้งต้น — อคติทางประวัติศาสตร์: การตัดสินความน่าเชื่อถือของข้อกล่าวอ้างเชิงสาเหตุมักถูกตัดสินด้วยว่า "ฟังดูสมเหตุสมผล" ตามความเชื่อยุคนั้นหรือไม่ — ตัวอย่างเตือนใจ: Oliver Wendell Holmes และ Ignaz Semmelweis เสนอว่าไข้หลังคลอด (puerperal fever) แพร่จากมือแพทย์ที่ไม่ล้างมือ แต่ถูกปฏิเสธนานหลายทศวรรษเพราะยังไม่มีทฤษฎีเชื้อโรค (germ theory) มารองรับ — เช่นเดียวกับการค้นพบว่า H. pylori ก่อแผลในกระเพาะ ที่ถูกตั้งข้อสงสัยในยุค 1990 เพราะ "ทุกคนรู้ว่าแผลในกระเพาะไม่ใช่โรคติดเชื้อ"

Koch's Postulates: หลักการดั้งเดิมสำหรับพิสูจน์ว่าเชื้อโรคเป็นสาเหตุ (ต้องพบเชื้อในทุกเคส แยกเพาะเลี้ยงได้ ทำให้เกิดโรคเมื่อฉีดเข้าสัตว์ทดลอง แล้วแยกเชื้อกลับมาได้อีก) — ตั้งอยู่บนสมมติฐาน "หนึ่งสาเหตุ หนึ่งโรค" ซึ่งใช้ได้ดีกับโรคติดเชื้อบางชนิด แต่เกินความจริงไปมากสำหรับโรคส่วนใหญ่

Multiple Causes และ Web of Causation: โรคส่วนใหญ่มีหลายสาเหตุร่วมกันเป็น "ใยแห่งสาเหตุ (web of causation)" — แม้แต่โรคติดเชื้ออย่างวัณโรคก็ต้องอาศัยทั้งการสัมผัสเชื้อ ความไวต่อการติดเชื้อ (ภาวะทุพโภชนาการ ภูมิคุ้มกัน) และปัจจัยทางสังคม — เมื่อหลายปัจจัยรวมกัน ผลรวมอาจมากกว่าผลรวมของแต่ละปัจจัยแยกกัน (effect modification/interaction) เช่น ความเสี่ยงโรคหัวใจ 10 ปีในชาย 60 ปีที่มีทั้งคอเลสเตอรอลสูง HDL ต่ำ สูบบุหรี่ ความดันสูง และเบาหวานรวมกัน สูงกว่าผลรวมของแต่ละปัจจัยเดี่ยว ๆ เกือบ 10 เท่า — ในทางปฏิบัติ แพทย์มักสนใจสาเหตุที่แก้ไขได้ (เช่น ความดัน คอเลสเตอรอล) มากกว่าสาเหตุที่แก้ไม่ได้ (อายุ เพศ) แม้ทั้งสองจะมีน้ำหนักพอ ๆ กันทางสถิติ

ความใกล้ของสาเหตุกับผล (Proximal vs. Distal Causes): วัณโรคเป็นตัวอย่างที่ดี — สาเหตุใกล้ตัว (proximal) คือการติดเชื้อ Mycobacterium tuberculosis ในเนื้อเยื่อ ส่วนสาเหตุไกลตัว (distal) คือความแออัด ทุพโภชนาการ การขาดวัคซีน — ข้อมูลทางประวัติศาสตร์ที่น่าทึ่งคือ อัตราตายจากวัณโรคในอังกฤษลดลงอย่างมากก่อนที่จะค้นพบเชื้อวัณโรคด้วยซ้ำ และก่อนมียาปฏิชีวนะเป็นศตวรรษ สะท้อนว่าปัจจัยทางสังคม-เศรษฐกิจ (สาเหตุไกลตัว) มีบทบาทมากกว่าที่แพทย์ที่มุ่งเน้นกลไกโรคระดับโมเลกุลมักคาดไม่ถึง — และในช่วงปี 1985-1992 วัณโรคในสหรัฐฯ กลับเพิ่มขึ้นอีกครั้งเพราะการอพยพ โรคเอดส์ที่ทำให้ภูมิคุ้มกันอ่อนแอ และเชื้อดื้อยาหลายขนาน แสดงว่า "ใยแห่งสาเหตุ" เปลี่ยนแปลงตลอดเวลา

หลักฐานทางตรง — วิเคราะห์ทีละงานวิจัย: ต้องตัดความเป็นไปได้เรื่อง bias, chance, และ confounding ออกก่อนจึงจะสรุปเป็นสาเหตุได้ — ลำดับขั้นความน่าเชื่อถือของรูปแบบงานวิจัย (hierarchy): Systematic review ของ RCT > RCT เดี่ยว > Cohort study > Case-control study > Cross-sectional study > Case series > ประสบการณ์ส่วนตัว/ความเห็นผู้เชี่ยวชาญ — แต่หลักการนี้เป็นเพียงแนวทางคร่าว ๆ เพราะ "RCT ที่ทำแย่ ให้ข้อมูลเรื่องสาเหตุน้อยกว่า cohort study ที่ทำอย่างดีเยี่ยม" — RCT มีประโยชน์ในการพิสูจน์สาเหตุได้ใน 2 สถานการณ์: (1) เมื่อทดลองรักษา "สาเหตุที่สงสัย" แล้วป้องกันโรคได้จริง (2) เมื่อพบผลข้างเคียงที่ไม่คาดคิดจากการทดลองที่ทำเพื่อจุดประสงค์อื่น (เช่น ยา rofecoxib ที่ทดลองเพื่อลดปวด กลับพบว่าเพิ่มโรคหัวใจ)

Bradford Hill Criteria — เกณฑ์พิจารณาความเป็นสาเหตุ (ใช้บุหรี่กับมะเร็งปอดเป็นตัวอย่างหลัก):

- Temporality — สาเหตุต้องเกิดก่อนผล (ดูง่ายแต่พลาดได้ในการศึกษา cross-sectional/case-control เช่น กรณี whiplash ที่พบว่าจริง ๆ แล้วความวิตกกังวล/ซึมเศร้าที่มีอยู่ก่อนอุบัติเหตุ ต่างหากที่เพิ่มโอกาสรายงานอาการปวดคอ ไม่ใช่อุบัติเหตุที่ทำให้เกิดความวิตกกังวล)
- Strength — ความสัมพันธ์ที่แรง (relative risk สูง) เป็นหลักฐานที่หนักแน่นกว่า เพราะ bias ที่ไม่รู้ตัวมักสร้าง RR ขนาดเล็กได้ง่ายกว่า RR ขนาดใหญ่มาก (เช่น บุหรี่เพิ่มความเสี่ยงมะเร็งปอด 20 เท่า เป็นหลักฐานหนักแน่นกว่าความสัมพันธ์กับมะเร็งไตที่ RR เพียง 1.5)
- Dose-response — ยิ่งสัมผัสมากยิ่งเกิดผลมาก (บุหรี่ยิ่งสูบมากยิ่งตายจากมะเร็งปอดมาก) แต่การไม่มี dose-response ก็ไม่ใช่หลักฐานคัดค้านที่หนักแน่นนัก
- Reversibility — ลดการสัมผัสแล้วความเสี่ยงลดลงตาม (เลิกบุหรี่แล้วอัตราตายมะเร็งปอดลดลงตามจำนวนปีที่เลิก)
- Consistency — พบผลเดียวกันซ้ำ ๆ ในหลายการศึกษา หลายสถานที่ หลายวิธีวิจัย
- Biologic plausibility — สอดคล้องกับความรู้ทางชีววิทยา (แต่การไม่มีคำอธิบายทางชีววิทยาไม่ได้แปลว่าความสัมพันธ์นั้นไม่จริง เพียงแต่สะท้อนข้อจำกัดความรู้ปัจจุบัน — ตัวอย่างตรงข้าม: สาร Laetrile ที่ไม่มีกลไกทางชีวภาพรองรับเลย และเมื่อทดสอบด้วย RCT จริง ๆ ก็พบว่าไม่ได้ผลจริง ยืนยันว่าความสงสัยเชิงชีววิทยานั้นถูกต้อง)
- Specificity — หนึ่งสาเหตุก่อหนึ่งผล พบได้ชัดในโรคติดเชื้อ/พันธุกรรม แต่โรคเรื้อรังส่วนใหญ่ไม่มี specificity (บุหรี่ก่อได้หลายโรค) — จึงเป็นหลักฐานสนับสนุนที่ดีถ้ามี แต่การไม่มีไม่ใช่หลักฐานคัดค้าน
- Analogy — มีตัวอย่างสาเหตุที่คล้ายกันซึ่งพิสูจน์แล้ว (สารพิษอื่นอย่างแร่ใยหิน สารหนู ยูเรเนียม ก็ก่อมะเร็งปอดได้เช่นกัน)
- การใช้เกณฑ์เหล่านี้ร่วมกันคือการใช้เหตุผลแบบ Bayesian — แต่ละหลักฐานเสริม/ลดความเชื่อว่าเป็นสาเหตุจริงไปเรื่อย ๆ ไม่มีเกณฑ์ใดเกณฑ์เดียวชี้ขาด
Aggregate Risk Studies (Ecological Studies): ใช้เมื่อวัด exposure ได้แค่ระดับ "กลุ่ม" ไม่ใช่รายบุคคล (เช่น เทียบอัตราดื่มไวน์เฉลี่ยของประเทศกับอัตราตายโรคหัวใจของประเทศ) — ปัญหาสำคัญคือ ecological fallacy (คนที่ป่วยในกลุ่มที่มีการสัมผัสสูงอาจไม่ใช่คนที่สัมผัสจริงเลย) ทำให้เป็นเพียงหลักฐานตั้งสมมติฐาน ไม่ใช่หลักฐานยืนยัน

- Time-series studies — วัดอัตราการเกิดโรคก่อน-หลังการแทรกแซง ถ้ามีจุดเปลี่ยนชัดเจนตรงกับเวลาที่แทรกแซงพอดี (และตัดปัจจัยอื่นที่เกิดพร้อมกันออกได้) จะเป็นหลักฐานที่น่าเชื่อถือ — ตัวอย่าง: แผนงาน MRSA bundle ในโรงพยาบาล VA ที่อัตราติดเชื้อลดลงชัดเจนหลังนำมาตรการมาใช้
- Multiple time-series studies — สาเหตุเดียวกันถูกนำไปใช้ในหลายกลุ่ม ณ เวลาต่างกัน แล้วดูว่าผลเกิดตามลำดับเวลาที่สอดคล้องกันหรือไม่ — ให้หลักฐานที่แข็งแรงเกือบเทียบเท่า RCT เพราะยากที่ confounding จะเกิดซ้ำในทุกที่ทุกเวลาพอดี (ตัวอย่าง: อัตราตายมะเร็งปากมดลูกในกลุ่มประเทศนอร์ดิกลดลงตามช่วงเวลาที่แต่ละประเทศเริ่มโครงการคัดกรอง Pap smear แบบทั่วประเทศ — ประเทศที่ครอบคลุมประชากรมากกว่าก็ลดอัตราตายได้มากกว่า)
Modeling เพื่อประเมินสัดส่วนสาเหตุ: ใช้แบบจำลองทางคณิตศาสตร์แยกสัดส่วนที่แต่ละปัจจัยมีส่วนในการเปลี่ยนแปลงอัตราโรค — ตัวอย่าง: การลดลงของอัตราตายมะเร็งลำไส้ใหญ่ในสหรัฐฯ (1975-2000) ถูกแยกได้ว่ามาจากการลดปัจจัยเสี่ยง 35% การคัดกรอง 53% และการรักษา 12% — มีประโยชน์ในการตอบคำถามระดับนโยบายที่กว้างเกินกว่าจะทำวิจัยเดี่ยว ๆ ได้

เครื่องมือประยุกต์ผลสู่การตัดสินใจ: Decision analysis (หาทางเลือกที่ให้ผลลัพธ์ดีที่สุดตามความน่าจะเป็น) Cost-effectiveness analysis (เทียบต้นทุนกับผลลัพธ์สุขภาพ) Cost-benefit analysis (แปลงทั้งต้นทุนและประโยชน์เป็นหน่วยเงินทั้งคู่) — ทุกแบบจำลองควรใช้ sensitivity analysis ตรวจสอบว่าข้อสรุปเปลี่ยนไปมากแค่ไหนถ้าค่าที่ป้อนเข้าไปไม่แม่นยำ


#### บทที่ 13: การสรุปรวมหลักฐาน (Summarizing the Evidence)

Narrative Review vs. Systematic Review:

- Narrative (traditional) review — ผู้เชี่ยวชาญสรุปหลักฐานและให้คำแนะนำ ครอบคลุมหัวข้อกว้าง ๆ ได้ดี (เช่น "การดูแลผู้ป่วยเบาหวานโดยรวม") แต่ข้อเสียคือขาดความโปร่งใส — ไม่รู้ว่าค้นหางานวิจัยมาอย่างไร อาจเลือกอ้างอิงเฉพาะที่สนับสนุนมุมมองของผู้เขียน (selective citation) และใช้ตัวแทนคุณภาพงานวิจัยแบบหยาบ ๆ เช่น ชื่อเสียงวารสารหรือผู้เขียน แทนการประเมินตัวงานวิจัยจริง
- Systematic review — ทบทวนหลักฐานตามแผนที่กำหนดไว้ล่วงหน้าอย่างชัดเจนทุกขั้นตอน ทำให้ผู้อ่านตรวจสอบความน่าเชื่อถือได้เอง เหมาะกับคำถามที่เฉพาะเจาะจง (ไม่ใช่กว้าง) และมีประโยชน์มากเมื่อผลการศึกษาต่าง ๆ ขัดแย้งกัน หรือสงสัยว่าการเมือง/ผลประโยชน์ทับซ้อนมีผลต่อการตีความ
องค์ประกอบของ Systematic Review (9 ขั้นตอน):

- นิยามคำถามให้ชัดเจน — ใช้กรอบ PICO (Patient, Intervention, Comparison, Outcome) หรือขยายเป็น PICOTS (เพิ่ม Time, Study design)
- ค้นหางานวิจัยที่เกี่ยวข้องทั้งหมด — ต้องค้นหลายฐานข้อมูล (MEDLINE, EMBASE, Cochrane) ร่วมกับตำรา ผู้เชี่ยวชาญ รายการอ้างอิงในบทความที่พบแล้ว และทะเบียนงานวิจัยที่ยังไม่ตีพิมพ์ — เปรียบเสมือนใช้ "การทดสอบคู่ขนานหลายตัว" เพื่อเพิ่ม sensitivity ของการค้นหา แม้จะได้ผลลัพธ์ปลอมมาปนบ้างก็ตาม
- คัดเลือกเฉพาะงานวิจัยที่เข้มแข็งทางวิทยาศาสตร์และเกี่ยวข้องทางคลินิก — มักเหลือเพียงส่วนน้อยจากทั้งหมด (ตัวอย่าง: บทความ 632 ชิ้นเกี่ยวกับ statin กับการติดเชื้อ สุดท้ายเข้าเกณฑ์เพียง 11 ชิ้น)
- ประเมินความเข้มแข็งทางวิทยาศาสตร์ของงานวิจัยที่คัดมา
- ตรวจสอบว่าคุณภาพสัมพันธ์กับผลลัพธ์หรือไม่
- สรุปเป็นรูปภาพ/ตาราง (forest plot)
- ตัดสินใจว่าควรรวมผล (meta-analysis) หรือไม่
- คำนวณขนาดผลรวมและ confidence interval (ถ้ารวมได้)
- หาสาเหตุความแตกต่างระหว่างการศึกษา (heterogeneity) ถ้ามี
Publication Bias — ปัญหาสำคัญ: งานวิจัยที่ตีพิมพ์มักเป็น "ผลบวก" มากกว่าที่ควรเป็นจริง เพราะนักวิจัยมักไม่ทำให้เสร็จ/ไม่ส่งตีพิมพ์งานวิจัยที่ผลลบ และวารสารก็ไม่ค่อยสนใจตีพิมพ์ผลลบเช่นกัน — ตรวจจับได้ด้วย Funnel Plot (พล็อตขนาดผลเทียบกับขนาด/ความแม่นยำของการศึกษา) ถ้าไม่มี publication bias รูปจะสมมาตรคล้ายกรวยคว่ำ แต่ถ้ามี bias จะเห็นช่องว่างตรงมุมล่างขวา (ขาดการศึกษาขนาดเล็กที่ผลไม่สนับสนุนการรักษา) — สาเหตุอื่นของ publication bias ยังรวมถึงการที่บริษัทผู้สนับสนุนงานวิจัยบางรายขัดขวางการตีพิมพ์ผลที่ไม่เป็นไปตามที่ต้องการ

การประเมินคุณภาพงานวิจัยที่รวบรวมมา: ใช้เกณฑ์คุณภาพจำเพาะ (allocation concealment, blinding, intention-to-treat, ขนาดตัวอย่าง) — คะแนนสรุปรวม (เช่น Jadad Scale) มีข้อจำกัดเพราะให้น้ำหนักแต่ละองค์ประกอบเท่ากันโดยไม่มีเหตุผลรองรับ ทั้งที่ในความเป็นจริงจุดอ่อนเพียงจุดเดียว (เช่น ผู้ป่วยรู้ว่าตนได้ยาอะไรเพราะยามีผลข้างเคียงเฉพาะตัว) อาจทำลายความน่าเชื่อถือทั้งการศึกษาได้ แม้ด้านอื่นจะดีเยี่ยม — ดังนั้นควรตรวจสอบรายละเอียดแต่ละการศึกษาด้วยวิจารณญาณ ไม่ใช่พึ่งคะแนนรวมเพียงอย่างเดียว

Forest Plot — เครื่องมือสรุปผลหลัก: แสดง point estimate และ confidence interval ของแต่ละการศึกษาเป็นแถว ขนาดกล่องสี่เหลี่ยมแปรผันตามน้ำหนัก (ขนาด) ของการศึกษานั้น เส้นตั้งกลางคือ "ไม่มีผล" — ข้อดีคือช่วยให้เห็น "แพทเทิร์นรวม" ได้ แม้บางการศึกษาเดี่ยว ๆ จะไม่ถึงระดับนัยสำคัญทางสถิติ (เช่น ตัวอย่าง quinine รักษาตะคริว: 6 ใน 13 การศึกษาเป็น "ผลลบ" ทางสถิติ แต่ทุกการศึกษาชี้ไปทิศทางเดียวกันสนับสนุน quinine)

Meta-analysis — การรวมผลเชิงปริมาณ:

- เงื่อนไขก่อนรวมผล: การศึกษาต้อง "คล้ายกันพอ" — ห้ามรวม "แอปเปิลกับส้ม" (ตัวอย่างเตือนใจ: การรวมผลวิตามิน/แร่ธาตุต้านอนุมูลอิสระหลายชนิดกับมะเร็งทางเดินอาหารหลายชนิดที่กลไกทางชีวภาพต่างกันโดยสิ้นเชิง แม้จะได้ผลว่า "ไม่มีผล" แต่ก็อาจเป็นเพราะความหลากหลายของคำถามวิจัยที่ถูกยัดรวมกัน ไม่ใช่เพราะไม่มีผลจริง) — ใช้การตัดสินทางคลินิกร่วมกับสถิติทดสอบ heterogeneity (แต่มักมี statistical power ต่ำเมื่อจำนวนการศึกษาน้อย)
- Patient-level meta-analysis — รวมข้อมูลรายบุคคลจากทุกการศึกษา (ไม่ใช่แค่ผลสรุป) ทรงพลังกว่าเพราะวิเคราะห์ subgroup ได้ละเอียดกว่า แต่ทำได้ยากเพราะต้องได้ข้อมูลดิบจากผู้วิจัยทุกคน
- Fixed effect model — สมมติว่าทุกการศึกษาตอบคำถามเดียวกันเป๊ะ ต่างกันแค่จากการสุ่ม (chance) ให้ CI แคบกว่า ใช้เมื่อการศึกษาคล้ายกันมาก
- Random effects model — สมมติว่าการศึกษามีความแตกต่างกันจริง (เป็น "ครอบครัว" ของคำถามที่คล้ายกัน ไม่ใช่คำถามเดียวกันเป๊ะ) ให้ CI กว้างกว่าและสมจริงกว่าเมื่อพบ heterogeneity
- Meta-regression — สำรวจว่าลักษณะใดของการศึกษา (เช่น อายุเฉลี่ย ขนาดยา) อธิบาย heterogeneity ได้ (คล้าย multivariable analysis แต่หน่วยวิเคราะห์คือ "การศึกษา" ไม่ใช่ "ผู้ป่วย" จึงเสี่ยงต่อ ecological fallacy เช่นกัน)
- Network meta-analysis — ประมาณประสิทธิผลเปรียบเทียบระหว่างการรักษาที่ไม่เคยถูกเทียบกันโดยตรงในงานวิจัยใด ๆ เลย โดยอาศัยการเชื่อมโยงผ่านตัวเปรียบเทียบร่วม (เช่น เปรียบเทียบวิธีผ่าตัดลดน้ำหนักหลายวิธีที่แต่ละวิธีถูกเทียบกับการดูแลปกติเท่านั้น แต่ไม่เคยเทียบกันเองโดยตรง)
- Cumulative meta-analysis — เรียงผลตามลำดับเวลาที่แต่ละการศึกษาตีพิมพ์ แล้วคำนวณผลรวมสะสมทุกครั้งที่มีการศึกษาใหม่เข้ามา (เป็นแนวคิดแบบ Bayesian) — ตัวอย่างสำคัญและน่าตกใจ: การวิเคราะห์สะสมของยา rofecoxib พบว่าความเสี่ยงโรคหัวใจมีนัยสำคัญทางสถิติชัดเจนตั้งแต่ปี 2000 แต่ยาถูกถอนออกจากตลาดจริงในปี 2004 — ช้ากว่าที่ควรถึง 4 ปี ถ้ามีการทำ cumulative meta-analysis อย่างต่อเนื่องตั้งแต่แรก (ปัจจุบัน Cochrane Collaboration ทำการอัปเดต meta-analysis ทุกครั้งที่มีงานวิจัยใหม่)
Systematic Review ของ Observational และ Diagnostic Studies: หลักการเดียวกันนี้ใช้ได้กับการรวมผลการศึกษาความเสี่ยง (cohort/case-control) และการศึกษาประสิทธิภาพการทดสอบวินิจฉัย (sensitivity/specificity) ไม่ใช่แค่ RCT เท่านั้น


#### บทที่ 14: การจัดการความรู้ (Knowledge Management)

นิยาม: การจัดการความรู้ คือการจัดระเบียบและใช้ความรู้อย่างมีประสิทธิภาพ ในยุคที่ข้อมูลอิเล็กทรอนิกส์เข้าถึงง่าย ความท้าทายไม่ใช่การหาข้อมูล แต่คือการคัดกรองข้อมูลที่น่าเชื่อถือออกจากข้อมูลจำนวนมหาศาลที่ด้อยคุณภาพ

หลักการพื้นฐาน:

- ทำเองหรือมอบหมาย? แพทย์ต้องมีทักษะประเมินงานวิจัยด้วยตนเองเป็นพื้นฐาน แต่ในทางปฏิบัติไม่มีเวลาพอจะทำเองทุกคำถาม จึงต้องหา "ตัวกลางที่น่าเชื่อถือ" (แหล่งข้อมูลรอง) มาช่วย
- สื่อใดก็ได้ ขอแค่มีคุณภาพ — ความน่าเชื่อถือขึ้นกับผู้เขียน ผู้ตรวจทาน (peer reviewer) และบรรณาธิการ ไม่ใช่รูปแบบสื่อ (หนังสือ vs. เว็บไซต์) แต่ในยุคที่ความรู้เปลี่ยนเร็ว ควรอิงข้อมูลอิเล็กทรอนิกส์บนอินเทอร์เน็ตเป็นหลัก เพราะปรับปรุงทันความรู้ใหม่ได้เร็วกว่าสื่อสิ่งพิมพ์
- การให้เกรดข้อมูล ช่วยให้แพทย์เข้าใจคุณค่าของข้อมูลได้เร็ว — ระบบ GRADE เป็นตัวอย่างที่ใช้กันแพร่หลาย โดยให้เกรดแยก 2 มิติ: คุณภาพหลักฐาน (A/B/C) และ ความหนักแน่นของคำแนะนำ (1=strong / 2=weak) เช่น "1A" = คำแนะนำหนักแน่นจากหลักฐานคุณภาพสูง (RCT ที่ทำดีและสอดคล้องกัน) ควรปฏิบัติตามเว้นแต่มีเหตุผลชัดเจนให้ทำต่างออกไป ในขณะที่ "2C" = คำแนะนำอ่อนจากหลักฐานคุณภาพต่ำ (observational study/ประสบการณ์ทางคลินิก) ทางเลือกอื่นอาจเหมาะสมพอ ๆ กัน
รายงานวิจัยที่บิดเบือน — Conflict of Interest: นอกเหนือจาก bias/chance ที่กล่าวมาตลอดทั้งเล่ม ยังมีอิทธิพลของมนุษย์ที่ทำให้ผลวิจัยถูกบิดเบือนได้ ได้แก่:

- ผลประโยชน์ทางการเงิน (ถือว่าทรงพลังที่สุดและตรวจจับยากที่สุด)
- ความสัมพันธ์ส่วนตัว, ความหลงใหลทางวิชาการในความคิดตนเอง, ความภักดีต่อองค์กร, และแรงจูงใจด้านความก้าวหน้าทางอาชีพ
- แสดงออกได้ตั้งแต่ระดับรุนแรงสุด (scientific misconduct — ปลอมแปลง/ลอกเลียนข้อมูล) ไปจนถึงระดับที่แนบเนียนกว่า เช่น publication bias (ไม่รายงานผลลบ) หรือการ "spin" ผลลัพธ์ให้ดูดีเกินจริง (เช่น บอกว่า P-value ต่ำมากแปลว่าผลมีความสำคัญทางคลินิก) — วิธีป้องกันในปัจจุบัน ได้แก่ การลงทะเบียน RCT ล่วงหน้าในเว็บไซต์สาธารณะก่อนเริ่มเก็บข้อมูล เพื่อตรวจสอบภายหลังได้ว่าผลที่ตีพิมพ์ตรงกับที่วางแผนไว้แต่แรกหรือไม่ และการเปิดเผยผลประโยชน์ทับซ้อนอย่างชัดเจน
การค้นหาคำตอบ ณ จุดดูแลผู้ป่วย (Point of Care / Just-in-Time Learning): การตอบคำถามทันทีขณะดูแลผู้ป่วยมีประสิทธิภาพกว่าการเลื่อนไปทีหลัง (ซึ่งมักไม่ได้ตอบเลย) เงื่อนไขที่จำเป็น: (1) เข้าถึงได้รวดเร็วภายในไม่กี่นาที (2) ทันสมัยอยู่เสมอ (3) ตรงกับสถานการณ์ผู้ป่วยเฉพาะราย (4) คัดกรองตามความเข้มแข็งทางวิทยาศาสตร์มาแล้ว (5) ใช้งานได้ตรงจุดที่ดูแลผู้ป่วยจริง

แหล่งข้อมูลสำคัญ:

- ตำราอิเล็กทรอนิกส์ เช่น UpToDate — ปรับปรุงต่อเนื่อง ผ่าน peer review เชื่อมโยงกับบทคัดย่องานวิจัยต้นฉบับ และให้เกรดคำแนะนำ
- Clinical Practice Guidelines — คำแนะนำสำหรับดูแลผู้ป่วยตามภาวะเฉพาะ ควรตรวจสอบความน่าเชื่อถือด้วยเกณฑ์ เช่น ความโปร่งใสของกระบวนการจัดทำ การเปิดเผยผลประโยชน์ทับซ้อนของสมาชิกคณะทำงาน องค์ประกอบคณะทำงานที่หลากหลายสาขา การอิง systematic review ที่มีคุณภาพ การระบุระดับความเชื่อมั่นของหลักฐานในแต่ละคำแนะนำ และการมีแผนปรับปรุงเมื่อมีหลักฐานใหม่ — guidelines เป็นเพียง "แนวทาง" ไม่ใช่ "กฎตายตัว" ต้องปรับใช้ตามวิจารณญาณทางคลินิกของแต่ละราย
- Cochrane Library — คลังรวม systematic review/meta-analysis คุณภาพสูงจากนักวิจัยอาสาสมัครทั่วโลก
- MEDLINE/PubMed — ฐานข้อมูลบรรณานุกรมทางการแพทย์ที่ใหญ่ที่สุด (~5,000 วารสาร) มีข้อจำกัดสำคัญคือให้ทั้งfalse negative (พลาดบทความที่เกี่ยวข้องจริง) และfalse positive (ได้บทความที่ไม่เกี่ยวข้องปนมาจำนวนมาก) — จากการศึกษาพบว่าแพทย์ผู้เชี่ยวชาญค้นหาบทความที่เกี่ยวข้องได้เพียง 46% และอัตราส่วนบทความที่เกี่ยวข้องต่อไม่เกี่ยวข้องเพียง 1:16 — เหมาะสำหรับค้นหาว่ามีรายงานเหตุการณ์หายากเกิดขึ้นหรือไม่ มากกว่าการค้นหาคำตอบด่วนในเวชปฏิบัติประจำวัน
การติดตามความก้าวหน้าใหม่ (Surveillance): ความรู้สำคัญกระจัดกระจายอยู่ในวารสารจำนวนมาก — ข้อมูลจาก ACP Journal Club แสดงว่าต้องอ่านวารสารถึง 4 ฉบับเพื่อพบบทความสำคัญ 50% และต้องอ่านถึง 20 ฉบับเพื่อพบ 90% ของบทความสำคัญทั้งหมดในสาขาอายุรศาสตร์ — จึงเป็นไปไม่ได้ที่แพทย์แต่ละคนจะติดตามด้วยตนเองครบถ้วน ต้องมอบหมายงานนี้ให้ตัวกลางที่น่าเชื่อถือ (เช่น วารสารสรุปที่คัดกรองบทความสำคัญ, RSS feeds, social media ในวงการวิชาการ) ซึ่งช่วยกลั่นกรองข้อมูลตามเกณฑ์ความเข้มแข็งทางวิทยาศาสตร์และความเกี่ยวข้องทางคลินิกให้แทน

จบสรุปทั้ง 14 บทของหนังสือ Clinical Epidemiology: The Essentials (5th ed.) — ครอบคลุมตั้งแต่หลักการพื้นฐานของระบาดวิทยาคลินิก การวัดความถี่และความผิดปกติของโรค หลักการประเมินความเสี่ยง (ทั้งเชิง cohort และ case-control) การพยากรณ์โรค การวินิจฉัย การรักษา การป้องกัน บทบาทของโอกาสทางสถิติ การวิเคราะห์สาเหตุ การรวบรวมหลักฐานเชิงระบบ ไปจนถึงการจัดการความรู้ทางการแพทย์ในทางปฏิบัติ

- Cumulative incidence — ติดตามกลุ่มคนขนาดคงที่ตลอดช่วงเวลา
- Incidence density (person-years) — ใช้ในประชากรพลวัต (dynamic population) ที่มีคนเข้า-ออกตลอดเวลา หน่วยเป็น "คน-ปี" ซึ่งมีข้อจำกัดคือคนที่ติดตามนานกับคนที่ติดตามสั้นถูกนำมารวมกัน อาจทำให้ตีความผิดถ้าลักษณะสองกลุ่มต่างกันอย่างเป็นระบบ (เช่น มะเร็งที่มี latency period ยาว ต้องติดตามนานพอถึงจะเห็นอุบัติการณ์เพิ่มขึ้นจริง)


## Biostatistics (Daniel 9th ed) (ID: 3d20abc4-4cc7-808a-804d-e73bd48b76b5)

Biostatistics (Daniel, 9th ed.) — สรุปเนื้อหารายบท


#### 🗺️ ภาพรวมของหนังสือ

หนังสือเล่มนี้เป็นตำราชีวสถิติมาตรฐานที่ใช้สอนหลักสูตรวิทยาศาสตร์สุขภาพทั่วโลก มีเป้าหมาย 2 อย่าง:

- สอนการจัดระเบียบและสรุปข้อมูล (descriptive statistics)
- สอนการตัดสินใจเกี่ยวกับข้อมูลชุดใหญ่จากการศึกษาข้อมูลเพียงส่วนน้อย (inferential statistics)
เนื้อหามี 14 บท ครอบคลุมตั้งแต่แนวคิดพื้นฐาน สถิติเชิงพรรณนา ความน่าจะเป็น การแจกแจงความน่าจะเป็น การแจกแจงกลุ่มตัวอย่าง การประมาณค่า การทดสอบสมมติฐาน การวิเคราะห์ความแปรปรวน การถดถอยเชิงเส้นอย่างง่ายและพหุคูณ ไคสแควร์ สถิติไร้พารามิเตอร์ และสถิติชีพ (vital statistics)


#### 📑 สารบัญ


#### 📘 บทที่ 1: บทนำสู่ชีวสถิติ (Introduction to Biostatistics)


#### 📊 บทที่ 2: สถิติเชิงพรรณนา (Descriptive Statistics)


#### 🎲 บทที่ 3: แนวคิดพื้นฐานเรื่องความน่าจะเป็น (Some Basic Probability Concepts)


#### 🔔 บทที่ 4: การแจกแจงความน่าจะเป็น (Probability Distributions)


#### 🧮 บทที่ 5: การแจกแจงกลุ่มตัวอย่างที่สำคัญ (Some Important Sampling Distributions)


#### 🎯 บทที่ 6: การประมาณค่า (Estimation)


#### 🧪 บทที่ 7: การทดสอบสมมติฐาน (Hypothesis Testing)


#### 🧬 บทที่ 8: การวิเคราะห์ความแปรปรวน (Analysis of Variance, ANOVA)


#### 📈 บทที่ 9: การถดถอยเชิงเส้นอย่างง่ายและสหสัมพันธ์ (Simple Linear Regression and Correlation)


#### 📉 บทที่ 10: การถดถอยพหุคูณและสหสัมพันธ์ (Multiple Regression and Correlation)


#### 🧩 บทที่ 11: การถดถอย — เทคนิคเพิ่มเติม (Regression Analysis: Some Additional Techniques)


#### ✖️ บทที่ 12: การแจกแจงไคสแควร์และการวิเคราะห์ความถี่ (The Chi-Square Distribution and the Analysis of Frequencies)


#### 🔀 บทที่ 13: สถิติไร้พารามิเตอร์และสถิติไม่อิงการแจกแจง (Nonparametric and Distribution-Free Statistics)


#### 🏥 บทที่ 14: สถิติชีพ (Vital Statistics)

จบสรุปทั้ง 14 บทของหนังสือ Biostatistics: A Foundation for Analysis in the Health Sciences (9th ed.) โดย Wayne W. Daniel — ครอบคลุมตั้งแต่แนวคิดพื้นฐานของสถิติ สถิติเชิงพรรณนา ความน่าจะเป็นและ Bayes' theorem การแจกแจงความน่าจะเป็นหลัก (binomial, Poisson, normal) การแจกแจงกลุ่มตัวอย่างและ Central Limit Theorem การประมาณค่าและการทดสอบสมมติฐาน การวิเคราะห์ความแปรปรวน การถดถอยเชิงเส้นทั้งอย่างง่ายและพหุคูณ (รวมถึง logistic regression) การวิเคราะห์ไคสแควร์ ความเสี่ยงสัมพัทธ์/odds ratio และ survival analysis สถิติไร้พารามิเตอร์ ไปจนถึงสถิติชีพที่ใช้ในงานสาธารณสุข

> สรุปเนื้อหาจากหนังสือ Biostatistics: A Foundation for Analysis in the Health Sciences (9th edition) โดย Wayne W. Daniel — จัดทำเป็นสรุปรายบทเพื่อการทบทวน (เรียบเรียงใหม่เป็นภาษาไทย ไม่ใช่การคัดลอกต้นฉบับ)


#### ภาพรวมของหนังสือ

หนังสือเล่มนี้เป็นตำราชีวสถิติมาตรฐานที่ใช้สอนหลักสูตรวิทยาศาสตร์สุขภาพทั่วโลก มีเป้าหมาย 2 อย่าง: (1) สอนการจัดระเบียบและสรุปข้อมูล (descriptive statistics) และ (2) สอนการตัดสินใจเกี่ยวกับข้อมูลชุดใหญ่จากการศึกษาข้อมูลเพียงส่วนน้อย (inferential statistics) เนื้อหามี 14 บท ครอบคลุมตั้งแต่แนวคิดพื้นฐาน สถิติเชิงพรรณนา ความน่าจะเป็น การแจกแจงความน่าจะเป็น การแจกแจงกลุ่มตัวอย่าง การประมาณค่า การทดสอบสมมติฐาน การวิเคราะห์ความแปรปรวน การถดถอยเชิงเส้นอย่างง่ายและพหุคูณ ไคสแควร์ สถิติไร้พารามิเตอร์ และสถิติชีพ (vital statistics)


#### บทที่ 1: บทนำสู่ชีวสถิติ (Introduction to Biostatistics)

แหล่งที่มาของข้อมูล: บันทึกประจำ (routinely kept records เช่น เวชระเบียน), การสำรวจ (surveys), การทดลอง (experiments), และแหล่งข้อมูลภายนอก (external sources เช่น งานวิจัยที่ตีพิมพ์แล้ว)

ประเภทของตัวแปร (Variables):

นิยามพื้นฐาน: สถิติ (Statistics) คือศาสตร์ที่เกี่ยวกับ (1) การเก็บ จัดระเบียบ สรุป และวิเคราะห์ข้อมูล และ (2) การอนุมาน (inference) เกี่ยวกับข้อมูลทั้งชุดจากการสังเกตเพียงบางส่วน — เมื่อข้อมูลมาจากวิทยาศาสตร์ชีวภาพและการแพทย์ เรียกว่า ชีวสถิติ (Biostatistics) หนังสือแบ่งเนื้อหาเป็น 2 ส่วนใหญ่: descriptive statistics (จัดระเบียบ/สรุปข้อมูล) และ inferential statistics (อนุมานเกี่ยวกับประชากรจากกลุ่มตัวอย่าง)

- Qualitative variable — จำแนกเป็นหมวดหมู่เท่านั้น บอกคุณลักษณะ (เช่น การวินิจฉัยโรค กลุ่มชาติพันธุ์)

#### สารบัญ (จะทยอยเพิ่มเนื้อหาแต่ละบทด้านล่างนี้ทีละบท)

- Quantitative variable — วัดค่าได้จริง บอกปริมาณ (เช่น ส่วนสูง น้ำหนัก อายุ)
- Random variable — ค่าที่เกิดจากปัจจัยสุ่ม ไม่สามารถทำนายล่วงหน้าได้แม่นยำ
- Ordinal scale — จัดลำดับได้ แต่ระยะห่างระหว่างลำดับไม่เท่ากัน/ไม่ทราบ (เช่น อาการดีขึ้นมาก/ดีขึ้น/ไม่ดีขึ้น)
- Discrete variable — มีช่องว่างระหว่างค่าที่เป็นไปได้ (เช่น จำนวนผู้ป่วยรับใหม่ต่อวัน ต้องเป็นจำนวนเต็ม)
มาตรวัด (Measurement Scales) — 4 ระดับจากต่ำไปสูง:

Population vs. Sample: Population คือกลุ่มข้อมูล/หน่วยทั้งหมดที่เราสนใจ ณ เวลาหนึ่ง (มีขนาด N) อาจเป็น finite หรือ infinite ก็ได้ ส่วน Sample คือส่วนหนึ่งของ population (มีขนาด n)

- Simple random sample — ตัวอย่างขนาด n จากประชากรขนาด N ที่ทุกชุดตัวอย่างที่เป็นไปได้ขนาด n มีโอกาสถูกเลือกเท่ากัน (นิยมสุ่มแบบไม่คืนที่ (without replacement) ในทางปฏิบัติ) — ใช้ตารางเลขสุ่ม (random number table) เป็นเครื่องมือ
การสุ่มตัวอย่างและการอนุมานทางสถิติ: Statistical inference คือกระบวนการสรุปเกี่ยวกับประชากรจากข้อมูลตัวอย่าง — เพื่อให้อนุมานได้ถูกต้อง ต้องใช้ scientific sample ไม่ใช่ตัวอย่างใดก็ได้

- Nominal scale — จำแนกเป็นหมวดหมู่ที่แยกจากกันชัดเจน ไม่มีลำดับ (เช่น ชาย-หญิง, แต่งงานแล้ว-ยังไม่แต่งงาน)
- Systematic sampling — เลือกจุดเริ่มต้นแบบสุ่ม แล้วเลือกทุก ๆ ระยะห่าง k (interval) ถัดไปเรื่อย ๆ — สะดวกกับข้อมูลที่เก็บเป็นแฟ้ม/ลำดับ (เช่น เวชระเบียน)
- Interval scale — จัดลำดับได้และรู้ระยะห่างที่แท้จริง แต่จุดศูนย์เป็นค่าที่กำหนดขึ้นเอง ไม่ใช่ศูนย์แท้ (เช่น องศาเซลเซียส/ฟาเรนไฮต์)
- Ratio scale — ระดับสูงสุด มีทั้งระยะห่างที่แท้จริงและจุดศูนย์แท้ (true zero) ทำให้เปรียบเทียบเป็นอัตราส่วนได้ (เช่น ส่วนสูง น้ำหนัก)
- Continuous variable — ไม่มีช่องว่าง รับค่าใดก็ได้ในช่วงที่กำหนด (เช่น ส่วนสูง น้ำหนัก) แม้ในทางปฏิบัติจะถูกบันทึกแบบปัดเศษก็ตาม
- การตั้งสมมติฐาน (Hypothesis) — แบ่งเป็น research hypothesis (ข้อความทั่วไป เช่น "การออกกำลังกายลดน้ำหนัก") และ statistical hypothesis (ระบุเชิงปริมาณ เช่น "น้ำหนักเฉลี่ยที่ลดลงของกลุ่มออกกำลังกายมากกว่ากลุ่มไม่ออกกำลังกาย")
- Stratified random sampling — แบ่งประชากรเป็นชั้น (strata) ที่หน่วยภายในชั้นเดียวกันคล้ายกันมากกว่าข้ามชั้น แล้วสุ่มแยกในแต่ละชั้น — ให้ความแปรปรวนต่ำกว่าการสุ่มข้ามทั้งประชากรตรง ๆ (ตัวอย่าง: สุ่มผู้ป่วยจาก trauma center แต่ละระดับ 1/2/3 แยกกัน เพราะอัตรารอดชีวิตน่าจะต่างกันตามระดับศูนย์) — มีรูปแบบย่อยคือ stratified systematic sample และ stratified sampling proportional to size (จำนวนตัวอย่างต่อชั้นแปรผันตามขนาดประชากรของชั้นนั้น เพื่อไม่ให้ชั้นเล็กถูกแทนค่าเกินจริง)
ระเบียบวิธีทางวิทยาศาสตร์ (Scientific Method) และการออกแบบการทดลอง: ประกอบด้วย 4 ขั้นตอนหลัก

- การออกแบบการทดลอง (Designing an Experiment) — การออกแบบที่ผิดพลาดเป็นสาเหตุอันดับต้น ๆ ของผลวิจัยที่ไม่ถูกต้อง ต้องคำนึงถึง accuracy (ความถูกต้อง/ตรงกับค่าจริง) และ precision (ความสม่ำเสมอ/แม่นยำในการวัดซ้ำ) ซึ่งเป็นคนละเรื่องกัน (เครื่องชั่งที่เพี้ยนคงที่ +3 ปอนด์ทุกครั้ง มี precision ดีแต่ accuracy แย่) — true experimental design ต้องมีการสุ่มแบ่งกลุ่มทดลอง (experimental/treatment group) และกลุ่มควบคุม (control group) เพื่อให้สรุปความสัมพันธ์เชิงเหตุ-ผลได้
- การสังเกต (Observation) — พบปรากฏการณ์ที่น่าสนใจ นำไปสู่คำถามวิจัย
คอมพิวเตอร์กับการวิเคราะห์ชีวสถิติ: ซอฟต์แวร์สถิติสมัยใหม่ (เช่น SPSS, SAS, R) ช่วยให้การคำนวณที่ซับซ้อนทำได้รวดเร็วและแม่นยำ ทำให้นักวิจัยทางการแพทย์เน้นการตีความผลลัพธ์และออกแบบการศึกษาที่ดีมากกว่ากังวลกับการคำนวณด้วยมือ

การจัดกลุ่มข้อมูล (Frequency Distribution): แบ่งข้อมูลเป็นช่วงชั้น (class intervals) ที่ไม่ทับซ้อนกัน — กฎทั่วไปคือควรมี 5-15 ช่วงชั้น ไม่มากไม่น้อยเกินไป มีสูตรช่วยคำนวณจำนวนช่วงชั้นที่เหมาะสมคือ Sturges' rule: k = 1 + 3.322(log₁₀n) และความกว้างช่วงชั้น w = R/k (R คือ range) แต่ท้ายที่สุดควรปรับด้วยดุลยพินิจให้อ่านง่าย (เช่น ใช้ความกว้าง 5 หรือ 10) — จากตารางความถี่สามารถคำนวณ relative frequency (สัดส่วน = ความถี่ ÷ จำนวนทั้งหมด) ซึ่งตีความได้เป็นความน่าจะเป็นเชิงประจักษ์ (empirical probability) ของค่านั้น ๆ ด้วย และมีcumulative frequency (ความถี่สะสม) ที่แสดงจำนวน/สัดส่วนที่ต่ำกว่าหรือเท่ากับค่าหนึ่ง ๆ — การแสดงข้อมูลเชิงกราฟทำได้ด้วย histogram และ frequency polygon


#### บทที่ 2: สถิติเชิงพรรณนา (Descriptive Statistics)

Statistic vs. Parameter: ค่าที่คำนวณจากตัวอย่างเรียกว่า statistic ส่วนค่าที่คำนวณจากประชากรทั้งหมดเรียกว่า parameter — เป็นความแตกต่างพื้นฐานที่ใช้ตลอดทั้งเล่ม

- ข้อสรุป (Conclusion) — ผลจากการศึกษาเดียวไม่ควรถือเป็นข้อสรุปเด็ดขาด ต้องมีการทำซ้ำ (replication) หลายครั้งก่อนจะได้รับการยอมรับทางวิทยาศาสตร์อย่างมั่นคง
Ordered Array: ขั้นแรกของการจัดระเบียบข้อมูลคือการเรียงค่าจากน้อยไปมาก (ordered array) ช่วยให้เห็นค่าต่ำสุด/สูงสุด และภาพรวมของข้อมูลได้ง่ายขึ้น

- Mode — ค่าที่พบบ่อยที่สุด อาจมีได้หลายค่าหรือไม่มีเลยก็ได้ ใช้ได้แม้กับข้อมูลเชิงคุณภาพ (เช่น การวินิจฉัยที่พบบ่อยที่สุด)
Skewness (ความเบ้): วัดความไม่สมมาตรของการกระจายข้อมูล — skewed right (positive) เมื่อหางยาวไปทางขวา (mean > mode) และ skewed left (negative) เมื่อหางยาวไปทางซ้าย (mean < mode)

- เมื่อ mean = median = mode ทั้งสามค่าเท่ากัน จะได้กราฟรูประฆังคว่ำแบบสมมาตร (เช่น normal distribution)
การวัดแนวโน้มเข้าสู่ส่วนกลาง (Measures of Central Tendency):

การวัดการกระจาย (Measures of Dispersion):

- Median — ค่ากึ่งกลางที่แบ่งข้อมูลเป็นสองส่วนเท่ากัน (ตำแหน่งที่ (n+1)/2 เมื่อเรียงค่าแล้ว) — ทนทานต่อค่าผิดปกติมากกว่า mean
- Mean (ค่าเฉลี่ยเลขคณิต) — μ = Σxᵢ/N (ประชากร) หรือ x̄ = Σxᵢ/n (ตัวอย่าง) — ข้อดี: มีค่าเดียวแน่นอน (uniqueness) คำนวณง่าย — ข้อเสีย: อ่อนไหวต่อค่าผิดปกติสุดขั้ว (extreme values) มาก (ตัวอย่าง: ค่าธรรมเนียมแพทย์ 5 คน $75,75,80,80,280 — mean=$118 ซึ่งไม่ได้เป็นตัวแทนที่ดีของข้อมูลชุดนี้เลย)
- Coefficient of Variation (C.V.) = (s/x̄)×100% — ใช้เปรียบเทียบการกระจายของข้อมูลที่มีหน่วยต่างกัน หรือค่าเฉลี่ยต่างกันมาก เพราะเป็นค่าไร้หน่วย (ตัวอย่าง: น้ำหนักผู้ชายอายุ 25 ปี mean=145 SD=10 → C.V.=6.9% เทียบกับเด็กอายุ 11 ปี mean=80 SD=10 → C.V.=12.5% แม้ SD เท่ากันแต่การกระจายสัมพัทธ์ของเด็กสูงกว่ามาก)
- Variance — วัดการกระจายรอบค่าเฉลี่ย: s² = Σ(xᵢ-x̄)²/(n-1) สำหรับตัวอย่าง (หารด้วย N สำหรับประชากร σ²) — เหตุผลที่หารด้วย n-1 ไม่ใช่ n เรียกว่า degrees of freedom — เมื่อรู้ค่าเบี่ยงเบน n-1 ค่า ค่าสุดท้ายจะถูกกำหนดโดยอัตโนมัติ (เพราะผลรวมของค่าเบี่ยงเบนทั้งหมดต้องเท่ากับศูนย์) การหารด้วย n-1 จำเป็นสำหรับให้ค่า variance ของตัวอย่างใช้งานได้ถูกต้องในขั้นตอนการอนุมานทางสถิติต่อไป
Kurtosis (ความโด่ง): วัดว่าการกระจายข้อมูล "แหลม" หรือ "แบน" เทียบกับ normal distribution — Leptokurtic (แหลมกว่าปกติ, kurtosis>0), Platykurtic (แบนกว่าปกติ, kurtosis<0), Mesokurtic (ปกติ, kurtosis=0 ตามสูตรที่ปรับลบ 3 แล้ว)

- Range = ค่าสูงสุด - ค่าต่ำสุด — ง่ายแต่ใช้ข้อมูลแค่ 2 ค่า ให้ข้อมูลน้อย
มุมมองความน่าจะเป็น 2 แบบ:

- Standard Deviation (SD) = √variance — มีหน่วยเดียวกับข้อมูลต้นฉบับ (ต่างจาก variance ที่เป็นหน่วยยกกำลังสอง)
Percentiles และ Quartiles: เปอร์เซ็นไทล์ที่ p (Pₚ) คือค่าที่ p% ของข้อมูลน้อยกว่าหรือเท่ากับค่านี้ — Q1 = เปอร์เซ็นไทล์ 25, Q2 = median = เปอร์เซ็นไทล์ 50, Q3 = เปอร์เซ็นไทล์ 75 — Interquartile Range (IQR) = Q3-Q1 สะท้อนการกระจายของข้อมูลกลาง 50% ทนทานต่อค่าผิดปกติมากกว่า range ทั้งชุด

คุณสมบัติพื้นฐาน 3 ข้อของความน่าจะเป็น (Kolmogorov's axioms):


#### บทที่ 3: แนวคิดพื้นฐานเรื่องความน่าจะเป็น (Some Basic Probability Concepts)

- P(Eᵢ) ≥ 0 เสมอ (ไม่มีความน่าจะเป็นติดลบ)
Box-and-Whisker Plot (Boxplot): เครื่องมือแสดงผลภาพที่ใช้ Q1, median, Q3 และค่าสุดขั้ว ช่วยให้เห็นภาพรวมการกระจาย ความเบ้ และค่าผิดปกติ (outliers) ได้ในกราฟเดียว

- สำหรับเหตุการณ์ที่แยกจากกัน (mutually exclusive) สองเหตุการณ์ P(Eᵢ หรือ Eⱼ) = P(Eᵢ) + P(Eⱼ)
- Subjective probability — สะท้อนความเชื่อมั่นส่วนบุคคลต่อความจริงของข้อความหนึ่ง ๆ ไม่ต้องอาศัยการทำซ้ำ ใช้ได้แม้กับเหตุการณ์ที่เกิดครั้งเดียว (เช่น "โอกาสที่จะพบวิธีรักษามะเร็งใน 10 ปีข้างหน้า") — เป็นฐานคิดของ Bayesian methods ที่ใช้ prior probability (ความเชื่อก่อนหน้า) ปรับปรุงเป็น posterior probability (ความเชื่อหลังได้ข้อมูลใหม่)
- Objective probability แบ่งเป็น (1) Classical (a priori) — คำนวณจากเหตุผลเชิงนามธรรมล้วน ๆ P(E)=m/N เมื่อมี N ผลลัพธ์ที่เกิดขึ้นได้เท่า ๆ กัน (เช่น ทอยลูกเต๋า 1 หน้าใน 6 หน้า) และ (2) Relative frequency (a posteriori) — ประมาณจากการทำซ้ำจริงจำนวนมาก P(E)≈m/n (m คือจำนวนครั้งที่เกิดเหตุการณ์ n คือจำนวนครั้งทั้งหมด)
- Conditional probability — P(A|B) = P(A∩B)/P(B) — ความน่าจะเป็นของ A "เมื่อกำหนดว่า" B เกิดขึ้นแล้ว (ตัวส่วนคือกลุ่มย่อยที่ B เกิดขึ้น ไม่ใช่ทั้งหมด)
- Marginal probability — ใช้ผลรวมชายขอบของตาราง (เช่น จำนวนคนทั้งหมดในแถว/คอลัมน์) เป็นตัวเศษ
- ผลรวมความน่าจะเป็นของเหตุการณ์ที่แยกจากกันหมด (mutually exclusive) และครอบคลุมทุกความเป็นไปได้ (exhaustive) เท่ากับ 1
- Joint probability — P(A∩B) — ความน่าจะเป็นที่ทั้ง A และ B เกิดขึ้นพร้อมกัน
Multiplication Rule: P(A∩B) = P(B)×P(A|B) = P(A)×P(B|A) — ใช้หาความน่าจะเป็นร่วมจากความน่าจะเป็นชายขอบคูณเงื่อนไข หรือย้อนกลับหาความน่าจะเป็นเงื่อนไขจากความน่าจะเป็นร่วมก็ได้

Complementary Events: P(Ā) = 1 - P(A) เพราะ A และส่วนเติมเต็ม Ā แยกจากกันโดยสมบูรณ์และครอบคลุมทุกความเป็นไปได้

ประเภทของความน่าจะเป็น:

Bayes' Theorem กับการประเมินการทดสอบคัดกรอง (Screening Tests) — หัวใจสำคัญของบทนี้:

ประเด็นสำคัญที่สุด: Sensitivity และ Specificity เป็นคุณสมบัติของตัวทดสอบเอง (ค่อนข้างคงที่) แต่ PPV และ PNV ขึ้นกับ P(D) หรือ "อัตราชุกของโรค (prevalence) ในประชากรที่ตรวจ" ด้วยเสมอ — ตัวอย่างในหนังสือ: การทดสอบคัดกรองอัลไซเมอร์ที่มี sensitivity=97%, specificity=99% ให้ PPV สูงถึง 93% เมื่อความชุกของโรคในกลุ่มอายุ 65 ปีขึ้นไปอยู่ที่ 11.3% — แต่ถ้านำการทดสอบเดียวกันไปใช้ในกลุ่มที่มีความชุกโรคต่ำมาก PPV จะลดฮวบลงทันที (สอดคล้องกับหลักการที่พบในตำราระบาดวิทยาคลินิกเช่นกัน) การคำนวณค่าเหล่านี้ให้ถูกต้องต้องแยกใช้ prevalence ของโรคจากแหล่งข้อมูลภายนอก ไม่ใช่จากอัตราส่วนตัวอย่างในการศึกษาวิจัยสองกลุ่มที่สุ่มมาแยกกัน (กลุ่มมีโรค vs. กลุ่มไม่มีโรค) เพราะอัตราส่วนนั้นถูกกำหนดโดยผู้วิจัยเอง ไม่ใช่อัตราชุกที่แท้จริงในธรรมชาติ

- Specificity = P(T̄|D̄) = d/(b+d) — ความน่าจะเป็นที่ผลตรวจเป็นลบ เมื่อไม่มีโรคจริง
- Predictive Value Positive (PPV) = P(D|T) — ความน่าจะเป็นที่มีโรคจริง เมื่อผลตรวจเป็นบวก — คำนวณด้วย Bayes' theorem:
- Predictive Value Negative (PNV) = P(D̄|T̄) — ความน่าจะเป็นที่ไม่มีโรคจริง เมื่อผลตรวจเป็นลบ — คำนวณด้วยสูตรคล้ายกัน
1) Binomial Distribution — การแจกแจงทวินาม: เกิดจาก Bernoulli trial (การทดลองที่ผลลัพธ์มีแค่ 2 แบบ "สำเร็จ/ล้มเหลว") ที่ทำซ้ำภายใต้เงื่อนไข Bernoulli process: (1) แต่ละครั้งมีผลแค่ 2 แบบ (2) ความน่าจะเป็นสำเร็จ p คงที่ทุกครั้ง (3) แต่ละครั้งเป็นอิสระต่อกัน — สูตร:

Probability Distribution ของตัวแปรไม่ต่อเนื่อง (Discrete): คือตาราง/กราฟ/สูตรที่ระบุค่าที่เป็นไปได้ทั้งหมดของตัวแปรสุ่ม พร้อมความน่าจะเป็นของแต่ละค่า p(x)=P(X=x) — คุณสมบัติสำคัญ 2 ข้อ: (1) 0≤P(X=x)≤1 เสมอ (2) ผลรวมของทุกความน่าจะเป็นเท่ากับ 1 — Cumulative distribution F(x)=P(X≤x) ได้จากการบวกสะสมความน่าจะเป็นทีละค่า กราฟเรียกว่า ogive — ค่าเฉลี่ยและความแปรปรวนของการแจกแจงคำนวณจาก μ=Σxp(x) และ σ²=Σx²p(x)-μ²

Addition Rule: P(A∪B) = P(A) + P(B) - P(A∩B) — ใช้เมื่อ A กับ B ไม่ได้แยกจากกันเด็ดขาด (อาจเกิดร่วมกันได้) ต้องลบส่วนที่นับซ้ำ (intersection) ออกหนึ่งครั้ง — ถ้า A กับ B แยกจากกันจริง (mutually exclusive) พจน์ P(A∩B) จะเป็น 0

Independent Events (เหตุการณ์อิสระต่อกัน): A และ B เป็นอิสระต่อกันถ้า P(A|B) = P(A) (การรู้ว่า B เกิดขึ้นไม่เปลี่ยนความน่าจะเป็นของ A) ในกรณีนี้ P(A∩B) = P(A)×P(B) — ข้อควรระวัง: "อิสระต่อกัน (independent)" กับ "แยกจากกัน (mutually exclusive)" เป็นคนละแนวคิด ไม่ใช่ความหมายเดียวกัน

เมื่อมีผลตรวจ (Test, T) เทียบกับสถานะโรคจริง (Disease, D) จัดเป็นตาราง 2×2 (บวก/ลบ × มี/ไม่มีโรค) สามารถคำนวณได้ 4 ค่า:

> f(x) = ₙCₓ pˣ qⁿ⁻ˣ, x=0,1,...,n (โดย q=1-p)

- Sensitivity = P(T|D) = a/(a+c) — ความน่าจะเป็นที่ผลตรวจเป็นบวก เมื่อมีโรคจริง
> f(x) = e⁻λλˣ/x!, x=0,1,2,...

โดย ₙCₓ = n!/[x!(n-x)!] คือจำนวนวิธีจัดลำดับที่แตกต่างกัน (combination) — Mean = np, Variance = np(1-p) — ใช้ตอบคำถามประเภท "โอกาสที่จะพบผู้ป่วยพอดี x คนจาก n คนที่มีลักษณะหนึ่ง ๆ" (เช่น ทารกคลอดครบกำหนด, ผู้ป่วยความดันสูง) — มีตารางความน่าจะเป็นสะสมสำเร็จรูปช่วยลดการคำนวณมือ

2) Poisson Distribution — การแจกแจงปัวซง: ใช้กับการนับ "จำนวนเหตุการณ์ที่เกิดขึ้นในช่วงเวลา/พื้นที่หนึ่ง ๆ" สูตร:


#### บทที่ 4: การแจกแจงความน่าจะเป็น (Probability Distributions)

3) Continuous Probability Distributions: เมื่อข้อมูลมีจำนวนมากและช่วงชั้นแคบลงเรื่อย ๆ histogram จะเปลี่ยนเป็นเส้นโค้งเรียบ (smooth curve) เรียกว่า probability density function (pdf) — พื้นที่ใต้เส้นโค้งทั้งหมดเท่ากับ 1 และพื้นที่ระหว่างจุด a กับ b คือ P(a<X<b) — ความน่าจะเป็นที่ตัวแปรต่อเนื่องจะมีค่าใดค่าหนึ่งพอดี (จุดเดียว) เท่ากับ 0 เสมอ เพราะพื้นที่เหนือจุดหนึ่งจุดบนแกน x เท่ากับศูนย์

4) Normal (Gaussian) Distribution — การแจกแจงปกติ — สำคัญที่สุดในวิชาสถิติทั้งหมด:

โดย λ (lambda) คือค่าเฉลี่ยจำนวนครั้งที่เกิดเหตุการณ์ในช่วงที่กำหนด — เงื่อนไขของ Poisson process: (1) เหตุการณ์เกิดอิสระต่อกัน (2) เกิดได้ไม่จำกัดจำนวนในทางทฤษฎี (3) ความน่าจะเป็นแปรผันตรงกับความยาวของช่วง (4) โอกาสเกิด 2 เหตุการณ์พร้อมกันในช่วงเล็กจิ๋วนั้นน้อยมากจนตัดทิ้งได้ — คุณสมบัติพิเศษ: Mean = Variance = λ — ใช้บ่อยในทางการแพทย์กับอัตราการเกิดโรค/ภาวะแทรกซ้อนที่หายาก (เช่น จำนวนผู้ป่วยแพ้ยารุนแรงต่อปี) และยังใช้ประมาณค่า Binomial distribution เมื่อ n มากและ p น้อย (โดยตั้ง λ=np)

สูตร: f(x) = [1/(σ√2π)]·e^{-(x-μ)²/2σ²} กำหนดโดย 2 พารามิเตอร์: μ (mean, location parameter — กำหนดตำแหน่งกึ่งกลาง) และ σ (SD, shape parameter — กำหนดความกว้าง/แคบ)

- mean = median = mode
- กฎ 68-95-99.7: พื้นที่ในช่วง μ±1σ ≈ 68%, μ±2σ ≈ 95%, μ±3σ ≈ 99.7% ของข้อมูลทั้งหมด
คุณสมบัติสำคัญของ Normal Distribution:

ค่า z บอกว่า x อยู่ห่างจากค่าเฉลี่ยกี่ SD (z บวก = อยู่เหนือค่าเฉลี่ย, z ลบ = อยู่ใต้ค่าเฉลี่ย) — ใช้ตาราง Standard Normal (Appendix Table D) หาพื้นที่ใต้กราฟ/ความน่าจะเป็นได้โดยไม่ต้องคำนวณอินทิกรัลเอง — เป็นเครื่องมือพื้นฐานที่ใช้ตลอดทั้งเล่มสำหรับการประมาณค่า (estimation) และการทดสอบสมมติฐาน (hypothesis testing) ในบทถัดไป

- สมมาตรรอบค่าเฉลี่ย μ (ครึ่งซ้าย = กระจกเงาของครึ่งขวา)
- เป็น "ตระกูล" ของการแจกแจง — ค่า μ ต่างกันทำให้กราฟเลื่อนตำแหน่ง ค่า σ ต่างกันทำให้กราฟแบน/แหลมต่างกัน
- พื้นที่ใต้กราฟทั้งหมด = 1 (แบ่งครึ่งซ้าย-ขวาข้างละ 50%)
- หลักการสำคัญ: ต้องควบคุมความเสี่ยง Type I error ที่สะสมจากการทดสอบหลายคู่ ไม่ใช่ทำ t-test แยกทีละคู่ตามใจโดยไม่ปรับค่า α

#### บทที่ 5: การแจกแจงกลุ่มตัวอย่างที่สำคัญ (Some Important Sampling Distributions)

นิยาม Sampling Distribution: การแจกแจงของค่าที่เป็นไปได้ทั้งหมด ของสถิติหนึ่ง ๆ (เช่น mean, proportion) ที่คำนวณจากตัวอย่างขนาดเดียวกันทุกชุดที่สุ่มได้จากประชากรเดียวกัน — เป็นแนวคิดหัวใจสำคัญที่สุดของการอนุมานทางสถิติทั้งเล่ม เพราะช่วยให้ (1) ตอบคำถามความน่าจะเป็นเกี่ยวกับค่าสถิติของตัวอย่างได้ และ (2) เป็นรากฐานทางทฤษฎีที่ทำให้กระบวนการอนุมานทางสถิติสมเหตุสมผล

- Bonferroni's Method — แบ่งค่า α โดยจำนวนคู่ที่ทดสอบทั้งหมด (α/k) เพื่อควบคุม overall Type I error ไม่ให้เกิน α ที่ตั้งไว้ (เช่น ถ้ามี 3 คู่ทดสอบและ α=.05 → ใช้เกณฑ์ α/3=.017 ต่อการทดสอบแต่ละคู่) — เป็นวิธีที่ตรงไปตรงมาแต่ระมัดระวังมากเกินไป (conservative) เมื่อจำนวนคู่ทดสอบมาก
> ไม่ว่าประชากรต้นทางจะมีรูปแบบการแจกแจงอย่างไรก็ตาม (มี mean=μ, variance=σ² จำกัด) การแจกแจงของ x̄ จากตัวอย่างขนาด n จะมี mean=μ, variance=σ²/n และเข้าใกล้การแจกแจงแบบปกติมากขึ้นเรื่อย ๆ เมื่อ n มีขนาดใหญ่ขึ้น

Standard Normal Distribution (Z-distribution): สมาชิกพิเศษของตระกูล Normal ที่มี μ=0, σ=1 — แปลงค่าตัวแปรใด ๆ ให้เป็นมาตรฐานด้วยสูตร z-transformation:

2) Randomized Complete Block Design (RCBD) — Two-Way ANOVA: พัฒนาโดย R.A. Fisher เพื่องานวิจัยเกษตรกรรม — แบ่งหน่วยทดลองเป็น blocks (กลุ่มที่คล้ายกันภายในบล็อก) แล้วสุ่มทรีตเมนต์ภายในแต่ละบล็อก — แต่ละทรีตเมนต์ต้องปรากฏในทุกบล็อก

> z = (x - μ)/σ

1) Sampling Distribution ของค่าเฉลี่ยตัวอย่าง (x̄):

วัตถุประสงค์: แยก "ความแปรปรวนจากบล็อก" ออกจาก error term ทำให้ error mean square เล็กลง และ F ratio เพิ่มขึ้น → เพิ่มโอกาสตรวจพบความแตกต่างของทรีตเมนต์ได้ (power สูงขึ้น) — ตัวอย่างการ block: ใช้สายพันธุ์สัตว์เป็น block, ใช้ครอกเดียวกันเป็น block, จัดกลุ่มอายุคนเป็น block

หมายเหตุสำคัญ: Paired comparisons test (บทที่ 7) ที่จริงแล้วเป็นกรณีพิเศษของ RCBD ที่มีเพียง 2 ทรีตเมนต์ โดยผู้ป่วยแต่ละคนทำหน้าที่เป็น "block"

- ถ้าสุ่มจากประชากรที่ไม่ใช่การแจกแจงปกติ (หรือไม่ทราบรูปแบบ) → ต้องอาศัย Central Limit Theorem (ทฤษฎีบทลิมิตกลาง) — หัวใจสำคัญที่สุดของบทนี้:
Model: xᵢⱼ = μ + βᵢ + τⱼ + εᵢⱼ (เพิ่ม βᵢ = block effect เข้ามาจาก CRD model) — ข้อสมมติเพิ่มเติมสำคัญ: block effect กับ treatment effect ต้อง "additive" (ไม่มี interaction ระหว่างบล็อกกับทรีตเมนต์)

Standard Error of the Mean = σ/√n คือรากที่สองของ variance ของ sampling distribution — ยิ่ง n มากขึ้น standard error ยิ่งเล็กลง (การประมาณค่าเฉลี่ยประชากรแม่นยำขึ้น)

การสุ่มแบบไม่คืนที่จากประชากรจำกัด (Finite Population Correction): เมื่อสุ่มโดยไม่คืนที่จากประชากรที่มีขนาดจำกัด N ต้องคูณ variance ด้วย finite population correction factor = (N-n)/(N-1):

4) Factorial Experiment: ศึกษาผลของปัจจัย (factors) ตั้งแต่ 2 ตัวขึ้นไปพร้อมกัน — แต่ละปัจจัยมี levels (ระดับ) ของตัวเอง (เช่น ปัจจัย A=ขนาดยา 3 ระดับ, ปัจจัย B=กลุ่มอายุ 2 ระดับ) ข้อดีสำคัญคือสามารถศึกษา Interaction ระหว่างปัจจัยได้ ซึ่งการทดลองแยกทีละปัจจัยทำไม่ได้

3) Repeated Measures Design: วัดตัวแปรตามเดิมซ้ำหลายครั้งในหน่วยทดลองเดียวกัน (เช่น วัดค่าก่อน/หลังการรักษาหลายจุดเวลา) เป็นการขยาย RCBD ที่ "subject" ทำหน้าที่เป็น block — มีข้อดีคือลด variability จากความแตกต่างระหว่างบุคคล แต่ต้องระวังปัญหา correlation ระหว่างการวัดซ้ำในคนเดียวกัน

- ถ้าสุ่มจากประชากรที่มีการแจกแจงแบบปกติ (normal) อยู่แล้ว → การแจกแจงของ x̄ จะเป็นปกติเสมอ ไม่ว่าขนาดตัวอย่างจะเท่าไร โดยมี mean μₓ̄=μ (เท่ากับ mean ประชากร) และ variance σₓ̄²=σ²/n
2) Sampling Distribution ของผลต่างระหว่างค่าเฉลี่ยสองตัวอย่าง (x̄₁ - x̄₂): ใช้เมื่อต้องการเปรียบเทียบค่าเฉลี่ยของสองประชากร (เช่น เปรียบเทียบระดับคอเลสเตอรอลระหว่างคนทำงานนั่งโต๊ะกับคนใช้แรงงาน) — ถ้าสุ่มจากสองประชากรที่เป็นอิสระต่อกัน การแจกแจงของ x̄₁-x̄₂ จะมี:


#### บทที่ 9: การถดถอยเชิงเส้นอย่างง่ายและสหสัมพันธ์ (Simple Linear Regression and Correlation)

กฎง่าย ๆ ที่ใช้กันทั่วไปคือ n≥30 มักเพียงพอ ที่จะถือว่า x̄ มีการแจกแจงใกล้เคียงปกติแล้ว — ทำให้แปลงเป็น standard normal ได้ด้วยสูตร:

> z = (x̄ - μ)/(σ/√n)

โดย β₀=y-intercept, β₁=slope (ค่าพารามิเตอร์ประชากร), ε=error term

> mean = μ₁ - μ₂, variance = σ₁²/n₁ + σ₂²/n₂

เกณฑ์ที่ใช้การประมาณด้วยแบบปกติได้อย่างเหมาะสม: ทั้ง np และ n(1-p) ต้องมากกว่า 5 — สามารถปรับปรุงความแม่นยำเพิ่มเติมด้วย correction for continuity (ปรับแก้เพราะใช้การแจกแจงต่อเนื่องมาประมาณการแจกแจงไม่ต่อเนื่อง)

ในทางปฏิบัติ มักละเลย correction factor นี้เมื่อ n/N ≤ .05 (ตัวอย่างขนาดเล็กเทียบกับประชากร) เพราะผลต่างมีน้อยมาก


#### บทที่ 6: การประมาณค่า (Estimation)

- X วัดโดยไม่มีความคลาดเคลื่อน
> z = (p̂ - p) / √[p(1-p)/n]

Sampled Population vs. Target Population: Sampled population คือประชากรที่สุ่มตัวอย่างมาจริง ส่วน Target population คือประชากรที่ต้องการอนุมานถึง — การอนุมานทางสถิติใช้ได้ถูกต้องเฉพาะกับ sampled population เท่านั้น ถ้าต้องการอนุมานไปถึง target population ที่ต่างออกไป ต้องอาศัยเหตุผลเชิงเนื้อหา (non-statistical) เพิ่มเติมว่าทั้งสองประชากรคล้ายกันเพียงพอ

Interaction คืออะไร: เกิดขึ้นเมื่อผลของปัจจัยหนึ่งเปลี่ยนแปลงไปตามระดับของอีกปัจจัยหนึ่ง — ถ้าไม่มี interaction เส้นกราฟของแต่ละระดับปัจจัย (เมื่อพล็อตค่าเฉลี่ยตอบสนอง) จะขนานกัน — ถ้ามี interaction เส้นกราฟจะไม่ขนานกัน (อาจตัดกันหรือแยกออกจากกัน) — ตัวอย่าง: ถ้ายาลดเวลาปฏิกิริยาในคนหนุ่มแต่กลับเพิ่มเวลาปฏิกิริยาในคนสูงอายุ (ทิศทางผลตรงข้ามกันตามกลุ่มอายุ) นั่นคือ interaction ระหว่างยากับอายุ — การตรวจพบ interaction มีความสำคัญทางคลินิกมาก เพราะหมายความว่า "คำแนะนำที่ดีที่สุด" ขึ้นกับบริบท ไม่สามารถสรุปแบบเหมารวมได้

> σₓ̄² = (σ²/n) × [(N-n)/(N-1)]

3) Sampling Distribution ของสัดส่วนตัวอย่าง (p̂): ใช้กับตัวแปรที่เป็น dichotomous (เช่น เป็นโรค/ไม่เป็นโรค อ้วน/ไม่อ้วน) — เมื่อขนาดตัวอย่างใหญ่พอ p̂ จะมีการแจกแจงใกล้เคียงปกติ ด้วย mean=p (สัดส่วนจริงของประชากร) และ variance = p(1-p)/n = pq/n โดยที่ q=1-p — สูตร z-transformation:

> y = β₀ + β₁x + ε

สมมติฐาน 6 ข้อของ Simple Linear Regression (จำง่าย ๆ ด้วยคำย่อ "LINE"):

The Regression Model: ศึกษาความสัมพันธ์ระหว่างตัวแปรอิสระ X (independent/predictor variable) กับตัวแปรตาม Y (dependent/response variable) — สมการโมเดล:

> Estimator ± (Reliability Coefficient) × (Standard Error)

การแบ่งส่วนความแปรปรวน (Partitioning Deviations) — แนวคิดคล้าย ANOVA: สำหรับแต่ละจุดข้อมูล yᵢ:

ข้อสำคัญ: แม้ต้องการ "ผลต่าง" ของค่าเฉลี่ย แต่ variance ของทั้งสองประชากรจะถูก "บวกกันเสมอ" (ไม่ใช่ลบกัน) เพราะความแปรปรวนของทั้งสองแหล่งข้อมูลเพิ่มความไม่แน่นอนสะสมเข้าด้วยกัน — สูตร z-transformation:

- ค่า X ถูกกำหนดไว้ล่วงหน้า (fixed) ไม่ใช่ตัวแปรสุ่ม
- Point estimate — ค่าตัวเลขเดียว (เช่น x̄ เป็น point estimate ของ μ)
- สำหรับค่าเฉลี่ย: n = z²σ²/d² (เมื่อ ignore finite population correction) — ต้องมีค่าประมาณ σ ล่วงหน้าจาก pilot sample, การศึกษาก่อนหน้า, หรือประมาณคร่าว ๆ ว่า σ≈R/6 (range หารด้วย 6)
- สำหรับสัดส่วน: n = z²pq/d² — ถ้าไม่มีค่าประมาณ p มาก่อนเลย ให้ใช้ p=0.5 เพราะเป็นค่าที่ให้ n มากที่สุด (safest แต่อาจสิ้นเปลืองทรัพยากรเกินจำเป็นถ้า p จริงห่างจาก 0.5 มาก)
5) CI สำหรับ Variance ของประชากร (σ²) — ใช้ Chi-Square Distribution: ปริมาณ (n-1)s²/σ² มีการแจกแจงแบบ chi-square (χ²) ด้วย df=n-1 (เมื่อสุ่มจาก normal population) — CI สำหรับ σ²:

4) Sampling Distribution ของผลต่างระหว่างสัดส่วนสองตัวอย่าง (p̂₁-p̂₂): ใช้หลักการเดียวกับผลต่างของค่าเฉลี่ย — เมื่อขนาดตัวอย่างใหญ่พอ การแจกแจงของ p̂₁-p̂₂ ใกล้เคียงปกติ โดยมี mean=p₁-p₂ และ variance=p₁q₁/n₁+p₂q₂/n₂ — ใช้เปรียบเทียบสัดส่วนของสองกลุ่ม (เช่น อัตราการเกิดโรคระหว่างกลุ่มที่สูบบุหรี่กับไม่สูบบุหรี่)

Unbiased Estimator: ตัวประมาณค่า T เป็น unbiased ของพารามิเตอร์ θ ถ้า E(T)=θ (ค่าคาดหวังเท่ากับค่าพารามิเตอร์จริงพอดี) — x̄, p̂, และผลต่างของค่าเฉลี่ย/สัดส่วนสองกลุ่ม ล้วนเป็น unbiased estimator ของพารามิเตอร์ที่สอดคล้องกัน

Sample Regression Equation (Least-Squares Line): ŷ = b₀ + b₁x โดย b₀, b₁ เป็นตัวประมาณค่าของ β₀, β₁ จากข้อมูลตัวอย่าง — ขั้นตอนการวิเคราะห์การถดถอย: (1) ตรวจสอบสมมติฐานความเป็นเส้นตรง (2) หาสมการเส้นที่เหมาะสมที่สุด (3) ประเมินความแข็งแรงของความสัมพันธ์ (4) ใช้สมการทำนาย/ประมาณค่า

- Interval estimate (Confidence Interval) — ช่วงค่าที่มีระดับความเชื่อมั่นกำหนดว่าจะครอบคลุมพารามิเตอร์จริง
- Equal variances — variance ของทุก subpopulation ของ Y เท่ากัน (σ²)
- Independent — ค่า Y แต่ละค่าเป็นอิสระต่อกัน
Confidence Interval และการทำนาย: สมการถดถอยใช้ได้ 2 แบบ — การทำนาย (prediction) ค่า Y เดี่ยว ๆ ที่ค่า X หนึ่ง ๆ (CI กว้างกว่า) กับ การประมาณค่า (estimation) ค่าเฉลี่ยของ subpopulation Y ที่ X นั้น (CI แคบกว่า)

สูตรทั่วไปของ Confidence Interval:

ข้อควรระวังสำคัญ: เนื่องจาก chi-square distribution ไม่สมมาตร (ต่างจาก normal) จุดประมาณค่า (point estimate) จะไม่อยู่ตรงกลางของ CI และวิธีนี้ไม่ได้ให้ช่วงที่แคบที่สุดเท่าที่เป็นไปได้ นอกจากนี้ผลลัพธ์อ่อนไหวมากต่อสมมติฐานว่าประชากรมีการแจกแจงแบบ normal ถ้าไม่เป็นจริงผลอาจคลาดเคลื่อนมาก

- สำหรับแต่ละค่า X มี subpopulation ของ Y ที่มีการแจกแจงแบบ Normal
- Linearity — ค่าเฉลี่ยของทุก subpopulation ของ Y เรียงอยู่บนเส้นตรงเดียวกัน: μ_{y|x} = β₀+β₁x
การกำหนดขนาดตัวอย่าง (Sample Size Determination): หลักการคือกำหนด "ความกว้างที่ยอมรับได้ของ CI" (d = margin of error) ล่วงหน้า แล้วแก้สมการย้อนกลับหา n:

> z = [(x̄₁-x̄₂) - (μ₁-μ₂)] / √(σ₁²/n₁ + σ₂²/n₂)

> SST (Total SS) = SSR (Regression/Explained SS) + SSE (Error/Residual SS)

- t-test: t = b₁/SE(b₁) (df=n-2)
2) CI สำหรับผลต่างระหว่างค่าเฉลี่ยสองประชากร (μ₁-μ₂): (x̄₁-x̄₂) ± (reliability coeff)×√(σ₁²/n₁+σ₂²/n₂) — ถ้าช่วงที่ได้ไม่รวมค่า 0 แสดงว่าค่าเฉลี่ยสองประชากรน่าจะแตกต่างกันจริง ถ้าช่วงรวมค่า 0 แปลว่าค่าเฉลี่ยทั้งสองอาจเท่ากันได้

1) CI สำหรับค่าเฉลี่ยประชากร (μ):

Coefficient of Determination (r²):

- การทดสอบสัมประสิทธิ์แต่ละตัว (Individual t-tests): H₀: βᵢ=0 ทดสอบว่าตัวแปร Xᵢแต่ละตัวมีประโยชน์จริงหรือไม่ "เมื่อควบคุมตัวแปรอื่นในโมเดลแล้ว" ด้วย t = (β̂ᵢ-0)/SE(β̂ᵢ) (df=n-k-1)
ความหมาย: สัดส่วนของความแปรปรวนรวมใน Y ที่อธิบายได้ด้วยความสัมพันธ์เชิงเส้นกับ X — มีค่าระหว่าง 0 ถึง 1 — r²=1 หมายถึงจุดทุกจุดอยู่บนเส้นพอดี (ไม่มี error เลย) — r²=0 หมายถึงเส้นถดถอยไม่ได้ช่วยอธิบายอะไรเลยเมื่อเทียบกับการใช้ค่าเฉลี่ย ȳ อย่างเดียว (ตัวอย่างจากหนังสือ: r²=.67 หมายความว่าเส้นรอบเอวอธิบายความแปรปรวนของไขมันหน้าท้องได้ 67%)

- "สหสัมพันธ์ไม่ใช่สาเหตุ (correlation is not causation)" — พบ r ที่มีนัยสำคัญทางสถิติอาจหมายถึง: (a) X ก่อ Y จริง (b) Y ก่อ X จริง (c) ตัวแปรที่สามเป็นสาเหตุร่วมของทั้งคู่ (confounding) (d) เกิดจากความบังเอิญทางสถิติ (e) ความสัมพันธ์ไร้ความหมายเพราะวัดจากหน่วยที่ไม่เกี่ยวข้องกัน

#### บทที่ 7: การทดสอบสมมติฐาน (Hypothesis Testing)

- p-value — ความน่าจะเป็นที่จะได้ค่าสถิติทดสอบที่ "สุดขั้วเท่ากับหรือมากกว่า" ค่าที่สังเกตได้ ถ้า H₀ เป็นจริง — กติกา: ถ้า p-value ≤ α ให้ปฏิเสธ H₀, ถ้า p-value > α ไม่ปฏิเสธ H₀
- ต้องตรวจสอบสมมติฐาน (LINE) ก่อนเชื่อผลการวิเคราะห์
Multiple Correlation Model — ข้อแตกต่างสำคัญจาก Regression Model: ในโมเดลสหสัมพันธ์ ตัวแปร Xᵢ เป็นตัวแปรสุ่ม (random) ไม่ใช่ค่าคงที่ที่กำหนดไว้ล่วงหน้า — Y และ Xᵢ ทั้งหมดมีการแจกแจงร่วมแบบ multivariate normal distribution และไม่มีตัวแปรใดถูกกำหนดให้เป็น "ตัวแปรตาม" หรือ "ตัวแปรอิสระ" ตายตัว (สลับบทบาทกันได้ในทางทฤษฎี) — สมการถดถอยยังคำนวณด้วยวิธีเดียวกัน (least squares) แต่การตีความต่างออกไป

สรุปภาพรวม: บทนี้เป็นสะพานเชื่อมระหว่างสถิติเชิงพรรณนา (บทที่ 1-4) กับการอนุมานทางสถิติ (บทที่ 6 เป็นต้นไป) — Central Limit Theorem คือกุญแจสำคัญที่ทำให้เราสามารถใช้การแจกแจงแบบปกติในการคำนวณความน่าจะเป็นและสร้าง confidence interval / ทดสอบสมมติฐานเกี่ยวกับค่าเฉลี่ยและสัดส่วนได้ แม้ประชากรต้นทางจะไม่เป็น normal distribution ก็ตาม ตราบใดที่ขนาดตัวอย่างใหญ่เพียงพอ

4) CI สำหรับผลต่างระหว่างสัดส่วนสองประชากร (p₁-p₂): (p̂₁-p̂₂) ± z₍₁₋α/2₎√[p̂₁(1-p̂₁)/n₁ + p̂₂(1-p̂₂)/n₂]

Least-Squares Criterion: เส้นที่ "ดีที่สุด" คือเส้นที่ทำให้ผลรวมของกำลังสองของระยะห่างแนวตั้ง (vertical deviation) จากจุดข้อมูลถึงเส้น มีค่าน้อยที่สุด เมื่อเทียบกับเส้นอื่นใดที่เป็นไปได้ — เรียกว่า "least-squares line"

- Probabilistic interpretation — ถ้าสุ่มตัวอย่างซ้ำ ๆ จำนวนมาก 100(1-α)% ของช่วงที่สร้างด้วยวิธีนี้จะครอบคลุมค่าพารามิเตอร์จริง
- เมื่อไม่ทราบ σ แต่สมมติว่าvariance ของสองประชากรเท่ากัน ต้องคำนวณ Pooled variance:
The Correlation Coefficient (r): วัดความแข็งแรงของความสัมพันธ์เชิงเส้นระหว่างสองตัวแปร โดยไม่ได้กำหนดว่าตัวใดเป็นเหตุ/ผล (แตกต่างจาก regression ที่มี X, Y ชัดเจน) — r คือรากที่สองของ r² แต่มีเครื่องหมายตามทิศทางของ β₁ (slope):

> Total deviation (yᵢ-ȳ) = Explained deviation (ŷᵢ-ȳ) + Unexplained deviation (yᵢ-ŷᵢ)

- Practical interpretation — เรามั่นใจ 100(1-α)% ว่าช่วงที่คำนวณได้ครั้งนี้ครอบคลุมค่าพารามิเตอร์จริง
- ผลลัพธ์ n ที่คำนวณได้เศษเสมอต้องปัดขึ้น (round up) เป็นจำนวนเต็มถัดไปเสมอ เพื่อให้แน่ใจว่าได้ความแม่นยำตามต้องการ
ส่วนขยายจากบทที่ 9: เมื่อมีตัวแปรอิสระ (independent/explanatory/predictor variables) มากกว่า 1 ตัว (X₁, X₂, ..., Xₖ) ที่ร่วมกันอธิบายตัวแปรตาม Y

ถ้าสุ่มจากประชากรที่ไม่ใช่ normal หรือไม่ทราบรูปแบบ แต่ n₁,n₂ มีขนาดใหญ่พอ (>30) ก็ยังใช้ Central Limit Theorem ได้เช่นเดียวกัน

กฎสำคัญ: ถ้าตัวแปรเชิงคุณภาพมี k หมวดหมู่ ต้องใช้ dummy variable จำนวน k-1 ตัว (ไม่ใช่ k ตัว) เพื่อไม่ให้เกิดปัญหา perfect multicollinearity ในโมเดลที่มีค่าคงที่ (intercept) — ตัวอย่าง: เพศ (2 หมวด) ใช้ dummy 1 ตัว (1=ชาย, 0=หญิง); สถานะสูบบุหรี่ 4 หมวด (สูบปัจจุบัน/เลิกไม่เกิน 5 ปี/เลิกเกิน 5 ปี/ไม่เคยสูบ) ต้องใช้ dummy 3 ตัว — ค่าสัมประสิทธิ์ของ dummy variable แต่ละตัวบอกความแตกต่างของค่าเฉลี่ย Y ระหว่างหมวดหมู่นั้นกับหมวดหมู่อ้างอิง (reference category ที่ไม่มี dummy เป็นตัวแทน) เมื่อตัวแปรอื่นในโมเดลคงที่

แนวคิดพื้นฐาน: การประมาณค่าคือการคำนวณสถิติจากตัวอย่างเพื่อเป็นค่าประมาณของพารามิเตอร์ประชากร มี 2 รูปแบบ:

- SST — ความแปรปรวนรวมของ Y รอบค่าเฉลี่ย ȳ
- ทดสอบสมมติฐาน H₀: ρ=0 (ρ คือค่าสหสัมพันธ์ประชากร) ได้ด้วยวิธีเดียวกับการทดสอบ β₁=0
> (n-1)s² / χ²₍₁₋α/2₎ < σ² < (n-1)s² / χ²₍α/2₎

- Decision rule — กำหนด rejection region และ critical value ล่วงหน้าตามค่า α ที่เลือก (ก่อนดูข้อมูลจริง เพื่อความเป็นกลาง)
เมื่อยกกำลังสองและรวมทุกจุด:

- เมื่อทราบ σ (variance ประชากร) และสุ่มจาก normal population (หรือ n ใหญ่พอ): x̄ ± z₍₁₋α/2₎(σ/√n)
สมมติฐาน 4 ข้อ (คล้ายกับ simple regression): (1) ค่า Xᵢ เป็นค่าคงที่ (fixed/nonrandom) — นี่คือข้อแตกต่างสำคัญจาก "correlation model" ที่จะกล่าวถึงด้านล่าง (2) แต่ละชุดค่า Xᵢ มี subpopulation ของ Y ที่เป็น normal distribution (3) variance ของทุก subpopulation เท่ากัน (4) ค่า Y เป็นอิสระต่อกัน

- การทดสอบนัยสำคัญโดยรวม (Overall F-test): H₀: β₁=β₂=...=βₖ=0 (ตัวแปรอิสระทั้งหมด "ไร้ประโยชน์" ร่วมกัน) เทียบกับ Hₐ: ไม่ใช่ทุก βᵢ เป็น 0 — ใช้ F = MSR/MSE จาก ANOVA table (df ตัวเศษ=k, ตัวส่วน=n-k-1)
การตีความ Confidence Interval มี 2 แบบ:

- F-test (ผ่าน ANOVA table ของการถดถอย): F = MSR/MSE (df ตัวเศษ=1, ตัวส่วน=n-2)
- r = 0 → ไม่มีสหสัมพันธ์เชิงเส้น
- Coefficient of Multiple Determination (R²) = SSR/SST — สัดส่วนความแปรปรวนของ Y ที่อธิบายได้ด้วยตัวแปรอิสระทั้งหมดรวมกัน (คล้าย r² ในบทที่ 9 แต่ขยายเป็นหลายตัวแปร)
The Multiple Linear Regression Model:

- ถ้าvariance ไม่เท่ากัน ต้องใช้วิธีแก้ปัญหาแบบ Behrens-Fisher/Welch (สูตรซับซ้อนกว่า)
> p = exp(β₀+β₁x) / [1+exp(β₀+β₁x)]

3) CI สำหรับสัดส่วนประชากร (p): p̂ ± z₍₁₋α/2₎√[p̂(1-p̂)/n] — ใช้ p̂ แทน p ที่ไม่รู้ค่าจริงในการประมาณ standard error

Research Hypothesis vs. Statistical Hypothesis: Research hypothesis คือข้อสันนิษฐานทั่วไปที่กระตุ้นให้เกิดการวิจัย ส่วน Statistical hypothesis คือข้อความที่ถูกจัดรูปแบบให้ทดสอบได้ด้วยวิธีทางสถิติ — Null Hypothesis (H₀) คือสมมติฐานที่ถูกทดสอบ (มักเป็น "ไม่มีความแตกต่าง") ส่วน Alternative Hypothesis (Hₐ) คือสิ่งที่เราจะเชื่อถ้าปฏิเสธ H₀ ได้ — กติกาการตั้งสมมติฐาน: (1) สิ่งที่นักวิจัยหวังจะสรุปได้มักอยู่ใน Hₐ (2) H₀ ต้องมีเครื่องหมายเท่ากับเสมอ (=, ≤, หรือ ≥) (3) H₀ คือสิ่งที่ถูกทดสอบจริง (4) H₀ กับ Hₐ ต้องครอบคลุมทุกความเป็นไปได้ร่วมกัน

- SSR — ส่วนที่ "อธิบายได้" ด้วยความสัมพันธ์เชิงเส้นกับ X
> X² = Σ[(Oᵢ-Eᵢ)²/Eᵢ]

- The t Distribution: เมื่อไม่ทราบ σ (กรณีทั่วไปในชีวิตจริง) ต้องใช้ s (sample SD) แทน และเปลี่ยนจาก z เป็น t distribution ซึ่งมีคุณสมบัติ: สมมาตรรอบ 0, แบนกว่าและหางหนากว่า normal distribution, เป็น "ตระกูล" ของการแจกแจงตาม degrees of freedom (df=n-1), และเข้าใกล้ normal distribution เมื่อ df มากขึ้น — สูตร: x̄ ± t₍₁₋α/2,n-1₎(s/√n)
การหาสมการถดถอย: ใช้ method of least squares เหมือนบทที่ 9 คือหาค่าสัมประสิทธิ์ที่ทำให้ผลรวมกำลังสองของ residual (Σ(yⱼ-ŷⱼ)²) น้อยที่สุด — ในทางปฏิบัติคำนวณด้วยซอฟต์แวร์เสมอเพราะซับซ้อนเกินคำนวณมือ

- SSE — ส่วนที่ "อธิบายไม่ได้" (เป็น residual ที่เหลือหลังฟิตเส้น) — ค่านี้คือค่าที่ least-squares line ทำให้น้อยที่สุด
> r² = SSR/SST

- หลีกเลี่ยงการ Extrapolation — อย่าใช้สมการถดถอยทำนาย/ประมาณค่านอกช่วงของ X ที่มีในข้อมูลตัวอย่าง เพราะความสัมพันธ์เชิงเส้นอาจใช้ได้แค่ในช่วงที่สังเกตเท่านั้น นอกช่วงนั้นความสัมพันธ์ที่แท้จริงอาจเป็นเส้นโค้งก็ได้
- Test statistic — สูตรทั่วไป: (สถิติที่เกี่ยวข้อง - ค่าพารามิเตอร์ที่ตั้งสมมติฐาน) / (standard error ของสถิตินั้น)
การทดสอบว่าความสัมพันธ์มีนัยสำคัญหรือไม่ — H₀: β₁=0: ถ้าปฏิเสธ H₀ ไม่ได้ (β₁ อาจเป็น 0 จริง) แปลว่า X ไม่มีประโยชน์ในการทำนาย Y เชิงเส้น (อาจเป็นเพราะไม่มีความสัมพันธ์เลย หรือความสัมพันธ์เป็นแบบ curvilinear ไม่ใช่เส้นตรง) — ทดสอบได้ 2 วิธีที่ให้ผลตรงกัน:

- r = +1 → สหสัมพันธ์เชิงบวกสมบูรณ์แบบ (perfect direct)
ประโยชน์สำคัญ: ใช้ตรวจสอบว่าสมมติฐานความเท่ากันของ variance สองกลุ่ม (ที่จำเป็นสำหรับการใช้ pooled variance ในข้อ 2) เป็นจริงหรือไม่ — ถ้า CI ของอัตราส่วนนี้รวมค่า 1 แสดงว่า variance ของสองประชากรอาจเท่ากันได้จริง วิธีการทดสอบนี้เป็นที่รู้จักในชื่อ F-max Test หรือ Variance Ratio Test

- Calculation — คำนวณค่าสถิติทดสอบจากข้อมูลตัวอย่างจริง
One-tailed vs. Two-tailed Tests: ถ้า Hₐ มีเครื่องหมาย ≠ (ต้องการรู้ว่า "ต่างกัน" ไม่ว่าทิศทางไหน) → two-tailed test rejection region แบ่งครึ่งสองด้าน — ถ้า Hₐ มีเครื่องหมาย < หรือ > (สนใจทิศทางเดียว) → one-tailed test rejection region อยู่ด้านเดียวทั้งหมด

- β ขึ้นกับ 4 ปัจจัย: (1) ค่าจริงของพารามิเตอร์ (2) ค่าที่ตั้งสมมติฐาน (3) ค่า α ที่เลือก (4) ขนาดตัวอย่าง n
3) Test of Homogeneity: คำถามต่างจาก independence test — ถามว่ากลุ่มตัวอย่างหลายกลุ่มที่สุ่มมาแยกกัน (จากประชากรต่างกัน) มีสัดส่วนของคุณลักษณะเดียวกันหรือไม่ — สุ่มตัวอย่างจากหลายประชากรแยกกัน (ผลรวมของแถวหรือคอลัมน์หนึ่งชุดถูกกำหนดตายตัวโดยผู้วิจัย ไม่ใช่เกิดขึ้นเองแบบสุ่ม) — ข้อสำคัญ: แม้แนวคิดและวิธีสุ่มตัวอย่างต่างกัน แต่การคำนวณทางคณิตศาสตร์เหมือนกันทุกประการกับ test of independence

6) CI สำหรับอัตราส่วนของ Variance สองประชากร (σ₁²/σ₂²) — ใช้ F Distribution: ปริมาณ (s₁²/σ₁²)/(s₂²/σ₂²) มีการแจกแจงแบบ F distribution ที่กำหนดโดย 2 ค่า degrees of freedom (numerator df=n₁-1, denominator df=n₂-1) — สูตร CI:

- สัดส่วนเดี่ยว (p): z = (p̂-p₀)/√[p₀(1-p₀)/n] — ข้อสำคัญ: ใช้ p₀ (ค่าตั้งสมมติฐาน) ไม่ใช่ p̂ ในการคำนวณ standard error เพราะการทดสอบทั้งหมดตั้งอยู่บนสมมติฐานว่า H₀ เป็นจริง
> ln[p/(1-p)] = β₀ + β₁x

ตัวแปร 3 ชนิดในการทดลอง ANOVA: (1) Treatment variable — ตัวแปรที่สนใจศึกษา (เช่น ชนิดยา) (2) Response variable — ตัวแปรผลลัพธ์ที่วัด (3) Extraneous variable — ปัจจัยแทรกซ้อนอื่นที่ไม่ใช่จุดสนใจหลัก

> F = MSA / MSW

- ตัวแปรทั้งสองต้องวัดจากหน่วยเชื่อมโยงเดียวกัน (unit of association) — เช่น ส่วนสูงกับน้ำหนักต้องวัดจากคนคนเดียวกัน ไม่ใช่คนละกลุ่ม
> (s₁²/s₂²)/F₍₁₋α/2₎ < σ₁²/σ₂² < (s₁²/s₂²)/F₍α/2₎

- r = -1 → สหสัมพันธ์เชิงลบสมบูรณ์แบบ (perfect inverse)
- Statistical decision — reject หรือ fail to reject H₀
- ผลต่างระหว่างสองสัดส่วน (p₁-p₂): ใช้หลักการคล้ายกัน โดยรวม p̂ ทั้งสองกลุ่มเป็น pooled proportion ก่อนคำนวณ standard error ภายใต้ H₀
ข้อควรระวังสำคัญ 4 ข้อ (Some Precautions):


#### บทที่ 10: การถดถอยพหุคูณและสหสัมพันธ์ (Multiple Regression and Correlation)

1) Completely Randomized Design (CRD) — One-Way ANOVA: สุ่มหน่วยทดลองเข้ากลุ่มทรีตเมนต์ต่าง ๆ อย่างสมบูรณ์ (ใช้ตารางเลขสุ่มกำหนด)

- Retrospective study (case-control) — สุ่ม 2 กลุ่มตามสถานะโรค (cases/controls) แล้วย้อนดูปัจจัยเสี่ยงในอดีต — ไม่สามารถคำนวณ RR ได้โดยตรง เพราะสัดส่วนของกลุ่ม cases/controls ถูกกำหนดโดยผู้วิจัยเอง ไม่ใช่อัตราตามธรรมชาติ — ต้องใช้ Odds Ratio = ad/bc แทน — เมื่อโรคหายาก (rare disease) OR จะประมาณค่า RR ได้ใกล้เคียง (หลักการเดียวกับที่กล่าวในตำราระบาดวิทยาคลินิก)
> yⱼ = β₀ + β₁x₁ⱼ + β₂x₂ⱼ + ... + βₖxₖⱼ + εⱼ

> X² = Σ[(Oᵢ-Eᵢ)²/Eᵢ]

ขั้นตอนการทดสอบสมมติฐาน 10 ขั้นตอน:

Type II Error และ Power ของการทดสอบ — เจาะลึก:

เหตุผลที่ต้องมี ANOVA: เมื่อต้องการเปรียบเทียบค่าเฉลี่ยของมากกว่า 2 กลุ่ม การทำ t-test เทียบทีละคู่หลาย ๆ ครั้งจะเพิ่มโอกาสเกิด Type I error สะสม อย่างมาก — ตัวอย่างในหนังสือ: ถ้ามี 5 กลุ่ม ต้องเทียบ 10 คู่ (₅C₂) แม้ตั้ง α=.05 ต่อครั้ง แต่โอกาสเกิด Type I error อย่างน้อย 1 ครั้งจากทั้งหมดสูงถึง 40.13% — ANOVA แก้ปัญหานี้โดยทดสอบทุกกลุ่มพร้อมกันในการทดสอบเดียว โดยการแบ่งส่วน (partition) ความแปรปรวนรวมทั้งหมดออกเป็นองค์ประกอบที่มาจากแหล่งต่าง ๆ

Mantel-Haenszel Statistic — จัดการ Confounding Variable: เมื่อสงสัยว่ามีตัวแปรกวน (confounding variable) ที่อาจบดบังความสัมพันธ์ที่แท้จริงระหว่างโรคกับปัจจัยเสี่ยง (เช่น กลุ่มชาติพันธุ์ หรืออายุ) วิธีนี้จะแบ่งข้อมูลเป็นชั้น (strata) ตามค่าตัวแปรกวน แล้ววิเคราะห์แยกในแต่ละชั้นก่อนรวมผล — คำนวณสถิติทดสอบ χ²_MH เพื่อทดสอบว่ามีความสัมพันธ์จริงระหว่างโรคกับปัจจัยเสี่ยงหรือไม่ (ควบคุมตัวแปรกวนแล้ว) และคำนวณ Mantel-Haenszel common odds ratio (OR_MH) ซึ่งเป็นค่า OR รวมที่ปรับผลของตัวแปรกวนแล้ว — ตั้งอยู่บนสมมติฐานว่า OR ในแต่ละชั้นเท่ากัน (homogeneous odds ratio)

ความแตกต่างของศัพท์ (แม้มักใช้แทนกันได้ในทางปฏิบัติ): Nonparametric = การทดสอบที่ไม่ได้ตั้งสมมติฐานเกี่ยวกับพารามิเตอร์ประชากร ส่วน Distribution-free = การทดสอบที่ไม่ต้องอาศัยความรู้/สมมติฐานเกี่ยวกับรูปแบบการแจกแจงของประชากรต้นทาง

เรียกสมการนี้ว่า Logistic Regression Model — แปลงกลับเป็นความน่าจะเป็น p ได้ด้วย:

> SST (Total) = SSA (Among/Between groups) + SSW (Within groups)

Fisher Exact Test: ใช้แทน chi-square test เมื่อขนาดตัวอย่างเล็กเกินไป (เช่น n<20 หรือ n=20-40 ที่มี expected frequency น้อยกว่า 5 บางเซลล์) — คำนวณความน่าจะเป็นที่แน่นอน (exact) ของการได้ผลลัพธ์ที่สังเกตได้หรือสุดขั้วกว่านั้น โดยไม่ต้องอาศัยการประมาณแบบต่อเนื่อง — ใช้กับตาราง 2×2 เท่านั้น

- Hypotheses — ตั้ง H₀ และ Hₐ

#### บทที่ 8: การวิเคราะห์ความแปรปรวน (Analysis of Variance, ANOVA)

- หลักการสำคัญ: OR เป็นค่าประมาณที่ดีของ RR เมื่อโรคที่ศึกษาเป็น "โรคหายาก (rare disease)" — ตรงกับหลักการเดียวกันในตำราระบาดวิทยาคลินิก
2) Variable Selection Procedures — เมื่อมีตัวแปรอิสระที่เป็นไปได้จำนวนมาก: ข้อควรระวังสำคัญ: การเพิ่มตัวแปรอิสระเข้าไปในโมเดลจะทำให้ R² เพิ่มขึ้นเสมอ (ไม่มีทางลดลง) จึงไม่ควรใส่ตัวแปรเข้าไปตามอำเภอใจ ต้องมีเหตุผลรองรับ (รวมถึงต้นทุนการเก็บข้อมูล) — มีกลยุทธ์หลักที่ใช้กันแพร่หลาย:

Logistic Regression กับตัวแปรอิสระต่อเนื่อง (Continuous): ใช้หลักการเดียวกัน แต่ β₁ ตีความเป็น "การเปลี่ยนแปลงของ log-odds ต่อหน่วยที่เพิ่มขึ้นของ X" ซึ่งซับซ้อนกว่าการตีความ slope ในการถดถอยเชิงเส้นธรรมดา — สามารถใช้สมการเพื่อคำนวณความน่าจะเป็นของผลลัพธ์ (เช่น ความน่าจะเป็นที่ผู้ป่วยจะเข้าร่วมโปรแกรมฟื้นฟูหัวใจ) ณ ค่าตัวแปรอิสระใด ๆ ได้โดยตรงผ่านสูตร p ด้านบน — Logistic regression เป็นเครื่องมือที่ใช้แพร่หลายมากในงานระบาดวิทยาเพื่อประมาณความเสี่ยง (risk) ของการเกิดโรคจากปัจจัยเสี่ยงต่าง ๆ

Chi-Square Test Statistic — สูตรหลักของทั้งบท:

ทางแก้ — Logit Transformation: ถ้า p=P(Y=1) แปลงเป็น odds = p/(1-p) (มีค่า 0 ถึง +∞) แล้วนำ natural log มาใช้:

ตัวประมาณค่าความแปรปรวนร่วม (σ²) สองตัว:

คุณสมบัติทางคณิตศาสตร์ของ Chi-Square Distribution: เกิดจากผลรวมของค่า z² (ค่ามาตรฐานยกกำลังสอง) — ถ้าสุ่ม z จำนวน k ค่าที่เป็นอิสระต่อกันจากการแจกแจงปกติมาตรฐาน แล้วรวม z₁²+z₂²+...+zₖ² จะได้การแจกแจงไคสแควร์ที่มี df=k — คุณสมบัติ: mean=k, variance=2k, ค่าเป็นบวกเสมอ (0 ถึง +∞) เพราะเป็นผลรวมของค่ายกกำลังสอง, และผลรวมของตัวแปรไคสแควร์อิสระหลายตัวก็ยังเป็นไคสแควร์

- Paired Comparisons (การเปรียบเทียบแบบจับคู่) — ใช้เมื่อข้อมูลสองชุดไม่เป็นอิสระต่อกัน (เช่น วัดก่อน-หลังในผู้ป่วยคนเดียวกัน, ฝาแฝด, จับคู่ตามลักษณะ) — เหตุผลที่ต้องจับคู่: ช่วยกำจัดความแปรปรวนจากปัจจัยแทรกซ้อน (extraneous variation) ที่อาจบดบังหรือสร้างความแตกต่างปลอมขึ้นมา (ตัวอย่าง: เปรียบเทียบครีมกันแดด 2 ชนิดบนหลังคนเดียวกันคนละข้าง ดีกว่าเปรียบเทียบระหว่างคนสองกลุ่มที่อาจมีสีผิวต่างกันโดยบังเอิญ) — วิเคราะห์จากค่าผลต่าง (dᵢ) ของแต่ละคู่ แล้วทดสอบด้วย t = (d̄-μd₀)/(sd̄) โดยที่ sd̄=sd/√n (df=n-1) — ข้อดี: ไม่ต้องกังวลเรื่องความเท่ากันของ variance เหมือนตัวอย่างอิสระ เพราะเหลือตัวแปรเดียว (ผลต่าง)
- อัตราส่วนของสอง Variance (σ₁²/σ₂²): ใช้ F distribution — มักใช้ตรวจสอบสมมติฐานความเท่ากันของ variance ก่อนเลือกวิธี pooled-t หรือ separate-variance-t
- Operating Characteristic (OC) Curve — พล็อตค่า β แทน 1-β (เป็นส่วนกลับของ power curve)
> n = [(z₀+z₁)σ / (μ₀-μ₁)]²

ข้อเสีย: ถ้าใช้กับข้อมูลที่จริง ๆ แล้วเหมาะกับสถิติแบบพาราเมตริกอยู่แล้ว จะเป็นการ "เสียข้อมูล" (waste of data) เพราะไม่ได้ใช้ข้อมูลเต็มศักยภาพ และบางการทดสอบคำนวณยากเมื่อตัวอย่างมีขนาดใหญ่

Partial Correlation Coefficient: วัดความสัมพันธ์ระหว่างตัวแปรคู่หนึ่งหลังควบคุมอิทธิพลของตัวแปรอื่น ๆ ออกไปแล้ว — เช่น r_{y1.2} คือสหสัมพันธ์ระหว่าง Y กับ X₁ หลังควบคุม X₂ (ตัวเลขหลังจุดคือตัวแปรที่ถูกควบคุม) — Coefficient of Partial Determination (กำลังสองของค่านี้) บอกว่าสัดส่วนความแปรปรวนที่ "เหลืออยู่" ใน Y (หลังจาก X₂ อธิบายไปแล้วเท่าที่ทำได้) ถูกอธิบายเพิ่มเติมโดย X₁ ได้เท่าไร — มีประโยชน์มากในการแยกแยะว่าตัวแปรใดมีผลอิสระจริง ๆ เมื่อตัวแปรหลายตัวมีความสัมพันธ์กันเอง (เช่น อายุกับระดับการศึกษาที่อาจสัมพันธ์กันเองในการทำนายคะแนนทดสอบทางปัญญา)

Relative Risk (RR) และ Odds Ratio (OR) — เครื่องมือสำคัญสำหรับ Observational Studies:

- Sign Test — เทียบเท่ากับ one-sample/paired t-test แบบง่ายที่สุด ใช้เฉพาะเครื่องหมาย (+/-) ของผลต่างจากค่า median ที่ตั้งสมมติฐาน ไม่สนใจขนาด — ทดสอบด้วย binomial distribution ที่ p=.5 (H₀: P(+)=P(-)=.5) — สมมติฐานเดียวที่ต้องมี: ตัวแปรต่อเนื่อง — ข้อเสีย: เสียข้อมูลมากเพราะทิ้งขนาดของผลต่างไปหมด
- Prospective study — สุ่ม 2 กลุ่มตามสถานะปัจจัยเสี่ยง แล้วติดตามไปข้างหน้าดูว่าใครเป็นโรค — คำนวณ Relative Risk = [a/(a+b)] / [c/(c+d)] ได้โดยตรง (จากตาราง 2×2: risk factor present/absent × disease present/absent) — RR=1 หมายถึงไม่มีความสัมพันธ์, RR>1 หมายถึงเพิ่มความเสี่ยง, RR<1 หมายถึงลดความเสี่ยง
รายการการทดสอบไร้พารามิเตอร์หลัก (แต่ละตัวเป็น "คู่เทียบ" ของการทดสอบแบบพาราเมตริก):

2) Test of Independence: ทดสอบว่าเกณฑ์การจำแนก 2 ประเภท (เมื่อวัดจากกลุ่มตัวอย่างเดียวกัน) เป็นอิสระต่อกันหรือไม่ — ใช้ Contingency Table (r แถว × c คอลัมน์) — คำนวณ expected frequency ของแต่ละเซลล์ด้วยสูตร:

- Tukey's HSD Test (Honestly Significant Difference) — ใช้ studentized range statistic (q) คำนวณค่าวิกฤตเดียว (HSD) แล้วเทียบผลต่างสัมบูรณ์ของทุกคู่ค่าเฉลี่ยกับ HSD — ถ้าขนาดกลุ่มไม่เท่ากันใช้สูตรดัดแปลง Tukey-Kramer method (HSD*)
ข้อควรระวังเรื่อง Expected Frequency ต่ำ: ถ้า expected frequency บางกลุ่มต่ำเกินไป (กฎทั่วไป: ไม่ควรต่ำกว่า 5, หรือ Cochran เสนอว่าต่ำสุดได้ถึง 1 สำหรับ unimodal goodness-of-fit test) การประมาณด้วย chi-square distribution จะไม่แม่นยำ — วิธีแก้คือรวมกลุ่มที่ติดกัน (ลด df ลง) หรือใช้ Fisher Exact Test แทน

ข้อควรระวัง: วิธีต่าง ๆ ข้างต้นไม่ได้ให้ผลลัพธ์ตรงกันเสมอไปเมื่อใช้กับข้อมูลชุดเดียวกัน เพราะแต่ละวิธีมีลำดับการพิจารณาต่างกัน — การเลือกตัวแปรจึงยังต้องอาศัยความรู้เชิงเนื้อหา (biological/clinical plausibility) ประกอบเสมอ ไม่ใช่พึ่งพาสถิติล้วน ๆ

- SSW = Σ(xᵢⱼ-x̄.ⱼ)² — ความแปรปรวน "ภายในกลุ่ม" (สะท้อนความแปรปรวนตามธรรมชาติ/สุ่ม)
- ใช้ได้กับข้อมูลที่เป็นแค่อันดับ (rank) หรือการจัดหมวดหมู่ ไม่จำเป็นต้องมีมาตรวัดที่แข็งแรงพอสำหรับสถิติแบบพาราเมตริก
โดย Oᵢ=ความถี่ที่สังเกตได้ (observed), Eᵢ=ความถี่ที่คาดหวังถ้า H₀ เป็นจริง (expected) — df = k-r (k=จำนวนกลุ่ม, r=จำนวนข้อจำกัด/พารามิเตอร์ที่ประมาณจากข้อมูล) — ค่า X² น้อย = สอดคล้องกันดี, ค่า X² มาก = ไม่สอดคล้องกัน → ปฏิเสธ H₀ เมื่อ X² มากพอ

- k คือฐาน (base) เช่น 1,000, 10,000, 100,000 ใช้เพื่อเลี่ยงตัวเลขทศนิยมเล็กเกินไปและให้อ่านเข้าใจง่าย
- ยิ่งค่าพารามิเตอร์จริงอยู่ใกล้ค่าที่ตั้งสมมติฐาน (H₀) มากเท่าไร β ยิ่งสูง (ยากที่จะตรวจจับความแตกต่างเล็กน้อย) — ยิ่งห่างกันมาก β ยิ่งต่ำ (power สูง)
> Eᵢⱼ = (ผลรวมแถว i)×(ผลรวมคอลัมน์ j) / (ผลรวมทั้งหมด n)

สมมติฐาน (assumptions) ของ Fixed-Effects Model: (a) แต่ละกลุ่มเป็นตัวอย่างสุ่มอิสระ (b) แต่ละประชากรมีการแจกแจงแบบ normal (c) variance ของทุกกลุ่มเท่ากัน (homogeneity of variance) (d) ผลรวมของ τⱼ ทั้งหมดเท่ากับ 0

- MSW (Within groups Mean Square) = SSW/(N-k) — ประมาณ σ² ได้เสมอไม่ว่า H₀ จริงหรือไม่ (ตราบใดที่ variance เท่ากันจริง)
- Kruskal-Wallis One-Way ANOVA by Ranks — คู่เทียบของ one-way ANOVA (บทที่ 8) เมื่อไม่เข้าเงื่อนไข normality/equal variance — รวมทุกกลุ่มมาจัดอันดับ แล้วคำนวณสถิติ H จากผลรวมอันดับของแต่ละกลุ่ม (Rⱼ):
- Friedman Two-Way ANOVA by Ranks — คู่เทียบของ Randomized Complete Block Design (บทที่ 8) — ใช้เมื่อข้อมูลจัดเป็น blocks (แถว) × treatments (คอลัมน์) โดยแต่ละ block จัดอันดับ treatments ของตัวเอง แล้วรวมอันดับตามคอลัมน์ (Rⱼ) คำนวณสถิติ χ²r:
1) Test of Goodness-of-Fit: ทดสอบว่าการแจกแจงความถี่ที่สังเกตได้สอดคล้องกับการแจกแจงทางทฤษฎีที่ตั้งสมมติฐานไว้หรือไม่ (เช่น ทดสอบว่าข้อมูลตามการแจกแจงแบบปกติหรือทวินามหรือไม่)

Test Statistic — Variance Ratio (V.R.) หรือ F:

Multiple Comparison Procedures — หลัง ANOVA พบว่ามีความแตกต่างแล้ว จะรู้ได้อย่างไรว่า "คู่ไหน" ต่างกัน:

Kaplan-Meier Procedure (Product-Limit Method): ประมาณความน่าจะเป็นการรอดชีวิตสะสม ณ เวลาใด ๆ:

- Wilcoxon Signed-Rank Test — ปรับปรุงจาก Sign Test โดยใช้ทั้งเครื่องหมายและขนาด (rank) ของผลต่าง ไม่ทิ้งข้อมูลไปเยอะเท่า Sign test — เหมาะเมื่อข้อมูลอย่างน้อยเป็น interval scale และประชากรสมมาตรรอบค่าเฉลี่ย — คำนวณผลต่าง dᵢ จากค่าตั้งสมมติฐาน แล้วจัดอันดับตามค่าสัมบูรณ์ ให้เครื่องหมายกลับคืน แล้วรวมอันดับที่เป็นบวก (T+) กับลบ (T-) แยกกัน — เป็นคู่เทียบของ paired t-test
- Median Test — ทดสอบว่าสองประชากรอิสระมี median เท่ากันหรือไม่ — หา median ร่วมของสองกลุ่มรวมกัน แล้วนับจำนวนค่าที่อยู่เหนือ/ใต้ median นั้นในแต่ละกลุ่ม จัดเป็นตาราง 2×2 แล้วทดสอบด้วย chi-square ธรรมดา — ใช้ข้อมูลได้ค่อนข้างน้อย (แค่ตำแหน่งเทียบกับ median)
บทบาทของสถิติชีพ: เปรียบเทียบได้กับการที่แพทย์ส่วนตัวใช้ประวัติ+ตรวจร่างกาย+ผลแล็บวินิจฉัยผู้ป่วยรายบุคคล — ทีมสาธารณสุขใช้สถิติชีพ (การเกิด การตาย การเจ็บป่วย และอัตรา/สัดส่วนต่าง ๆ ที่คำนวณจากข้อมูลเหล่านี้) เพื่อ "วินิจฉัย" สุขภาพของชุมชนทั้งชุมชนในฐานะสิ่งมีชีวิตเดียว — เป็นเครื่องมือหลักของงานระบาดวิทยาและสาธารณสุข

2) Test of Independence — ทดสอบว่าเกณฑ์การจำแนก 2 อย่างที่ใช้กับกลุ่มตัวอย่างเดียวกันเป็นอิสระต่อกันหรือไม่ (เช่น เชื้อชาติ กับ การใช้กรดโฟลิกก่อนตั้งครรภ์) — ใช้ Contingency Table ขนาด r×c — คำนวณ Expected frequency ของแต่ละช่อง:

- Cause-of-Death Ratio = (ตายจากโรคเฉพาะ / ตายทั้งหมด) × 100 — ใช้วัดความสำคัญเชิงสัมพัทธ์ของสาเหตุตายหนึ่ง ๆ ระวังการตีความข้ามพื้นที่ (อัตราสูงอาจเป็นเพราะสาเหตุอื่นต่ำ ไม่ใช่สาเหตุนี้สูงจริง)
- SSA = Σnⱼ(x̄.ⱼ-x̄..)² — ความแปรปรวน "ระหว่างกลุ่ม" (สะท้อนความแตกต่างของทรีตเมนต์)
- MSA (Among groups Mean Square) = SSA/(k-1) — ประมาณ σ² ได้ถูกต้องเฉพาะเมื่อ H₀ เป็นจริงเท่านั้น (ถ้า H₀ เท็จ ค่านี้จะพองตัวขึ้นจากความแตกต่างจริงของค่าเฉลี่ย)
ถ้า H₀ จริง ค่า F ควรใกล้ 1 (สองตัวประมาณใกล้เคียงกัน) — ถ้า H₀ เท็จ MSA จะโตกว่า MSW มาก ทำให้ F สูงขึ้นชัดเจน — F มีการแจกแจงแบบ F distribution ด้วย numerator df=k-1, denominator df=N-k — ปฏิเสธ H₀ เมื่อค่า F ที่คำนวณได้ ≥ ค่าวิกฤตจากตาราง F

Survival Analysis: วิเคราะห์ survival time (ระยะเวลาตั้งแต่เข้าร่วมการศึกษาจนเกิดเหตุการณ์ที่สนใจ เช่น ตาย/กำเริบซ้ำ) — ข้อมูลมักมี censored data (ข้อมูลที่ไม่รู้ระยะเวลาที่แท้จริง เพราะขาดการติดตามหรือยังไม่เกิดเหตุการณ์เมื่อสิ้นสุดการศึกษา) แบ่งเป็น Type I censoring (สิ้นสุดตามเวลาที่กำหนด), Type II (สิ้นสุดเมื่อครบสัดส่วนที่กำหนด), Type III/progressive (ผู้ป่วยเข้าร่วมคนละเวลากัน)

ข้อดี 4 ประการของสถิติไร้พารามิเตอร์:

Chi-Square Test Statistic ทั่วไป:

- คำนวณง่ายและเร็วกว่า (แม้ปัจจุบันซอฟต์แวร์ทำให้ข้อได้เปรียบนี้มีน้ำหนักน้อยลง)
- Retrospective Study — เริ่มจากกลุ่ม cases/controls แล้วย้อนดูปัจจัยเสี่ยง → ไม่สามารถคำนวณ RR ได้โดยตรง (เพราะสัดส่วนของ cases/controls ถูกกำหนดโดยผู้วิจัย ไม่ใช่อัตราชุกตามธรรมชาติ) ต้องใช้ Odds Ratio แทน:
โดย p̂ₜ = สัดส่วนของคนที่ยังมีชีวิตอยู่ตอนต้นช่วงเวลา t แล้วรอดผ่านช่วงเวลา t ไปได้ — เป็นวิธีไร้พารามิเตอร์ (nonparametric) ที่ใช้ข้อมูลจากทุกคนอย่างเต็มที่แม้จะมี censored data ปะปนอยู่ (เชื่อมโยงกับวิธีเดียวกันที่กล่าวถึงในตำราระบาดวิทยาคลินิก)

1) Goodness-of-Fit Test — เปรียบเทียบการแจกแจงของตัวอย่างกับการแจกแจงทางทฤษฎีที่คาดว่าประชากรควรเป็น (เช่น ทดสอบว่าข้อมูลเป็นไปตาม normal distribution, Poisson distribution หรือสัดส่วนที่คาดหวังไว้หรือไม่)

- Data — ระบุชนิดข้อมูล (นับ/วัด)
ข้อจำกัดสำคัญ: การประมาณด้วย χ² ใช้ไม่ได้ดีเมื่อexpected frequency มีค่าน้อยเกินไป — แนวทางทั่วไป (Cochran) คือควรมี expected frequency ไม่ต่ำกว่า 5 ในแต่ละเซลล์ (สำหรับ goodness-of-fit อาจยอมรับต่ำถึง 1 ได้) หากพบเซลล์ที่ expected ต่ำเกินไป ให้รวมหมวดหมู่ที่ติดกันเข้าด้วยกัน (ลด df ลงตามไปด้วย)

Survival Analysis: วิเคราะห์เวลารอดชีวิต (survival time) — ระยะเวลาตั้งแต่เริ่มติดตาม (เช่น วันผ่าตัด) จนเกิดเหตุการณ์สนใจ (เช่น เสียชีวิต)

การประเมินสมการถดถอยพหุคูณ:

- ผลต่างระหว่างสองค่าเฉลี่ย (μ₁-μ₂): ใช้ z หรือ t (พร้อม pooled variance ถ้าสมมติว่า variance เท่ากัน) เหมือนบทที่ 6
- Power Curve — กราฟแสดง 1-β ที่ค่าทางเลือกต่าง ๆ ของพารามิเตอร์ ช่วยให้เห็นภาพว่าการทดสอบมีความสามารถแยกแยะ (discriminate) ได้ดีแค่ไหน (two-tailed test ให้กราฟรูปตัว V, one-tailed test ให้กราฟรูปตัว S ยืด)
โดย z₀ สอดคล้องกับ α และ z₁ สอดคล้องกับ β ที่เลือก — ยิ่งต้องการ power สูง (β ต่ำ) และตรวจจับความแตกต่างเล็ก (μ₀-μ₁ น้อย) ยิ่งต้องใช้ขนาดตัวอย่างใหญ่ขึ้นมาก

Fisher Exact Test: ใช้แทน chi-square test เมื่อขนาดตัวอย่างเล็กเกินไป (กฎทั่วไป: n<20, หรือ 20≤n≤40 และมี expected frequency ต่ำกว่า 5) — คำนวณความน่าจะเป็นที่แท้จริง (exact) ของผลที่สังเกตได้หรือรุนแรงกว่า โดยไม่ต้องอาศัยการประมาณแบบ chi-square — ใช้กับตาราง 2×2 เท่านั้น — เมื่อขนาดตัวอย่างใหญ่พอ ยังมีการประมาณด้วย normal distribution เป็นทางเลือก: z = [(a/A)-(b/B)] / √[p̂(1-p̂)(1/A+1/B)]

- Assumptions — เงื่อนไขที่ต้องเป็นจริง (normality, ความเท่ากันของ variance, ความเป็นอิสระของตัวอย่าง)
- ค่าเฉลี่ยเดี่ยว (μ): z = (x̄-μ₀)/(σ/√n) เมื่อทราบ σ, หรือ t = (x̄-μ₀)/(s/√n) เมื่อไม่ทราบ σ (df=n-1)
Relative Risk (RR) vs. Odds Ratio (OR) — แยกตามประเภทการศึกษา:

ข้อคิดสรุป: ทุกการทดสอบไร้พารามิเตอร์ข้างต้นถูกออกแบบให้เป็นทางเลือกที่ทนทานกว่าเมื่อสมมติฐานของการทดสอบแบบพาราเมตริก (normality, equal variance, interval/ratio scale) ไม่เป็นจริง — นักวิจัยควรเลือกใช้เมื่อมีเหตุผลจริง ๆ (ข้อมูลเป็นอันดับ, ตัวอย่างเล็กและไม่ normal) ไม่ใช่ใช้พร่ำเพรื่อโดยไม่จำเป็น เพราะจะสูญเสียประสิทธิภาพทางสถิติ (statistical power) เมื่อเทียบกับวิธีพาราเมตริกที่เหมาะสมกว่าในสถานการณ์ที่สมมติฐานเป็นจริง

Partial Regression Coefficients: β₁ วัดการเปลี่ยนแปลงเฉลี่ยของ Y ต่อหน่วยที่เพิ่มขึ้นของ X₁ เมื่อควบคุม (ตรึง) X₂ ให้คงที่ — เป็นแนวคิดสำคัญมาก: ค่าสัมประสิทธิ์แต่ละตัวสะท้อนผลของตัวแปรนั้น "โดยที่ตัวแปรอื่นในโมเดลถูกควบคุมไว้แล้ว" ไม่ใช่ผลเดี่ยว ๆ ที่ไม่คำนึงถึงตัวแปรอื่นเลย — ในเชิงเรขาคณิต โมเดล 2 ตัวแปรอิสระให้ระนาบ (plane) ในปริภูมิ 3 มิติ ถ้ามากกว่า 2 ตัวเรียกว่า hyperplane

ข้อควรระวังสำคัญ: การทดสอบสมมติฐานไม่เคย "พิสูจน์" สมมติฐานใด ๆ — เมื่อไม่ปฏิเสธ H₀ เราไม่พูดว่า H₀ "เป็นจริง" (accept) แต่พูดว่า "อาจเป็นจริง" (not rejected) เพราะอาจเกิด Type II error ได้

- Type II error (β) — ไม่ปฏิเสธ H₀ ทั้งที่จริง ๆ H₀ ผิด — β ไม่ได้ถูกควบคุมโดยตรงเหมือน α และในทางปฏิบัติมักมีค่ามากกว่า α
- ทั้ง RR และ OR สามารถสร้าง confidence interval ได้โดยอาศัยค่า X² ที่คำนวณจากตารางเดียวกัน
- Prospective Study — เริ่มจากกลุ่มที่มี/ไม่มีปัจจัยเสี่ยง แล้วติดตามไปข้างหน้าดูการเกิดโรค → คำนวณ Relative Risk ได้โดยตรง:
- Distribution of test statistic — ระบุว่าสถิติทดสอบมีการแจกแจงแบบใด (z, t, χ², F) เมื่อ H₀ เป็นจริง
ผลลัพธ์ที่ขัดแย้งกันได้ระหว่าง R² โดยรวมกับ βᵢ รายตัว: มีความเป็นไปได้ 6 แบบ เช่น R² มีนัยสำคัญแต่ βᵢ บางตัวไม่มีนัยสำคัญ (พบได้บ่อยมากเมื่อมีตัวแปรอิสระหลายตัว เพราะตัวแปรอาจสัมพันธ์กันเอง — multicollinearity) หรือในทางกลับกัน βᵢ ทุกตัวมีนัยสำคัญแต่ R² โดยรวมไม่มีนัยสำคัญ — จึงต้องดูทั้งสองอย่างประกอบกัน ไม่ใช่ดูอย่างใดอย่างหนึ่งเพียงลำพัง

- Variance เดี่ยว (σ²): ใช้ chi-square distribution χ²=(n-1)s²/σ₀²
- Fetal Death Rate = (ตายในครรภ์ / จำนวนการคลอดทั้งหมด) × 1,000 — ปัญหา: แต่ละพื้นที่นิยามอายุครรภ์ขั้นต่ำที่ต้องรายงานต่างกัน
- Type I error (α) — ปฏิเสธ H₀ ทั้งที่จริง ๆ H₀ ถูกต้อง — ค่า α ถูกกำหนดไว้ล่วงหน้าโดยผู้วิจัย (มักเป็น .01, .05, .10)
การกำหนดขนาดตัวอย่างเพื่อควบคุมทั้ง Type I และ Type II Error พร้อมกัน: ต่างจากบทที่ 6 ที่คุมแค่ α (ผ่าน confidence coefficient) ในบทนี้หากต้องการควบคุมทั้ง α และ β ให้อยู่ในระดับที่กำหนดพร้อมกัน โดยระบุค่าทางเลือก μ₁ ที่ต้องการตรวจจับให้ได้ ใช้สูตร:

การแบ่งส่วนผลรวมกำลังสอง (Sum of Squares):

df = (r-1)(c-1) — สถานการณ์: สุ่มตัวอย่างครั้งเดียวจากประชากรเดียว แล้วจำแนกตามสองเกณฑ์พร้อมกัน (ทั้งผลรวมแถวและคอลัมน์เป็นค่าสุ่ม ไม่ได้ถูกกำหนดไว้ล่วงหน้า)

Mantel-Haenszel Statistic — ควบคุม Confounding Variable: เมื่อสงสัยว่ามีตัวแปรกวน (confounding variable เช่น เชื้อชาติ อายุ) ที่อาจบดบังความสัมพันธ์ที่แท้จริงระหว่างโรคกับปัจจัยเสี่ยง วิธีนี้แบ่งข้อมูลเป็นชั้น (strata) ตามค่าของตัวแปรกวน แล้ววิเคราะห์ทั้งภายในแต่ละชั้นและรวมข้ามทุกชั้น เพื่อให้ได้ค่าความสัมพันธ์ที่ "ปรับแล้ว (adjusted)" ไม่ถูกบิดเบือนโดยตัวแปรกวน — ใช้ได้ทั้งข้อมูลจาก retrospective และ prospective study

- Kolmogorov-Smirnov Goodness-of-Fit Test — ทางเลือกของ chi-square goodness-of-fit เปรียบเทียบcumulative distribution function ของตัวอย่าง (Fs(x)) กับทฤษฎี (Fт(x)) — สถิติทดสอบ D = ระยะห่างแนวตั้งสูงสุดระหว่างสองเส้นโค้งสะสม — เหมาะกับข้อมูลต่อเนื่อง (ต่างจาก chi-square ที่เหมาะกับข้อมูลจัดกลุ่ม/หมวดหมู่)
Multiple Correlation Coefficient (R): = √R² — วัดความแข็งแรงของความสัมพันธ์ระหว่าง Y กับกลุ่มตัวแปร X ทั้งหมดรวมกัน

- Censored data — ข้อมูลที่ไม่ทราบเวลาที่แท้จริงจนครบ เพราะผู้ป่วยขาดการติดตามหรือยังมีชีวิตอยู่เมื่อสิ้นสุดการศึกษา — แบ่งเป็น Type I censoring (สิ้นสุดศึกษาตามเวลาที่กำหนดตายตัว), Type II censoring (สิ้นสุดเมื่อครบสัดส่วนผู้ป่วยที่เกิดเหตุการณ์ตามกำหนด), Type III (progressive) censoring (ผู้ป่วยเข้าร่วมศึกษาไม่พร้อมกัน)
- Kaplan-Meier Procedure (Product-Limit Method): ประมาณฟังก์ชันการรอดชีวิต (survivorship function) โดยการคูณความน่าจะเป็นการรอดชีวิตในแต่ละช่วงเวลาต่อเนื่องกัน:
Type I และ Type II Errors:

การทดสอบสมมติฐานสำหรับพารามิเตอร์ต่าง ๆ (ใช้หลักการเดียวกับการหา CI ในบทที่ 6 แต่กลับทิศทางตรรกะ):

โดย Oᵢ=ความถี่ที่สังเกตได้จริง (observed), Eᵢ=ความถี่ที่คาดหวังถ้า H₀ เป็นจริง (expected) — X² มีการแจกแจงประมาณเป็น χ² ด้วย df=k-r (k=จำนวนกลุ่ม, r=จำนวนข้อจำกัด/พารามิเตอร์ที่ต้องประมาณ) — ยิ่ง observed กับ expected ต่างกันมาก X² ยิ่งสูง → ปฏิเสธ H₀ เมื่อ X² ≥ ค่าวิกฤตจากตาราง χ²


#### บทที่ 13: สถิติไร้พารามิเตอร์และสถิติไม่อิงการแจกแจง (Nonparametric and Distribution-Free Statistics)

- Crude Death Rate = (จำนวนตายทั้งหมดในปี / ประชากรทั้งหมด ณ 1 กรกฎาคม) × 1,000 — ใช้วัดสุขภาพชุมชนโดยรวม แต่เปรียบเทียบระหว่างชุมชนที่มีโครงสร้างอายุ/เชื้อชาติ/เพศต่างกันได้ยาก เพราะไม่ได้ควบคุมปัจจัยเหล่านี้
ข้อควรระวังเรื่อง Multiple Comparisons: การทดสอบสัมประสิทธิ์หลายตัวพร้อมกัน (หรือสร้าง CI หลายช่วง) จากข้อมูลชุดเดียวกัน มีปัญหาสะสม Type I errorเหมือนที่กล่าวถึงในบทที่ 8 (multiple comparisons) — ค่า CI ที่สร้างแยกกันหลายช่วงจะไม่เป็นอิสระต่อกัน ต้องปรับด้วยวิธี family-wise error rate correction ถ้าต้องการความแม่นยำของระดับความเชื่อมั่นที่แท้จริง

1) Qualitative Independent Variables — Dummy Variables: เมื่อต้องการใส่ตัวแปรเชิงคุณภาพ (เช่น เพศ สถานะสูบบุหรี่ ที่อยู่อาศัย) เป็นตัวแปรอิสระในโมเดลถดถอย ต้อง "แปลงเป็นตัวเลข" ด้วย dummy variable ที่รับค่าจำกัด (มักเป็น 0 กับ 1) เพื่อระบุหมวดหมู่ — เรียกอีกชื่อว่า indicator variable หรือ (เมื่อมี 2 หมวดหมู่) dichotomous variable

Odds Ratio (OR): เมื่อตัวแปรอิสระเป็น dichotomous เช่นกัน (เช่น มี/ไม่มีปัจจัยเสี่ยง) OR = exp(β₁) — ค่านี้บอกว่าอัตราส่วนของ "odds การเกิดผลลัพธ์" ระหว่างกลุ่มที่มีปัจจัยเสี่ยงกับกลุ่มที่ไม่มี ต่างกันกี่เท่า (ตัวอย่างในหนังสือ: OR=5.84 ระหว่างเพศชายกับหญิงในการพบโรคหลอดเลือดหัวใจตีบ หมายความว่าผู้ชายมีโอกาส (odds) พบโรคนี้สูงกว่าผู้หญิงเกือบ 6 เท่า) — ข้อควรระวัง: การตีความ OR ว่าใกล้เคียงกับ relative risk ใช้ได้เมื่อผลลัพธ์ที่ศึกษาเป็นเหตุการณ์ที่พบได้ค่อนข้างน้อย (rare event) เท่านั้น (เชื่อมโยงกับหลักการเดียวกันในตำราระบาดวิทยาคลินิกเรื่อง odds ratio ≈ relative risk เมื่อความชุกต่ำ)

- Log-Rank Test: ใช้เปรียบเทียบเส้นโค้งการรอดชีวิตของสองกลุ่มว่าแตกต่างกันอย่างมีนัยสำคัญทางสถิติหรือไม่ — เป็นการประยุกต์ใช้ Mantel-Haenszel procedure โดยตรง โดยให้แต่ละเวลาที่มีการเสียชีวิตเกิดขึ้นเป็น "stratum" หนึ่ง แล้วสร้างตาราง 2×2 (จำนวนเสียชีวิต/มีชีวิตอยู่ × กลุ่ม A/กลุ่ม B) ในแต่ละ stratum ก่อนรวมผลด้วยสูตร Mantel-Haenszel เดียวกัน
3) Test of Homogeneity — คำถามต่างจาก independence: "กลุ่มตัวอย่างที่สุ่มมาจากหลายประชากร มีการกระจายตามตัวแปรหนึ่ง ๆ เหมือนกันหรือไม่" — สถานการณ์: ผลรวมของแถวหรือคอลัมน์ฝั่งหนึ่งถูกกำหนดไว้ล่วงหน้าโดยผู้วิจัย (เช่น กำหนดจะสุ่ม 96 คนจากกลุ่ม narcolepsy และ 96 คนจากกลุ่มควบคุม) — แม้แนวคิดและวิธีการสุ่มตัวอย่างต่างกัน แต่การคำนวณทางคณิตศาสตร์เหมือนกันทุกประการกับ test of independence

- ใช้ได้แม้ไม่ทราบรูปแบบการแจกแจงของประชากร (เช่น เมื่อข้อมูลไม่เป็น normal distribution และตัวอย่างเล็กเกินกว่า Central Limit Theorem จะช่วยได้)
- Spearman Rank Correlation Coefficient (rₛ) — คู่เทียบของ Pearson correlation coefficient (บทที่ 9) เมื่อข้อมูลเป็นอันดับหรือไม่เป็น normal — จัดอันดับทั้ง X และ Y แยกกัน แล้วหาผลต่างอันดับ dᵢ ในแต่ละคู่:
- Conclusion — ตีความผลในบริบท

#### บทที่ 11: การถดถอย — เทคนิคเพิ่มเติม (Regression Analysis: Some Additional Techniques)

- SST = Σ(xᵢⱼ-x̄..)² — ความแปรปรวนรวมทั้งหมด
ความเชื่อมโยงระหว่าง Confidence Interval กับ Hypothesis Testing: สามารถทดสอบ H₀ ได้ด้วย CI เช่นกัน — ถ้าค่าพารามิเตอร์ที่ตั้งสมมติฐาน (เช่น μ₀) ไม่อยู่ใน 100(1-α)% CI ให้ปฏิเสธ H₀ ที่ระดับนัยสำคัญ α ถ้าอยู่ใน CI ไม่ปฏิเสธ H₀ — สองวิธีนี้ให้ข้อสรุปตรงกันเสมอ (สำหรับ two-sided test)

ที่มาทางคณิตศาสตร์ของ Chi-Square Distribution: ถ้าสุ่มตัวแปร z (standard normal) มายกกำลังสองและบวกรวมกัน k ตัวที่เป็นอิสระต่อกัน ผลรวม z₁²+z₂²+...+zₖ² จะมีการแจกแจงแบบ chi-square (χ²) ด้วย k degrees of freedom — คุณสมบัติ: mean=k, variance=2k, ค่าที่เป็นไปได้ตั้งแต่ 0 ถึง +∞ เท่านั้น (ไม่มีค่าติดลบเพราะเป็นผลรวมของค่ายกกำลังสอง), และผลรวมของตัวแปร chi-square อิสระหลายตัวก็ยังเป็น chi-square เช่นกัน

- Stepwise Regression — วิธีที่นิยมที่สุด ทำงานเป็นขั้นตอน (steps) ที่แต่ละขั้นประเมินทุกตัวแปรในโมเดลปัจจุบันว่ายังคุ้มค่าที่จะอยู่ต่อหรือไม่ (ใช้เกณฑ์สถิติ F) — ตัวแปรที่ไม่ผ่านเกณฑ์ (F ต่ำสุด) จะถูกตัดออก แล้วโมเดลใหม่จะถูกประเมินหาตัวแปรใหม่ที่ควรเพิ่มเข้ามา — จุดเด่นสำคัญ: ตัวแปรที่เคยถูกตัดออกไปแล้ว สามารถถูกพิจารณากลับเข้ามาใหม่ได้ในขั้นตอนถัดไป — ทำซ้ำจนไม่มีตัวแปรใดเพิ่ม/ลดได้อีก — ต้องกำหนดค่า F-to-enter และ F-to-remove ล่วงหน้า (ค่า F-to-enter ควรมากกว่าหรือเท่ากับ F-to-remove เสมอ)
- Backward Elimination — เริ่มจากใส่ตัวแปรทั้งหมด แล้วตัดออกทีละตัวตามลำดับ partial correlation ต่ำสุดที่ไม่ผ่านเกณฑ์ — เช่นกัน ตัวแปรที่ถูกตัดออกแล้วจะไม่ถูกนำกลับมาพิจารณาอีก
- Forward Selection — เริ่มจากไม่มีตัวแปรเลย แล้วเพิ่มทีละตัวตามลำดับความสัมพันธ์กับตัวแปรตาม (เริ่มจากตัวที่มี correlation สูงสุด) — ข้อจำกัดสำคัญ: ตัวแปรที่เพิ่มเข้ามาแล้วจะไม่ถูกพิจารณาถอดออกอีก (ต่างจาก stepwise)

#### บทที่ 12: การแจกแจงไคสแควร์และการวิเคราะห์ความถี่ (The Chi-Square Distribution and the Analysis of Frequencies)

Log-Rank Test: ใช้เปรียบเทียบเส้นโค้งการรอดชีวิต (survival curve) จาก Kaplan-Meier ของสองกลุ่มขึ้นไปว่าแตกต่างกันอย่างมีนัยสำคัญทางสถิติหรือไม่ — เป็นการประยุกต์ใช้ Mantel-Haenszel procedure กับข้อมูล survival โดยตรง: สร้างตาราง 2×2 (จำนวนตายสังเกต/จำนวนที่ยังมีชีวิต × กลุ่ม A/กลุ่ม B) ที่แต่ละเวลาที่มีการตายเกิดขึ้น เป็นแต่ละ stratum แล้วรวมผลทุก stratum เป็นค่าสถิติทดสอบเดียว

- Ratio — ตัวเศษและตัวส่วนเป็นปริมาณคนละชุด ไม่ใช่ส่วนหนึ่งของกัน (เช่น สัดส่วนแพทย์ต่อประชากร) รูปแบบ: (c/d)×k
3) Logistic Regression — เมื่อตัวแปรตามเป็น Dichotomous (0/1): ปัญหาสำคัญของการใช้ simple linear regression ตรง ๆ กับตัวแปรตามแบบ 0/1 คือ ค่าที่ทำนายได้ (E(Y|X)) ควรอยู่ในช่วง [0,1] เท่านั้น (เพราะมันคือความน่าจะเป็น) แต่สมการเส้นตรงธรรมดาให้ค่าได้ตั้งแต่ -∞ ถึง +∞ ซึ่งขัดกับความเป็นจริง

ANOVA Table สรุปผลการคำนวณเป็นตาราง: Source of Variation | Sum of Squares | df | Mean Square | F

- Power (1-β) = ความน่าจะเป็นที่จะปฏิเสธ H₀ ได้ถูกต้องเมื่อ H₀ เป็นเท็จจริง — เป็นตัวชี้วัดว่าการทดสอบ "ไวพอ" จะจับความแตกต่างที่มีอยู่จริงได้หรือไม่
Model: xᵢⱼ = μ + τⱼ + εᵢⱼ โดย μ=grand mean, τⱼ=treatment effect (ค่าเบี่ยงเบนของกลุ่ม j จาก grand mean), εᵢⱼ=error term

df = (r-1)(c-1) — สุ่มตัวอย่างเพียงครั้งเดียวจากประชากรเดียว แล้วจำแนกตามสองเกณฑ์พร้อมกัน (เช่น เชื้อชาติกับการใช้กรดโฟลิกก่อนตั้งครรภ์)

3 ประเภทการใช้งานหลักของ Chi-Square Test:

3 ประเภทการทดสอบด้วย Chi-Square:

หลักการสำคัญ: Rank Transformation — เทคนิคพื้นฐานที่การทดสอบไร้พารามิเตอร์ส่วนใหญ่ใช้ร่วมกันคือแปลงข้อมูลดิบเป็นอันดับ (rank) ก่อน แล้วจึงวิเคราะห์บนอันดับแทนค่าจริง — สูญเสียข้อมูลบางส่วน (เช่น ไม่สามารถหา mean/variance ที่แท้จริงได้) แต่ทำให้การทดสอบทนทานต่อรูปแบบการแจกแจงที่ผิดปกติ

สมมติฐาน: H₀: μ₁=μ₂=...=μₖ เทียบกับ Hₐ: ไม่ใช่ทุกค่าเท่ากัน

> Eᵢⱼ = (ผลรวมแถว i × ผลรวมคอลัมน์ j) / ผลรวมทั้งหมด

- ทั้ง RR และ OR สร้าง CI ได้ด้วยสูตรอิงจากค่า chi-square: 100(1-α)%CI = point estimate^(1±zα/√X²)

#### บทที่ 12: การแจกแจงไคสแควร์และการวิเคราะห์ความถี่ (The Chi-Square Distribution and the Analysis of Frequencies)

- Perinatal Mortality Rate = รวม fetal death (อายุครรภ์≥28สัปดาห์) กับ infant death (อายุ<7วัน) เข้าด้วยกัน เพราะมักมีสาเหตุร่วมกัน

#### บทที่ 14: สถิติชีพ (Vital Statistics)

- Rate — ตัวเศษเป็นส่วนหนึ่งของตัวส่วน (เช่น จำนวนตาย/จำนวนประชากรที่เสี่ยงตาย) รูปแบบทั่วไป: [a/(a+b)]×k
> Ŝ(t) = p̂₁ × p̂₂ × ... × p̂ₜ

- ทดสอบสมมติฐานที่ไม่ใช่ข้อความเกี่ยวกับพารามิเตอร์ได้ (เช่น chi-square goodness-of-fit)
- Mann-Whitney Test (Mann-Whitney-Wilcoxon Test) — ปรับปรุงจาก Median Test โดยใช้อันดับของทุกค่าแทนแค่ตำแหน่งเทียบ median — รวมสองกลุ่มมาจัดอันดับพร้อมกัน แล้วเปรียบเทียบผลรวมอันดับของแต่ละกลุ่ม — เป็นคู่เทียบของ independent samples t-test — สมมติฐาน: สุ่มอิสระ มาตรวัดอย่างน้อย ordinal ตัวแปรต่อเนื่อง และถ้าประชากรต่างกัน ต่างแค่ตำแหน่ง (location/median) เท่านั้น
ความแตกต่างระหว่าง Rate กับ Ratio:

1) อัตราการตาย (Death Rates and Ratios):

Biostatistics: A Foundation for Analysis in the Health Sciences (9th edition) โดย Wayne W. Daniel

สรุปเนื้อหารายบทเพื่อการทบทวน — เรียบเรียงใหม่เป็นภาษาไทย (ไม่ใช่การคัดลอกต้นฉบับ)


##### 🏷️ นิยามพื้นฐาน

สถิติ (Statistics) คือศาสตร์ที่เกี่ยวกับ (1) การเก็บ จัดระเบียบ สรุป และวิเคราะห์ข้อมูล และ (2) การอนุมาน (inference) เกี่ยวกับข้อมูลทั้งชุดจากการสังเกตเพียงบางส่วน — เมื่อข้อมูลมาจากวิทยาศาสตร์ชีวภาพและการแพทย์ เรียกว่า ชีวสถิติ (Biostatistics) หนังสือแบ่งเนื้อหาเป็น 2 ส่วนใหญ่: descriptive statistics (จัดระเบียบ/สรุปข้อมูล) และ inferential statistics (อนุมานเกี่ยวกับประชากรจากกลุ่มตัวอย่าง)


##### 🔹 แหล่งที่มาของข้อมูล

บันทึกประจำ (routinely kept records เช่น เวชระเบียน), การสำรวจ (surveys), การทดลอง (experiments), และแหล่งข้อมูลภายนอก (external sources เช่น งานวิจัยที่ตีพิมพ์แล้ว)

ประเภทของตัวแปร (Variables):

- Quantitative variable — วัดค่าได้จริง บอกปริมาณ (เช่น ส่วนสูง น้ำหนัก อายุ)
- Qualitative variable — จำแนกเป็นหมวดหมู่เท่านั้น บอกคุณลักษณะ (เช่น การวินิจฉัยโรค กลุ่มชาติพันธุ์)
- Random variable — ค่าที่เกิดจากปัจจัยสุ่ม ไม่สามารถทำนายล่วงหน้าได้แม่นยำ
- Discrete variable — มีช่องว่างระหว่างค่าที่เป็นไปได้ (เช่น จำนวนผู้ป่วยรับใหม่ต่อวัน ต้องเป็นจำนวนเต็ม)
- Continuous variable — ไม่มีช่องว่าง รับค่าใดก็ได้ในช่วงที่กำหนด (เช่น ส่วนสูง น้ำหนัก) แม้ในทางปฏิบัติจะถูกบันทึกแบบปัดเศษก็ตาม

##### 🔹 Population vs. Sample

Population คือกลุ่มข้อมูล/หน่วยทั้งหมดที่เราสนใจ ณ เวลาหนึ่ง (มีขนาด N) อาจเป็น finite หรือ infinite ก็ได้ ส่วน Sample คือส่วนหนึ่งของ population (มีขนาด n)

มาตรวัด (Measurement Scales) — 4 ระดับจากต่ำไปสูง:

- Nominal scale — จำแนกเป็นหมวดหมู่ที่แยกจากกันชัดเจน ไม่มีลำดับ (เช่น ชาย-หญิง, แต่งงานแล้ว-ยังไม่แต่งงาน)
- Ordinal scale — จัดลำดับได้ แต่ระยะห่างระหว่างลำดับไม่เท่ากัน/ไม่ทราบ (เช่น อาการดีขึ้นมาก/ดีขึ้น/ไม่ดีขึ้น)
- Interval scale — จัดลำดับได้และรู้ระยะห่างที่แท้จริง แต่จุดศูนย์เป็นค่าที่กำหนดขึ้นเอง ไม่ใช่ศูนย์แท้ (เช่น องศาเซลเซียส/ฟาเรนไฮต์)
- Ratio scale — ระดับสูงสุด มีทั้งระยะห่างที่แท้จริงและจุดศูนย์แท้ (true zero) ทำให้เปรียบเทียบเป็นอัตราส่วนได้ (เช่น ส่วนสูง น้ำหนัก)

##### 🧪 การสุ่มตัวอย่างและการอนุมานทางสถิติ

Statistical inference คือกระบวนการสรุปเกี่ยวกับประชากรจากข้อมูลตัวอย่าง — เพื่อให้อนุมานได้ถูกต้อง ต้องใช้ scientific sample ไม่ใช่ตัวอย่างใดก็ได้

- Simple random sample — ตัวอย่างขนาด n จากประชากรขนาด N ที่ทุกชุดตัวอย่างที่เป็นไปได้ขนาด n มีโอกาสถูกเลือกเท่ากัน (นิยมสุ่มแบบไม่คืนที่ (without replacement) ในทางปฏิบัติ) — ใช้ตารางเลขสุ่ม (random number table) เป็นเครื่องมือ
- Systematic sampling — เลือกจุดเริ่มต้นแบบสุ่ม แล้วเลือกทุก ๆ ระยะห่าง k (interval) ถัดไปเรื่อย ๆ — สะดวกกับข้อมูลที่เก็บเป็นแฟ้ม/ลำดับ (เช่น เวชระเบียน)
- Stratified random sampling — แบ่งประชากรเป็นชั้น (strata) ที่หน่วยภายในชั้นเดียวกันคล้ายกันมากกว่าข้ามชั้น แล้วสุ่มแยกในแต่ละชั้น — ให้ความแปรปรวนต่ำกว่าการสุ่มข้ามทั้งประชากรตรง ๆ (ตัวอย่าง: สุ่มผู้ป่วยจาก trauma center แต่ละระดับ 1/2/3 แยกกัน เพราะอัตรารอดชีวิตน่าจะต่างกันตามระดับศูนย์) — มีรูปแบบย่อยคือ stratified systematic sample และ stratified sampling proportional to size (จำนวนตัวอย่างต่อชั้นแปรผันตามขนาดประชากรของชั้นนั้น เพื่อไม่ให้ชั้นเล็กถูกแทนค่าเกินจริง)

##### 🔹 ระเบียบวิธีทางวิทยาศาสตร์ (Scientific Method) และการออกแบบการทดลอง

ประกอบด้วย 4 ขั้นตอนหลัก

- การสังเกต (Observation) — พบปรากฏการณ์ที่น่าสนใจ นำไปสู่คำถามวิจัย
- การตั้งสมมติฐาน (Hypothesis) — แบ่งเป็น research hypothesis (ข้อความทั่วไป เช่น "การออกกำลังกายลดน้ำหนัก") และ statistical hypothesis (ระบุเชิงปริมาณ เช่น "น้ำหนักเฉลี่ยที่ลดลงของกลุ่มออกกำลังกายมากกว่ากลุ่มไม่ออกกำลังกาย")
- การออกแบบการทดลอง (Designing an Experiment) — การออกแบบที่ผิดพลาดเป็นสาเหตุอันดับต้น ๆ ของผลวิจัยที่ไม่ถูกต้อง ต้องคำนึงถึง accuracy (ความถูกต้อง/ตรงกับค่าจริง) และ precision (ความสม่ำเสมอ/แม่นยำในการวัดซ้ำ) ซึ่งเป็นคนละเรื่องกัน (เครื่องชั่งที่เพี้ยนคงที่ +3 ปอนด์ทุกครั้ง มี precision ดีแต่ accuracy แย่) — true experimental design ต้องมีการสุ่มแบ่งกลุ่มทดลอง (experimental/treatment group) และกลุ่มควบคุม (control group) เพื่อให้สรุปความสัมพันธ์เชิงเหตุ-ผลได้
- ข้อสรุป (Conclusion) — ผลจากการศึกษาเดียวไม่ควรถือเป็นข้อสรุปเด็ดขาด ต้องมีการทำซ้ำ (replication) หลายครั้งก่อนจะได้รับการยอมรับทางวิทยาศาสตร์อย่างมั่นคง

##### 🔹 คอมพิวเตอร์กับการวิเคราะห์ชีวสถิติ

ซอฟต์แวร์สถิติสมัยใหม่ (เช่น SPSS, SAS, R) ช่วยให้การคำนวณที่ซับซ้อนทำได้รวดเร็วและแม่นยำ ทำให้นักวิจัยทางการแพทย์เน้นการตีความผลลัพธ์และออกแบบการศึกษาที่ดีมากกว่ากังวลกับการคำนวณด้วยมือ


##### 🔹 Ordered Array

ขั้นแรกของการจัดระเบียบข้อมูลคือการเรียงค่าจากน้อยไปมาก (ordered array) ช่วยให้เห็นค่าต่ำสุด/สูงสุด และภาพรวมของข้อมูลได้ง่ายขึ้น


##### 🔹 การจัดกลุ่มข้อมูล (Frequency Distribution)

แบ่งข้อมูลเป็นช่วงชั้น (class intervals) ที่ไม่ทับซ้อนกัน — กฎทั่วไปคือควรมี 5-15 ช่วงชั้น ไม่มากไม่น้อยเกินไป มีสูตรช่วยคำนวณจำนวนช่วงชั้นที่เหมาะสมคือ Sturges' rule: k = 1 + 3.322(log₁₀n) และความกว้างช่วงชั้น w = R/k (R คือ range) แต่ท้ายที่สุดควรปรับด้วยดุลยพินิจให้อ่านง่าย (เช่น ใช้ความกว้าง 5 หรือ 10) — จากตารางความถี่สามารถคำนวณ relative frequency (สัดส่วน = ความถี่ ÷ จำนวนทั้งหมด) ซึ่งตีความได้เป็นความน่าจะเป็นเชิงประจักษ์ (empirical probability) ของค่านั้น ๆ ด้วย และมีcumulative frequency (ความถี่สะสม) ที่แสดงจำนวน/สัดส่วนที่ต่ำกว่าหรือเท่ากับค่าหนึ่ง ๆ — การแสดงข้อมูลเชิงกราฟทำได้ด้วย histogram และ frequency polygon


##### 🔹 Statistic vs. Parameter

ค่าที่คำนวณจากตัวอย่างเรียกว่า statistic ส่วนค่าที่คำนวณจากประชากรทั้งหมดเรียกว่า parameter — เป็นความแตกต่างพื้นฐานที่ใช้ตลอดทั้งเล่ม

การวัดแนวโน้มเข้าสู่ส่วนกลาง (Measures of Central Tendency):

- Mean (ค่าเฉลี่ยเลขคณิต) — μ = Σxᵢ/N (ประชากร) หรือ x̄ = Σxᵢ/n (ตัวอย่าง) — ข้อดี: มีค่าเดียวแน่นอน (uniqueness) คำนวณง่าย — ข้อเสีย: อ่อนไหวต่อค่าผิดปกติสุดขั้ว (extreme values) มาก (ตัวอย่าง: ค่าธรรมเนียมแพทย์ 5 คน $75,75,80,80,280 — mean=$118 ซึ่งไม่ได้เป็นตัวแทนที่ดีของข้อมูลชุดนี้เลย)
- Median — ค่ากึ่งกลางที่แบ่งข้อมูลเป็นสองส่วนเท่ากัน (ตำแหน่งที่ (n+1)/2 เมื่อเรียงค่าแล้ว) — ทนทานต่อค่าผิดปกติมากกว่า mean
- Mode — ค่าที่พบบ่อยที่สุด อาจมีได้หลายค่าหรือไม่มีเลยก็ได้ ใช้ได้แม้กับข้อมูลเชิงคุณภาพ (เช่น การวินิจฉัยที่พบบ่อยที่สุด)
- เมื่อ mean = median = mode ทั้งสามค่าเท่ากัน จะได้กราฟรูประฆังคว่ำแบบสมมาตร (เช่น normal distribution)

##### 🔹 Skewness (ความเบ้)

วัดความไม่สมมาตรของการกระจายข้อมูล — skewed right (positive) เมื่อหางยาวไปทางขวา (mean > mode) และ skewed left (negative) เมื่อหางยาวไปทางซ้าย (mean < mode)

การวัดการกระจาย (Measures of Dispersion):

- Range = ค่าสูงสุด - ค่าต่ำสุด — ง่ายแต่ใช้ข้อมูลแค่ 2 ค่า ให้ข้อมูลน้อย
- Variance — วัดการกระจายรอบค่าเฉลี่ย: s² = Σ(xᵢ-x̄)²/(n-1) สำหรับตัวอย่าง (หารด้วย N สำหรับประชากร σ²) — เหตุผลที่หารด้วย n-1 ไม่ใช่ n เรียกว่า degrees of freedom — เมื่อรู้ค่าเบี่ยงเบน n-1 ค่า ค่าสุดท้ายจะถูกกำหนดโดยอัตโนมัติ (เพราะผลรวมของค่าเบี่ยงเบนทั้งหมดต้องเท่ากับศูนย์) การหารด้วย n-1 จำเป็นสำหรับให้ค่า variance ของตัวอย่างใช้งานได้ถูกต้องในขั้นตอนการอนุมานทางสถิติต่อไป
- Standard Deviation (SD) = √variance — มีหน่วยเดียวกับข้อมูลต้นฉบับ (ต่างจาก variance ที่เป็นหน่วยยกกำลังสอง)
- Coefficient of Variation (C.V.) = (s/x̄)×100% — ใช้เปรียบเทียบการกระจายของข้อมูลที่มีหน่วยต่างกัน หรือค่าเฉลี่ยต่างกันมาก เพราะเป็นค่าไร้หน่วย (ตัวอย่าง: น้ำหนักผู้ชายอายุ 25 ปี mean=145 SD=10 → C.V.=6.9% เทียบกับเด็กอายุ 11 ปี mean=80 SD=10 → C.V.=12.5% แม้ SD เท่ากันแต่การกระจายสัมพัทธ์ของเด็กสูงกว่ามาก)

##### 🔹 Percentiles และ Quartiles

เปอร์เซ็นไทล์ที่ p (Pₚ) คือค่าที่ p% ของข้อมูลน้อยกว่าหรือเท่ากับค่านี้ — Q1 = เปอร์เซ็นไทล์ 25, Q2 = median = เปอร์เซ็นไทล์ 50, Q3 = เปอร์เซ็นไทล์ 75 — Interquartile Range (IQR) = Q3-Q1 สะท้อนการกระจายของข้อมูลกลาง 50% ทนทานต่อค่าผิดปกติมากกว่า range ทั้งชุด


##### 🔹 Kurtosis (ความโด่ง)

วัดว่าการกระจายข้อมูล "แหลม" หรือ "แบน" เทียบกับ normal distribution — Leptokurtic (แหลมกว่าปกติ, kurtosis>0), Platykurtic (แบนกว่าปกติ, kurtosis<0), Mesokurtic (ปกติ, kurtosis=0 ตามสูตรที่ปรับลบ 3 แล้ว)


##### 🔹 Box-and-Whisker Plot (Boxplot)

เครื่องมือแสดงผลภาพที่ใช้ Q1, median, Q3 และค่าสุดขั้ว ช่วยให้เห็นภาพรวมการกระจาย ความเบ้ และค่าผิดปกติ (outliers) ได้ในกราฟเดียว


##### 🔹 มุมมองความน่าจะเป็น 2 แบบ

- Objective probability แบ่งเป็น (1) Classical (a priori) — คำนวณจากเหตุผลเชิงนามธรรมล้วน ๆ P(E)=m/N เมื่อมี N ผลลัพธ์ที่เกิดขึ้นได้เท่า ๆ กัน (เช่น ทอยลูกเต๋า 1 หน้าใน 6 หน้า) และ (2) Relative frequency (a posteriori) — ประมาณจากการทำซ้ำจริงจำนวนมาก P(E)≈m/n (m คือจำนวนครั้งที่เกิดเหตุการณ์ n คือจำนวนครั้งทั้งหมด)
- Subjective probability — สะท้อนความเชื่อมั่นส่วนบุคคลต่อความจริงของข้อความหนึ่ง ๆ ไม่ต้องอาศัยการทำซ้ำ ใช้ได้แม้กับเหตุการณ์ที่เกิดครั้งเดียว (เช่น "โอกาสที่จะพบวิธีรักษามะเร็งใน 10 ปีข้างหน้า") — เป็นฐานคิดของ Bayesian methods ที่ใช้ prior probability (ความเชื่อก่อนหน้า) ปรับปรุงเป็น posterior probability (ความเชื่อหลังได้ข้อมูลใหม่)

##### 🔹 คุณสมบัติพื้นฐาน 3 ข้อของความน่าจะเป็น (Kolmogorov's axioms)

- P(Eᵢ) ≥ 0 เสมอ (ไม่มีความน่าจะเป็นติดลบ)
- ผลรวมความน่าจะเป็นของเหตุการณ์ที่แยกจากกันหมด (mutually exclusive) และครอบคลุมทุกความเป็นไปได้ (exhaustive) เท่ากับ 1
- สำหรับเหตุการณ์ที่แยกจากกัน (mutually exclusive) สองเหตุการณ์ P(Eᵢ หรือ Eⱼ) = P(Eᵢ) + P(Eⱼ)
ประเภทของความน่าจะเป็น:

- Marginal probability — ใช้ผลรวมชายขอบของตาราง (เช่น จำนวนคนทั้งหมดในแถว/คอลัมน์) เป็นตัวเศษ
- Conditional probability — P(A|B) = P(A∩B)/P(B) — ความน่าจะเป็นของ A "เมื่อกำหนดว่า" B เกิดขึ้นแล้ว (ตัวส่วนคือกลุ่มย่อยที่ B เกิดขึ้น ไม่ใช่ทั้งหมด)
- Joint probability — P(A∩B) — ความน่าจะเป็นที่ทั้ง A และ B เกิดขึ้นพร้อมกัน

##### 📐 Multiplication Rule

P(A∩B) = P(B)×P(A|B) = P(A)×P(B|A) — ใช้หาความน่าจะเป็นร่วมจากความน่าจะเป็นชายขอบคูณเงื่อนไข หรือย้อนกลับหาความน่าจะเป็นเงื่อนไขจากความน่าจะเป็นร่วมก็ได้


##### 📐 Addition Rule

P(A∪B) = P(A) + P(B) - P(A∩B) — ใช้เมื่อ A กับ B ไม่ได้แยกจากกันเด็ดขาด (อาจเกิดร่วมกันได้) ต้องลบส่วนที่นับซ้ำ (intersection) ออกหนึ่งครั้ง — ถ้า A กับ B แยกจากกันจริง (mutually exclusive) พจน์ P(A∩B) จะเป็น 0


##### 🔹 Independent Events (เหตุการณ์อิสระต่อกัน)

A และ B เป็นอิสระต่อกันถ้า P(A|B) = P(A) (การรู้ว่า B เกิดขึ้นไม่เปลี่ยนความน่าจะเป็นของ A) ในกรณีนี้ P(A∩B) = P(A)×P(B) — ข้อควรระวัง: "อิสระต่อกัน (independent)" กับ "แยกจากกัน (mutually exclusive)" เป็นคนละแนวคิด ไม่ใช่ความหมายเดียวกัน


##### 🔹 Complementary Events

P(Ā) = 1 - P(A) เพราะ A และส่วนเติมเต็ม Ā แยกจากกันโดยสมบูรณ์และครอบคลุมทุกความเป็นไปได้


##### 🔹 Bayes' Theorem กับการประเมินการทดสอบคัดกรอง (Screening Tests) — หัวใจสำคัญของบทนี้

เมื่อมีผลตรวจ (Test, T) เทียบกับสถานะโรคจริง (Disease, D) จัดเป็นตาราง 2x2 (บวก/ลบ × มี/ไม่มีโรค) สามารถคำนวณได้ 4 ค่า:

- Sensitivity = P(T|D) = a/(a+c) — ความน่าจะเป็นที่ผลตรวจเป็นบวก เมื่อมีโรคจริง
- Specificity = P(T̄|D̄) = d/(b+d) — ความน่าจะเป็นที่ผลตรวจเป็นลบ เมื่อไม่มีโรคจริง
- Predictive Value Positive (PPV) = P(D|T) — ความน่าจะเป็นที่มีโรคจริง เมื่อผลตรวจเป็นบวก — คำนวณด้วย Bayes' theorem:
> P(D|T) = [P(T|D)×P(D)] / [P(T|D)×P(D) + P(T|D̄)×P(D̄)]

- Predictive Value Negative (PNV) = P(D̄|T̄) — ความน่าจะเป็นที่ไม่มีโรคจริง เมื่อผลตรวจเป็นลบ — คำนวณด้วยสูตรคล้ายกัน

##### ⚠️ ประเด็นสำคัญที่สุด

Sensitivity และ Specificity เป็นคุณสมบัติของตัวทดสอบเอง (ค่อนข้างคงที่) แต่ PPV และ PNV ขึ้นกับ P(D) หรือ "อัตราชุกของโรค (prevalence) ในประชากรที่ตรวจ" ด้วยเสมอ — ตัวอย่างในหนังสือ: การทดสอบคัดกรองอัลไซเมอร์ที่มี sensitivity=97%, specificity=99% ให้ PPV สูงถึง 93% เมื่อความชุกของโรคในกลุ่มอายุ 65 ปีขึ้นไปอยู่ที่ 11.3% — แต่ถ้านำการทดสอบเดียวกันไปใช้ในกลุ่มที่มีความชุกโรคต่ำมาก PPV จะลดฮวบลงทันที (สอดคล้องกับหลักการที่พบในตำราระบาดวิทยาคลินิกเช่นกัน) การคำนวณค่าเหล่านี้ให้ถูกต้องต้องแยกใช้ prevalence ของโรคจากแหล่งข้อมูลภายนอก ไม่ใช่จากอัตราส่วนตัวอย่างในการศึกษาวิจัยสองกลุ่มที่สุ่มมาแยกกัน (กลุ่มมีโรค vs. กลุ่มไม่มีโรค) เพราะอัตราส่วนนั้นถูกกำหนดโดยผู้วิจัยเอง ไม่ใช่อัตราชุกที่แท้จริงในธรรมชาติ


##### 🔹 Probability Distribution ของตัวแปรไม่ต่อเนื่อง (Discrete)

คือตาราง/กราฟ/สูตรที่ระบุค่าที่เป็นไปได้ทั้งหมดของตัวแปรสุ่ม พร้อมความน่าจะเป็นของแต่ละค่า p(x)=P(X=x) — คุณสมบัติสำคัญ 2 ข้อ: (1) 0≤P(X=x)≤1 เสมอ (2) ผลรวมของทุกความน่าจะเป็นเท่ากับ 1 — Cumulative distribution F(x)=P(X≤x) ได้จากการบวกสะสมความน่าจะเป็นทีละค่า กราฟเรียกว่า ogive — ค่าเฉลี่ยและความแปรปรวนของการแจกแจงคำนวณจาก μ=Σxp(x) และ σ²=Σx²p(x)-μ²


##### 🔹 1) Binomial Distribution — การแจกแจงทวินาม

เกิดจาก Bernoulli trial (การทดลองที่ผลลัพธ์มีแค่ 2 แบบ "สำเร็จ/ล้มเหลว") ที่ทำซ้ำภายใต้เงื่อนไข Bernoulli process: (1) แต่ละครั้งมีผลแค่ 2 แบบ (2) ความน่าจะเป็นสำเร็จ p คงที่ทุกครั้ง (3) แต่ละครั้งเป็นอิสระต่อกัน — สูตร:

> f(x) = ₙCₓ pˣ qⁿ⁻ˣ, x=0,1,...,n (โดย q=1-p)

โดย ₙCₓ = n!/[x!(n-x)!] คือจำนวนวิธีจัดลำดับที่แตกต่างกัน (combination) — Mean = np, Variance = np(1-p) — ใช้ตอบคำถามประเภท "โอกาสที่จะพบผู้ป่วยพอดี x คนจาก n คนที่มีลักษณะหนึ่ง ๆ" (เช่น ทารกคลอดครบกำหนด, ผู้ป่วยความดันสูง) — มีตารางความน่าจะเป็นสะสมสำเร็จรูปช่วยลดการคำนวณมือ


##### 🔹 2) Poisson Distribution — การแจกแจงปัวซง

ใช้กับการนับ "จำนวนเหตุการณ์ที่เกิดขึ้นในช่วงเวลา/พื้นที่หนึ่ง ๆ" สูตร:

> f(x) = e⁻λλˣ/x!, x=0,1,2,...

โดย λ (lambda) คือค่าเฉลี่ยจำนวนครั้งที่เกิดเหตุการณ์ในช่วงที่กำหนด — เงื่อนไขของ Poisson process: (1) เหตุการณ์เกิดอิสระต่อกัน (2) เกิดได้ไม่จำกัดจำนวนในทางทฤษฎี (3) ความน่าจะเป็นแปรผันตรงกับความยาวของช่วง (4) โอกาสเกิด 2 เหตุการณ์พร้อมกันในช่วงเล็กจิ๋วนั้นน้อยมากจนตัดทิ้งได้ — คุณสมบัติพิเศษ: Mean = Variance = λ — ใช้บ่อยในทางการแพทย์กับอัตราการเกิดโรค/ภาวะแทรกซ้อนที่หายาก (เช่น จำนวนผู้ป่วยแพ้ยารุนแรงต่อปี) และยังใช้ประมาณค่า Binomial distribution เมื่อ n มากและ p น้อย (โดยตั้ง λ=np)


##### 🔹 3) Continuous Probability Distributions

เมื่อข้อมูลมีจำนวนมากและช่วงชั้นแคบลงเรื่อย ๆ histogram จะเปลี่ยนเป็นเส้นโค้งเรียบ (smooth curve) เรียกว่า probability density function (pdf) — พื้นที่ใต้เส้นโค้งทั้งหมดเท่ากับ 1 และพื้นที่ระหว่างจุด a กับ b คือ P(a<X<b) — ความน่าจะเป็นที่ตัวแปรต่อเนื่องจะมีค่าใดค่าหนึ่งพอดี (จุดเดียว) เท่ากับ 0 เสมอ เพราะพื้นที่เหนือจุดหนึ่งจุดบนแกน x เท่ากับศูนย์


##### 🔹 4) Normal (Gaussian) Distribution — การแจกแจงปกติ — สำคัญที่สุดในวิชาสถิติทั้งหมด

สูตร: f(x) = [1/(σ√2π)]·e^{-(x-μ)²/2σ²} กำหนดโดย 2 พารามิเตอร์: μ (mean, location parameter — กำหนดตำแหน่งกึ่งกลาง) และ σ (SD, shape parameter — กำหนดความกว้าง/แคบ)

คุณสมบัติสำคัญของ Normal Distribution:

- สมมาตรรอบค่าเฉลี่ย μ (ครึ่งซ้าย = กระจกเงาของครึ่งขวา)
- mean = median = mode
- พื้นที่ใต้กราฟทั้งหมด = 1 (แบ่งครึ่งซ้าย-ขวาข้างละ 50%)
- กฎ 68-95-99.7: พื้นที่ในช่วง μ±1σ ≈ 68%, μ±2σ ≈ 95%, μ±3σ ≈ 99.7% ของข้อมูลทั้งหมด
- เป็น "ตระกูล" ของการแจกแจง — ค่า μ ต่างกันทำให้กราฟเลื่อนตำแหน่ง ค่า σ ต่างกันทำให้กราฟแบน/แหลมต่างกัน

##### 🔹 Standard Normal Distribution (Z-distribution)

สมาชิกพิเศษของตระกูล Normal ที่มี μ=0, σ=1 — แปลงค่าตัวแปรใด ๆ ให้เป็นมาตรฐานด้วยสูตร z-transformation:

> z = (x - μ)/σ

ค่า z บอกว่า x อยู่ห่างจากค่าเฉลี่ยกี่ SD (z บวก = อยู่เหนือค่าเฉลี่ย, z ลบ = อยู่ใต้ค่าเฉลี่ย) — ใช้ตาราง Standard Normal (Appendix Table D) หาพื้นที่ใต้กราฟ/ความน่าจะเป็นได้โดยไม่ต้องคำนวณอินทิกรัลเอง — เป็นเครื่องมือพื้นฐานที่ใช้ตลอดทั้งเล่มสำหรับการประมาณค่า (estimation) และการทดสอบสมมติฐาน (hypothesis testing) ในบทถัดไป


##### 🏷️ Sampling Distribution

การแจกแจงของค่าที่เป็นไปได้ทั้งหมด ของสถิติหนึ่ง ๆ (เช่น mean, proportion) ที่คำนวณจากตัวอย่างขนาดเดียวกันทุกชุดที่สุ่มได้จากประชากรเดียวกัน — เป็นแนวคิดหัวใจสำคัญที่สุดของการอนุมานทางสถิติทั้งเล่ม เพราะช่วยให้ (1) ตอบคำถามความน่าจะเป็นเกี่ยวกับค่าสถิติของตัวอย่างได้ และ (2) เป็นรากฐานทางทฤษฎีที่ทำให้กระบวนการอนุมานทางสถิติสมเหตุสมผล


##### 🔹 1) Sampling Distribution ของค่าเฉลี่ยตัวอย่าง (x̄)

- ถ้าสุ่มจากประชากรที่มีการแจกแจงแบบปกติ (normal) อยู่แล้ว → การแจกแจงของ x̄ จะเป็นปกติเสมอ ไม่ว่าขนาดตัวอย่างจะเท่าไร โดยมี mean μₓ̄=μ (เท่ากับ mean ประชากร) และ variance σₓ̄²=σ²/n
- ถ้าสุ่มจากประชากรที่ไม่ใช่การแจกแจงปกติ (หรือไม่ทราบรูปแบบ) → ต้องอาศัย Central Limit Theorem (ทฤษฎีบทลิมิตกลาง) — หัวใจสำคัญที่สุดของบทนี้:
> ไม่ว่าประชากรต้นทางจะมีรูปแบบการแจกแจงอย่างไรก็ตาม (มี mean=μ, variance=σ² จำกัด) การแจกแจงของ x̄ จากตัวอย่างขนาด n จะมี mean=μ, variance=σ²/n และเข้าใกล้การแจกแจงแบบปกติมากขึ้นเรื่อย ๆ เมื่อ n มีขนาดใหญ่ขึ้น

กฎง่าย ๆ ที่ใช้กันทั่วไปคือ n≥30 มักเพียงพอ ที่จะถือว่า x̄ มีการแจกแจงใกล้เคียงปกติแล้ว — ทำให้แปลงเป็น standard normal ได้ด้วยสูตร:

> z = (x̄ - μ)/(σ/√n)

Standard Error of the Mean = σ/√n คือรากที่สองของ variance ของ sampling distribution — ยิ่ง n มากขึ้น standard error ยิ่งเล็กลง (การประมาณค่าเฉลี่ยประชากรแม่นยำขึ้น)


##### 🔹 การสุ่มแบบไม่คืนที่จากประชากรจำกัด (Finite Population Correction)

เมื่อสุ่มโดยไม่คืนที่จากประชากรที่มีขนาดจำกัด N ต้องคูณ variance ด้วย finite population correction factor = (N-n)/(N-1):

> σₓ̄² = (σ²/n) × [(N-n)/(N-1)]

ในทางปฏิบัติ มักละเลย correction factor นี้เมื่อ n/N ≤ .05 (ตัวอย่างขนาดเล็กเทียบกับประชากร) เพราะผลต่างมีน้อยมาก


##### 🔹 2) Sampling Distribution ของผลต่างระหว่างค่าเฉลี่ยสองตัวอย่าง (x̄₁ - x̄₂)

ใช้เมื่อต้องการเปรียบเทียบค่าเฉลี่ยของสองประชากร (เช่น เปรียบเทียบระดับคอเลสเตอรอลระหว่างคนทำงานนั่งโต๊ะกับคนใช้แรงงาน) — ถ้าสุ่มจากสองประชากรที่เป็นอิสระต่อกัน การแจกแจงของ x̄₁-x̄₂ จะมี:

> mean = μ₁ - μ₂, variance = σ₁²/n₁ + σ₂²/n₂

ข้อสำคัญ: แม้ต้องการ "ผลต่าง" ของค่าเฉลี่ย แต่ variance ของทั้งสองประชากรจะถูก "บวกกันเสมอ" (ไม่ใช่ลบกัน) เพราะความแปรปรวนของทั้งสองแหล่งข้อมูลเพิ่มความไม่แน่นอนสะสมเข้าด้วยกัน — สูตร z-transformation:

> z = [(x̄₁-x̄₂) - (μ₁-μ₂)] / √(σ₁²/n₁ + σ₂²/n₂)

ถ้าสุ่มจากประชากรที่ไม่ใช่ normal หรือไม่ทราบรูปแบบ แต่ n₁,n₂ มีขนาดใหญ่พอ (>30) ก็ยังใช้ Central Limit Theorem ได้เช่นเดียวกัน


##### 🔹 3) Sampling Distribution ของสัดส่วนตัวอย่าง (p̂)

ใช้กับตัวแปรที่เป็น dichotomous (เช่น เป็นโรค/ไม่เป็นโรค อ้วน/ไม่อ้วน) — เมื่อขนาดตัวอย่างใหญ่พอ p̂ จะมีการแจกแจงใกล้เคียงปกติ ด้วย mean=p (สัดส่วนจริงของประชากร) และ variance = p(1-p)/n = pq/n โดยที่ q=1-p — สูตร z-transformation:

> z = (p̂ - p) / √[p(1-p)/n]

เกณฑ์ที่ใช้การประมาณด้วยแบบปกติได้อย่างเหมาะสม: ทั้ง np และ n(1-p) ต้องมากกว่า 5 — สามารถปรับปรุงความแม่นยำเพิ่มเติมด้วย correction for continuity (ปรับแก้เพราะใช้การแจกแจงต่อเนื่องมาประมาณการแจกแจงไม่ต่อเนื่อง)


##### 🔹 4) Sampling Distribution ของผลต่างระหว่างสัดส่วนสองตัวอย่าง (p̂₁-p̂₂)

ใช้หลักการเดียวกับผลต่างของค่าเฉลี่ย — เมื่อขนาดตัวอย่างใหญ่พอ การแจกแจงของ p̂₁-p̂₂ ใกล้เคียงปกติ โดยมี mean=p₁-p₂ และ variance=p₁q₁/n₁+p₂q₂/n₂ — ใช้เปรียบเทียบสัดส่วนของสองกลุ่ม (เช่น อัตราการเกิดโรคระหว่างกลุ่มที่สูบบุหรี่กับไม่สูบบุหรี่)


##### ✅ สรุปภาพรวม

บทนี้เป็นสะพานเชื่อมระหว่างสถิติเชิงพรรณนา (บทที่ 1-4) กับการอนุมานทางสถิติ (บทที่ 6 เป็นต้นไป) — Central Limit Theorem คือกุญแจสำคัญที่ทำให้เราสามารถใช้การแจกแจงแบบปกติในการคำนวณความน่าจะเป็นและสร้าง confidence interval / ทดสอบสมมติฐานเกี่ยวกับค่าเฉลี่ยและสัดส่วนได้ แม้ประชากรต้นทางจะไม่เป็น normal distribution ก็ตาม ตราบใดที่ขนาดตัวอย่างใหญ่เพียงพอ


##### 🔹 แนวคิดพื้นฐาน

การประมาณค่าคือการคำนวณสถิติจากตัวอย่างเพื่อเป็นค่าประมาณของพารามิเตอร์ประชากร มี 2 รูปแบบ:

- Point estimate — ค่าตัวเลขเดียว (เช่น x̄ เป็น point estimate ของ μ)
- Interval estimate (Confidence Interval) — ช่วงค่าที่มีระดับความเชื่อมั่นกำหนดว่าจะครอบคลุมพารามิเตอร์จริง

##### 🏷️ Unbiased Estimator

ตัวประมาณค่า T เป็น unbiased ของพารามิเตอร์ θ ถ้า E(T)=θ (ค่าคาดหวังเท่ากับค่าพารามิเตอร์จริงพอดี) — x̄, p̂, และผลต่างของค่าเฉลี่ย/สัดส่วนสองกลุ่ม ล้วนเป็น unbiased estimator ของพารามิเตอร์ที่สอดคล้องกัน


##### 🔹 Sampled Population vs. Target Population

Sampled population คือประชากรที่สุ่มตัวอย่างมาจริง ส่วน Target population คือประชากรที่ต้องการอนุมานถึง — การอนุมานทางสถิติใช้ได้ถูกต้องเฉพาะกับ sampled population เท่านั้น ถ้าต้องการอนุมานไปถึง target population ที่ต่างออกไป ต้องอาศัยเหตุผลเชิงเนื้อหา (non-statistical) เพิ่มเติมว่าทั้งสองประชากรคล้ายกันเพียงพอ


##### 📐 สูตรทั่วไปของ Confidence Interval

> Estimator ± (Reliability Coefficient) × (Standard Error)

การตีความ Confidence Interval มี 2 แบบ:

- Probabilistic interpretation — ถ้าสุ่มตัวอย่างซ้ำ ๆ จำนวนมาก 100(1-α)% ของช่วงที่สร้างด้วยวิธีนี้จะครอบคลุมค่าพารามิเตอร์จริง
- Practical interpretation — เรามั่นใจ 100(1-α)% ว่าช่วงที่คำนวณได้ครั้งนี้ครอบคลุมค่าพารามิเตอร์จริง

##### 🔹 1) CI สำหรับค่าเฉลี่ยประชากร (μ)

- เมื่อทราบ σ (variance ประชากร) และสุ่มจาก normal population (หรือ n ใหญ่พอ): x̄ ± z₍₁₋α/2₎(σ/√n)
- The t Distribution: เมื่อไม่ทราบ σ (กรณีทั่วไปในชีวิตจริง) ต้องใช้ s (sample SD) แทน และเปลี่ยนจาก z เป็น t distribution ซึ่งมีคุณสมบัติ: สมมาตรรอบ 0, แบนกว่าและหางหนากว่า normal distribution, เป็น "ตระกูล" ของการแจกแจงตาม degrees of freedom (df=n-1), และเข้าใกล้ normal distribution เมื่อ df มากขึ้น — สูตร: x̄ ± t₍₁₋α/2,n-1₎(s/√n)

##### 🔹 2) CI สำหรับผลต่างระหว่างค่าเฉลี่ยสองประชากร (μ₁-μ₂)

(x̄₁-x̄₂) ± (reliability coeff)×√(σ₁²/n₁+σ₂²/n₂) — ถ้าช่วงที่ได้ไม่รวมค่า 0 แสดงว่าค่าเฉลี่ยสองประชากรน่าจะแตกต่างกันจริง ถ้าช่วงรวมค่า 0 แปลว่าค่าเฉลี่ยทั้งสองอาจเท่ากันได้

- เมื่อไม่ทราบ σ แต่สมมติว่าvariance ของสองประชากรเท่ากัน ต้องคำนวณ Pooled variance:
> s²ₚ = [(n₁-1)s₁² + (n₂-1)s₂²] / (n₁+n₂-2)

แล้วใช้ df=n₁+n₂-2 กับ t-distribution

- ถ้าvariance ไม่เท่ากัน ต้องใช้วิธีแก้ปัญหาแบบ Behrens-Fisher/Welch (สูตรซับซ้อนกว่า)

##### 🔹 3) CI สำหรับสัดส่วนประชากร (p)

p̂ ± z₍₁₋α/2₎√[p̂(1-p̂)/n] — ใช้ p̂ แทน p ที่ไม่รู้ค่าจริงในการประมาณ standard error


##### 🔹 4) CI สำหรับผลต่างระหว่างสัดส่วนสองประชากร (p₁-p₂)

(p̂₁-p̂₂) ± z₍₁₋α/2₎√[p̂₁(1-p̂₁)/n₁ + p̂₂(1-p̂₂)/n₂]


##### 🔹 การกำหนดขนาดตัวอย่าง (Sample Size Determination)

หลักการคือกำหนด "ความกว้างที่ยอมรับได้ของ CI" (d = margin of error) ล่วงหน้า แล้วแก้สมการย้อนกลับหา n:

- สำหรับค่าเฉลี่ย: n = z²σ²/d² (เมื่อ ignore finite population correction) — ต้องมีค่าประมาณ σ ล่วงหน้าจาก pilot sample, การศึกษาก่อนหน้า, หรือประมาณคร่าว ๆ ว่า σ≈R/6 (range หารด้วย 6)
- สำหรับสัดส่วน: n = z²pq/d² — ถ้าไม่มีค่าประมาณ p มาก่อนเลย ให้ใช้ p=0.5 เพราะเป็นค่าที่ให้ n มากที่สุด (safest แต่อาจสิ้นเปลืองทรัพยากรเกินจำเป็นถ้า p จริงห่างจาก 0.5 มาก)
- ผลลัพธ์ n ที่คำนวณได้เศษเสมอต้องปัดขึ้น (round up) เป็นจำนวนเต็มถัดไปเสมอ เพื่อให้แน่ใจว่าได้ความแม่นยำตามต้องการ

##### 🔹 5) CI สำหรับ Variance ของประชากร (σ²) — ใช้ Chi-Square Distribution

ปริมาณ (n-1)s²/σ² มีการแจกแจงแบบ chi-square (χ²) ด้วย df=n-1 (เมื่อสุ่มจาก normal population) — CI สำหรับ σ²:

> (n-1)s² / χ²₍₁₋α/2₎ < σ² < (n-1)s² / χ²₍α/2₎


##### ⚠️ ข้อควรระวังสำคัญ

เนื่องจาก chi-square distribution ไม่สมมาตร (ต่างจาก normal) จุดประมาณค่า (point estimate) จะไม่อยู่ตรงกลางของ CI และวิธีนี้ไม่ได้ให้ช่วงที่แคบที่สุดเท่าที่เป็นไปได้ นอกจากนี้ผลลัพธ์อ่อนไหวมากต่อสมมติฐานว่าประชากรมีการแจกแจงแบบ normal ถ้าไม่เป็นจริงผลอาจคลาดเคลื่อนมาก


##### 🔹 6) CI สำหรับอัตราส่วนของ Variance สองประชากร (σ₁²/σ₂²) — ใช้ F Distribution

ปริมาณ (s₁²/σ₁²)/(s₂²/σ₂²) มีการแจกแจงแบบ F distribution ที่กำหนดโดย 2 ค่า degrees of freedom (numerator df=n₁-1, denominator df=n₂-1) — สูตร CI:

> (s₁²/s₂²)/F₍₁₋α/2₎ < σ₁²/σ₂² < (s₁²/s₂²)/F₍α/2₎

ประโยชน์สำคัญ: ใช้ตรวจสอบว่าสมมติฐานความเท่ากันของ variance สองกลุ่ม (ที่จำเป็นสำหรับการใช้ pooled variance ในข้อ 2) เป็นจริงหรือไม่ — ถ้า CI ของอัตราส่วนนี้รวมค่า 1 แสดงว่า variance ของสองประชากรอาจเท่ากันได้จริง วิธีการทดสอบนี้เป็นที่รู้จักในชื่อ F-max Test หรือ Variance Ratio Test


##### 🏷️ Research Hypothesis vs. Statistical Hypothesis

Research hypothesis คือข้อสันนิษฐานทั่วไปที่กระตุ้นให้เกิดการวิจัย ส่วน Statistical hypothesis คือข้อความที่ถูกจัดรูปแบบให้ทดสอบได้ด้วยวิธีทางสถิติ — Null Hypothesis (H₀) คือสมมติฐานที่ถูกทดสอบ (มักเป็น "ไม่มีความแตกต่าง") ส่วน Alternative Hypothesis (Hₐ) คือสิ่งที่เราจะเชื่อถ้าปฏิเสธ H₀ ได้ — กติกาการตั้งสมมติฐาน: (1) สิ่งที่นักวิจัยหวังจะสรุปได้มักอยู่ใน Hₐ (2) H₀ ต้องมีเครื่องหมายเท่ากับเสมอ (=, ≤, หรือ ≥) (3) H₀ คือสิ่งที่ถูกทดสอบจริง (4) H₀ กับ Hₐ ต้องครอบคลุมทุกความเป็นไปได้ร่วมกัน

ขั้นตอนการทดสอบสมมติฐาน 10 ขั้นตอน:

- Data — ระบุชนิดข้อมูล (นับ/วัด)
- Assumptions — เงื่อนไขที่ต้องเป็นจริง (normality, ความเท่ากันของ variance, ความเป็นอิสระของตัวอย่าง)
- Hypotheses — ตั้ง H₀ และ Hₐ
- Test statistic — สูตรทั่วไป: (สถิติที่เกี่ยวข้อง - ค่าพารามิเตอร์ที่ตั้งสมมติฐาน) / (standard error ของสถิตินั้น)
- Distribution of test statistic — ระบุว่าสถิติทดสอบมีการแจกแจงแบบใด (z, t, χ², F) เมื่อ H₀ เป็นจริง
- Decision rule — กำหนด rejection region และ critical value ล่วงหน้าตามค่า α ที่เลือก (ก่อนดูข้อมูลจริง เพื่อความเป็นกลาง)
- Calculation — คำนวณค่าสถิติทดสอบจากข้อมูลตัวอย่างจริง
- Statistical decision — reject หรือ fail to reject H₀
- Conclusion — ตีความผลในบริบท
- p-value — ความน่าจะเป็นที่จะได้ค่าสถิติทดสอบที่ "สุดขั้วเท่ากับหรือมากกว่า" ค่าที่สังเกตได้ ถ้า H₀ เป็นจริง — กติกา: ถ้า p-value ≤ α ให้ปฏิเสธ H₀, ถ้า p-value > α ไม่ปฏิเสธ H₀

##### ⚠️ ข้อควรระวังสำคัญ

การทดสอบสมมติฐานไม่เคย "พิสูจน์" สมมติฐานใด ๆ — เมื่อไม่ปฏิเสธ H₀ เราไม่พูดว่า H₀ "เป็นจริง" (accept) แต่พูดว่า "อาจเป็นจริง" (not rejected) เพราะอาจเกิด Type II error ได้


##### 🏷️ Type I และ Type II Errors

- Type I error (α) — ปฏิเสธ H₀ ทั้งที่จริง ๆ H₀ ถูกต้อง — ค่า α ถูกกำหนดไว้ล่วงหน้าโดยผู้วิจัย (มักเป็น .01, .05, .10)
- Type II error (β) — ไม่ปฏิเสธ H₀ ทั้งที่จริง ๆ H₀ ผิด — β ไม่ได้ถูกควบคุมโดยตรงเหมือน α และในทางปฏิบัติมักมีค่ามากกว่า α

##### 🔹 ความเชื่อมโยงระหว่าง Confidence Interval กับ Hypothesis Testing

สามารถทดสอบ H₀ ได้ด้วย CI เช่นกัน — ถ้าค่าพารามิเตอร์ที่ตั้งสมมติฐาน (เช่น μ₀) ไม่อยู่ใน 100(1-α)% CI ให้ปฏิเสธ H₀ ที่ระดับนัยสำคัญ α ถ้าอยู่ใน CI ไม่ปฏิเสธ H₀ — สองวิธีนี้ให้ข้อสรุปตรงกันเสมอ (สำหรับ two-sided test)


##### 🔹 One-tailed vs. Two-tailed Tests

ถ้า Hₐ มีเครื่องหมาย ≠ (ต้องการรู้ว่า "ต่างกัน" ไม่ว่าทิศทางไหน) → two-tailed test rejection region แบ่งครึ่งสองด้าน — ถ้า Hₐ มีเครื่องหมาย < หรือ > (สนใจทิศทางเดียว) → one-tailed test rejection region อยู่ด้านเดียวทั้งหมด

การทดสอบสมมติฐานสำหรับพารามิเตอร์ต่าง ๆ (ใช้หลักการเดียวกับการหา CI ในบทที่ 6 แต่กลับทิศทางตรรกะ):

- ค่าเฉลี่ยเดี่ยว (μ): z = (x̄-μ₀)/(σ/√n) เมื่อทราบ σ, หรือ t = (x̄-μ₀)/(s/√n) เมื่อไม่ทราบ σ (df=n-1)
- ผลต่างระหว่างสองค่าเฉลี่ย (μ₁-μ₂): ใช้ z หรือ t (พร้อม pooled variance ถ้าสมมติว่า variance เท่ากัน) เหมือนบทที่ 6
- Paired Comparisons (การเปรียบเทียบแบบจับคู่) — ใช้เมื่อข้อมูลสองชุดไม่เป็นอิสระต่อกัน (เช่น วัดก่อน-หลังในผู้ป่วยคนเดียวกัน, ฝาแฝด, จับคู่ตามลักษณะ) — เหตุผลที่ต้องจับคู่: ช่วยกำจัดความแปรปรวนจากปัจจัยแทรกซ้อน (extraneous variation) ที่อาจบดบังหรือสร้างความแตกต่างปลอมขึ้นมา (ตัวอย่าง: เปรียบเทียบครีมกันแดด 2 ชนิดบนหลังคนเดียวกันคนละข้าง ดีกว่าเปรียบเทียบระหว่างคนสองกลุ่มที่อาจมีสีผิวต่างกันโดยบังเอิญ) — วิเคราะห์จากค่าผลต่าง (dᵢ) ของแต่ละคู่ แล้วทดสอบด้วย t = (d̄-μd₀)/(sd̄) โดยที่ sd̄=sd/√n (df=n-1) — ข้อดี: ไม่ต้องกังวลเรื่องความเท่ากันของ variance เหมือนตัวอย่างอิสระ เพราะเหลือตัวแปรเดียว (ผลต่าง)
- สัดส่วนเดี่ยว (p): z = (p̂-p₀)/√[p₀(1-p₀)/n] — ข้อสำคัญ: ใช้ p₀ (ค่าตั้งสมมติฐาน) ไม่ใช่ p̂ ในการคำนวณ standard error เพราะการทดสอบทั้งหมดตั้งอยู่บนสมมติฐานว่า H₀ เป็นจริง
- ผลต่างระหว่างสองสัดส่วน (p₁-p₂): ใช้หลักการคล้ายกัน โดยรวม p̂ ทั้งสองกลุ่มเป็น pooled proportion ก่อนคำนวณ standard error ภายใต้ H₀
- Variance เดี่ยว (σ²): ใช้ chi-square distribution χ²=(n-1)s²/σ₀²
- อัตราส่วนของสอง Variance (σ₁²/σ₂²): ใช้ F distribution — มักใช้ตรวจสอบสมมติฐานความเท่ากันของ variance ก่อนเลือกวิธี pooled-t หรือ separate-variance-t

##### 🔹 Type II Error และ Power ของการทดสอบ — เจาะลึก

- Power (1-β) = ความน่าจะเป็นที่จะปฏิเสธ H₀ ได้ถูกต้องเมื่อ H₀ เป็นเท็จจริง — เป็นตัวชี้วัดว่าการทดสอบ "ไวพอ" จะจับความแตกต่างที่มีอยู่จริงได้หรือไม่
- β ขึ้นกับ 4 ปัจจัย: (1) ค่าจริงของพารามิเตอร์ (2) ค่าที่ตั้งสมมติฐาน (3) ค่า α ที่เลือก (4) ขนาดตัวอย่าง n
- ยิ่งค่าพารามิเตอร์จริงอยู่ใกล้ค่าที่ตั้งสมมติฐาน (H₀) มากเท่าไร β ยิ่งสูง (ยากที่จะตรวจจับความแตกต่างเล็กน้อย) — ยิ่งห่างกันมาก β ยิ่งต่ำ (power สูง)
- Power Curve — กราฟแสดง 1-β ที่ค่าทางเลือกต่าง ๆ ของพารามิเตอร์ ช่วยให้เห็นภาพว่าการทดสอบมีความสามารถแยกแยะ (discriminate) ได้ดีแค่ไหน (two-tailed test ให้กราฟรูปตัว V, one-tailed test ให้กราฟรูปตัว S ยืด)
- Operating Characteristic (OC) Curve — พล็อตค่า β แทน 1-β (เป็นส่วนกลับของ power curve)

##### 🔹 การกำหนดขนาดตัวอย่างเพื่อควบคุมทั้ง Type I และ Type II Error พร้อมกัน

ต่างจากบทที่ 6 ที่คุมแค่ α (ผ่าน confidence coefficient) ในบทนี้หากต้องการควบคุมทั้ง α และ β ให้อยู่ในระดับที่กำหนดพร้อมกัน โดยระบุค่าทางเลือก μ₁ ที่ต้องการตรวจจับให้ได้ ใช้สูตร:

> n = [(z₀+z₁)σ / (μ₀-μ₁)]²

โดย z₀ สอดคล้องกับ α และ z₁ สอดคล้องกับ β ที่เลือก — ยิ่งต้องการ power สูง (β ต่ำ) และตรวจจับความแตกต่างเล็ก (μ₀-μ₁ น้อย) ยิ่งต้องใช้ขนาดตัวอย่างใหญ่ขึ้นมาก


##### 🔹 เหตุผลที่ต้องมี ANOVA

เมื่อต้องการเปรียบเทียบค่าเฉลี่ยของมากกว่า 2 กลุ่ม การทำ t-test เทียบทีละคู่หลาย ๆ ครั้งจะเพิ่มโอกาสเกิด Type I error สะสม อย่างมาก — ตัวอย่างในหนังสือ: ถ้ามี 5 กลุ่ม ต้องเทียบ 10 คู่ (₅C₂) แม้ตั้ง α=.05 ต่อครั้ง แต่โอกาสเกิด Type I error อย่างน้อย 1 ครั้งจากทั้งหมดสูงถึง 40.13% — ANOVA แก้ปัญหานี้โดยทดสอบทุกกลุ่มพร้อมกันในการทดสอบเดียว โดยการแบ่งส่วน (partition) ความแปรปรวนรวมทั้งหมดออกเป็นองค์ประกอบที่มาจากแหล่งต่าง ๆ


##### 🔹 ตัวแปร 3 ชนิดในการทดลอง ANOVA

(1) Treatment variable — ตัวแปรที่สนใจศึกษา (เช่น ชนิดยา) (2) Response variable — ตัวแปรผลลัพธ์ที่วัด (3) Extraneous variable — ปัจจัยแทรกซ้อนอื่นที่ไม่ใช่จุดสนใจหลัก


##### 🏷️ 1) Completely Randomized Design (CRD) — One-Way ANOVA

สุ่มหน่วยทดลองเข้ากลุ่มทรีตเมนต์ต่าง ๆ อย่างสมบูรณ์ (ใช้ตารางเลขสุ่มกำหนด)

Model: xᵢⱼ = μ + τⱼ + εᵢⱼ โดย μ=grand mean, τⱼ=treatment effect (ค่าเบี่ยงเบนของกลุ่ม j จาก grand mean), εᵢⱼ=error term

สมมติฐาน (assumptions) ของ Fixed-Effects Model: (a) แต่ละกลุ่มเป็นตัวอย่างสุ่มอิสระ (b) แต่ละประชากรมีการแจกแจงแบบ normal (c) variance ของทุกกลุ่มเท่ากัน (homogeneity of variance) (d) ผลรวมของ τⱼ ทั้งหมดเท่ากับ 0

สมมติฐาน: H₀: μ₁=μ₂=...=μₖ เทียบกับ Hₐ: ไม่ใช่ทุกค่าเท่ากัน


##### 📐 การแบ่งส่วนผลรวมกำลังสอง (Sum of Squares)

> SST (Total) = SSA (Among/Between groups) + SSW (Within groups)

- SST = Σ(xᵢⱼ-x̄..)² — ความแปรปรวนรวมทั้งหมด
- SSA = Σnⱼ(x̄.ⱼ-x̄..)² — ความแปรปรวน "ระหว่างกลุ่ม" (สะท้อนความแตกต่างของทรีตเมนต์)
- SSW = Σ(xᵢⱼ-x̄.ⱼ)² — ความแปรปรวน "ภายในกลุ่ม" (สะท้อนความแปรปรวนตามธรรมชาติ/สุ่ม)
ตัวประมาณค่าความแปรปรวนร่วม (σ²) สองตัว:

- MSW (Within groups Mean Square) = SSW/(N-k) — ประมาณ σ² ได้เสมอไม่ว่า H₀ จริงหรือไม่ (ตราบใดที่ variance เท่ากันจริง)
- MSA (Among groups Mean Square) = SSA/(k-1) — ประมาณ σ² ได้ถูกต้องเฉพาะเมื่อ H₀ เป็นจริงเท่านั้น (ถ้า H₀ เท็จ ค่านี้จะพองตัวขึ้นจากความแตกต่างจริงของค่าเฉลี่ย)

##### 📐 Test Statistic — Variance Ratio (V.R.) หรือ F

> F = MSA / MSW

ถ้า H₀ จริง ค่า F ควรใกล้ 1 (สองตัวประมาณใกล้เคียงกัน) — ถ้า H₀ เท็จ MSA จะโตกว่า MSW มาก ทำให้ F สูงขึ้นชัดเจน — F มีการแจกแจงแบบ F distribution ด้วย numerator df=k-1, denominator df=N-k — ปฏิเสธ H₀ เมื่อค่า F ที่คำนวณได้ ≥ ค่าวิกฤตจากตาราง F

ANOVA Table สรุปผลการคำนวณเป็นตาราง: Source of Variation | Sum of Squares | df | Mean Square | F


##### 🔹 Multiple Comparison Procedures — หลัง ANOVA พบว่ามีความแตกต่างแล้ว จะรู้ได้อย่างไรว่า "คู่ไหน" ต่างกัน

- Tukey's HSD Test (Honestly Significant Difference) — ใช้ studentized range statistic (q) คำนวณค่าวิกฤตเดียว (HSD) แล้วเทียบผลต่างสัมบูรณ์ของทุกคู่ค่าเฉลี่ยกับ HSD — ถ้าขนาดกลุ่มไม่เท่ากันใช้สูตรดัดแปลง Tukey-Kramer method (HSD*)
- Bonferroni's Method — แบ่งค่า α โดยจำนวนคู่ที่ทดสอบทั้งหมด (α/k) เพื่อควบคุม overall Type I error ไม่ให้เกิน α ที่ตั้งไว้ (เช่น ถ้ามี 3 คู่ทดสอบและ α=.05 → ใช้เกณฑ์ α/3=.017 ต่อการทดสอบแต่ละคู่) — เป็นวิธีที่ตรงไปตรงมาแต่ระมัดระวังมากเกินไป (conservative) เมื่อจำนวนคู่ทดสอบมาก
- หลักการสำคัญ: ต้องควบคุมความเสี่ยง Type I error ที่สะสมจากการทดสอบหลายคู่ ไม่ใช่ทำ t-test แยกทีละคู่ตามใจโดยไม่ปรับค่า α

##### 🏷️ 2) Randomized Complete Block Design (RCBD) — Two-Way ANOVA

พัฒนาโดย R.A. Fisher เพื่องานวิจัยเกษตรกรรม — แบ่งหน่วยทดลองเป็น blocks (กลุ่มที่คล้ายกันภายในบล็อก) แล้วสุ่มทรีตเมนต์ภายในแต่ละบล็อก — แต่ละทรีตเมนต์ต้องปรากฏในทุกบล็อก

วัตถุประสงค์: แยก "ความแปรปรวนจากบล็อก" ออกจาก error term ทำให้ error mean square เล็กลง และ F ratio เพิ่มขึ้น → เพิ่มโอกาสตรวจพบความแตกต่างของทรีตเมนต์ได้ (power สูงขึ้น) — ตัวอย่างการ block: ใช้สายพันธุ์สัตว์เป็น block, ใช้ครอกเดียวกันเป็น block, จัดกลุ่มอายุคนเป็น block


##### ⚠️ หมายเหตุสำคัญ

Paired comparisons test (บทที่ 7) ที่จริงแล้วเป็นกรณีพิเศษของ RCBD ที่มีเพียง 2 ทรีตเมนต์ โดยผู้ป่วยแต่ละคนทำหน้าที่เป็น "block"

Model: xᵢⱼ = μ + βᵢ + τⱼ + εᵢⱼ (เพิ่ม βᵢ = block effect เข้ามาจาก CRD model) — ข้อสมมติเพิ่มเติมสำคัญ: block effect กับ treatment effect ต้อง "additive" (ไม่มี interaction ระหว่างบล็อกกับทรีตเมนต์)


##### 🏷️ 3) Repeated Measures Design

วัดตัวแปรตามเดิมซ้ำหลายครั้งในหน่วยทดลองเดียวกัน (เช่น วัดค่าก่อน/หลังการรักษาหลายจุดเวลา) เป็นการขยาย RCBD ที่ "subject" ทำหน้าที่เป็น block — มีข้อดีคือลด variability จากความแตกต่างระหว่างบุคคล แต่ต้องระวังปัญหา correlation ระหว่างการวัดซ้ำในคนเดียวกัน


##### 🏷️ 4) Factorial Experiment

ศึกษาผลของปัจจัย (factors) ตั้งแต่ 2 ตัวขึ้นไปพร้อมกัน — แต่ละปัจจัยมี levels (ระดับ) ของตัวเอง (เช่น ปัจจัย A=ขนาดยา 3 ระดับ, ปัจจัย B=กลุ่มอายุ 2 ระดับ) ข้อดีสำคัญคือสามารถศึกษา Interaction ระหว่างปัจจัยได้ ซึ่งการทดลองแยกทีละปัจจัยทำไม่ได้


##### 🏷️ Interaction คืออะไร

เกิดขึ้นเมื่อผลของปัจจัยหนึ่งเปลี่ยนแปลงไปตามระดับของอีกปัจจัยหนึ่ง — ถ้าไม่มี interaction เส้นกราฟของแต่ละระดับปัจจัย (เมื่อพล็อตค่าเฉลี่ยตอบสนอง) จะขนานกัน — ถ้ามี interaction เส้นกราฟจะไม่ขนานกัน (อาจตัดกันหรือแยกออกจากกัน) — ตัวอย่าง: ถ้ายาลดเวลาปฏิกิริยาในคนหนุ่มแต่กลับเพิ่มเวลาปฏิกิริยาในคนสูงอายุ (ทิศทางผลตรงข้ามกันตามกลุ่มอายุ) นั่นคือ interaction ระหว่างยากับอายุ — การตรวจพบ interaction มีความสำคัญทางคลินิกมาก เพราะหมายความว่า "คำแนะนำที่ดีที่สุด" ขึ้นกับบริบท ไม่สามารถสรุปแบบเหมารวมได้


##### 🏷️ The Regression Model

ศึกษาความสัมพันธ์ระหว่างตัวแปรอิสระ X (independent/predictor variable) กับตัวแปรตาม Y (dependent/response variable) — สมการโมเดล:

> y = β₀ + β₁x + ε

โดย β₀=y-intercept, β₁=slope (ค่าพารามิเตอร์ประชากร), ε=error term

สมมติฐาน 6 ข้อของ Simple Linear Regression (จำง่าย ๆ ด้วยคำย่อ "LINE"):

- ค่า X ถูกกำหนดไว้ล่วงหน้า (fixed) ไม่ใช่ตัวแปรสุ่ม
- X วัดโดยไม่มีความคลาดเคลื่อน
- สำหรับแต่ละค่า X มี subpopulation ของ Y ที่มีการแจกแจงแบบ Normal
- Equal variances — variance ของทุก subpopulation ของ Y เท่ากัน (σ²)
- Linearity — ค่าเฉลี่ยของทุก subpopulation ของ Y เรียงอยู่บนเส้นตรงเดียวกัน: μ_{y|x} = β₀+β₁x
- Independent — ค่า Y แต่ละค่าเป็นอิสระต่อกัน

##### 🏷️ Sample Regression Equation (Least-Squares Line)

ŷ = b₀ + b₁x โดย b₀, b₁ เป็นตัวประมาณค่าของ β₀, β₁ จากข้อมูลตัวอย่าง — ขั้นตอนการวิเคราะห์การถดถอย: (1) ตรวจสอบสมมติฐานความเป็นเส้นตรง (2) หาสมการเส้นที่เหมาะสมที่สุด (3) ประเมินความแข็งแรงของความสัมพันธ์ (4) ใช้สมการทำนาย/ประมาณค่า


##### 🔹 Least-Squares Criterion

เส้นที่ "ดีที่สุด" คือเส้นที่ทำให้ผลรวมของกำลังสองของระยะห่างแนวตั้ง (vertical deviation) จากจุดข้อมูลถึงเส้น มีค่าน้อยที่สุด เมื่อเทียบกับเส้นอื่นใดที่เป็นไปได้ — เรียกว่า "least-squares line"


##### 🔹 การแบ่งส่วนความแปรปรวน (Partitioning Deviations) — แนวคิดคล้าย ANOVA

สำหรับแต่ละจุดข้อมูล yᵢ:

> Total deviation (yᵢ-ȳ) = Explained deviation (ŷᵢ-ȳ) + Unexplained deviation (yᵢ-ŷᵢ)

เมื่อยกกำลังสองและรวมทุกจุด:

> SST (Total SS) = SSR (Regression/Explained SS) + SSE (Error/Residual SS)

- SST — ความแปรปรวนรวมของ Y รอบค่าเฉลี่ย ȳ
- SSR — ส่วนที่ "อธิบายได้" ด้วยความสัมพันธ์เชิงเส้นกับ X
- SSE — ส่วนที่ "อธิบายไม่ได้" (เป็น residual ที่เหลือหลังฟิตเส้น) — ค่านี้คือค่าที่ least-squares line ทำให้น้อยที่สุด

##### 📐 Coefficient of Determination (r²)

> r² = SSR/SST

ความหมาย: สัดส่วนของความแปรปรวนรวมใน Y ที่อธิบายได้ด้วยความสัมพันธ์เชิงเส้นกับ X — มีค่าระหว่าง 0 ถึง 1 — r²=1 หมายถึงจุดทุกจุดอยู่บนเส้นพอดี (ไม่มี error เลย) — r²=0 หมายถึงเส้นถดถอยไม่ได้ช่วยอธิบายอะไรเลยเมื่อเทียบกับการใช้ค่าเฉลี่ย ȳ อย่างเดียว (ตัวอย่างจากหนังสือ: r²=.67 หมายความว่าเส้นรอบเอวอธิบายความแปรปรวนของไขมันหน้าท้องได้ 67%)


##### 🔹 การทดสอบว่าความสัมพันธ์มีนัยสำคัญหรือไม่ — H₀: β₁=0

ถ้าปฏิเสธ H₀ ไม่ได้ (β₁ อาจเป็น 0 จริง) แปลว่า X ไม่มีประโยชน์ในการทำนาย Y เชิงเส้น (อาจเป็นเพราะไม่มีความสัมพันธ์เลย หรือความสัมพันธ์เป็นแบบ curvilinear ไม่ใช่เส้นตรง) — ทดสอบได้ 2 วิธีที่ให้ผลตรงกัน:

- F-test (ผ่าน ANOVA table ของการถดถอย): F = MSR/MSE (df ตัวเศษ=1, ตัวส่วน=n-2)
- t-test: t = b₁/SE(b₁) (df=n-2)

##### 🔹 Confidence Interval และการทำนาย

สมการถดถอยใช้ได้ 2 แบบ — การทำนาย (prediction) ค่า Y เดี่ยว ๆ ที่ค่า X หนึ่ง ๆ (CI กว้างกว่า) กับ การประมาณค่า (estimation) ค่าเฉลี่ยของ subpopulation Y ที่ X นั้น (CI แคบกว่า)


##### 🏷️ The Correlation Coefficient (r)

วัดความแข็งแรงของความสัมพันธ์เชิงเส้นระหว่างสองตัวแปร โดยไม่ได้กำหนดว่าตัวใดเป็นเหตุ/ผล (แตกต่างจาก regression ที่มี X, Y ชัดเจน) — r คือรากที่สองของ r² แต่มีเครื่องหมายตามทิศทางของ β₁ (slope):

- r = +1 → สหสัมพันธ์เชิงบวกสมบูรณ์แบบ (perfect direct)
- r = -1 → สหสัมพันธ์เชิงลบสมบูรณ์แบบ (perfect inverse)
- r = 0 → ไม่มีสหสัมพันธ์เชิงเส้น
- ทดสอบสมมติฐาน H₀: ρ=0 (ρ คือค่าสหสัมพันธ์ประชากร) ได้ด้วยวิธีเดียวกับการทดสอบ β₁=0

##### ⚠️ ข้อควรระวังสำคัญ 4 ข้อ (Some Precautions)

- ต้องตรวจสอบสมมติฐาน (LINE) ก่อนเชื่อผลการวิเคราะห์
- ตัวแปรทั้งสองต้องวัดจากหน่วยเชื่อมโยงเดียวกัน (unit of association) — เช่น ส่วนสูงกับน้ำหนักต้องวัดจากคนคนเดียวกัน ไม่ใช่คนละกลุ่ม
- "สหสัมพันธ์ไม่ใช่สาเหตุ (correlation is not causation)" — พบ r ที่มีนัยสำคัญทางสถิติอาจหมายถึง: (a) X ก่อ Y จริง (b) Y ก่อ X จริง (c) ตัวแปรที่สามเป็นสาเหตุร่วมของทั้งคู่ (confounding) (d) เกิดจากความบังเอิญทางสถิติ (e) ความสัมพันธ์ไร้ความหมายเพราะวัดจากหน่วยที่ไม่เกี่ยวข้องกัน
- หลีกเลี่ยงการ Extrapolation — อย่าใช้สมการถดถอยทำนาย/ประมาณค่านอกช่วงของ X ที่มีในข้อมูลตัวอย่าง เพราะความสัมพันธ์เชิงเส้นอาจใช้ได้แค่ในช่วงที่สังเกตเท่านั้น นอกช่วงนั้นความสัมพันธ์ที่แท้จริงอาจเป็นเส้นโค้งก็ได้

##### 🔹 ส่วนขยายจากบทที่ 9

เมื่อมีตัวแปรอิสระ (independent/explanatory/predictor variables) มากกว่า 1 ตัว (X₁, X₂, ..., Xₖ) ที่ร่วมกันอธิบายตัวแปรตาม Y


##### 🏷️ The Multiple Linear Regression Model

> yⱼ = β₀ + β₁x₁ⱼ + β₂x₂ⱼ + ... + βₖxₖⱼ + εⱼ

สมมติฐาน 4 ข้อ (คล้ายกับ simple regression): (1) ค่า Xᵢ เป็นค่าคงที่ (fixed/nonrandom) — นี่คือข้อแตกต่างสำคัญจาก "correlation model" ที่จะกล่าวถึงด้านล่าง (2) แต่ละชุดค่า Xᵢ มี subpopulation ของ Y ที่เป็น normal distribution (3) variance ของทุก subpopulation เท่ากัน (4) ค่า Y เป็นอิสระต่อกัน


##### 🔹 Partial Regression Coefficients

β₁ วัดการเปลี่ยนแปลงเฉลี่ยของ Y ต่อหน่วยที่เพิ่มขึ้นของ X₁ เมื่อควบคุม (ตรึง) X₂ ให้คงที่ — เป็นแนวคิดสำคัญมาก: ค่าสัมประสิทธิ์แต่ละตัวสะท้อนผลของตัวแปรนั้น "โดยที่ตัวแปรอื่นในโมเดลถูกควบคุมไว้แล้ว" ไม่ใช่ผลเดี่ยว ๆ ที่ไม่คำนึงถึงตัวแปรอื่นเลย — ในเชิงเรขาคณิต โมเดล 2 ตัวแปรอิสระให้ระนาบ (plane) ในปริภูมิ 3 มิติ ถ้ามากกว่า 2 ตัวเรียกว่า hyperplane


##### 🔹 การหาสมการถดถอย

ใช้ method of least squares เหมือนบทที่ 9 คือหาค่าสัมประสิทธิ์ที่ทำให้ผลรวมกำลังสองของ residual (Σ(yⱼ-ŷⱼ)²) น้อยที่สุด — ในทางปฏิบัติคำนวณด้วยซอฟต์แวร์เสมอเพราะซับซ้อนเกินคำนวณมือ

การประเมินสมการถดถอยพหุคูณ:

- Coefficient of Multiple Determination (R²) = SSR/SST — สัดส่วนความแปรปรวนของ Y ที่อธิบายได้ด้วยตัวแปรอิสระทั้งหมดรวมกัน (คล้าย r² ในบทที่ 9 แต่ขยายเป็นหลายตัวแปร)
- การทดสอบนัยสำคัญโดยรวม (Overall F-test): H₀: β₁=β₂=...=βₖ=0 (ตัวแปรอิสระทั้งหมด "ไร้ประโยชน์" ร่วมกัน) เทียบกับ Hₐ: ไม่ใช่ทุก βᵢ เป็น 0 — ใช้ F = MSR/MSE จาก ANOVA table (df ตัวเศษ=k, ตัวส่วน=n-k-1)
- การทดสอบสัมประสิทธิ์แต่ละตัว (Individual t-tests): H₀: βᵢ=0 ทดสอบว่าตัวแปร Xᵢแต่ละตัวมีประโยชน์จริงหรือไม่ "เมื่อควบคุมตัวแปรอื่นในโมเดลแล้ว" ด้วย t = (β̂ᵢ-0)/SE(β̂ᵢ) (df=n-k-1)

##### ⚠️ ผลลัพธ์ที่ขัดแย้งกันได้ระหว่าง R² โดยรวมกับ βᵢ รายตัว

มีความเป็นไปได้ 6 แบบ เช่น R² มีนัยสำคัญแต่ βᵢ บางตัวไม่มีนัยสำคัญ (พบได้บ่อยมากเมื่อมีตัวแปรอิสระหลายตัว เพราะตัวแปรอาจสัมพันธ์กันเอง — multicollinearity) หรือในทางกลับกัน βᵢ ทุกตัวมีนัยสำคัญแต่ R² โดยรวมไม่มีนัยสำคัญ — จึงต้องดูทั้งสองอย่างประกอบกัน ไม่ใช่ดูอย่างใดอย่างหนึ่งเพียงลำพัง


##### ⚠️ ข้อควรระวังเรื่อง Multiple Comparisons

การทดสอบสัมประสิทธิ์หลายตัวพร้อมกัน (หรือสร้าง CI หลายช่วง) จากข้อมูลชุดเดียวกัน มีปัญหาสะสม Type I errorเหมือนที่กล่าวถึงในบทที่ 8 (multiple comparisons) — ค่า CI ที่สร้างแยกกันหลายช่วงจะไม่เป็นอิสระต่อกัน ต้องปรับด้วยวิธี family-wise error rate correction ถ้าต้องการความแม่นยำของระดับความเชื่อมั่นที่แท้จริง


##### 🏷️ Multiple Correlation Model — ข้อแตกต่างสำคัญจาก Regression Model

ในโมเดลสหสัมพันธ์ ตัวแปร Xᵢ เป็นตัวแปรสุ่ม (random) ไม่ใช่ค่าคงที่ที่กำหนดไว้ล่วงหน้า — Y และ Xᵢ ทั้งหมดมีการแจกแจงร่วมแบบ multivariate normal distribution และไม่มีตัวแปรใดถูกกำหนดให้เป็น "ตัวแปรตาม" หรือ "ตัวแปรอิสระ" ตายตัว (สลับบทบาทกันได้ในทางทฤษฎี) — สมการถดถอยยังคำนวณด้วยวิธีเดียวกัน (least squares) แต่การตีความต่างออกไป


##### 🔹 Multiple Correlation Coefficient (R)

= √R² — วัดความแข็งแรงของความสัมพันธ์ระหว่าง Y กับกลุ่มตัวแปร X ทั้งหมดรวมกัน


##### 🔹 Partial Correlation Coefficient

วัดความสัมพันธ์ระหว่างตัวแปรคู่หนึ่งหลังควบคุมอิทธิพลของตัวแปรอื่น ๆ ออกไปแล้ว — เช่น r_{y1.2} คือสหสัมพันธ์ระหว่าง Y กับ X₁ หลังควบคุม X₂ (ตัวเลขหลังจุดคือตัวแปรที่ถูกควบคุม) — Coefficient of Partial Determination (กำลังสองของค่านี้) บอกว่าสัดส่วนความแปรปรวนที่ "เหลืออยู่" ใน Y (หลังจาก X₂ อธิบายไปแล้วเท่าที่ทำได้) ถูกอธิบายเพิ่มเติมโดย X₁ ได้เท่าไร — มีประโยชน์มากในการแยกแยะว่าตัวแปรใดมีผลอิสระจริง ๆ เมื่อตัวแปรหลายตัวมีความสัมพันธ์กันเอง (เช่น อายุกับระดับการศึกษาที่อาจสัมพันธ์กันเองในการทำนายคะแนนทดสอบทางปัญญา)


##### 🏷️ 1) Qualitative Independent Variables — Dummy Variables

เมื่อต้องการใส่ตัวแปรเชิงคุณภาพ (เช่น เพศ สถานะสูบบุหรี่ ที่อยู่อาศัย) เป็นตัวแปรอิสระในโมเดลถดถอย ต้อง "แปลงเป็นตัวเลข" ด้วย dummy variable ที่รับค่าจำกัด (มักเป็น 0 กับ 1) เพื่อระบุหมวดหมู่ — เรียกอีกชื่อว่า indicator variable หรือ (เมื่อมี 2 หมวดหมู่) dichotomous variable


##### ⚠️ กฎสำคัญ

ถ้าตัวแปรเชิงคุณภาพมี k หมวดหมู่ ต้องใช้ dummy variable จำนวน k-1 ตัว (ไม่ใช่ k ตัว) เพื่อไม่ให้เกิดปัญหา perfect multicollinearity ในโมเดลที่มีค่าคงที่ (intercept) — ตัวอย่าง: เพศ (2 หมวด) ใช้ dummy 1 ตัว (1=ชาย, 0=หญิง); สถานะสูบบุหรี่ 4 หมวด (สูบปัจจุบัน/เลิกไม่เกิน 5 ปี/เลิกเกิน 5 ปี/ไม่เคยสูบ) ต้องใช้ dummy 3 ตัว — ค่าสัมประสิทธิ์ของ dummy variable แต่ละตัวบอกความแตกต่างของค่าเฉลี่ย Y ระหว่างหมวดหมู่นั้นกับหมวดหมู่อ้างอิง (reference category ที่ไม่มี dummy เป็นตัวแทน) เมื่อตัวแปรอื่นในโมเดลคงที่


##### 🏷️ 2) Variable Selection Procedures — เมื่อมีตัวแปรอิสระที่เป็นไปได้จำนวนมาก

ข้อควรระวังสำคัญ: การเพิ่มตัวแปรอิสระเข้าไปในโมเดลจะทำให้ R² เพิ่มขึ้นเสมอ (ไม่มีทางลดลง) จึงไม่ควรใส่ตัวแปรเข้าไปตามอำเภอใจ ต้องมีเหตุผลรองรับ (รวมถึงต้นทุนการเก็บข้อมูล) — มีกลยุทธ์หลักที่ใช้กันแพร่หลาย:

- Stepwise Regression — วิธีที่นิยมที่สุด ทำงานเป็นขั้นตอน (steps) ที่แต่ละขั้นประเมินทุกตัวแปรในโมเดลปัจจุบันว่ายังคุ้มค่าที่จะอยู่ต่อหรือไม่ (ใช้เกณฑ์สถิติ F) — ตัวแปรที่ไม่ผ่านเกณฑ์ (F ต่ำสุด) จะถูกตัดออก แล้วโมเดลใหม่จะถูกประเมินหาตัวแปรใหม่ที่ควรเพิ่มเข้ามา — จุดเด่นสำคัญ: ตัวแปรที่เคยถูกตัดออกไปแล้ว สามารถถูกพิจารณากลับเข้ามาใหม่ได้ในขั้นตอนถัดไป — ทำซ้ำจนไม่มีตัวแปรใดเพิ่ม/ลดได้อีก — ต้องกำหนดค่า F-to-enter และ F-to-remove ล่วงหน้า (ค่า F-to-enter ควรมากกว่าหรือเท่ากับ F-to-remove เสมอ)
- Forward Selection — เริ่มจากไม่มีตัวแปรเลย แล้วเพิ่มทีละตัวตามลำดับความสัมพันธ์กับตัวแปรตาม (เริ่มจากตัวที่มี correlation สูงสุด) — ข้อจำกัดสำคัญ: ตัวแปรที่เพิ่มเข้ามาแล้วจะไม่ถูกพิจารณาถอดออกอีก (ต่างจาก stepwise)
- Backward Elimination — เริ่มจากใส่ตัวแปรทั้งหมด แล้วตัดออกทีละตัวตามลำดับ partial correlation ต่ำสุดที่ไม่ผ่านเกณฑ์ — เช่นกัน ตัวแปรที่ถูกตัดออกแล้วจะไม่ถูกนำกลับมาพิจารณาอีก

##### ⚠️ ข้อควรระวัง

วิธีต่าง ๆ ข้างต้นไม่ได้ให้ผลลัพธ์ตรงกันเสมอไปเมื่อใช้กับข้อมูลชุดเดียวกัน เพราะแต่ละวิธีมีลำดับการพิจารณาต่างกัน — การเลือกตัวแปรจึงยังต้องอาศัยความรู้เชิงเนื้อหา (biological/clinical plausibility) ประกอบเสมอ ไม่ใช่พึ่งพาสถิติล้วน ๆ


##### 🏷️ 3) Logistic Regression — เมื่อตัวแปรตามเป็น Dichotomous (0/1)

ปัญหาสำคัญของการใช้ simple linear regression ตรง ๆ กับตัวแปรตามแบบ 0/1 คือ ค่าที่ทำนายได้ (E(Y|X)) ควรอยู่ในช่วง [0,1] เท่านั้น (เพราะมันคือความน่าจะเป็น) แต่สมการเส้นตรงธรรมดาให้ค่าได้ตั้งแต่ -∞ ถึง +∞ ซึ่งขัดกับความเป็นจริง


##### 📐 ทางแก้ — Logit Transformation

ถ้า p=P(Y=1) แปลงเป็น odds = p/(1-p) (มีค่า 0 ถึง +∞) แล้วนำ natural log มาใช้:

> ln[p/(1-p)] = β₀ + β₁x

เรียกสมการนี้ว่า Logistic Regression Model — แปลงกลับเป็นความน่าจะเป็น p ได้ด้วย:

> p = exp(β₀+β₁x) / [1+exp(β₀+β₁x)]


##### 🏷️ Odds Ratio (OR)

เมื่อตัวแปรอิสระเป็น dichotomous เช่นกัน (เช่น มี/ไม่มีปัจจัยเสี่ยง) OR = exp(β₁) — ค่านี้บอกว่าอัตราส่วนของ "odds การเกิดผลลัพธ์" ระหว่างกลุ่มที่มีปัจจัยเสี่ยงกับกลุ่มที่ไม่มี ต่างกันกี่เท่า (ตัวอย่างในหนังสือ: OR=5.84 ระหว่างเพศชายกับหญิงในการพบโรคหลอดเลือดหัวใจตีบ หมายความว่าผู้ชายมีโอกาส (odds) พบโรคนี้สูงกว่าผู้หญิงเกือบ 6 เท่า) — ข้อควรระวัง: การตีความ OR ว่าใกล้เคียงกับ relative risk ใช้ได้เมื่อผลลัพธ์ที่ศึกษาเป็นเหตุการณ์ที่พบได้ค่อนข้างน้อย (rare event) เท่านั้น (เชื่อมโยงกับหลักการเดียวกันในตำราระบาดวิทยาคลินิกเรื่อง odds ratio ≈ relative risk เมื่อความชุกต่ำ)


##### 🔹 Logistic Regression กับตัวแปรอิสระต่อเนื่อง (Continuous)

ใช้หลักการเดียวกัน แต่ β₁ ตีความเป็น "การเปลี่ยนแปลงของ log-odds ต่อหน่วยที่เพิ่มขึ้นของ X" ซึ่งซับซ้อนกว่าการตีความ slope ในการถดถอยเชิงเส้นธรรมดา — สามารถใช้สมการเพื่อคำนวณความน่าจะเป็นของผลลัพธ์ (เช่น ความน่าจะเป็นที่ผู้ป่วยจะเข้าร่วมโปรแกรมฟื้นฟูหัวใจ) ณ ค่าตัวแปรอิสระใด ๆ ได้โดยตรงผ่านสูตร p ด้านบน — Logistic regression เป็นเครื่องมือที่ใช้แพร่หลายมากในงานระบาดวิทยาเพื่อประมาณความเสี่ยง (risk) ของการเกิดโรคจากปัจจัยเสี่ยงต่าง ๆ


##### 🔹 คุณสมบัติทางคณิตศาสตร์ของ Chi-Square Distribution

เกิดจากผลรวมของค่า z² (ค่ามาตรฐานยกกำลังสอง) — ถ้าสุ่ม z จำนวน k ค่าที่เป็นอิสระต่อกันจากการแจกแจงปกติมาตรฐาน แล้วรวม z₁²+z₂²+...+zₖ² จะได้การแจกแจงไคสแควร์ที่มี df=k — คุณสมบัติ: mean=k, variance=2k, ค่าเป็นบวกเสมอ (0 ถึง +∞) เพราะเป็นผลรวมของค่ายกกำลังสอง, และผลรวมของตัวแปรไคสแควร์อิสระหลายตัวก็ยังเป็นไคสแควร์


##### 📐 Chi-Square Test Statistic ทั่วไป

> X² = Σ[(Oᵢ-Eᵢ)²/Eᵢ]

โดย Oᵢ=ความถี่ที่สังเกตได้ (observed), Eᵢ=ความถี่ที่คาดหวังถ้า H₀ เป็นจริง (expected) — df = k-r (k=จำนวนกลุ่ม, r=จำนวนข้อจำกัด/พารามิเตอร์ที่ประมาณจากข้อมูล) — ค่า X² น้อย = สอดคล้องกันดี, ค่า X² มาก = ไม่สอดคล้องกัน → ปฏิเสธ H₀ เมื่อ X² มากพอ


##### ⚠️ ข้อควรระวังเรื่อง Expected Frequency ต่ำ

ถ้า expected frequency บางกลุ่มต่ำเกินไป (กฎทั่วไป: ไม่ควรต่ำกว่า 5, หรือ Cochran เสนอว่าต่ำสุดได้ถึง 1 สำหรับ unimodal goodness-of-fit test) การประมาณด้วย chi-square distribution จะไม่แม่นยำ — วิธีแก้คือรวมกลุ่มที่ติดกัน (ลด df ลง) หรือใช้ Fisher Exact Test แทน

3 ประเภทการทดสอบด้วย Chi-Square:


##### 🏷️ 1) Goodness-of-Fit Test

เปรียบเทียบการแจกแจงของตัวอย่างกับการแจกแจงทางทฤษฎีที่คาดว่าประชากรควรเป็น (เช่น ทดสอบว่าข้อมูลเป็นไปตาม normal distribution, Poisson distribution หรือสัดส่วนที่คาดหวังไว้หรือไม่)


##### 🏷️ 2) Test of Independence

ทดสอบว่าเกณฑ์การจำแนก 2 อย่างที่ใช้กับกลุ่มตัวอย่างเดียวกันเป็นอิสระต่อกันหรือไม่ (เช่น เชื้อชาติ กับ การใช้กรดโฟลิกก่อนตั้งครรภ์) — ใช้ Contingency Table ขนาด r×c — คำนวณ Expected frequency ของแต่ละช่อง:

> Eᵢⱼ = (ผลรวมแถว i × ผลรวมคอลัมน์ j) / ผลรวมทั้งหมด

df = (r-1)(c-1) — สถานการณ์: สุ่มตัวอย่างครั้งเดียวจากประชากรเดียว แล้วจำแนกตามสองเกณฑ์พร้อมกัน (ทั้งผลรวมแถวและคอลัมน์เป็นค่าสุ่ม ไม่ได้ถูกกำหนดไว้ล่วงหน้า)


##### 🏷️ 3) Test of Homogeneity

คำถามต่างจาก independence: "กลุ่มตัวอย่างที่สุ่มมาจากหลายประชากร มีการกระจายตามตัวแปรหนึ่ง ๆ เหมือนกันหรือไม่" — สถานการณ์: ผลรวมของแถวหรือคอลัมน์ฝั่งหนึ่งถูกกำหนดไว้ล่วงหน้าโดยผู้วิจัย (เช่น กำหนดจะสุ่ม 96 คนจากกลุ่ม narcolepsy และ 96 คนจากกลุ่มควบคุม) — แม้แนวคิดและวิธีการสุ่มตัวอย่างต่างกัน แต่การคำนวณทางคณิตศาสตร์เหมือนกันทุกประการกับ test of independence


##### 🏷️ Fisher Exact Test

ใช้แทน chi-square test เมื่อขนาดตัวอย่างเล็กเกินไป (กฎทั่วไป: n<20, หรือ 20≤n≤40 และมี expected frequency ต่ำกว่า 5) — คำนวณความน่าจะเป็นที่แท้จริง (exact) ของผลที่สังเกตได้หรือรุนแรงกว่า โดยไม่ต้องอาศัยการประมาณแบบ chi-square — ใช้กับตาราง 2×2 เท่านั้น — เมื่อขนาดตัวอย่างใหญ่พอ ยังมีการประมาณด้วย normal distribution เป็นทางเลือก: z = [(a/A)-(b/B)] / √[p̂(1-p̂)(1/A+1/B)]


##### 🏷️ Relative Risk (RR) vs. Odds Ratio (OR) — แยกตามประเภทการศึกษา

- Prospective Study — เริ่มจากกลุ่มที่มี/ไม่มีปัจจัยเสี่ยง แล้วติดตามไปข้างหน้าดูการเกิดโรค → คำนวณ Relative Risk ได้โดยตรง:
> RR = [a/(a+b)] / [c/(c+d)]

ตีความ: RR=1 ไม่มีความสัมพันธ์, RR>1 ความเสี่ยงเพิ่มขึ้นในกลุ่มมีปัจจัยเสี่ยง, RR<1 ความเสี่ยงลดลง

- Retrospective Study — เริ่มจากกลุ่ม cases/controls แล้วย้อนดูปัจจัยเสี่ยง → ไม่สามารถคำนวณ RR ได้โดยตรง (เพราะสัดส่วนของ cases/controls ถูกกำหนดโดยผู้วิจัย ไม่ใช่อัตราชุกตามธรรมชาติ) ต้องใช้ Odds Ratio แทน:
> OR = (a×d)/(b×c) = (a/b)/(c/d)

- หลักการสำคัญ: OR เป็นค่าประมาณที่ดีของ RR เมื่อโรคที่ศึกษาเป็น "โรคหายาก (rare disease)" — ตรงกับหลักการเดียวกันในตำราระบาดวิทยาคลินิก
- ทั้ง RR และ OR สร้าง CI ได้ด้วยสูตรอิงจากค่า chi-square: 100(1-α)%CI = point estimate^(1±zα/√X²)

##### 🏷️ Mantel-Haenszel Statistic — ควบคุม Confounding Variable

เมื่อสงสัยว่ามีตัวแปรกวน (confounding variable เช่น เชื้อชาติ อายุ) ที่อาจบดบังความสัมพันธ์ที่แท้จริงระหว่างโรคกับปัจจัยเสี่ยง วิธีนี้แบ่งข้อมูลเป็นชั้น (strata) ตามค่าของตัวแปรกวน แล้ววิเคราะห์ทั้งภายในแต่ละชั้นและรวมข้ามทุกชั้น เพื่อให้ได้ค่าความสัมพันธ์ที่ "ปรับแล้ว (adjusted)" ไม่ถูกบิดเบือนโดยตัวแปรกวน — ใช้ได้ทั้งข้อมูลจาก retrospective และ prospective study


##### 🏷️ Survival Analysis

วิเคราะห์ survival time (ระยะเวลาตั้งแต่เข้าร่วมการศึกษาจนเกิดเหตุการณ์ที่สนใจ เช่น ตาย/กำเริบซ้ำ) — ข้อมูลมักมี censored data (ข้อมูลที่ไม่รู้ระยะเวลาที่แท้จริง เพราะขาดการติดตามหรือยังไม่เกิดเหตุการณ์เมื่อสิ้นสุดการศึกษา) แบ่งเป็น Type I censoring (สิ้นสุดตามเวลาที่กำหนด), Type II (สิ้นสุดเมื่อครบสัดส่วนที่กำหนด), Type III/progressive (ผู้ป่วยเข้าร่วมคนละเวลากัน)


##### 🔹 Kaplan-Meier Procedure (Product-Limit Method)

ประมาณความน่าจะเป็นการรอดชีวิตสะสม ณ เวลาใด ๆ:

> Ŝ(t) = p̂₁ × p̂₂ × ... × p̂ₜ

โดย p̂ₜ = สัดส่วนของคนที่ยังมีชีวิตอยู่ตอนต้นช่วงเวลา t แล้วรอดผ่านช่วงเวลา t ไปได้ — เป็นวิธีไร้พารามิเตอร์ (nonparametric) ที่ใช้ข้อมูลจากทุกคนอย่างเต็มที่แม้จะมี censored data ปะปนอยู่ (เชื่อมโยงกับวิธีเดียวกันที่กล่าวถึงในตำราระบาดวิทยาคลินิก)


##### 🔹 Log-Rank Test

ใช้เปรียบเทียบเส้นโค้งการรอดชีวิต (survival curve) จาก Kaplan-Meier ของสองกลุ่มขึ้นไปว่าแตกต่างกันอย่างมีนัยสำคัญทางสถิติหรือไม่ — เป็นการประยุกต์ใช้ Mantel-Haenszel procedure กับข้อมูล survival โดยตรง: สร้างตาราง 2×2 (จำนวนตายสังเกต/จำนวนที่ยังมีชีวิต × กลุ่ม A/กลุ่ม B) ที่แต่ละเวลาที่มีการตายเกิดขึ้น เป็นแต่ละ stratum แล้วรวมผลทุก stratum เป็นค่าสถิติทดสอบเดียว


##### 🏷️ ความแตกต่างของศัพท์ (แม้มักใช้แทนกันได้ในทางปฏิบัติ)

Nonparametric = การทดสอบที่ไม่ได้ตั้งสมมติฐานเกี่ยวกับพารามิเตอร์ประชากร ส่วน Distribution-free = การทดสอบที่ไม่ต้องอาศัยความรู้/สมมติฐานเกี่ยวกับรูปแบบการแจกแจงของประชากรต้นทาง

ข้อดี 4 ประการของสถิติไร้พารามิเตอร์:

- ทดสอบสมมติฐานที่ไม่ใช่ข้อความเกี่ยวกับพารามิเตอร์ได้ (เช่น chi-square goodness-of-fit)
- ใช้ได้แม้ไม่ทราบรูปแบบการแจกแจงของประชากร (เช่น เมื่อข้อมูลไม่เป็น normal distribution และตัวอย่างเล็กเกินกว่า Central Limit Theorem จะช่วยได้)
- คำนวณง่ายและเร็วกว่า (แม้ปัจจุบันซอฟต์แวร์ทำให้ข้อได้เปรียบนี้มีน้ำหนักน้อยลง)
- ใช้ได้กับข้อมูลที่เป็นแค่อันดับ (rank) หรือการจัดหมวดหมู่ ไม่จำเป็นต้องมีมาตรวัดที่แข็งแรงพอสำหรับสถิติแบบพาราเมตริก

##### ⚠️ ข้อเสีย

ถ้าใช้กับข้อมูลที่จริง ๆ แล้วเหมาะกับสถิติแบบพาราเมตริกอยู่แล้ว จะเป็นการ "เสียข้อมูล" (waste of data) เพราะไม่ได้ใช้ข้อมูลเต็มศักยภาพ และบางการทดสอบคำนวณยากเมื่อตัวอย่างมีขนาดใหญ่


##### 🏷️ หลักการสำคัญ: Rank Transformation

เทคนิคพื้นฐานที่การทดสอบไร้พารามิเตอร์ส่วนใหญ่ใช้ร่วมกันคือแปลงข้อมูลดิบเป็นอันดับ (rank) ก่อน แล้วจึงวิเคราะห์บนอันดับแทนค่าจริง — สูญเสียข้อมูลบางส่วน (เช่น ไม่สามารถหา mean/variance ที่แท้จริงได้) แต่ทำให้การทดสอบทนทานต่อรูปแบบการแจกแจงที่ผิดปกติ

รายการการทดสอบไร้พารามิเตอร์หลัก (แต่ละตัวเป็น "คู่เทียบ" ของการทดสอบแบบพาราเมตริก):

- Sign Test — เทียบเท่ากับ one-sample/paired t-test แบบง่ายที่สุด ใช้เฉพาะเครื่องหมาย (+/-) ของผลต่างจากค่า median ที่ตั้งสมมติฐาน ไม่สนใจขนาด — ทดสอบด้วย binomial distribution ที่ p=.5 (H₀: P(+)=P(-)=.5) — สมมติฐานเดียวที่ต้องมี: ตัวแปรต่อเนื่อง — ข้อเสีย: เสียข้อมูลมากเพราะทิ้งขนาดของผลต่างไปหมด
- Wilcoxon Signed-Rank Test — ปรับปรุงจาก Sign Test โดยใช้ทั้งเครื่องหมายและขนาด (rank) ของผลต่าง ไม่ทิ้งข้อมูลไปเยอะเท่า Sign test — เหมาะเมื่อข้อมูลอย่างน้อยเป็น interval scale และประชากรสมมาตรรอบค่าเฉลี่ย — คำนวณผลต่าง dᵢ จากค่าตั้งสมมติฐาน แล้วจัดอันดับตามค่าสัมบูรณ์ ให้เครื่องหมายกลับคืน แล้วรวมอันดับที่เป็นบวก (T+) กับลบ (T-) แยกกัน — เป็นคู่เทียบของ paired t-test
- Median Test — ทดสอบว่าสองประชากรอิสระมี median เท่ากันหรือไม่ — หา median ร่วมของสองกลุ่มรวมกัน แล้วนับจำนวนค่าที่อยู่เหนือ/ใต้ median นั้นในแต่ละกลุ่ม จัดเป็นตาราง 2×2 แล้วทดสอบด้วย chi-square ธรรมดา — ใช้ข้อมูลได้ค่อนข้างน้อย (แค่ตำแหน่งเทียบกับ median)
- Mann-Whitney Test (Mann-Whitney-Wilcoxon Test) — ปรับปรุงจาก Median Test โดยใช้อันดับของทุกค่าแทนแค่ตำแหน่งเทียบ median — รวมสองกลุ่มมาจัดอันดับพร้อมกัน แล้วเปรียบเทียบผลรวมอันดับของแต่ละกลุ่ม — เป็นคู่เทียบของ independent samples t-test — สมมติฐาน: สุ่มอิสระ มาตรวัดอย่างน้อย ordinal ตัวแปรต่อเนื่อง และถ้าประชากรต่างกัน ต่างแค่ตำแหน่ง (location/median) เท่านั้น
- Kolmogorov-Smirnov Goodness-of-Fit Test — ทางเลือกของ chi-square goodness-of-fit เปรียบเทียบcumulative distribution function ของตัวอย่าง (Fs(x)) กับทฤษฎี (Fт(x)) — สถิติทดสอบ D = ระยะห่างแนวตั้งสูงสุดระหว่างสองเส้นโค้งสะสม — เหมาะกับข้อมูลต่อเนื่อง (ต่างจาก chi-square ที่เหมาะกับข้อมูลจัดกลุ่ม/หมวดหมู่)
- Kruskal-Wallis One-Way ANOVA by Ranks — คู่เทียบของ one-way ANOVA (บทที่ 8) เมื่อไม่เข้าเงื่อนไข normality/equal variance — รวมทุกกลุ่มมาจัดอันดับ แล้วคำนวณสถิติ H จากผลรวมอันดับของแต่ละกลุ่ม (Rⱼ):
> H = [12/(n(n+1))] × Σ(Rⱼ²/nⱼ) - 3(n+1)

เมื่อ n มากพอ H มีการแจกแจงประมาณ chi-square ด้วย df=k-1

- Friedman Two-Way ANOVA by Ranks — คู่เทียบของ Randomized Complete Block Design (บทที่ 8) — ใช้เมื่อข้อมูลจัดเป็น blocks (แถว) × treatments (คอลัมน์) โดยแต่ละ block จัดอันดับ treatments ของตัวเอง แล้วรวมอันดับตามคอลัมน์ (Rⱼ) คำนวณสถิติ χ²r:
> χ²r = [12/(nk(k+1))] × Σ(Rⱼ²) - 3n(k+1)

(n=จำนวน block, k=จำนวน treatment)

- Spearman Rank Correlation Coefficient (rₛ) — คู่เทียบของ Pearson correlation coefficient (บทที่ 9) เมื่อข้อมูลเป็นอันดับหรือไม่เป็น normal — จัดอันดับทั้ง X และ Y แยกกัน แล้วหาผลต่างอันดับ dᵢ ในแต่ละคู่:
> rₛ = 1 - [6Σdᵢ²] / [n(n²-1)]

ค่า rₛ อยู่ระหว่าง -1 ถึง +1 เหมือน Pearson r — ถ้า n>30 สามารถแปลงเป็น z=rₛ√(n-1) เพื่อทดสอบด้วย standard normal ได้ — มีการปรับแก้พิเศษสำหรับข้อมูลที่มีค่าเท่ากัน (ties) จำนวนมาก


##### ✅ ข้อคิดสรุป

ทุกการทดสอบไร้พารามิเตอร์ข้างต้นถูกออกแบบให้เป็นทางเลือกที่ทนทานกว่าเมื่อสมมติฐานของการทดสอบแบบพาราเมตริก (normality, equal variance, interval/ratio scale) ไม่เป็นจริง — นักวิจัยควรเลือกใช้เมื่อมีเหตุผลจริง ๆ (ข้อมูลเป็นอันดับ, ตัวอย่างเล็กและไม่ normal) ไม่ใช่ใช้พร่ำเพรื่อโดยไม่จำเป็น เพราะจะสูญเสียประสิทธิภาพทางสถิติ (statistical power) เมื่อเทียบกับวิธีพาราเมตริกที่เหมาะสมกว่าในสถานการณ์ที่สมมติฐานเป็นจริง


##### 🔹 บทบาทของสถิติชีพ

เปรียบเทียบได้กับการที่แพทย์ส่วนตัวใช้ประวัติ+ตรวจร่างกาย+ผลแล็บวินิจฉัยผู้ป่วยรายบุคคล — ทีมสาธารณสุขใช้สถิติชีพ (การเกิด การตาย การเจ็บป่วย และอัตรา/สัดส่วนต่าง ๆ ที่คำนวณจากข้อมูลเหล่านี้) เพื่อ "วินิจฉัย" สุขภาพของชุมชนทั้งชุมชนในฐานะสิ่งมีชีวิตเดียว — เป็นเครื่องมือหลักของงานระบาดวิทยาและสาธารณสุข


##### 🏷️ ความแตกต่างระหว่าง Rate กับ Ratio

- Rate — ตัวเศษเป็นส่วนหนึ่งของตัวส่วน (เช่น จำนวนตาย/จำนวนประชากรที่เสี่ยงตาย) รูปแบบทั่วไป: [a/(a+b)]×k
- Ratio — ตัวเศษและตัวส่วนเป็นปริมาณคนละชุด ไม่ใช่ส่วนหนึ่งของกัน (เช่น สัดส่วนแพทย์ต่อประชากร) รูปแบบ: (c/d)×k
- k คือฐาน (base) เช่น 1,000, 10,000, 100,000 ใช้เพื่อเลี่ยงตัวเลขทศนิยมเล็กเกินไปและให้อ่านเข้าใจง่าย

##### 🏷️ 1) อัตราการตาย (Death Rates and Ratios)

- Crude Death Rate = (จำนวนตายทั้งหมดในปี / ประชากรทั้งหมด ณ 1 กรกฎาคม) × 1,000 — ใช้วัดสุขภาพชุมชนโดยรวม แต่เปรียบเทียบระหว่างชุมชนที่มีโครงสร้างอายุ/เชื้อชาติ/เพศต่างกันได้ยาก เพราะไม่ได้ควบคุมปัจจัยเหล่านี้
- Specific Death Rate — แยกตามกลุ่มย่อยเฉพาะ (อายุ เพศ เชื้อชาติ หรือสาเหตุการตาย) ให้ข้อมูลละเอียดกว่า แต่มีจำนวนมากเกินจะดูภาพรวมง่าย ๆ
- Adjusted/Standardized Death Rate — สำคัญที่สุด: แก้ปัญหาการเปรียบเทียบระหว่างประชากรที่มีโครงสร้างต่างกัน โดยใช้ Direct Method of Adjustment — นำอัตราตายเฉพาะกลุ่ม (specific rate) ของประชากรที่สนใจ ไปคำนวณกับประชากรมาตรฐาน (standard population) (มักใช้สำมะโนประชากรแห่งชาติ ปรับเป็น "standard million") เพื่อหาว่า "ถ้าประชากรที่สนใจมีโครงสร้างอายุเหมือนประชากรมาตรฐาน จะมีอัตราตายเท่าไร" — ทำให้เปรียบเทียบข้ามพื้นที่/เวลาได้อย่างเป็นธรรม (ตัวอย่างในหนังสือ: Crude death rate ของจอร์เจียปี 2000 = 7.8 แต่หลังปรับอายุแล้วกลายเป็น 9.3 เพราะประชากรจอร์เจียตอนนั้นอายุน้อยกว่าค่าเฉลี่ยสหรัฐฯ ทำให้ crude rate ต่ำกว่าความเป็นจริงที่ควรเปรียบเทียบได้)
- Maternal Mortality Rate = (ตายจากสาเหตุเกี่ยวกับการตั้งครรภ์/คลอด / จำนวนเกิดมีชีพ) × 100,000 — ข้อจำกัด: ไม่รวม fetal death ในตัวส่วน, การตายจากครรภ์แฝดนับซ้อนได้ไม่ถูกต้อง, ปัญหาการลงทะเบียนเกิดไม่ครบ
- Infant Mortality Rate = (ตายอายุต่ำกว่า 1 ปี / เกิดมีชีพ) × 1,000
- Neonatal Mortality Rate = (ตายอายุต่ำกว่า 28 วัน / เกิดมีชีพ) × 1,000
- Fetal Death Rate = (ตายในครรภ์ / จำนวนการคลอดทั้งหมด) × 1,000 — ปัญหา: แต่ละพื้นที่นิยามอายุครรภ์ขั้นต่ำที่ต้องรายงานต่างกัน
- Fetal Death Ratio = (ตายในครรภ์ / เกิดมีชีพ) × k — แก้ปัญหาไม่คำนึงถึงระดับการเจริญพันธุ์ของชุมชนของ fetal death rate
- Perinatal Mortality Rate = รวม fetal death (อายุครรภ์≥28สัปดาห์) กับ infant death (อายุ<7วัน) เข้าด้วยกัน เพราะมักมีสาเหตุร่วมกัน
- Cause-of-Death Ratio = (ตายจากโรคเฉพาะ / ตายทั้งหมด) × 100 — ใช้วัดความสำคัญเชิงสัมพัทธ์ของสาเหตุตายหนึ่ง ๆ ระวังการตีความข้ามพื้นที่ (อัตราสูงอาจเป็นเพราะสาเหตุอื่นต่ำ ไม่ใช่สาเหตุนี้สูงจริง)
- Proportional Mortality Ratio = (ตายในกลุ่มย่อยหนึ่ง / ตายทั้งหมด) × 100

##### 🏷️ 2) การวัดภาวะเจริญพันธุ์ (Measures of Fertility)

ในทางประชากรศาสตร์ Fertility = การมีบุตรจริง (ต่างจาก Fecundity = ศักยภาพในการมีบุตร)

- Crude Birth Rate = (เกิดมีชีพ / ประชากรทั้งหมด) × 1,000
- General Fertility Rate = (เกิดมีชีพ / จำนวนหญิงวัยเจริญพันธุ์ อายุ 15-44 หรือ 15-49) × 1,000 — ดีกว่า crude birth rate เพราะตัวส่วนใกล้เคียง "กลุ่มเสี่ยง" ที่แท้จริงมากกว่า
- Age-Specific Fertility Rate = อัตราเกิดแยกตามช่วงอายุมารดา (มักเป็นช่วง 5 ปี)
- Total Fertility Rate = ผลรวมของ age-specific fertility rate ทุกช่วงอายุ (คูณด้วยความกว้างช่วงอายุ) — ตีความเป็น "จำนวนบุตรเฉลี่ยที่ผู้หญิง 1,000 คนจะมีตลอดชีวิตการเจริญพันธุ์ ถ้าอัตราการเกิดคงที่ตามที่สังเกตในปีนั้น"
- Cumulative Fertility Rate — เหมือน total fertility rate แต่หยุดสะสมที่ช่วงอายุใดก็ได้ (ไม่ต้องครบทุกช่วง)
- Standardized Fertility Rate — ปรับด้วยวิธี direct method เหมือน death rate เพื่อเทียบระหว่างประชากรที่มีโครงสร้างอายุต่างกัน

##### 🏷️ 3) การวัดภาวะเจ็บป่วย (Measures of Morbidity)

- Incidence Rate = (เคสใหม่ของโรคหนึ่ง / ประชากรทั้งหมด) × k — บอกว่าโรคเกิดใหม่เร็วแค่ไหน มีประโยชน์สำหรับตัดสินใจว่าควรเริ่มมาตรการป้องกันหรือไม่ (ใช้ได้ทั้งโรคเฉียบพลันและเรื้อรัง)
- Prevalence Rate (จริง ๆ เป็น ratio) = (เคสทั้งหมดทั้งเก่าและใหม่ ณ จุดเวลาหนึ่ง / ประชากรทั้งหมด ณ เวลานั้น) × k — เหมาะกับโรคเรื้อรังมากกว่า
- Case-Fatality Ratio = (ตายจากโรค / ผู้ป่วยด้วยโรคนั้นทั้งหมด) × 100 — ตีความเป็นความน่าจะเป็นที่จะตายหลังเป็นโรคนั้น สะท้อนความรุนแรงของโรคและประสิทธิผลการรักษา
- Immaturity Ratio = (เกิดมีชีพน้ำหนักต่ำกว่า 2,500 กรัม / เกิดมีชีพทั้งหมด) × 100
- Secondary Attack Rate = (เคสเพิ่มเติมในผู้สัมผัสโรคติดต่อภายในระยะฟักตัวสูงสุด / ผู้สัมผัสที่เสี่ยงทั้งหมด) × 100 — ใช้วัดการแพร่กระจายของโรคติดต่อในกลุ่มปิด เช่น ครัวเรือนหรือห้องเรียน
จบสรุปทั้ง 14 บทของหนังสือ Biostatistics: A Foundation for Analysis in the Health Sciences (9th ed.) โดย Wayne W. Daniel — ครอบคลุมตั้งแต่แนวคิดพื้นฐานของสถิติ สถิติเชิงพรรณนา ความน่าจะเป็นและ Bayes' theorem การแจกแจงความน่าจะเป็นหลัก (binomial, Poisson, normal) การแจกแจงกลุ่มตัวอย่างและ Central Limit Theorem การประมาณค่าและการทดสอบสมมติฐาน การวิเคราะห์ความแปรปรวน การถดถอยเชิงเส้นทั้งอย่างง่ายและพหุคูณ (รวมถึง logistic regression) การวิเคราะห์ไคสแควร์ ความเสี่ยงสัมพัทธ์/odds ratio และ survival analysis สถิติไร้พารามิเตอร์ ไปจนถึงสถิติชีพที่ใช้ในงานสาธารณสุข

> P(D|T) = [P(T|D)×P(D)] / [P(T|D)×P(D) + P(T|D̄)×P(D̄)]

> s²ₚ = [(n₁-1)s₁² + (n₂-1)s₂²] / (n₁+n₂-2)

แล้วใช้ df=n₁+n₂-2 กับ t-distribution

> H = [12/(n(n+1))] × Σ(Rⱼ²/nⱼ) - 3(n+1)

เมื่อ n มากพอ H มีการแจกแจงประมาณ chi-square ด้วย df=k-1

> χ²r = [12/(nk(k+1))] × Σ(Rⱼ²) - 3n(k+1)

(n=จำนวน block, k=จำนวน treatment)

> OR = (a×d)/(b×c) = (a/b)/(c/d)

> RR = [a/(a+b)] / [c/(c+d)]

ตีความ: RR=1 ไม่มีความสัมพันธ์, RR>1 ความเสี่ยงเพิ่มขึ้นในกลุ่มมีปัจจัยเสี่ยง, RR<1 ความเสี่ยงลดลง

> Ŝ(t) = p̂₁ × p̂₂ × ... × p̂ₜ

โดย p̂ₜ = สัดส่วนผู้ป่วยที่รอดในช่วงเวลา t จากผู้ป่วยที่ยังมีชีวิตอยู่ตอนต้นช่วง t — เป็นวิธีไร้พารามิเตอร์ (nonparametric) ที่ไม่ต้องสมมติรูปแบบการแจกแจงของเวลารอดชีวิต ใช้ข้อมูลจาก censored cases ได้อย่างมีประสิทธิภาพ

> rₛ = 1 - [6Σdᵢ²] / [n(n²-1)]

ค่า rₛ อยู่ระหว่าง -1 ถึง +1 เหมือน Pearson r — ถ้า n>30 สามารถแปลงเป็น z=rₛ√(n-1) เพื่อทดสอบด้วย standard normal ได้ — มีการปรับแก้พิเศษสำหรับข้อมูลที่มีค่าเท่ากัน (ties) จำนวนมาก

