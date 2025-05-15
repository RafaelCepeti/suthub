# SUTHUB - teste backend

| Requisito                                                | Status     | Detalhe                                                                 |
| -------------------------------------------------------- | ---------- | ----------------------------------------------------------------------- |
| **Docker para API, worker e MongoDB**                    | ✅ Completo | Compose com 3 serviços funcionando                                      |
| **API FastAPI com endpoints (age-groups + enrollments)** | ✅ Completo | GET, POST e DELETE funcionando                                          |
| **Worker (fila lógica com tempo mínimo de 2s)**          | ✅ Completo | Log mostra "\[Worker] Processando inscrições pendentes..."              |
| **MongoDB como DocumentDB local**                        | ✅ Completo | `mongodb:6.0` via Docker                                                |
| **Autenticação via Basic Auth**                          | ✅ Completo | `auth/basic_auth.py` com `Depends(security)` e `secrets.compare_digest` |
| **Testes automatizados com Pytest**                      | ✅ Completo | `test/test_api.py` cobre 3 endpoints com `TestClient` e autenticação    |
| **README com comandos de build/run**                     | ✅ Completo |                                                                         |


------------------------------------------------------------------------------------------------------------------------
# Visão Geral

API REST em FastAPI / Worker assíncrono / MongoDB como banco de dados

Autenticação básica

Stack Tecnológica: Python 3.11, FastAPI, Uvicorn, PyMongo, Docker.

------------------------------------------------------------------------------------------------------------------------
# Credenciais
# API: 
Login: admin
senha: admin123

MongoDB: Sem autenticação (apenas em localhost)

------------------------------------------------------------------------------------------------------------------------
# Pré-requisitos

# Verificar instalações necessárias
docker --version

docker-compose --version

python --version

------------------------------------------------------------------------------------------------------------------------

# 1-Configuração e Execução
python -m venv .venv

source .venv/bin/activate  # Linux/Mac

.\.venv\Scripts\activate   # Windows

pip install -r requirements.txt

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Em outro terminal:
python run_worker.py

# 2-Docker
docker-compose up --build

# 3-Acesso
API: http://localhost:8000/docs

MongoDB: mongodb://localhost:27017

------------------------------------------------------------------------------------------------------------------------
# Endpoints da API

# Grupos Etários
POST /age-groups - Cria novo grupo

GET /age-groups - Lista todos grupos

DELETE /age-groups/{id} - Remove grupo


# Inscrições

POST /enrollments - Cria nova inscrição

GET /enrollments/{cpf} - Busca inscrição

------------------------------------------------------------------------------------------------------------------------
# Processamento do Worker

Verifica inscrições pendentes a cada 2s

Aprova/rejeita com base na faixa etária

Atualiza status no banco de dados

------------------------------------------------------------------------------------------------------------------------
# Logs:
docker-compose exec api pytest tests/ -v

------------------------------------------------------------------------------------------------------------------------
# Testes

# 1-Automatizados

docker-compose exec api pytest tests/ -v

# 2-Manuais

2.1-Crie um grupo etário

2.2-Faça uma inscrição

2.3-Verifique processamento:

docker-compose exec mongodb mongosh inscription_db \
  --eval "db.enrollments.find()"

------------------------------------------------------------------------------------------------------------------------
# Comando final para iniciar

docker-compose up --build -d

------------------------------------------------------------------------------------------------------------------------
