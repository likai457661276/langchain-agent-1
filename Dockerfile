FROM python:3.10-slim

WORKDIR /app

# 安装uv
RUN pip install --upgrade pip && pip install uv

# 复制项目文件
COPY . .

# 安装依赖
RUN uv sync

# 设置环境变量
ENV PYTHONPATH=/app

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["uv", "run", "python", "-m", "src.agent_1.server"]
