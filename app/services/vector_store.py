import json
import logging
from pathlib import Path
from typing import List, Optional
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from config import (
LEARNING_DATA_DIR,
CHATS_DATA_DIR,
VECTOR_STORE_DIR,
EMBEDDING_MODEL,
CHUNK_SIZE,
CHUNK_OVERLAP,
)