from langchain_google_genai import ChatGoogleGenerativeAI
from config import Config

config = Config()


llm = ChatGoogleGenerativeAI(
    google_api_key=config.apikey,
    model="gemini-pro"
    )