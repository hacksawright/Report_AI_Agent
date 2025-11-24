from src.graph.schema import State
from src.models import llm

def football_expert_agent(state: State):
    print("football_expert")
    last_message = state["messages"][-1]

    messages = [
        {"role": "system",
         "content": """You are a world-class football expert.
                    Focus on analysis, definition, statistics, history and information related to football.
                    Answer questions about players, clubs, tournaments (Champions League, World Cup, Premier League, etc.), tactics and match history.
                    Use a passionate, knowledgeable tone and never answer questions unrelated to football.
                    If you need the latest information (live scores, new transfers), assume you have the latest data."""
        },
        {
            "role": "user",
            "content": last_message.content
        }
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}