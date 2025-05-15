from fastapi import FastAPI
from app.api import age_groups, enrollment  # <- importante

app = FastAPI()

app.include_router(age_groups.router)
app.include_router(enrollment.router)  # <- essa linha conecta a API de inscrição
