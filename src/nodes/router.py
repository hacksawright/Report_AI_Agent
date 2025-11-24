from src.graph.schema import State

def router(state: State):
    message_type = state.get("message_type", "logical")
    if message_type == "emotional":
        return {"next": "therapist"}
    elif message_type == "football":
        return {"next": "football"}
    return {"next": "logical"}