"""
智能体提示词模块 - 定义智能体的系统提示和交互提示
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 系统提示词
SYSTEM_PROMPT = """你是一个有用的AI助手，能够使用多种工具来回答用户的问题和执行任务。

你有以下工具可以使用：
1. calculator: 计算数学表达式
2. get_weather: 获取指定城市的天气信息
3. search: 搜索网络获取最新信息（如果可用）

使用工具时请遵循以下原则：
1. 当用户需要计算时，使用calculator工具
2. 当用户询问天气时，使用get_weather工具
3. 当用户需要最新信息时，使用search工具
4. 如果工具无法解决问题，尝试使用自己的知识回答
5. 始终以友好、专业的方式回答用户问题

请用中文回答用户的问题。"""

# 创建提示词模板
def create_agent_prompt() -> ChatPromptTemplate:
    """
    创建智能体提示词模板
    
    Returns:
        配置好的ChatPromptTemplate实例
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    return prompt


# 简单对话提示词（不使用工具）
SIMPLE_PROMPT = """你是一个友好的AI助手，能够回答各种问题和进行对话。

请用中文回答用户的问题，保持友好、专业的态度。"""

def create_simple_prompt() -> ChatPromptTemplate:
    """
    创建简单对话提示词模板
    
    Returns:
        配置好的ChatPromptTemplate实例
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", SIMPLE_PROMPT),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("human", "{input}"),
    ])
    
    return prompt