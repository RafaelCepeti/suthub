from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class AgeGroup(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    name: str
    min_age: int
    max_age: int

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
