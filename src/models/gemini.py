from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def init_chat_model():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    )

llm = init_chat_model()