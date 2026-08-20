from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

model = init_chat_model(
    model="deepseek:deepseek-v4-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"), 
    
)

data = [
    ("system", "你是一个{device_type}助手"),
    ("user", "用户问题：{question}"),
]

prompt = ChatPromptTemplate.from_messages(
    data,
)

messages = prompt.invoke({
    "device_type": "饮水机",
    "question": "不出水了怎么办？",
})

res = model.stream(messages)

for chunk in res:
    if chunk.content:
        print(chunk.content, end="", flush=True)