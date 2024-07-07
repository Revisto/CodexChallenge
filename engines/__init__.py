from .offline_ai_engine import OfflineAIEngine
from .online_ai_engine import OnlineAIEngine
from .offline_engine import OfflineEngine

def get_engine(engine_type):
    if engine_type == "offline":
        return OfflineEngine()
    elif engine_type == "online_ai":
        return OnlineAIEngine()
    elif engine_type == "offline_ai":
        return OfflineAIEngine()
    else:
        raise ValueError("Unknown engine type")
