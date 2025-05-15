from fastapi import FastAPI
from app.api import age_groups, enrollment

app = FastAPI()

app.include_router(age_groups.router)
app.include_router(enrollment.router)
