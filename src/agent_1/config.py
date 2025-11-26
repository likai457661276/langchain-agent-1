"""
配置模块 - 管理环境变量和应用配置
"""

import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings, Field

# 加载环境变量
load_dotenv()


class Settings(BaseSettings):
    """应用设置"""
    
    # OpenAI配置
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    openai_model: str = Field(default="gpt-3.5-turbo", env="OPENAI_MODEL")
    openai_temperature: float = Field(default=0.7, env="OPENAI_TEMPERATURE")
    
    # Tavily搜索配置
    tavily_api_key: Optional[str] = Field(default=None, env="TAVILY_API_KEY")
    
    # LangSmith配置
    langchain_tracing_v2: bool = Field(default=False, env="LANGCHAIN_TRACING_V2")
    langchain_api_key: Optional[str] = Field(default=None, env="LANGCHAIN_API_KEY")
    langchain_project: str = Field(default="agent_1", env="LANGCHAIN_PROJECT")
    
    # LangServe配置
    host: str = Field(default="localhost", env="HOST")
    port: int = Field(default=8000, env="PORT")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# 创建全局设置实例
settings = Settings()

# 设置LangChain环境变量
if settings.langchain_tracing_v2:
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = settings.langchain_project
    
    if settings.langchain_api_key:
        os.environ["LANGCHAIN_API_KEY"] = settings.langchain_api_key