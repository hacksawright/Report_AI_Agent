from src.graph.schema import State
from src.models import llm

def default_agent(state: State):
    print("default agent")
    last_message = state["messages"][-1]

    messages = [
        {"role": "system",
         "content": """You are a friendly, cheerful virtual assistant.
            You are called to handle greeting messages, general messages, or unclear requests.
            Respond in a friendly manner, then ask the user what type of support they would like."""
         },
        {
            "role": "user",
            "content": last_message.content
        }
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}