import os
import json
from typing import Dict, Any, Optional

class BaseMedicalAgent:
    def __init__(self, name: str, role: str, description: str):
        self.name = name
        self.role = role
        self.description = description
        self.knowledge_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "knowledge"
        )
        self.llm = self._setup_llm()

    def _setup_llm(self):
        """Initializes LLM client if API key is provided, else None (runs deterministic expert mode)."""
        if os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"):
            try:
                from langchain_google_genai import ChatGoogleGenerativeAI
                key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
                return ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=key, temperature=0.1)
            except Exception:
                return None
        elif os.environ.get("OPENAI_API_KEY"):
            try:
                from langchain_openai import ChatOpenAI
                return ChatOpenAI(model="gpt-4o", temperature=0.1)
            except Exception:
                return None
        return None

    def load_knowledge(self, filename: str) -> Dict[str, Any]:
        path = os.path.join(self.knowledge_dir, filename)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def query_llm_or_fallback(self, prompt: str, fallback_fn) -> Any:
        if self.llm:
            try:
                response = self.llm.invoke(prompt)
                return response.content
            except Exception as e:
                print(f"[{self.name}] LLM invocation failed ({e}), falling back to deterministic expert engine.")
                return fallback_fn()
        return fallback_fn()
