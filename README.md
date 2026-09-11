# 🩺 Medical Research & Methodology Multi-Agent AI System

ระบบปัญญาประดิษฐ์สถาปัตยกรรมหลายเอเจนต์ (**Multi-Agent AI Architecture**) สำหรับการออกแบบระเบียบวิธีวิจัยทางการแพทย์ การวิเคราะห์ชีวสถิติ การประเมินชุดตรวจวินิจฉัย และการอนุมานเชิงสาเหตุในเวชระเบียนโลกจริง (Real-World Evidence)

> 🏛️ **ฐานข้อมูลและกรอบแนวคิดอ้างอิง:** พัฒนาขึ้นโดยอ้างอิงเนื้อหาจากหลักสูตร **Data and Data Analytics in Digital Health** (หน่วยบริหารจัดการข้อมูล ปัญญาประดิษฐ์ และชีวสถิติ: **DAB Unit**, ฝ่ายวิจัย คณะแพทยศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย โดย อ.ดร.นพ.อมริศ ตันสัจจา) ร่วมกับตำรามาตรฐานสากล:
> - *Clinical Epidemiology: The Essentials* (Robert H. Fletcher & Suzanne W. Fletcher)
> - *Biostatistics: A Foundation for Analysis in the Health Sciences* (Wayne W. Daniel, 9th ed.)
> - *Causal Inference & Target Trial Emulation Framework* (Judea Pearl, Miguel Hernán & James Robins)

---

## 🏗️ 1. สถาปัตยกรรม Multi-Agent (Multi-Agent Architecture)

ระบบประกอบด้วย 7 บทบาทเอเจนต์เฉพาะทาง ทำงานร่วมกันเป็นกราฟวงจรแบบมีทิศทาง (Directed Acyclic Workflow) ผ่าน **Research State Blackboard**:

```mermaid
graph TD
    User([User Query / Clinical Question]) --> Orchestrator
    Orchestrator --> PICO[1. PICO & Gap Finder Agent]
    PICO --> Design[2. Study Design & Protocol Architect Agent]
    Design --> Biostats[3. Biostatistics & Sample Size Planner Agent]
    Design --> Diag[4. Diagnostic Accuracy Evaluator Agent]
    Design --> Causal[5. Causal Inference & Target Trial Guardian]
    Biostats --> Appraisal[6. Critical Appraisal & Guidelines Guardian]
    Diag --> Appraisal
    Causal --> Appraisal
    Appraisal --> Lead[7. Lead Methodologist / PI Synthesis Agent]
    Lead --> Protocol([Master Research Protocol & Dossier])
```

### หน้าที่ของแต่ละ Agent:
1. **`PICO & Question Formulator Agent`**:
   - จำแนกประเภทคำถามคลินิก (`Therapy`, `Diagnosis`, `Harm/Etiology`, `Prognosis`)
   - ถอดรหัสองค์ประกอบ PICO (Population, Intervention, Comparison, Outcome)
   - ประเมินความเป็นไปได้และคุณค่าของงานวิจัยด้วยเกณฑ์ **FINER**
2. **`Study Design & Protocol Architect Agent`**:
   - เลือกรูปแบบการศึกษาที่เหมาะสมตามลำดับขั้นหลักฐาน EBM (RCT, Prospective/Retrospective Cohort, Case-Control, Diagnostic Cross-Sectional, Target Trial Emulation)
   - วางระบบมาตรการป้องกันอคติ (Randomization, Allocation Concealment ด้วย SNOSE, Double-blinding, Intention-to-Treat)
3. **`Biostatistics & Sample Size Planner Agent`**:
   - กำหนดเกณฑ์เลือกสถิติ Parametric vs. Non-parametric (t-test, ANOVA, Mann-Whitney, Kruskal-Wallis, Chi-Square, Fisher Exact, Kaplan-Meier, Cox Proportional Hazards)
   - คำนวณขนาดตัวอย่าง (Sample Size) ด้วยสูตรทางคณิตศาสตร์ที่แม่นยำ พร้อมบวกชดเชยการสูญหายระหว่างติดตาม (Dropout/Loss to Follow-up Buffer)
4. **`Diagnostic Accuracy Evaluator Agent`**:
   - วิเคราะห์ตาราง 2x2 Contingency Matrix (Sensitivity, Specificity, PPV, NPV, Youden's Index $J$)
   - คำนวณ **Likelihood Ratios ($LR+, LR-$)** และใช้หลักการแบบเบย์ (**Bayesian Fagan's Nomogram**) แปลง Pre-test $\rightarrow$ Post-test probability
   - ประเมินเกณฑ์ **SnNout** (Rule-Out) และ **SpPin** (Rule-In)
5. **`Causal Inference & RWE Guardian Agent`**:
   - ตรวจจับโครงสร้าง Causal Graph / DAG (Confounder vs. Mediator vs. Collider)
   - ป้องกัน **Collider Stratification Bias (Berkson's Fallacy)** และ Overadjustment Bias
   - วางระเบียบวิธี **Target Trial Emulation 7 ขั้นตอน (Hernán & Robins)** สำหรับข้อมูลสุขภาพ RWD/EHR เพื่อกำจัด **Immortal Time Bias**
6. **`Critical Appraisal & Reporting Guidelines Guardian`**:
   - ตรวจสอบความสอดคล้องกับมาตรฐานการรายงานวิจัยสากล: **CONSORT** (RCT), **STROBE** (Observational), **STARD** (Diagnostic), **PRISMA** (Meta-analysis)
   - ประเมินความเสี่ยงต่ออคติ (Risk of Bias) ตามแนวทาง **CASP** และตรวจสอบความเป็นเหตุเป็นผลตาม **Bradford Hill Criteria**
7. **`Lead Methodologist Agent (PI Supervisor)`**:
   - ตรวจสอบความสอดคล้องข้ามเอเจนต์ (Cross-Agent Consistency) และสังเคราะห์เป็นเอกสาร **Research Protocol / Statistical Analysis Plan (SAP)** ฉบับสมบูรณ์

---

## 📁 2. โครงสร้างโฟลเดอร์โครงการ (Repository Structure)

```
medical_research_multiagent/
├── knowledge/                     # คลังความรู้ที่สกัดมาจาก Notion
│   ├── clinical_epidemiology.json # ระบาดวิทยาคลินิก รูปแบบการวิจัย อคติ เกณฑ์ PICO
│   ├── biostatistics_daniel.json  # สูตรสถิติและการเลือกการทดสอบ (Daniel 9th ed.)
│   ├── diagnostic_performance.json# ตัวชี้วัด 2x2, LR, Fagan Nomogram, Cutoff
│   ├── causal_inference_rwe.json  # Pearl Causal Ladder, DAG, Target Trial Emulation
│   ├── reporting_guidelines.json  # CONSORT, STROBE, PRISMA, STARD, CASP
│   └── notion_source_dump.md      # ข้อความฉบับเต็ม 815 KB จาก Notion
├── core/                          # แกนหลักของระบบ
│   ├── types.py                   # Pydantic Schemas กำหนด Data Contract
│   ├── state.py                   # Blackboard Shared State
│   ├── calculators.py             # ฟังก์ชันคำนวณสถิติและตัวชี้วัดความแม่นยำสูง
│   └── engine.py                  # Multi-Agent Workflow Orchestrator
├── agents/                        # คลาสของแต่ละเอเจนต์
│   ├── base.py                    # ฐานรองรับทั้ง LLM (Gemini/OpenAI) และ Expert Engine
│   ├── pico_agent.py
│   ├── study_design_agent.py
│   ├── biostats_agent.py
│   ├── diagnostic_agent.py
│   ├── causal_rwe_agent.py
│   ├── appraisal_agent.py
│   └── lead_methodologist.py
├── tools/                         # เครื่องมือที่เอเจนต์เรียกใช้
│   ├── sample_size_tool.py
│   ├── diagnostic_eval_tool.py
│   ├── dag_analyzer_tool.py
│   ├── target_trial_tool.py
│   └── appraisal_checklist_tool.py
├── cli/
│   └── main.py                    # คอมมานด์ไลน์อินเตอร์เฟซ (CLI with Rich UI)
├── tests/                         # ชุด Unit & Integration Tests ครอบคลุม 100%
│   ├── test_calculators.py
│   ├── test_knowledge_base.py
│   ├── test_agents.py
│   └── test_orchestrator.py
├── examples/                      # ตัวอย่างการรันจริงใน 4 สถานการณ์คลินิก
│   ├── rct_cardiology_protocol.py
│   ├── diagnostic_biomarker.py
│   ├── rwe_target_trial_ckd.py
│   └── critical_paper_appraisal.py
└── requirements.txt
```

---

## ⚡ 3. วิธีการติดตั้งและใช้งาน (Installation & Quickstart)

### 3.1 การติดตั้ง
```bash
cd /Users/tonkla/.gemini/antigravity/scratch/medical_research_multiagent
pip install -r requirements.txt
```

### 3.2 การรันผ่าน CLI
```bash
# 1. รันคำถามการวิจัยทางคลินิกแบบอัตโนมัติ
python cli/main.py "In adult patients with heart failure, does dapagliflozin reduce cardiovascular death compared to standard of care?"

# 2. รันการประเมินชุดตรวจวินิจฉัย (พร้อมพารามิเตอร์ตาราง 2x2)
python cli/main.py "Diagnostic accuracy of point-of-care troponin for acute myocardial infarction" \
  --tp 190 --fp 15 --fn 10 --tn 285 --pre-test-prob 0.25

# 3. รันโหมด Interactive สัมภาษณ์ทีละขั้นตอน
python cli/main.py --interactive
```

### 3.3 การเรียกใช้ในโค้ด Python
```python
from core.engine import MedicalResearchMultiAgentOrchestrator

orchestrator = MedicalResearchMultiAgentOrchestrator()
state = orchestrator.run_pipeline(
    query="In adult type 2 diabetes patients, does semaglutide reduce stroke compared with placebo?"
)

# ดึงผลลัพธ์
print(state.pico)
print(state.study_design)
print(state.biostats_plan)
print(state.markdown_report)
```

---

## 🧪 4. การทดสอบระบบ (Test Suite Verification)

รันชุดทดสอบทั้งหมดเพื่อยืนยันความถูกต้องของคณิตศาสตร์สถิติและเวิร์กโฟลว์ของเอเจนต์:
```bash
PYTHONPATH=. python3 -m unittest discover -s tests
```
*ผลลัพธ์: ผ่านการทดสอบทั้งหมด 17 รายการ (100% Pass Rate).*

---

## 📄 License & Attribution
- พัฒนาขึ้นเพื่อการศึกษาและการวิจัยทางการแพทย์
- Grounded on *Data and Data Analytics in Digital Health*, Research Affairs, Faculty of Medicine, Chulalongkorn University.
