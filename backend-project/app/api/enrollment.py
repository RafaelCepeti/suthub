from fastapi import APIRouter, Depends, HTTPException
from app.auth.basic_auth import authenticate
from app.models.enrollment import Enrollment
from app.db.mongo import enrollments_collection
from bson import ObjectId

router = APIRouter()

@router.get("/enrollments/{cpf}", response_model=Enrollment)
def get_enrollment(cpf: str, user=Depends(authenticate)):
    enrollment = enrollments_collection.find_one({"cpf": cpf})
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    enrollment["_id"] = str(enrollment["_id"])
    return enrollment

@router.post("/enrollments", response_model=Enrollment)
def create_enrollment(data: Enrollment, user=Depends(authenticate)):
    result = enrollments_collection.insert_one(data.dict(by_alias=True, exclude={"id"}))
    data.id = str(result.inserted_id)
    return data