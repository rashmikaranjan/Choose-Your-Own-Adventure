# How to load env variables into the project - Standard practice
# take all the env variables and map them into a python object that we can then use and reference in our code

from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

# pydantic is a library that allows us to do some advannced kind of type handling and validation
# pydantic settings - allows us to load env variables(which is not a python object) into a python object

class Settings(BaseSettings):   # inherit from BaseSettings from pydantic
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    
    DATABASE_URL: str   # no default value - must be provided in the env file
    
    ALLOWED_ORIGINS: str = ""
    
    OPENAI_API_KEY: str
    
    # whatever is specified here must map with the env variables in the .env file
    # if not, the program won't load correctly because the config will state that variable hasn't been specified in the configuration
    
    @field_validator("ALLOWED_ORIGINS")     # validate and transform the env variable into a list of strings
    def parse_allowed_origins(cls, v:str) -> List[str]: 
        return v.split(",") if v else []
    
    class Config:       # internal class to specify some config settings
        env_file = ".env"   # specify the env file to load the variables from
        env_file_encoding = "utf-8"
        case_sensitive = True
        
settings = Settings()   # create an instance of the Settings class to be used in the project
# this will load the env variables from the .env file and map them to the Settings class attributes
# we can then import this settings object and use it in our code
