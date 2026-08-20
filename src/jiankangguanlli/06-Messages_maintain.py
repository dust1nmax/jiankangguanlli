import os

from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# 初始化模型
model = init_chat_model(
    model="deepseek:deepseek-v4-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)

# 维护 messages 历史：用消息类型对象构建初始上下文
messages = [
    SystemMessage(content="你是一个乐于助人的 AI 助手。"),
]

print("开始对话，输入 exit 退出。")

while True:
    user_input = input("\n你: ").strip()
    if user_input.lower() in ("exit", "quit"):
        break

    # 将用户消息包装为 HumanMessage 追加到历史
    messages.append(HumanMessage(content=user_input))

    print("AI: ", end="", flush=True)
    reply_parts = []

    # 流式输出：边生成边显示
    for chunk in model.stream(messages):
        if chunk.content:
            print(chunk.content, end="", flush=True)
            reply_parts.append(chunk.content)

    # 将 AI 回复包装为 AIMessage 追加到历史，供下一轮携带上下文
    # "".join(reply_parts)："" 是分隔符（字符串方法），把 reply_parts 的碎片粘成完整文本
    messages.append(AIMessage(content="".join(reply_parts)))
