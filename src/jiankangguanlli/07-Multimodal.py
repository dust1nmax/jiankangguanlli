import os

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

# 初始化多模态模型：Qwen-VL（通过 DashScope 兼容接口）
model = init_chat_model(
    model="qwen-vl-max",
    model_provider="openai",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 多模态消息：图片 + 文本 一起发给模型
message = HumanMessage(
    content=[
        {"type": "image_url", "image_url": {"url": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"}},
        {"type": "text", "text": "这张图片里有什么？"},
    ]
)

# 流式输出：边生成边显示
for chunk in model.stream([message]):
    if chunk.content:
        print(chunk.content, end="", flush=True)
