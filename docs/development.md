# Agent_1 开发指南

本文档提供了 Agent_1 项目的详细开发指南，包括项目结构、功能特性、开发流程和部署说明。

## 目录

1. [项目概述](#项目概述)
2. [项目结构](#项目结构)
3. [核心功能](#核心功能)
4. [开发环境设置](#开发环境设置)
5. [使用指南](#使用指南)
6. [API 文档](#api文档)
7. [测试指南](#测试指南)
8. [部署指南](#部署指南)
9. [常见问题](#常见问题)

## 项目概述

Agent_1 是一个基于 LangChain 框架构建的基础智能体项目，展示了如何创建、测试和部署 AI 代理。该项目集成了多种工具、记忆功能和推理链，支持本地测试和生产环境部署。

### 主要特性

- 基于 LangChain 的智能代理实现
- 集成多种工具（计算器、天气查询、网络搜索）
- 支持对话历史记忆
- 使用 UV 进行依赖管理
- 支持 LangGraph CLI 本地测试
- 支持 LangServe 服务部署
- 提供 RESTful API 接口

## 项目结构

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
│   └── development.md       # 开发指南
├── config/                  # 配置文件目录
├── pyproject.toml           # 项目配置和依赖
├── langgraph.json           # LangGraph配置
├── .env.example             # 环境变量模板
├── .gitignore               # Git忽略文件
└── README.md                # 项目说明
```

## 核心功能

### 1. 智能体核心 (agent.py)

`BasicAgent`类是项目的核心，提供以下功能：

- 初始化 Silicon Flow (硅基流动) 模型 - 兼容 OpenAI API 格式
- 集成多种工具
- 管理对话历史
- 处理用户输入

### 2. 工具系统 (tools.py)

项目包含以下工具：

- `calculator`: 数学计算工具
- `get_weather`: 天气查询工具
- `TavilySearchResults`: 网络搜索工具（需要 Tavily API 密钥）

### 3. 提示词系统 (prompts.py)

定义了智能体的行为和交互方式：

- 系统提示词：定义智能体角色和能力
- 工具使用指导：指导智能体何时使用何种工具
- 对话格式：定义交互格式

### 4. 记忆系统

实现了基于`ChatMessageHistory`的记忆系统，支持：

- 对话历史存储
- 上下文保持
- 历史清除

## 开发环境设置

### 前置要求

- Python 3.10 或更高版本
- UV 包管理器
- Silicon Flow (硅基流动) API 密钥
- （可选）Tavily API 密钥（用于网络搜索）

### 安装步骤

1. 克隆项目

   ```bash
   git clone <repository-url>
   cd agent_1
   ```

2. 安装 UV（如果尚未安装）

   ```bash
   pip install uv
   ```

3. 同步依赖

   ```bash
   uv sync
   ```

4. 配置环境变量
   ```bash
   cp .env.example .env
   # 编辑.env文件，添加你的API密钥
   ```

## 使用指南

### 1. 命令行交互

运行主程序进行命令行交互：

```bash
uv run python src/agent_1/main.py
```

### 2. LangGraph CLI 测试

使用 LangGraph 进行本地测试：

```bash
uv run langgraph dev
```

然后在浏览器中打开显示的 URL 进行可视化测试。

### 3. API 服务

启动 LangServe API 服务：

```bash
uv run python src/agent_1/server.py
```

服务将在`http://localhost:8000`启动，你可以：

- 使用`http://localhost:8000/chat`端点进行聊天
- 使用`http://localhost:8000/agent`端点访问完整智能体功能
- 使用`http://localhost:8000/graph`端点访问 LangGraph 功能

注意：API 文档自动生成功能已禁用，如需查看 API 文档，请参考源代码或文档说明

### 4. 客户端示例

运行客户端示例：

```bash
uv run python src/agent_1/client.py
```

## API 文档

### 端点列表

1. `GET /` - API 信息
2. `POST /chat` - 简单聊天端点
3. `POST /agent/invoke` - 完整智能体端点
4. `POST /agent/stream` - 流式响应端点
5. `POST /agent/batch` - 批量处理端点
6. `POST /graph/invoke` - LangGraph 端点

### 请求/响应格式

#### /chat 端点

**请求:**

```json
{
  "message": "你好",
  "session_id": "optional_session_id"
}
```

**响应:**

```json
{
  "response": "你好！我是AI助手，有什么可以帮助您的吗？",
  "session_id": "optional_session_id"
}
```

## 测试指南

### 运行测试

```bash
uv run pytest
```

### 测试覆盖率

```bash
uv run pytest --cov=src/agent_1
```

### 添加新测试

1. 在`tests/`目录下创建新的测试文件
2. 使用 pytest 框架编写测试
3. 确保测试覆盖关键功能

## 部署指南

### 本地部署

1. 使用 LangServe：

   ```bash
   uv run python src/agent_1/server.py
   ```

2. 使用 LangGraph CLI：
   ```bash
   uv run langgraph serve
   ```

### 生产部署

1. 使用 Docker（需要创建 Dockerfile）
2. 使用云服务（如 AWS、GCP、Azure）
3. 使用容器编排（如 Kubernetes）

### 环境变量配置

生产环境中需要配置以下环境变量：

- `SILICONFLOW_API_KEY`: Silicon Flow (硅基流动) API 密钥
- `SILICONFLOW_MODEL`: 模型名称 (默认: THUDM/GLM-Z1-9B-0414)
- `SILICONFLOW_TEMPERATURE`: 温度参数 (默认: 0.7)
- `SILICONFLOW_BASE_URL`: API 基础 URL (默认: https://api.siliconflow.cn/v1)
- `TAVILY_API_KEY`: Tavily API 密钥（可选）

## 常见问题

### 1. 如何添加新工具？

1. 在`tools.py`中定义新工具函数
2. 使用`@tool`装饰器标记函数
3. 在`get_all_tools()`函数中添加新工具

示例：

```python
@tool
def my_new_tool(input: str) -> str:
    """新工具的描述"""
    # 实现工具逻辑
    return "结果"
```

### 2. 如何修改智能体行为？

1. 修改`prompts.py`中的系统提示词
2. 调整`config.py`中的模型参数
3. 修改`agent.py`中的智能体逻辑

### 3. 如何处理长对话？

1. 调整记忆系统的存储策略
2. 实现对话摘要功能
3. 使用向量数据库存储长期记忆

### 4. 如何提高性能？

1. 使用流式响应
2. 实现缓存机制
3. 优化工具调用
4. 使用更快的模型

## 贡献指南

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 创建 Pull Request

## 许可证

MIT License
