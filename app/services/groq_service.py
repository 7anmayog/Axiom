from typing import List, Optional
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

import logging

from config import GROQ_API_KEYS, GROQ_MODEL, JARVIS_SYSTEM_PROMPT
from app.services.vector_store import VectorStoreService
from app.utils.time_info import get_time_information

logger = logging.getLogger("A.X.I.O.M")

def escape_curly_braces(text: str) -> str:
    if not text:
        return text
    return text.replace("{", "{{").replace("}", "}}")

def _is_rate_limit_error(exc: BaseException) -> bool:
    msg = str(exc).lower()
    return "429" in str(exc) or "rate limit" in msg or "tokens per day" in msg

def _mask_api_key(key: str) -> str:
    if not key or len(key) <=12:
        return "***masked***"
    return f"{key[:8]}...{key[-4:]}"

