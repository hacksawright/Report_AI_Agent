from src.graph.schema import State

def router(state: State):
    message_type = state.get("message_type", "general")
    if message_type == "emotional":
        return {"next": "therapist"}
    elif message_type == "football":
        return {"next": "football"}
    elif message_type == "logical":
        return {"next": "logical"}
    return {"next": "general"}