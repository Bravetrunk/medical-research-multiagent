# 📘 Tutorial Guide: คู่มือการใช้งาน Medical Research & Methodology Multi-Agent AI System

คู่มือแนะนำขั้นตอนการใช้งานระบบ **Medical Research Multi-Agent AI** ตั้งแต่ขั้นพื้นฐานไปจนถึงระดับสูง สำหรับแพทย์ นักวิจัยทางคลินิก นักระบาดวิทยา และผู้พัฒนาระบบสุขภาพดิจิทัล (Digital Health)

---

## 📑 สารบัญ (Table of Contents)
1. [บทนำและแนวคิดเบื้องหลัง (Introduction)](#1-บทนำและแนวคิดเบื้องหลัง)
2. [การติดตั้งและเริ่มต้นใช้งานด่วนใน 3 นาที (Quickstart)](#2-การติดตั้งและเริ่มต้นใช้งานด่วนใน-3-นาที)
3. [คู่มือฝึกปฏิบัติจริง 4 เวิร์กโฟลว์หลัก (4 Hands-On Scenarios)](#3-คู่มือฝึกปฏิบัติจริง-4-เวิร์กโฟลว์หลัก)
   - [Scenario 1: ออกแบบงานวิจัยรักษาทางคลินิก (Therapeutic RCT)](#scenario-1-ออกแบบงานวิจัยรักษาทางคลินิก-therapeutic-rct)
   - [Scenario 2: ประเมินชุดตรวจวินิจฉัยและไบโอมาร์กเกอร์ (Diagnostic Accuracy & Fagan Nomogram)](#scenario-2-ประเมินชุดตรวจวินิจฉัยและไบโอมาร์กเกอร์-diagnostic-accuracy)
   - [Scenario 3: วิเคราะห์เวชระเบียนโลกจริง (RWE & Target Trial Emulation)](#scenario-3-วิเคราะห์เวชระเบียนโลกจริง-rwe--target-trial-emulation)
   - [Scenario 4: ประเมินวิพากษ์บทความวิจัยทางการแพทย์ (Critical Paper Appraisal)](#scenario-4-ประเมินวิพากษ์บทความวิจัยทางการแพทย์-critical-paper-appraisal)
4. [ตารางสรุปคำสั่ง Command Cheat Sheet & Options](#4-ตารางสรุปคำสั่ง-command-cheat-sheet--options)
5. [การเรียกใช้งานผ่าน Python SDK](#5-การเรียกใช้งานผ่าน-python-sdk)
6. [วิธีอ่านผลลัพธ์และนำ Proposal ไปใช้งานจริง](#6-วิธีอ่านผลลัพธ์และนำ-proposal-ไปใช้งานจริง)
7. [คำถามที่พบบ่อย (FAQ) & Troubleshooting](#7-คำถามที่พบบ่อย-faq--troubleshooting)

---

## 1. บทนำและแนวคิดเบื้องหลัง

ระบบนี้สร้างขึ้นเพื่อแก้ปัญหาความยุ่งยากและความผิดพลาดทางระเบียบวิธีวิจัย (Methodological & Statistical Pitfalls) โดยแปลงองค์ความรู้ระดับบัณฑิตศึกษาจากคณะแพทยศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย (**DAB Unit**, อ.ดร.นพ.อมริศ ตันสัจจา) ผสานกับตำราสากล:
- **Clinical Epidemiology** (Fletcher)
- **Biostatistics** (Daniel 9th ed.)
- **Causal AI & RWE** (Judea Pearl, Hernán & Robins)

### การทำงานประสานกันของ 7 Agents
```
[User Query]
      │
      ▼
1. PICO Agent (จำแนก P-I-C-O + FINER + Question Type)
      │
      ▼
2. Study Design Agent (เลือก RCT / Cohort / Diagnostic + วาง Bias Safeguards)
      ├──► 3. Biostats Agent (คำนวณ Sample Size + เลือก Parametric/Nonparametric Test)
      ├──► 4. Diagnostic Agent (2x2 Matrix, Sens/Spec, LR+, LR-, Fagan Nomogram)
      └──► 5. Causal RWE Agent (DAGs, Backdoor Set, Target Trial 7 ขั้นตอน)
      │
      ▼
6. Appraisal Agent (ตรวจสอบเช็กลิสต์สากล CONSORT, STROBE, STARD, CASP)
      │
      ▼
7. Lead Methodologist (สังเคราะห์เอกสาร Research Protocol & SAP ฉบับสมบูรณ์)
```

---

## 2. การติดตั้งและเริ่มต้นใช้งานด่วนใน 3 นาที

### ขั้นตอนที่ 1: เข้าสู่ไดเรกทอรีโครงการ
เปิด Terminal บนเครื่อง Mac ของคุณ แล้วพิมพ์คำสั่ง:
```bash
cd /Users/tonkla/.gemini/antigravity/scratch/medical_research_multiagent
```

### ขั้นตอนที่ 2: รันคำถามทดสอบคำถามแรก
```bash
python cli/main.py "In adult patients with heart failure, does dapagliflozin reduce cardiovascular death compared with standard of care?"
```

**ผลลัพธ์:** ระบบจะแสดง Trace การทำงานของเอเจนต์แต่ละตัวบนหน้าจอ Terminal แบบสีสันสวยงาม (Rich UI) พร้อมบันทึกไฟล์ข้อเสนอโครงการชื่อ `medical_research_protocol.md` ให้โดยอัตโนมัติ!

---

## 3. คู่มือฝึกปฏิบัติจริง 4 เวิร์กโฟลว์หลัก

---

### Scenario 1: ออกแบบงานวิจัยรักษาทางคลินิก (Therapeutic RCT)
* **โจทย์:** ต้องการออกแบบงานวิจัยเปรียบเทียบประสิทธิผลของยา Semaglutide ในการลดภาวะ Stroke ในผู้ป่วยเบาหวาน
* **คำสั่ง:**
```bash
python cli/main.py "In adult type 2 diabetes patients, does semaglutide reduce ischemic stroke compared with placebo?" \
  --output protocol_semaglutide_rct.md
```
* **สิ่งที่เอเจนต์ส่งมอบ:**
  1. **PICO Table:** แยกประชากร, ตัวแทรกแซง, ตัวเปรียบเทียบ, ผลลัพธ์
  2. **Study Design:** แนะนำ **Parallel Double-Blind RCT** พร้อมระบบสุ่มบล็อกคอมพิวเตอร์และการปกปิดลำดับการสุ่มด้วย **SNOSE**
  3. **Biostatistics:** คำนวณขนาดตัวอย่าง ($n$) สำหรับเปรียบเทียบสัดส่วน 2 กลุ่ม พร้อมชดเชย Dropout 15%
  4. **Reporting Compliance:** สอดคล้องตามเกณฑ์ **CONSORT 2010 Checklist**

---

### Scenario 2: ประเมินชุดตรวจวินิจฉัยและไบโอมาร์กเกอร์ (Diagnostic Accuracy)
* **โจทย์:** มีผลการทดสอบชุดตรวจ Rapid Antigen หรือ Biomarker ใหม่ โดยเก็บตัวอย่างผู้ป่วยจริง 500 ราย (เป็นโรค 200 ราย, ไม่เป็นโรค 300 ราย) ได้ผล:
  - True Positive (TP) = 185
  - False Positive (FP) = 15
  - False Negative (FN) = 15
  - True Negative (TN) = 285
  - ความชุกในคลินิก (Pre-test Probability) = 20% (0.20)
* **คำสั่ง:**
```bash
python cli/main.py "Diagnostic accuracy of novel biomarker assay for rapid screening" \
  --tp 185 --fp 15 --fn 15 --tn 285 --pre-test-prob 0.20 \
  --output diagnostic_report.md
```
* **สิ่งที่เอเจนต์ส่งมอบ:**
  1. **Intrinsic Metrics:** Sensitivity (92.5%), Specificity (95.0%)
  2. **Clinical Rules:** ยืนยันว่าผ่านเกณฑ์ **SnNout** (Rule-Out ได้ผลดีเยี่ยม) และ **SpPin** (Rule-In ได้แม่นยำ)
  3. **Likelihood Ratios:** $LR+ = 18.5$ (Very Strong Rule-In), $LR- = 0.079$ (Very Strong Rule-Out)
  4. **Bayesian Shift:** คำนวณการเปลี่ยนความน่าจะเป็น:
     - ก่อนตรวจ (Pre-test): **20%**
     - ผลตรวจเป็นบวก $\rightarrow$ โอกาสเป็นโรคพุ่งขึ้นเป็น **82.2%**
     - ผลตรวจเป็นลบ $\rightarrow$ โอกาสเป็นโรคลดฮวบเหลือเพียง **1.9%**
  5. **Checklist:** รายงานตามเกณฑ์ **STARD 2015**

---

### Scenario 3: วิเคราะห์เวชระเบียนโลกจริง (RWE & Target Trial Emulation)
* **โจทย์:** ต้องการใช้ข้อมูลโรงพยาบาล (EHR) ศึกษาว่ายาลดความดันกลุ่ม ARB เทียบกับ ACEI ช่วยลดอุบัติการณ์ของโรคไตวายเรื้อรังหรือไม่ แต่กังวลเรื่อง **Immortal Time Bias** และ Confounders
* **คำสั่ง:**
```bash
python cli/main.py "In hypertensive patients, does ARB vs ACEI initiation prevent chronic kidney disease using real-world EHR data (Target Trial Emulation)?" \
  --output rwe_target_trial.md
```
* **สิ่งที่เอเจนต์ส่งมอบ:**
  1. **Causal Graph / DAG Analysis:**
     - ระบุตัวแปรที่ต้องควบคุม (**Minimal Sufficient Adjustment Set**) เช่น อายุ, เบาหวานเดิม, eGFR เริ่มต้น
     - ตรวจจับ **Collider:** เตือนห้ามนำตัวแปร "อัตราการนอน รพ. หลังเริ่มยา" มาเป็นตัวแปรควบคุม เพราะจะทำให้เกิด **Collider Stratification Bias (Berkson's Fallacy)** ทันที
  2. **Target Trial Protocol 7 ขั้นตอน (Hernán & Robins):**
     - กำหนดจุด **Time Zero** ณ วันแรกที่เริ่มรับยาตัวใหม่ (New-User Active Comparator Design)
     - ตัด Prevalent Users ทิ้งเพื่อป้องกัน Selection Bias
     - วางแผนวิเคราะห์ด้วย **IPTW (Inverse Probability of Treatment Weighting)** ร่วมกับ Cox Regression

---

### Scenario 4: ประเมินวิพากษ์บทความวิจัยทางการแพทย์ (Critical Paper Appraisal)
* **โจทย์:** ต้องการนำรายงานวิจัยหรือเปเปอร์ที่ตีพิมพ์แล้วมาตรวจสอบหาจุดบกพร่องและคำนวณขนาดอิทธิพล (Effect Size) ใหม่
* **คำสั่ง:** สามารถรันสคริปต์ตัวอย่างใน `examples/`:
```bash
python examples/critical_paper_appraisal.py
```
* **ผลลัพธ์ที่ได้:**
  - ตรวจสอบผ่านเกณฑ์ **STROBE** และ **CASP Checklist**
  - คำนวณซ้ำค่า **Risk Ratio (RR)**, **Absolute Risk Reduction (ARR)**, **Number Needed to Treat (NNT)**, และ **Attributable Risk Percent**

---

## 4. ตารางสรุปคำสั่ง Command Cheat Sheet & Options

| อาร์กิวเมนต์ | ชื่อย่อ | คำอธิบาย | ตัวอย่างการใส่ค่า |
| :--- | :--- | :--- | :--- |
| `query` | *(ไม่มี)* | คำถามการวิจัยทางคลินิก (ภาษาไทยหรืออังกฤษ) | `"In adults, does drug X reduce mortality?"` |
| `--population` | `-p` | ระบุกลุ่มประชากรเป้าหมายแบบเจาะจง | `-p "Patients with CKD Stage 3"` |
| `--intervention`| `-i` | ระบุตัวแทรกแซงหรือยาที่ศึกษา | `-i "Empagliflozin 10 mg daily"` |
| `--comparison`  | `-c` | ระบุตัวเปรียบเทียบ | `-c "Matching Placebo"` |
| `--outcome`     | `-o` | ระบุผลลัพธ์หลักทางคลินิก | `-o "All-cause mortality at 2 years"` |
| `--output`      | `-f` | กำหนดชื่อไฟล์ผลลัพธ์ Markdown ที่จะบันทึก | `-f "my_study_protocol.md"` |
| `--tp, --fp`    | *(ไม่มี)* | ค่า True Positive / False Positive ในตาราง 2x2 | `--tp 180 --fp 20` |
| `--fn, --tn`    | *(ไม่มี)* | ค่า False Negative / True Negative ในตาราง 2x2 | `--fn 10 --tn 290` |
| `--pre-test-prob`| *(ไม่มี)* | ความชุกก่อนตรวจ (ค่าระหว่าง 0.0 – 1.0) | `--pre-test-prob 0.15` |
| `--interactive` | *(ไม่มี)* | เข้าสู่โหมดสัมภาษณ์ทีละขั้นตอน | `python cli/main.py --interactive` |

---

## 5. การเรียกใช้งานผ่าน Python SDK

หากต้องการนำระบบไปต่อยอดในโปรเจกต์ Python หรือ Web Dashboard สามารถเรียกใช้งานได้โดยตรง:

```python
import sys
# เพิ่ม Path ของโมดูล
sys.path.append("/Users/tonkla/.gemini/antigravity/scratch/medical_research_multiagent")

from core.engine import MedicalResearchMultiAgentOrchestrator

# 1. สร้างอินสแตนซ์ของ Orchestrator
orchestrator = MedicalResearchMultiAgentOrchestrator()

# 2. ป้อนคำถามการวิจัย
state = orchestrator.run_pipeline(
    query="In adult heart failure patients, does sacubitril/valsartan reduce hospitalization compared with enalapril?"
)

# 3. ดึงผลลัพธ์เชิงโครงสร้าง (Structured Data)
print(f"Study Design: {state.study_design.selected_design.value}")
print(f"Sample Size per Arm: {state.biostats_plan.n_per_arm}")
print(f"Total Sample Size (+15% Dropout): {state.biostats_plan.total_n_with_dropout}")
print(f"Primary Test: {state.biostats_plan.formula_used}")

# 4. บันทึกผลรายงานฉบับสมบูรณ์
with open("protocol_output.md", "w", encoding="utf-8") as f:
    f.write(state.markdown_report)
```

---

## 6. วิธีอ่านผลลัพธ์และนำ Proposal ไปใช้งานจริง

ไฟล์ผลลัพธ์ `.md` ที่ระบบสร้างขึ้นจะประกอบด้วย 8 หัวข้อมาตรฐาน สามารถนำไปส่งคณะกรรมการจริยธรรมการวิจัย (IRB) หรือแนบขอทุนวิจัยได้ทันที:

1. **Section 1: PICO & FINER Matrix**
   - ตรวจสอบว่าคำถามมีองค์ประกอบครบและผ่านเกณฑ์ Feasible, Interesting, Novel, Ethical, Relevant หรือไม่
2. **Section 2: Study Design & Bias Safeguards**
   - ดูแผนการสุ่ม (Randomization) และการปกปิด (Blinding & Allocation Concealment)
3. **Section 3: Biostatistics & Sample Size**
   - นำตัวเลข **Total Sample Size with Attrition Buffer** ไปใส่ในระเบียบวิธีวิจัยและงบประมาณ
4. **Section 4: Diagnostic Performance (ถ้ามี)**
   - ดูค่า LR+ และ LR- เพื่อประเมินความคุ้มค่าในการนำชุดตรวจไปใช้จริงในคลินิก
5. **Section 5: Causal DAG & Target Trial (สำหรับงาน RWE/EHR)**
   - นำรายชื่อ **Minimal Sufficient Adjustment Set** ไปใส่เป็น Covariates ในสมการ Cox Regression / Propensity Score
6. **Section 6: Reporting Compliance**
   - ใช้เช็กลิสต์ CONSORT หรือ STROBE เพื่อเตรียมร่างบทความตีพิมพ์ในวารสารระดับนานาชาติ
7. **Section 7: Statistical Analysis Plan (SAP) Summary**
   - สรุปแผนการวิเคราะห์ข้อมูลทางสถิติฉบับย่อ

---

## 7. คำถามที่พบบ่อย (FAQ) & Troubleshooting

* **Q: ต้องต่ออินเทอร์เน็ตหรือมี API Key ก่อนใช้งานหรือไม่?**
  * **A:** **ไม่จำเป็นครับ!** ระบบมีโหมด *Deterministic Clinical Expert Engine* ซึ่งคำนวณชีวสถิติ วิเคราะห์ DAG และดึงความรู้จาก Notion ได้โดยตรง 100% แม้ไม่มีอินเทอร์เน็ต แต่หากคุณใส่ `GEMINI_API_KEY` หรือ `OPENAI_API_KEY` ใน Environment ระบบจะเพิ่มความสละสลวยทางภาษาให้โดยอัตโนมัติ
* **Q: ทำไมการคำนวณ Sample Size ของระบบจึงมีตัวเลขมากกว่าสูตรทั่วไป?**
  * **A:** ระบบได้บวก **Dropout Rate Buffer (ค่าเริ่มต้น 15%)** ให้โดยอัตโนมัติตามมาตรฐานการวิจัยสากล เพื่อป้องกันปัญหา Power ตกเมื่อมีผู้ป่วยสูญหายระหว่างการติดตาม
* **Q: สามารถแก้ไขความรู้หรือเพิ่มเช็กลิสต์ในระบบได้หรือไม่?**
  * **A:** ได้อย่างง่ายดาย โดยเข้าไปแก้ไขไฟล์ JSON ในโฟลเดอร์ `knowledge/` เช่น `clinical_epidemiology.json` หรือ `reporting_guidelines.json` ระบบจะดึงความรู้ใหม่ไปใช้งานทันที
