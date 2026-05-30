from dotenv import load_dotenv
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI, ChatAnthropic

load_dotenv()

llm = ChatOpenAI(model="gpt-4", temperature=0.9)

llm2 = ChatAnthropic(model="claude-2", temperature=0.9)