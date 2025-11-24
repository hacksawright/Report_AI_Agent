from langgraph.graph import StateGraph, START, END
from src.nodes import classify_message, logical_agent, router, therapist_agent, football_expert_agent

from .schema import MessageClassifier, State

graph_builder = StateGraph(State)

graph_builder.add_node("classifier", classify_message)
graph_builder.add_node("router", router)
graph_builder.add_node("therapist", therapist_agent)
graph_builder.add_node("logical", logical_agent)
graph_builder.add_node("football", football_expert_agent)
graph_builder.add_edge(START, "classifier")
graph_builder.add_edge("classifier", "router")

graph_builder.add_conditional_edges(
    "router",
    lambda state: state.get("next"),
    {"therapist": "therapist", "logical": "logical", "football" : "football"}
)

graph_builder.add_edge("therapist", END)
graph_builder.add_edge("logical", END)
graph_builder.add_edge("football", END)

graph = graph_builder.compile()
