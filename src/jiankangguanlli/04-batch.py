import os

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
    model="deepseek:deepseek-v4-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"), 
)

res = model.batch(
    [
        "你好",
        "什么是langchain",
        "什么是langgraph",
    ]
)

for re in res:
    print(re.content)