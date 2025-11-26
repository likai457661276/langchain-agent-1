"""
主程序入口 - 运行智能体应用
"""

import os
import sys
from typing import Optional

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agent_1.agent import BasicAgent


def main():
    """主函数 - 运行交互式智能体"""
    print("=" * 50)
    print("欢迎使用基础LangChain智能体!")
    print("=" * 50)
    print("输入 'quit' 或 'exit' 退出程序")
    print("输入 'clear' 清除对话历史")
    print("=" * 50)
    
    # 创建智能体实例
    agent = BasicAgent()
    
    # 主循环
    while True:
        try:
            # 获取用户输入
            user_input = input("\n您: ").strip()
            
            # 检查退出命令
            if user_input.lower() in ["quit", "exit", "退出"]:
                print("再见!")
                break
            
            # 检查清除命令
            if user_input.lower() in ["clear", "清除"]:
                agent.clear_memory()
                print("对话历史已清除。")
                continue
            
            # 处理空输入
            if not user_input:
                continue
            
            # 调用智能体
            print("\n智能体: ", end="", flush=True)
            response = agent.invoke(user_input)
            print(response)
            
        except KeyboardInterrupt:
            print("\n\n程序被用户中断。再见!")
            break
        except Exception as e:
            print(f"\n发生错误: {str(e)}")


if __name__ == "__main__":
    main()