# core/fireworks_client.py
from openai import OpenAI
from .config import settings

client = OpenAI(
    api_key=settings.FIREWORKS_API_KEY,
    base_url=settings.FIREWORKS_BASE_URL,
)
