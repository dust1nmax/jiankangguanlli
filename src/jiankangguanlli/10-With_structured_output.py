from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

# schema 数据格式说明书
class Movie(BaseModel):
    title: str = Field(..., description="电影名称")
    year: int = Field(..., description="上映年份")
    director: str = Field(..., description="导演")
    rating: float = Field(..., description="评分，满分 10 分")

load_dotenv()

model = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 

# fun1

# 同样是model
# model_with_structure = model.with_structured_output(Movie)
# response = model_with_structure.invoke("请提取电影《我不是药神》的基本信息")

# print(response.title)
# print(response.year)
# print(response.director)
# print(response.rating) 

# fun2 
model_with_structure = model.with_structured_output(Movie, include_raw=True)
response = model_with_structure.invoke("请提取电影《我不是药神》的基本信息")

print(response["raw"].content)
print(response["parsed"].title)
print(response["parsed"].director)