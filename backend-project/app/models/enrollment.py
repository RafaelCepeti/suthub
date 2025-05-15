from pydantic import BaseModel, Field, validator
from typing import Optional
from bson import ObjectId

class Enrollment(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    name: str
    cpf: str
    age: int
    status: Optional[str] = "pending"  # pending, approved, rejected
    age_group_id: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
