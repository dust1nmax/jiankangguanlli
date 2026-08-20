from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_deepseek import ChatDeepSeek
#搜索工具
from langchain_tavily import TaviLySearch

from dotenv import load_dotenv

load_dotenv()

web_search = TaviLySearch(max_results=2)
model = ChatDeepSeek(model="deepseek-chat")

agent = create_agent(
    model=model,
    tools=[web_search],
    system_prompt="你是一名多才多艺的智能助手，可以调用工具帮助用户解决问题。",
)

res = agent.invoke({
    "messages": [
        {"role": "system","content": "你是一个乐于助人的 AI 助手。"},
        {"role": "user","content": "你好，我是教 AI 的 Yuan 老师。"},
        {"role": "assistant","content": "你好，Yuan 老师，很高兴认识你。"},
        {"role": "user","content": "请查询 SpaceX 最近 7 天的最新消息。"}
    ]
})

for message in res["messages"]:
    message.pretty_print()