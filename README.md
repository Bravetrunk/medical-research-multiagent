# 🩺 Medical Research & Methodology Multi-Agent AI System

ระบบปัญญาประดิษฐ์สถาปัตยกรรมหลายเอเจนต์ (**Multi-Agent AI Architecture**) สำหรับการออกแบบระเบียบวิธีวิจัยทางการแพทย์ การวิเคราะห์ชีวสถิติ การประเมินชุดตรวจวินิจฉัย และการอนุมานเชิงสาเหตุในเวชระเบียนโลกจริง (Real-World Evidence)

> 🏛️ **ฐานข้อมูลและกรอบแนวคิดอ้างอิง:** พัฒนาขึ้นโดยอ้างอิงเนื้อหาจากหลักสูตร **Data and Data Analytics in Digital Health** (หน่วยบริหารจัดการข้อมูล ปัญญาประดิษฐ์ และชีวสถิติ: **DAB Unit**, ฝ่ายวิจัย คณะแพทยศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย โดย อ.ดร.นพ.อมริศ ตันสัจจา) ร่วมกับตำรามาตรฐานสากล:
> - *Clinical Epidemiology: The Essentials* (Robert H. Fletcher & Suzanne W. Fletcher)
> - *Biostatistics: A Foundation for Analysis in the Health Sciences* (Wayne W. Daniel, 9th ed.)
> - *Causal Inference & Target Trial Emulation Framework* (Judea Pearl, Miguel Hernán & James Robins)

---

## 🚀 1. ติดตั้งและใช้งานผ่าน npm ได้ทันที (Zero-Dependency Node.js & npx)

**ไม่ต้องใช้ `pip install` หรือตั้งค่า Python venv ใดๆ!** ระบบรองรับการติดตั้งและรันผ่าน `npm` / `npx` โดยตรงจาก GitHub:

### วิธีที่ 1: รันด่วนทันทีผ่าน `npx` (ไม่ต้องติดตั้งลงเครื่อง)
```bash
npx github:Bravetrunk/medical-research-multiagent "In adult patients with heart failure, does dapagliflozin reduce cardiovascular death compared with standard of care?"
```

### วิธีที่ 2: ติดตั้งผ่าน `npm install` จาก GitHub
```bash
# ติดตั้งไว้ในโปรเจกต์ของคุณ
npm install github:Bravetrunk/medical-research-multiagent

# หรือติดตั้งเป็นคำสั่งระดับเครื่อง (Global CLI)
npm install -g github:Bravetrunk/medical-research-multiagent

# เรียกใช้คำสั่งได้ทันที
medical-research "In patients with CKD, does SGLT2i reduce ESRD?"
```

### วิธีที่ 3: เรียกใช้เป็นไลบรารีใน Node.js / TypeScript
```javascript
const { MedicalResearchOrchestrator } = require('medical-research-multiagent');

const orchestrator = new MedicalResearchOrchestrator();
const state = orchestrator.runPipeline(
  "In adult type 2 diabetes patients, does semaglutide reduce stroke compared with placebo?"
);

console.log(state.pico);
console.log(state.studyDesign);
console.log(state.biostatsPlan);
console.log(state.markdownReport);
```

---

## 🐍 2. รองรับ Python SDK ด้วยเช่นกัน (Dual-Stack)

สำหรับผู้ใช้งานสาย Python ยังคงสามารถใช้งาน CLI และโมดูล Python ได้ตามปกติ:
```bash
git clone https://github.com/Bravetrunk/medical-research-multiagent.git
cd medical-research-multiagent
python cli/main.py "Your clinical research question"
```

---

## 🏗️ 3. สถาปัตยกรรม Multi-Agent (Multi-Agent Architecture)

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
   - วางมาตรการป้องกันอคติ (Randomization, Allocation Concealment ด้วย SNOSE, Double-blinding, Intention-to-Treat)
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

## 📁 4. โครงสร้างโฟลเดอร์โครงการ (Repository Structure)

```
medical_research_multiagent/
├── package.json                   # การตั้งค่าสำหรับ npm install และ bin CLI
├── bin/
│   └── cli.js                     # Node.js CLI executable (zero dependencies)
├── lib/                           # Native Node.js Multi-Agent Implementation
│   ├── calculators.js             # Biostats & Diagnostic calculators (Node.js)
│   ├── agents.js                  # 7 Agents implementation in JavaScript
│   └── engine.js                  # Node.js Orchestrator & State
├── index.js                       # CommonJS Entrypoint
├── index.d.ts                     # TypeScript Type Definitions
├── test.js                        # Node.js Test Runner (100% Pass)
├── knowledge/                     # คลังความรู้ที่สกัดมาจาก Notion
│   ├── clinical_epidemiology.json # ระบาดวิทยาคลินิก รูปแบบการวิจัย อคติ เกณฑ์ PICO
│   ├── biostatistics_daniel.json  # สูตรสถิติและการเลือกการทดสอบ (Daniel 9th ed.)
│   ├── diagnostic_performance.json# ตัวชี้วัด 2x2, LR, Fagan Nomogram, Cutoff
│   ├── causal_inference_rwe.json  # Pearl Causal Ladder, DAG, Target Trial Emulation
│   ├── reporting_guidelines.json  # CONSORT, STROBE, PRISMA, STARD, CASP
│   └── notion_source_dump.md      # ข้อความฉบับเต็ม 815 KB จาก Notion
├── core/                          # แกนหลักระบบ Python
├── agents/                        # คลาสเอเจนต์ Python
├── tools/                         # เครื่องมือสำหรับ Python
├── cli/main.py                    # Python CLI Interface (Rich UI)
├── tests/                         # ชุด Python Unit Tests (17 tests)
└── requirements.txt               # สำหรับ Python users
```

---

## 🧪 5. การทดสอบระบบ (Test Suite Verification)

```bash
# ทดสอบฝั่ง Node.js
npm test

# ทดสอบฝั่ง Python
python3 -m unittest discover -s tests
```
*ผลลัพธ์: ผ่านการทดสอบทั้งหมด 100% ทั้งฝั่ง Node.js และ Python*

---

## 📄 License & Attribution
- พัฒนาขึ้นเพื่อการศึกษาและการวิจัยทางการแพทย์
- Grounded on *Data and Data Analytics in Digital Health*, Research Affairs, Faculty of Medicine, Chulalongkorn University.
