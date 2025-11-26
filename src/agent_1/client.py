"""
API客户端示例 - 展示如何使用智能体API
"""

import requests
import json
from typing import Dict, Any


class AgentClient:
    """智能体API客户端"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        """
        初始化客户端
        
        Args:
            base_url: API服务器地址
        """
        self.base_url = base_url.rstrip("/")
        self.session_id = "default_session"
    
    def chat(self, message: str, session_id: str = None) -> str:
        """
        发送聊天消息
        
        Args:
            message: 用户消息
            session_id: 会话ID，可选
            
        Returns:
            智能体回复
        """
        url = f"{self.base_url}/chat"
        
        payload = {
            "message": message,
            "session_id": session_id or self.session_id
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            
            data = response.json()
            return data.get("response", "抱歉，没有收到回复。")
        except requests.exceptions.RequestException as e:
            return f"请求错误: {str(e)}"
        except json.JSONDecodeError:
            return "解析响应时出错"
    
    def invoke_agent(self, message: str) -> Dict[str, Any]:
        """
        调用智能体端点
        
        Args:
            message: 用户消息
            
        Returns:
            完整的响应数据
        """
        url = f"{self.base_url}/agent/invoke"
        
        payload = {
            "input": {
                "message": message,
                "session_id": self.session_id
            }
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"请求错误: {str(e)}"}
        except json.JSONDecodeError:
            return {"error": "解析响应时出错"}
    
    def get_api_info(self) -> Dict[str, Any]:
        """
        获取API信息
        
        Returns:
            API信息字典
        """
        url = f"{self.base_url}/"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"请求错误: {str(e)}"}
        except json.JSONDecodeError:
            return {"error": "解析响应时出错"}


def main():
    """主函数 - 演示客户端使用"""
    print("智能体API客户端示例")
    print("=" * 50)
    
    # 创建客户端
    client = AgentClient()
    
    # 获取API信息
    print("获取API信息...")
    api_info = client.get_api_info()
    print(f"API信息: {json.dumps(api_info, indent=2, ensure_ascii=False)}")
    
    # 简单聊天示例
    print("\n简单聊天示例:")
    questions = [
        "你好，请介绍一下你自己",
        "帮我计算 25 * 4",
        "北京的天气怎么样？"
    ]
    
    for question in questions:
        print(f"\n用户: {question}")
        response = client.chat(question)
        print(f"智能体: {response}")
    
    # 使用智能体端点示例
    print("\n使用智能体端点示例:")
    response = client.invoke_agent("请用一句话总结人工智能")
    print(f"响应: {json.dumps(response, indent=2, ensure_ascii=False)}")


if __name__ == "__main__":
    main()