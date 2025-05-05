from fastapi import FastAPI, HTTPException, Form
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "Hello World"}
from models import Tarefa
from typing import List
 
#uvicorn main:app RODA O APP
#/docs para debug

app = FastAPI()
 
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
tarefas: List[Tarefa] = []
id = 0
 
#USAREMOS JQUERY E AJAX

@app.get("/tarefas/",response_model=List[Tarefa])
def listar_tarefas():
    return tarefas
 
@app.post("/tarefas/",response_model=Tarefa)
def criar_tarefa(tarefa:Tarefa):
    #global id
    # tarefas.append(tarefa)
    #id += 1
    #nova_tarefa = Tarefa(id=id, titulo=titulo, descricao=descricao, concluido=False)
    #tarefas.append(nova_tarefa)
    tarefas.append(tarefa)
    return tarefa
 
@app.delete("/tarefas/{tarefa_id}",response_model=Tarefa)
def excluir_tarefa(tarefa_id:int):
    for index, tarefa in enumerate(tarefas):
        if tarefa.id == tarefa_id:
            del tarefas[index]
            return tarefa