from src.models import llm
from src.graph.schema import MessageClassifier, State

from src.models import llm
from src.graph.schema import MessageClassifier, State

def classify_message(state: State):
    last_message = state["messages"][-1]
    classifier_llm = llm.with_structured_output(MessageClassifier)

    result = classifier_llm.invoke([
        {
            "role": "system",
            "content": """Classify the user message as one of the following types:
            - 'emotional': if it asks for emotional support, therapy, deals with feelings, or personal problems.
            - 'logical': ONLY if it asks for non-sports facts, technical information, analysis, or practical solutions. **DO NOT use 'logical' for simple greetings or non-information requests.
            - 'football': if the query is specifically about soccer/football (scores, history, analysis, teams, players, or tournaments).
            - 'general': if the message is a **simple greeting** (e.g., 'Hi', 'Hello'), idle chat, or if the intent is **completely unclear** and does not require an expert.
            """
        },
        {"role": "user", "content": last_message.content}
    ])
    return {"message_type": result.message_type}