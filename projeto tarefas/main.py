from fastapi import FastAPI, HTTPException
from models import Tarefa
from typing import List

app = FastAPI()

tarefas: List[Tarefa] = []

@app.get("/tarefas/",response_model=List[Tarefa])
def listar_tarefas():
    return tarefas

@app.post("/tarefas/",response_model=Tarefa)
def criar_tarefa(tarefa:Tarefa):
    
    tarefas.append(tarefa)
    return tarefa