import time
from app.db.mongo import enrollments_collection, age_groups_collection
from bson import ObjectId

def find_matching_group(age: int):
    groups = age_groups_collection.find()
    for group in groups:
        if group["min_age"] <= age <= group["max_age"]:
            return str(group["_id"])
    return None

def process_enrollments():
    print("[Worker] Processando inscrições pendentes...")
    while True:
        enrollment = enrollments_collection.find_one({"status": "pending"})
        if enrollment:
            print(f"[Worker] Processando inscrição de: {enrollment['name']} (CPF: {enrollment['cpf']})")
            group_id = find_matching_group(enrollment["age"])
            status = "approved" if group_id else "rejected"

            enrollments_collection.update_one(
                {"_id": enrollment["_id"]},
                {"$set": {"status": status, "age_group_id": group_id}}
            )
            time.sleep(2)
        else:
            time.sleep(1)
