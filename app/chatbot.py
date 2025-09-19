from app.tools.ai_chat import get_ai_response
from app.tools.weather import get_weather

def get_response(mode: str, message: str) -> str:
    if mode == "weather":
        return get_weather(message)
    else:
        return get_ai_response(message)
