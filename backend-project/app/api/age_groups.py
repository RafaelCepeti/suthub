from fastapi import APIRouter, Depends, HTTPException
from app.auth.basic_auth import authenticate
from app.models.age_group import AgeGroup
from app.db.mongo import age_groups_collection
from bson import ObjectId

router = APIRouter()

@router.get("/age-groups", response_model=list[AgeGroup])
def list_age_groups(user=Depends(authenticate)):
    age_groups = list(age_groups_collection.find())
    for group in age_groups:
        group["_id"] = str(group["_id"])
    return age_groups

@router.post("/age-groups", response_model=AgeGroup)
def create_age_group(group: AgeGroup, user=Depends(authenticate)):
    result = age_groups_collection.insert_one(group.dict(by_alias=True, exclude={"id"}))
    group.id = str(result.inserted_id)
    return group

@router.delete("/age-groups/{group_id}")
def delete_age_group(group_id: str, user=Depends(authenticate)):
    result = age_groups_collection.delete_one({"_id": ObjectId(group_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Group not found")
    return {"detail": "Group deleted"}
