from fastapi import FastAPI

from database import criar_tabela_alunos
from rotas import router

app = FastAPI(title="CRUD de alunos")

criar_tabela_alunos()

app.include_router(router)
