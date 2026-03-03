from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
import logging

from app.models import ChatRequest, ChatResponse

RATE_LIMIT_MESSAGE = (
"You've reached your daily API limit for this assistant. "
"Your credits will reset in a few hours, or you can upgrade your plan for more. "
"Please try again later."
)

def _is_rate_limit_error(exc: Exception) -> bool:
    """True if the exception is a Groq rate limit (429 / tokens per day)."""
    msg = str(exc).lower()
    return "429" in str(exc) or "rate limit" in msg or "tokens per day" in msg

from app.services.vector_store import VectorStoreService
from app.services.groq_service import GroqService
from app.services.realtime_service import RealtimeGroqService
from app.services.chat_service import ChatService
from config import VECTOR_STORE_DIR
from langchain_community.vectorstores import FAISS

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger("A.X.I.O.M")

vector_store_service: VectorStoreService = None
groq_service: GroqService = None
realtime_service: RealtimeGroqService = None
chat_service: ChatService = None



def print_title():
    title = """

            __   __  _____    ____    __  __ 
     /\     \ \ / / |_   _|  / __ \  |  \/  |
    /  \     \ V /    | |   | |  | | | \  / |
   / /\ \     > <     | |   | |  | | | |\/| |
  / ____ \   / . \   _| |_  | |__| | | |  | |
 /_/    \_\ /_/ \_\ |_____|  \____/  |_|  |_|

           I DON'T GUESS, I KNOW.                                   
 

"""
    print(title)                                            