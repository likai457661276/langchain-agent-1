"""
测试模块 - 测试智能体功能
"""

import pytest
from unittest.mock import Mock, patch

from src.agent_1.agent import BasicAgent
from src.agent_1.tools import calculator, get_weather


class TestBasicAgent:
    """测试基础智能体"""
    
    @patch('src.agent_1.agent.settings.openai_api_key', 'test_api_key')
    def test_agent_initialization(self):
        """测试智能体初始化"""
        agent = BasicAgent(use_tools=False)
        assert agent.llm is not None
        assert agent.memory is not None
        assert agent.agent is not None
    
    @patch('src.agent_1.agent.settings.openai_api_key', 'test_api_key')
    def test_agent_memory(self):
        """测试智能体记忆功能"""
        agent = BasicAgent(use_tools=False)
        
        # 初始状态应该没有历史记录
        assert len(agent.get_chat_history()) == 0
        
        # 清除记忆应该仍然没有历史记录
        agent.clear_memory()
        assert len(agent.get_chat_history()) == 0


class TestTools:
    """测试工具功能"""
    
    def test_calculator(self):
        """测试计算器工具"""
        result = calculator("2 + 2")
        assert "计算结果: 4" in result
        
        result = calculator("10 * 5")
        assert "计算结果: 50" in result
        
        # 测试错误表达式
        result = calculator("invalid expression")
        assert "计算错误" in result
    
    def test_get_weather(self):
        """测试天气工具"""
        result = get_weather("北京")
        assert "北京的天气" in result
        
        result = get_weather("上海")
        assert "上海的天气" in result
        
        # 测试不存在的城市
        result = get_weather("不存在的城市")
        assert "暂时没有" in result


if __name__ == "__main__":
    pytest.main([__file__])