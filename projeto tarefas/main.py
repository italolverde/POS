from fastapi import FastAPI, HTTPException, Form
from models import Tarefa
from typing import List

#uvicorn main:app RODA O APP

app = FastAPI()

tarefas: List[Tarefa] = []
id = 0

#USAREMOS JQUERY E AJAX

@app.get("/tarefas/",response_model=List[Tarefa])
def listar_tarefas():
    return tarefas

@app.post("/tarefas/",response_model=Tarefa)
def criar_tarefa(titulo: str = Form(...), descricao: str = Form(...)):
    
    id_tarefa = id
    id += 1
    nova_tarefa = Tarefa(id=id_novo, titulo=titulo, descricao=descricao, concluido=False)
    tarefas.append(nova_tarefa)
    return tarefa

@app.delete("/tarefas/{tarefa_id}",response_model=Tarefa)
def excluir_tarefa(tarefa_id:int):
    for index, tarefa in enumerate(tarefas):
        if tarefa.id == tarefa_id:
            del tarefas[index]
            return tarefa
    raise HTTPException(status_code=404,detail="Tarefa não localizada")