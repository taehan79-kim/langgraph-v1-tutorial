from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_teddynote.tools.tavily import TavilySearch
from langgraph.checkpoint.memory import MemorySaver

load_dotenv(override=True)

# 모델 초기화
model = init_chat_model("claude-sonnet-4-5")

# 도구 정의: Tavily 검색 도구
tools = [TavilySearch(max_results=3)]

# 메모리 체크포인터 설정
memory = MemorySaver()

# 에이전트 그래프 생성
graph = create_agent(
    model,
    tools=tools,
    checkpointer=memory,
)
