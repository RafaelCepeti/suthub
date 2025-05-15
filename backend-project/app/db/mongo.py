from pymongo import MongoClient
import os

MONGO_HOST = os.getenv("MONGO_HOST", "mongodb")  # Nome do serviço no docker-compose
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_DB = os.getenv("MONGO_DB", "inscription_db")

client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}")
db = client[MONGO_DB]

age_groups_collection = db["age_groups"]
enrollments_collection = db["enrollments"]
