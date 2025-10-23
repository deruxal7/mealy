from pydantic import BaseModel as BaseModel_
from pydantic import Field
from typing import Any

class BaseModel(BaseModel_):
    def to_dict(self, *args: Any, **kwargs: Any):
        return super().model_dump(*args, **kwargs)
    
    class Config:
        from_attributes = True

class Version(BaseModel):
    version: str = Field("0.01", description="The version of API")