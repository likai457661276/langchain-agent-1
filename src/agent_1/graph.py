"""
LangGraph图定义 - 用于LangGraph CLI测试
"""

from typing import Annotated, Optional
from typing_extensions import TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph import StateGraph, add_messages
from langgraph.prebuilt import ToolNode

from src.agent_1.agent import BasicAgent
from src.agent_1.tools import get_all_tools


class AgentState(TypedDict):
    """智能体状态定义"""
    messages: Annotated[list[BaseMessage], add_messages]


def create_graph():
    """创建LangGraph图"""
    from langchain_openai import ChatOpenAI
    from src.agent_1.config import settings
    
    # 创建LLM - 使用硅基流动(Silicon Flow) API
    llm = ChatOpenAI(
        model=settings.siliconflow_model,
        temperature=settings.siliconflow_temperature,
        api_key=settings.siliconflow_api_key,
        base_url=settings.siliconflow_base_url
    )
    
    # 创建工具
    tools = get_all_tools()
    
    # 创建工具节点
    tool_node = ToolNode(tools)
    
    # 创建模型绑定工具
    model = llm.bind_tools(tools)
    
    # 定义模型调用函数
    def call_model(state: AgentState):
        """调用模型"""
        messages = state["messages"]
        response = model.invoke(messages)
        return {"messages": [response]}
    
    # 定义决策函数
    def should_continue(state: AgentState) -> str:
        """决定是否继续使用工具"""
        messages = state["messages"]
        last_message = messages[-1]
        
        # 如果模型请求调用工具，则调用工具
        if last_message.tool_calls:
            return "tools"
        
        # 否则结束
        return "__end__"
    
    # 创建图
    workflow = StateGraph(AgentState)
    
    # 添加节点
    workflow.add_node("agent", call_model)
    workflow.add_node("tools", tool_node)
    
    # 设置入口点
    workflow.set_entry_point("agent")
    
    # 添加条件边
    workflow.add_conditional_edges(
        "agent",
        should_continue,
    )
    
    # 添加从工具到代理的边
    workflow.add_edge("tools", "agent")
    
    # 编译图
    app = workflow.compile()
    
    return app