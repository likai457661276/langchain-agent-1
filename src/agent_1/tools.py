"""
智能体工具模块 - 定义智能体可以使用的工具
"""

from typing import Any, Dict, List, Optional

try:
    # 尝试使用新的langchain-tavily包
    from langchain_tavily import TavilySearch
    USE_NEW_TAVILY = True
except ImportError:
    # 回退到旧的实现
    from langchain_community.tools.tavily_search import TavilySearchResults
    USE_NEW_TAVILY = False

from langchain_core.tools import BaseTool, tool


@tool
def calculator(expression: str) -> str:
    """
    计算数学表达式
    
    Args:
        expression: 要计算的数学表达式，例如 "2 + 2" 或 "10 * 5"
        
    Returns:
        计算结果的字符串表示
    """
    try:
        # 使用eval进行简单计算，注意在生产环境中应该使用更安全的方法
        result = eval(expression)
        return f"计算结果: {result}"
    except Exception as e:
        return f"计算错误: {str(e)}"


@tool
def get_weather(city: str) -> str:
    """
    获取指定城市的天气信息
    
    Args:
        city: 城市名称
        
    Returns:
        天气信息的字符串表示
    """
    # 这里只是一个模拟实现，实际应用中应该调用真实的天气API
    weather_data = {
        "北京": "晴天，温度25°C",
        "上海": "多云，温度22°C",
        "广州": "雨天，温度28°C",
        "深圳": "晴天，温度26°C",
    }
    
    if city in weather_data:
        return f"{city}的天气: {weather_data[city]}"
    else:
        return f"抱歉，暂时没有{city}的天气信息"


def get_search_tool() -> Optional[BaseTool]:
    """
    获取搜索工具
    
    Returns:
        如果配置了Tavily API密钥，返回Tavily搜索工具，否则返回None
    """
    from .config import settings
    
    if settings.tavily_api_key:
        if USE_NEW_TAVILY:
            # 使用新的TavilySearch类
            return TavilySearch(
                api_key=settings.tavily_api_key,
                max_results=5
            )
        else:
            # 回退到旧的TavilySearchResults
            return TavilySearchResults(
                max_results=5,
                api_key=settings.tavily_api_key,
                description="搜索网络获取最新信息"
            )
    return None


def get_all_tools() -> List[BaseTool]:
    """
    获取所有可用工具
    
    Returns:
        工具列表
    """
    tools = [calculator, get_weather]
    
    search_tool = get_search_tool()
    if search_tool:
        tools.append(search_tool)
    
    return tools