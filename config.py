''' implement an LRU cache strategy
Caching is an optimization technique that you can use in your 
applications to keep recent or often-used data in memory'''
from functools import lru_cache

from pydantic import BaseSettings
''' pydantic is a library that uses type annotation to validate data and manage settings. '''

class Settings(BaseSettings):
    env_name: str = "local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"
    
    class Config():
        env_file = '.env'
   
@lru_cache(maxsize=None)  
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings

