from typing import List, Optional
from tavily import TavilyClient
import logging
import os

from app.services.groq_service import GroqService, escape_curly_braces
from app.services.vector_store import VectorStoreService
from app.utils.time_info import get_time_information
from app.utils.retry import with_retry
from config import AXIOM_SYSTEM_PROMPT
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

logger = logging.getLogger("A.X.I.O.M")