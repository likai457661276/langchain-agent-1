"""
LangServe服务器配置 - 部署智能体为API服务
"""

from typing import Any, Dict, List, Optional

from fastapi import FastAPI
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.runnables import RunnableConfig
from langserve import add_routes
from langserve.pydantic_v1 import BaseModel, Field

from .agent import BasicAgent
from .config import settings
from .graph import create_graph


# 创建FastAPI应用
app = FastAPI(
    title="Agent_1 API",
    description="基于LangChain的基础智能体API服务",
    version="0.1.0",
)


# 定义请求和响应模型
class ChatInput(BaseModel):
    """聊天输入模型"""
    message: str = Field(..., description="用户消息")
    session_id: Optional[str] = Field(None, description="会话ID，用于保持对话上下文")


class ChatOutput(BaseModel):
    """聊天输出模型"""
    response: str = Field(..., description="智能体回复")
    session_id: Optional[str] = Field(None, description="会话ID")


# 创建全局智能体实例
agent_instance = BasicAgent()
graph_instance = create_graph()


# 添加智能体路由
add_routes(
    app,
    agent_instance.agent,
    path="/agent",
    input_type=ChatInput,
    output_type=ChatOutput,
)


# 添加图路由
add_routes(
    app,
    graph_instance,
    path="/graph",
)


# 创建自定义端点
@app.post("/chat", response_model=ChatOutput)
async def chat_endpoint(input_data: ChatInput) -> ChatOutput:
    """
    自定义聊天端点，提供更简单的接口
    """
    # 调用智能体
    response = agent_instance.invoke(input_data.message)
    
    return ChatOutput(
        response=response,
        session_id=input_data.session_id
    )


@app.get("/")
async def root():
    """根端点，提供API信息"""
    return {
        "name": "Agent_1 API",
        "version": "0.1.0",
        "description": "基于LangChain的基础智能体API服务",
        "endpoints": {
            "agent": "/agent",
            "graph": "/graph",
            "chat": "/chat",
            "docs": "/docs",
        }
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "src.agent_1.server:app",
        host=settings.host,
        port=settings.port,
        reload=True,
    )