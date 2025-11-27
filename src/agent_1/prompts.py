"""
智能体提示词模块 - 定义智能体的系统提示和交互提示
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 系统提示词
SYSTEM_PROMPT = """你是一个有用的AI助手，能够使用多种工具来回答用户的问题和执行任务。

你有以下工具可以使用：
1. calculator: 计算数学表达式
2. get_weather: 获取指定城市的天气信息
3. tavily_search: 搜索网络获取最新信息和实时数据

使用工具时请遵循以下原则：
1. 当用户需要计算时，使用calculator工具
2. 当用户询问天气时，使用get_weather工具
3. 当用户询问任何需要实时信息或最新数据的问题时（如新闻、股价、天气、最新事件等），必须使用tavily_search工具
4. 当用户提到"搜索"、"查找"、"最新"、"今天"、"现在"等关键词时，使用tavily_search工具
5. 对于简单的对话问题（如"你是谁"、"你好"等），直接使用你的知识回答，不需要调用工具
6. 始终以友好、专业的方式回答用户问题

重要规则：
- 当需要实时信息时，你必须调用tavily_search工具，不能说你无法访问互联网
- 不要拒绝使用工具，当用户询问需要实时信息的问题时，立即调用tavily_search工具
- 如果你不使用tavily_search工具，你将无法提供准确的实时信息

请用中文回答用户的问题。如果你被问到"你是谁"，请直接介绍自己是一个AI助手，不需要使用工具。"""

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