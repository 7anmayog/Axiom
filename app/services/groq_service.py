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



class GroqService:
    _shared_key_index = 0
    _lock = None

    def __init__(self, vector_store_serice: VectorStoreService):
        if not GROQ_API_KEYS:
            raise ValueError(
                "No Groq API Keys connfigured. Set GROQ_API_KEY (and optionally GROQ_API_KEY_2, GROQ_API_KEY_3, ...) in .env"
            )
        self.llms = [
            ChatGroq(
                groq_api_key = key,
                model_name=GROQ_MODEL,
                temperature=0.8,
            )
            for key in GROQ_API_KEYS
        ]
        self.vector_store_service = vector_store_serice
        logger.info(f"Initialized GroqService with {len(GROQ_API_KEYS)} API key(s)")
