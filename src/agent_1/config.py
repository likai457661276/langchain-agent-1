"""
配置模块 - 管理环境变量和应用配置
"""

import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

# 加载环境变量
load_dotenv()


class Settings(BaseSettings):
    """应用设置"""
    
    # Silicon Flow (硅基流动) 配置 - 兼容OpenAI API格式
    siliconflow_api_key: str = Field(..., env="SILICONFLOW_API_KEY")
    siliconflow_model: str = Field(default="THUDM/GLM-Z1-9B-0414", env="SILICONFLOW_MODEL")
    siliconflow_temperature: float = Field(default=0.7, env="SILICONFLOW_TEMPERATURE")
    siliconflow_base_url: str = Field(default="https://api.siliconflow.cn/v1", env="SILICONFLOW_BASE_URL")
    
    # Tavily搜索配置
    tavily_api_key: Optional[str] = Field(default=None, env="TAVILY_API_KEY")
    
    # LangSmith配置
    langsmith_api_key: Optional[str] = Field(default=None, env="LANGSMITH_API_KEY")
    langsmith_project: str = Field(default="langchain-agent-1", env="LANGSMITH_PROJECT")
    langsmith_tracing: bool = Field(default=True, env="LANGSMITH_TRACING")
    
    # LangServe配置
    host: str = Field(default="0.0.0.0", env="HOST")  # 监听所有网络接口，支持Docker访问
    port: int = Field(default=8000, env="PORT")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# 创建全局设置实例
settings = Settings()

# 已移除LangSmith相关环境变量设置