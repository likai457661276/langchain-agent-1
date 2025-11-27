"""
智能体核心模块 - 实现LangChain智能体的核心功能
"""

import os
from typing import List, Optional

from langchain_classic.agents import create_openai_tools_agent, AgentExecutor
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
# from langchain_core.memory import BaseMemory  # 移除这个导入
from langchain_core.messages import BaseMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI  # 硅基流动兼容OpenAI API格式

from .config import settings
from .prompts import create_agent_prompt, create_simple_prompt
from .tools import get_all_tools


class AgentMemory:  # 移除 BaseMemory 继承
    """自定义记忆类，用于存储对话历史"""
    
    def __init__(self, chat_history: Optional[BaseChatMessageHistory] = None):
        self.chat_history = chat_history or ChatMessageHistory()
    
    def save_context(self, inputs: dict, outputs: dict) -> None:
        # 从输入中获取用户消息
        if "input" in inputs:
            self.chat_history.add_user_message(inputs["input"])
        
        # 从输出中获取助手回复
        if "output" in outputs:
            self.chat_history.add_ai_message(outputs["output"])
    
    def clear(self) -> None:
        self.chat_history.clear()


class BasicAgent:
    """基础智能体类"""
    
    def __init__(
        self, 
        model_name: Optional[str] = None,
        temperature: Optional[float] = None,
        use_tools: bool = True,
        memory: Optional[AgentMemory] = None
    ):
        """
        初始化智能体
        
        Args:
            model_name: 模型名称，默认使用配置中的模型
            temperature: 温度参数，默认使用配置中的温度
            use_tools: 是否使用工具，默认为True
            memory: 记忆对象，如果不提供则创建默认记忆
        """
        # 设置LangSmith环境变量
        if settings.langsmith_api_key:
            os.environ["LANGSMITH_API_KEY"] = settings.langsmith_api_key
        if settings.langsmith_project:
            os.environ["LANGSMITH_PROJECT"] = settings.langsmith_project
        os.environ["LANGSMITH_TRACING"] = str(settings.langsmith_tracing).lower()
        
        # 初始化LLM - 使用硅基流动(Silicon Flow) API
        self.llm = ChatOpenAI(
            model=model_name or settings.siliconflow_model,
            temperature=temperature or settings.siliconflow_temperature,
            api_key=settings.siliconflow_api_key,
            base_url=settings.siliconflow_base_url  # 硅基流动API端点
        )
        
        # 设置记忆
        self.memory = memory or AgentMemory()
        
        # 创建智能体
        if use_tools:
            self.agent = self._create_agent_with_tools()
        else:
            self.agent = self._create_simple_agent()
    
    def _create_agent_with_tools(self) -> AgentExecutor:
        """创建带工具的智能体"""
        # 获取工具
        tools = get_all_tools()
        
        # 创建提示词
        prompt = create_agent_prompt()
        
        # 创建智能体
        agent = create_openai_tools_agent(self.llm, tools, prompt)
        
        # 创建执行器
        agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            handle_parsing_errors=True,
        )
        
        return agent_executor
    
    def _create_simple_agent(self) -> Runnable:
        """创建简单对话智能体"""
        # 创建提示词
        prompt = create_simple_prompt()
        
        # 创建链
        chain = prompt | self.llm
        
        return chain
    
    def invoke(self, input_text: str) -> str:
        """
        调用智能体处理输入
        
        Args:
            input_text: 用户输入文本
            
        Returns:
            智能体的回复
        """
        try:
            if isinstance(self.agent, AgentExecutor):
                result = self.agent.invoke({"input": input_text})
                return result.get("output", "抱歉，我没有生成回复。")
            else:
                # 简单链式调用
                messages = self.memory.chat_history.messages
                if messages:
                    # 如果有历史记录，需要将其包含在输入中
                    result = self.agent.invoke({
                        "input": input_text,
                        "chat_history": messages
                    })
                else:
                    result = self.agent.invoke({"input": input_text})
                
                # 保存到记忆中
                self.memory.save_context({"input": input_text}, {"output": result.content})
                
                return result.content
        except Exception as e:
            return f"处理请求时出错: {str(e)}"
    
    def clear_memory(self) -> None:
        """清除记忆"""
        self.memory.clear()
    
    def get_chat_history(self) -> List[BaseMessage]:
        """获取聊天历史"""
        return self.memory.chat_history.messages