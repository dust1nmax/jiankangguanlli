'''
import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

Client = OpenAI(

    base_url="https://api.deepseek.com",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)

res = Client.chat.completions.create(
    model= "deepseek-v4-flash",
    messages= [
        {"role":"user","content":"你是谁，来自哪个厂商"}
    ]
)

print(res.choices[0].message.content)

'''
# 使用 init_chat_model 模范化

import os

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
# fun1 init_chat_model + provider
    # model="deepseek-v4-flash",
    # model_provider="deepseek",
    model="deepseek:deepseek-v4-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"), 

# fun2 init_chat_model + openAI/compatible

    # "openai" 表示按照openai兼容协议发送请求
    # model="openai:deepseek-v4-flash",
    # base_url="https://api.deepseek.com",
    # api_key=os.getenv("DEEPSEEK_API_KEY"), 
)

print(model.invoke("你是谁").content)
