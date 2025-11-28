# Agent_1 - 基础 LangChain 智能体项目

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1.0+-green.svg)](https://langchain.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

这是一个基于 LangChain 框架构建的基础智能体项目，展示了如何创建、测试和部署 AI 代理。该项目集成了多种工具、记忆功能和推理链，支持本地测试和生产环境部署。

## ✨ 功能特性

- 🤖 **智能代理**: 基于 LangChain 的智能代理实现
- 🛠️ **多种工具**: 集成计算器、天气查询、网络搜索等工具
- 🧠 **记忆功能**: 支持对话历史记忆和上下文保持
- 📦 **依赖管理**: 使用 UV 进行现代化的依赖管理
- 🧪 **本地测试**: 支持 LangGraph CLI 本地测试和可视化调试
- 🚀 **服务部署**: 支持 LangServe 服务部署和 RESTful API
- 📝 **中文支持**: 完整的中文提示词和交互界面

## 🚀 快速开始

### 环境准备

1. 确保已安装 Python 3.10 或更高版本
2. 安装 UV 包管理器：
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
uv run python -m src.agent_1.server

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

### API 端点

启动服务后，可以使用以下 API 端点：

- 聊天接口: `http://localhost:8000/chat`
- 智能体接口: `http://localhost:8000/agent`
- 图接口: `http://localhost:8000/graph`

注意：API 文档自动生成功能已禁用

## 🌐 API 使用示例

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

## 🧪 LangGraph 可视化测试

1. 启动 LangGraph 开发服务器：

   ```bash
   uv run langgraph dev
   ```

2. 在浏览器中打开显示的 URL

3. 输入消息并查看智能体的执行流程和决策过程

## � Docker 部署

### 环境准备

1. 确保已安装 Docker 和 Docker Compose
2. 克隆项目并进入目录：
   ```bash
   git clone <repository-url>
   cd agent_1
   ```

### 配置环境变量

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑.env文件，添加你的API密钥
SILICONFLOW_API_KEY=your_siliconflow_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here
```

### 使用 Docker 构建和运行

```bash
# 构建Docker镜像
docker build -t agent-1 .

# 运行Docker容器
docker run -p 8000:8000 --env-file .env agent-1
```

### 使用 Docker Compose

```bash
# 构建并启动服务
docker-compose up --build

# 后台运行服务
docker-compose up -d

# 停止服务
docker-compose down

# 查看服务日志
docker-compose logs -f
```

### Docker 开发模式

```bash
# 启动开发模式（支持热重载）
docker-compose up

# 修改代码后，服务会自动重载
```

### Docker 环境变量

所有环境变量都可以在 `.env` 文件中配置，Docker 容器会自动加载这些变量。主要环境变量包括：

- `SILICONFLOW_API_KEY`: Silicon Flow API 密钥
- `SILICONFLOW_MODEL`: 使用的模型名称
- `SILICONFLOW_TEMPERATURE`: 模型温度参数
- `TAVILY_API_KEY`: Tavily 搜索 API 密钥
- `LANGSMITH_API_KEY`: LangSmith API 密钥
- `LANGSMITH_TRACING`: 是否启用 LangSmith 追踪

### Docker 服务访问

服务启动后，可以通过以下地址访问：

- API 根地址：http://localhost:8000
- 聊天端点：http://localhost:8000/chat
- 智能体端点：http://localhost:8000/agent/invoke
- 图端点：http://localhost:8000/graph/invoke

## �📚 详细文档

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

- [LangChain](https://github.com/langchain-ai/langchain) - 强大的 LLM 应用开发框架
- [LangGraph](https://github.com/langchain-ai/langgraph) - 构建有状态、多参与者应用程序的库
- [LangServe](https://github.com/langchain-ai/langserve) - 部署 LangChain 可运行对象的服务器
- [UV](https://github.com/astral-sh/uv) - 极速的 Python 包管理器
