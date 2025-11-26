# Agent_1 - 基础LangChain智能体项目

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1.0+-green.svg)](https://langchain.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

这是一个基于LangChain框架构建的基础智能体项目，展示了如何创建、测试和部署AI代理。该项目集成了多种工具、记忆功能和推理链，支持本地测试和生产环境部署。

## ✨ 功能特性

- 🤖 **智能代理**: 基于LangChain的智能代理实现
- 🛠️ **多种工具**: 集成计算器、天气查询、网络搜索等工具
- 🧠 **记忆功能**: 支持对话历史记忆和上下文保持
- 📦 **依赖管理**: 使用UV进行现代化的依赖管理
- 🧪 **本地测试**: 支持LangGraph CLI本地测试和可视化调试
- 🚀 **服务部署**: 支持LangServe服务部署和RESTful API
- 📝 **中文支持**: 完整的中文提示词和交互界面

## 🚀 快速开始

### 环境准备

1. 确保已安装Python 3.10或更高版本
2. 安装UV包管理器：
   ```bash
   pip install uv
   ```

### 安装项目

```bash
# 克隆项目
git clone <repository-url>
cd agent_1

# 同步依赖
uv sync
```

### 配置环境变量

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑.env文件，添加你的API密钥
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key  # 可选，用于搜索功能
```

### 运行智能体

```bash
# 命令行交互模式
uv run python src/agent_1/main.py

# 启动API服务
uv run python src/agent_1/server.py

# LangGraph CLI测试
uv run langgraph dev
```

## 📁 项目结构

```
agent_1/
├── src/agent_1/              # 主要源代码
│   ├── __init__.py          # 包初始化文件
│   ├── agent.py             # 智能体核心实现
│   ├── config.py            # 配置管理
│   ├── tools.py             # 工具定义
│   ├── prompts.py           # 提示词模板
│   ├── graph.py             # LangGraph图定义
│   ├── server.py            # LangServe服务器配置
│   ├── client.py            # API客户端示例
│   └── main.py              # 主程序入口
├── tests/                   # 测试文件
│   └── test_agent.py        # 智能体测试
├── docs/                    # 项目文档
│   └── development.md       # 详细开发指南
├── pyproject.toml           # 项目配置和依赖
├── langgraph.json           # LangGraph配置
├── .env.example             # 环境变量模板
└── README.md                # 项目说明
```

## 🛠️ 开发指南

### 代码格式化

```bash
# 格式化代码
uv run black src/ tests/

# 检查代码风格
uv run ruff check src/ tests/

# 类型检查
uv run mypy src/
```

### 运行测试

```bash
# 运行所有测试
uv run pytest

# 运行测试并生成覆盖率报告
uv run pytest --cov=src/agent_1
```

### API文档

启动服务后，访问以下地址查看API文档：

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🌐 API使用示例

### 简单聊天

```python
import requests

response = requests.post("http://localhost:8000/chat", json={
    "message": "你好，请介绍一下你自己",
    "session_id": "user123"
})

print(response.json()["response"])
```

### 使用智能体工具

```python
import requests

response = requests.post("http://localhost:8000/agent/invoke", json={
    "input": {
        "message": "帮我计算 25 * 4",
        "session_id": "user123"
    }
})

print(response.json()["output"])
```

## 🧪 LangGraph可视化测试

1. 启动LangGraph开发服务器：
   ```bash
   uv run langgraph dev
   ```

2. 在浏览器中打开显示的URL

3. 输入消息并查看智能体的执行流程和决策过程

## 📚 详细文档

查看[开发指南](docs/development.md)获取更多详细信息，包括：

- 核心功能详解
- 高级配置选项
- 自定义工具开发
- 部署最佳实践
- 常见问题解答

## 🤝 贡献指南

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

- [LangChain](https://github.com/langchain-ai/langchain) - 强大的LLM应用开发框架
- [LangGraph](https://github.com/langchain-ai/langgraph) - 构建有状态、多参与者应用程序的库
- [LangServe](https://github.com/langchain-ai/langserve) - 部署LangChain可运行对象的服务器
- [UV](https://github.com/astral-sh/uv) - 极速的Python包管理器