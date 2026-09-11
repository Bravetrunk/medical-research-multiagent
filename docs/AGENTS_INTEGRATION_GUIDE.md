# คู่มือการนำ Medical Research Multi-Agent ไปใช้งานร่วมกับ AI Agents
# (AI Agents & LLM Integration Guide)

คู่มือฉบับสมบูรณ์สำหรับการเชื่อมต่อระบบ **Medical Research Multi-Agent AI System** (Grounded on Chulalongkorn University DAB Unit, Fletcher Clinical Epidemiology, Daniel Biostatistics, and Judea Pearl Causal AI) เข้ากับ AI Coding Agents, Agentic IDEs, LLMs และ Frameworks ต่างๆ

---

## สารบัญ (Table of Contents)
1. [ตารางสรุปความเข้ากันได้ (Compatibility Matrix)](#1-ตารางสรุปความเข้ากันได้-compatibility-matrix)
2. [Claude Code (Anthropic)](#2-claude-code-anthropic)
3. [Google Antigravity (AGY)](#3-google-antigravity-agy)
4. [Cursor & Windsurf](#4-cursor--windsurf)
5. [xAI Grok & OpenAI Codex / ChatGPT](#5-xai-grok--openai-codex--chatgpt)
6. [Universal MCP Server (Claude Desktop, Cline, Roo Code)](#6-universal-mcp-server-claude-desktop-cline-roo-code)
7. [Multi-Agent Frameworks (CrewAI, LangGraph, Vercel AI SDK)](#7-multi-agent-frameworks-crewai-langgraph-vercel-ai-sdk)
8. [System Prompt Template สำหรับ Web UI (ChatGPT, Grok, Claude.ai)](#8-system-prompt-template-สำหรับ-web-ui)

---

## 1. ตารางสรุปความเข้ากันได้ (Compatibility Matrix)

| AI Platform / Agent | วิธีการเชื่อมต่อ (Integration Method) | Zero Install (`npx`) | Native MCP | Custom Rules |
| :--- | :--- | :---: | :---: | :---: |
| **Claude Code** | Native MCP / `CLAUDE.md` / CLI | ✅ | ✅ | ✅ |
| **Google Antigravity** | Builtin Skill / MCP / Subagent | ✅ | ✅ | ✅ |
| **Cursor IDE** | MCP / `.cursorrules` / MDC Rule | ✅ | ✅ | ✅ |
| **Windsurf IDE** | MCP / `.windsurfrules` | ✅ | ✅ | ✅ |
| **xAI Grok** | Function Calling API / System Prompt | ✅ | ผ่าน API | N/A |
| **OpenAI Codex / ChatGPT** | Function Calling / Custom GPT Action | ✅ | ผ่าน API | N/A |
| **Claude Desktop** | MCP stdio Server | ✅ | ✅ | N/A |
| **VS Code (Cline / Roo Code)** | MCP stdio Server | ✅ | ✅ | ✅ |
| **CrewAI / LangGraph** | Python Tool Wrapper | N/A | N/A | ✅ |

---

## 2. Claude Code (Anthropic)

Claude Code รองรับการเชื่อมต่อได้ 3 รูปแบบ:

### วิธีที่ 2.1: เชื่อมต่อผ่าน Model Context Protocol (MCP) [แนะนำสูงสุด]
รันคำสั่งเพียงครั้งเดียวใน Terminal เพื่อเพิ่ม Medical Research เข้าเป็นเครื่องมือประจำของ Claude Code:

```bash
claude mcp add medical-research -- npx -y github:Bravetrunk/medical-research-multiagent medical-research-mcp
```

เมื่อเชื่อมต่อแล้ว Claude Code จะมี Tool 5 ตัวใช้งานได้อัตโนมัติ:
- `design_clinical_protocol`: สร้าง Research Protocol ฉบับเต็ม 7 Agents
- `calculate_sample_size_rct`: คำนวณ Sample Size สำหรับ Parallel RCT
- `calculate_sample_size_means`: คำนวณ Sample Size สำหรับข้อมูลต่อเนื่อง (Continuous Means)
- `calculate_diagnostic_matrix`: คำนวณ Sensitivity, Specificity, LR+, LR-, Fagan Nomogram
- `calculate_epidemiologic_association`: คำนวณ RR, OR, ARR, NNT

### วิธีที่ 2.2: ใช้ผ่าน `CLAUDE.md` ในโปรเจกต์
ใน Repository นี้มีไฟล์ [`CLAUDE.md`](../CLAUDE.md) อยู่ที่ Root เรียบร้อยแล้ว หากนำไปวางในโปรเจกต์งานวิจัยของคุณ Claude Code จะอ่านคำแนะนำและเรียกใช้คำสั่ง CLI อัตโนมัติเมื่อถูกถามคำถามทางการแพทย์:

```bash
# ตัวอย่างที่ Claude Code จะรันให้โดยอัตโนมัติ:
npx -y github:Bravetrunk/medical-research-multiagent "Can topical calcipotriol reduce skin cancer risk in renal transplant recipients?"
```

---

## 3. Google Antigravity (AGY)

Google Antigravity รองรับทั้งระดับ **Global Skill**, **MCP Server**, และ **Subagent Workflow**:

### วิธีที่ 3.1: ติดตั้งเป็น Antigravity Skill
คัดลอกโฟลเดอร์ `skill/` ไปไว้ที่ไดเรกทอรีสกิลสากลของ Antigravity:

```bash
mkdir -p ~/.gemini/config/skills/medical-research-methodology
cp skill/SKILL.md ~/.gemini/config/skills/medical-research-methodology/SKILL.md
```

เมื่อลงทะเบียนแล้ว เวลาคุณพิมพ์คุยกับ Antigravity เช่น:
> *"ช่วยออกแบบ clinical trial protocol สำหรับยากลุ่ม SGLT2i ในผู้ป่วย CKD พร้อมคำนวณ sample size ให้หน่อย"*

Antigravity จะตรวจจับและ Activate สกิล `medical-research-methodology` ทันที

### วิธีที่ 3.2: ติดตั้งเป็น Antigravity MCP Server
เพิ่มคอนฟิกในไฟล์ MCP Configuration ของ Antigravity:

```json
{
  "mcpServers": {
    "medical-research": {
      "command": "npx",
      "args": [
        "-y",
        "github:Bravetrunk/medical-research-multiagent",
        "medical-research-mcp"
      ]
    }
  }
}
```

### วิธีที่ 3.3: ให้ Antigravity สั่งรัน Subagent ในโหมด Background
คุณสามารถสั่ง Antigravity ในแชทได้ว่า:
```text
/boost ให้รัน subagent วิจัยทางคลินิกโดยใช้ skill medical-research-methodology สังเคราะห์ full RCT protocol สำหรับ topic นี้
```

---

## 4. Cursor & Windsurf

### วิธีที่ 4.1: ติดตั้ง MCP Server ใน Cursor
1. เปิด **Cursor Settings** (`Cmd + ,` หรือ `Ctrl + ,`)
2. ไปที่แท็บ **Features** $\to$ **MCP**
3. คลิก **+ Add New MCP Server**
   - **Name**: `medical-research`
   - **Type**: `command`
   - **Command**: `npx -y github:Bravetrunk/medical-research-multiagent medical-research-mcp`
4. เมื่อสถานะขึ้นไฟสีเขียว Cursor Composer และ Chat จะสามารถเรียกฟังก์ชันคำนวณและออกแบบ Protocol ทางการแพทย์ได้ทันที

### วิธีที่ 4.2: ใช้ Cursor Rules (`.cursorrules` & `.cursor/rules/`)
ใน Repository นี้มีไฟล์คอนฟิกให้เรียบร้อยแล้ว:
- [`.cursorrules`](../.cursorrules): กฎระดับ Root สำหรับโปรเจกต์
- [`.cursor/rules/medical-research.mdc`](../.cursor/rules/medical-research.mdc): กฎแบบ Rich MDC Format

### วิธีที่ 4.3: ติดตั้งใน Windsurf (Cascade)
เพิ่ม MCP ใน `~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "medical-research": {
      "command": "npx",
      "args": [
        "-y",
        "github:Bravetrunk/medical-research-multiagent",
        "medical-research-mcp"
      ]
    }
  }
}
```
พร้อมทั้งมีไฟล์ [`.windsurfrules`](../.windsurfrules) คอยควบคุมคุณภาพระเบียบวิธีวิจัย

---

## 5. xAI Grok & OpenAI Codex / ChatGPT

สำหรับ xAI Grok (API `api.x.ai/v1`) และ OpenAI (GPT-4o, Codex, ChatGPT) สามารถใช้งานผ่าน **Function Calling** หรือ **Custom GPT Actions**:

### วิธีที่ 5.1: เชื่อมต่อผ่าน Function Calling API (Python)
เราเตรียมสคริปต์ตัวอย่างพร้อมรันไว้ใน [`integrations/openai_grok_agent.py`](../integrations/openai_grok_agent.py) และ Schema ใน [`integrations/openai_grok_tools.json`](../integrations/openai_grok_tools.json):

```python
import json
from openai import OpenAI
from integrations.openai_grok_agent import execute_tool_call, MEDICAL_TOOLS

# 1. สำหรับ OpenAI GPT-4o / Codex
client = OpenAI(api_key="your-openai-api-key")
model_name = "gpt-4o"

# 2. สำหรับ xAI Grok (เพียงเปลี่ยน client baseURL)
# client = OpenAI(api_key="your-xai-key", base_url="https://api.x.ai/v1")
# model_name = "grok-beta"

response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": "You are a Clinical Biostatistician & Epidemiologist."},
        {"role": "user", "content": "Calculate the sample size for a 2-arm parallel RCT where control event rate is 35% and treatment is 15%."}
    ],
    tools=MEDICAL_TOOLS,
    tool_choice="auto"
)

# จัดการ Tool Calls อัตโนมัติ
tool_call = response.choices[0].message.tool_calls[0]
result = execute_tool_call(tool_call.function.name, json.loads(tool_call.function.arguments))
print(result)
```

### วิธีที่ 5.2: ใช้งานกับ ChatGPT Custom GPTs (No-Code Action)
1. ไปที่ [ChatGPT GPT Builder](https://chatgpt.com/gpts/editor)
2. ไปที่แท็บ **Configure** $\to$ เลื่อนลงมาที่ **Actions** $\to$ คลิก **Create new action**
3. คัดลอกเนื้อหาจากไฟล์ [`integrations/openapi.json`](../integrations/openapi.json) ไปวางในช่อง **Schema**
4. บันทึก Action — ผู้ใช้งาน Custom GPT ของคุณจะสามารถคำนวณ Sample Size และ Diagnostic Performance ได้แบบ Interactive ทันที

---

## 6. Universal MCP Server (Claude Desktop, Cline, Roo Code)

โปรแกรมใดๆ ที่รองรับ Model Context Protocol (MCP) ผ่าน standard IO สามารถเชื่อมต่อได้ทันทีโดยไม่ต้อง clone repo ลงเครื่อง:

### คอนฟิกสำหรับ Claude Desktop (`claude_desktop_config.json`)
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "medical-research": {
      "command": "npx",
      "args": [
        "-y",
        "github:Bravetrunk/medical-research-multiagent",
        "medical-research-mcp"
      ]
    }
  }
}
```

### คอนฟิกสำหรับ Cline / Roo Code ใน VS Code
เปิดตั้งค่า MCP Settings ของ Extension แล้ววาง:

```json
{
  "mcpServers": {
    "medical-research": {
      "command": "npx",
      "args": [
        "-y",
        "github:Bravetrunk/medical-research-multiagent",
        "medical-research-mcp"
      ],
      "disabled": false,
      "autoApprove": [
        "design_clinical_protocol",
        "calculate_sample_size_rct",
        "calculate_diagnostic_matrix"
      ]
    }
  }
}
```

---

## 7. Multi-Agent Frameworks (CrewAI, LangGraph, Vercel AI SDK)

### วิธีที่ 7.1: CrewAI Integration
ไฟล์พร้อมใช้งาน: [`integrations/crewai_tool.py`](../integrations/crewai_tool.py)

```python
from crewai import Agent, Task, Crew
from integrations.crewai_tool import ClinicalProtocolTool, SampleSizeRCTTool

methodologist = Agent(
    role="Lead Medical Methodologist",
    goal="Design rigorous clinical protocols and statistical plans",
    backstory="Trained in Chulalongkorn DAB Unit, Daniel Biostatistics, and Fletcher Epidemiology",
    tools=[ClinicalProtocolTool(), SampleSizeRCTTool()],
    verbose=True
)
```

### วิธีที่ 7.2: LangChain / LangGraph Integration
ไฟล์พร้อมใช้งาน: [`integrations/langchain_tools.py`](../integrations/langchain_tools.py)

```python
from integrations.langchain_tools import (
    design_clinical_protocol_tool,
    calculate_rct_sample_size_tool,
    calculate_diagnostic_matrix_tool
)

tools = [design_clinical_protocol_tool, calculate_rct_sample_size_tool, calculate_diagnostic_matrix_tool]
# นำไปผูกกับ LangGraph StateGraph หรือ create_react_agent(model, tools)
```

### วิธีที่ 7.3: Vercel AI SDK (Next.js / Node.js TypeScript)
ไฟล์พร้อมใช้งาน: [`integrations/vercel_ai_tools.ts`](../integrations/vercel_ai_tools.ts)

```typescript
import { generateText } from 'ai';
import { openai } from '@ai-sdk/openai';
import { medicalResearchTools } from './integrations/vercel_ai_tools';

const { text } = await generateText({
  model: openai('gpt-4o'),
  prompt: 'Calculate sample size for an RCT comparing 35% vs 15% mortality',
  tools: medicalResearchTools,
  maxSteps: 5,
});
```

---

## 8. System Prompt Template สำหรับ Web UI

หากคุณต้องการใช้งานใน Web Chat ทั่วไป (เช่น ChatGPT Plus, Grok บน x.com, Claude.ai Web UI) โดยไม่มีการรันโค้ด สามารถคัดลอก Prompt ด้านล่างนี้ไปวางใน Custom Instructions หรือเปิดแชทใหม่ได้ทันที:

```markdown
You are an elite Clinical Epidemiologist and Biostatistician grounded strictly in:
1. Faculty of Medicine, Chulalongkorn University (Doctoral & Advanced Biostatistics / DAB Unit)
2. Fletcher's Clinical Epidemiology (The Essentials)
3. Daniel's Biostatistics (A Foundation for Analysis in the Health Sciences)
4. Judea Pearl's Causal AI & Miguel Hernán's Target Trial Emulation

When answering ANY clinical research or methodology questions, strictly enforce:
- Structured PICO & FINER Feasibility appraisal
- Study Design Hierarchy (RCT, Prospective Cohort, Case-Control, Cross-Sectional, Diagnostic Test)
- Exact mathematical sample size estimation (Z_alpha/2=1.96, Z_beta=0.842 for 80% power) with 10-15% dropout inflation: N_adj = N / (1 - dropout)
- Diagnostic Testing: Sensitivity, Specificity, Likelihood Ratios (LR+, LR-), SnNout (rule out if Sn>=90%), SpPin (rule in if Sp>=90%), and Bayesian Fagan Nomogram updating
- Causal Inference: Explicitly map Confounders, Mediators, and Colliders. NEVER adjust for colliders or post-treatment intermediates.
- Reporting Guidelines compliance: CONSORT (RCT), STROBE (Observational), STARD (Diagnostic), PRISMA (Systematic Reviews), and Cochrane RoB 2 / ROBINS-I.
```
