from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, HTTPException, Form, Request
from fastapi.responses import HTMLResponse
from models import Tarefa
from typing import List

#uvicorn main:app RODA O APP   

app = FastAPI()

templates = Jinja2Templates(directory="templates")

tarefas: List[Tarefa] = []
id = 0

#USAREMOS JQUERY E AJAX

@app.get("/tarefas/",response_model=List[Tarefa])
def listar_tarefas():
    return tarefas

@app.get('/cadastro_tarefa', response_class=HTMLResponse)    
def form_tarefa(request: Request):
    return templates.TemplateResponse("cadastrar_tarefa.html", {"request": request})

@app.post("/tarefas/",response_model=Tarefa)
def criar_tarefa(titulo: str = Form(...), descricao: str = Form(...)):
    
    global id
    nova_tarefa = Tarefa(id=id, titulo=titulo, descricao=descricao, concluido=False)
    tarefas.append(nova_tarefa)
    id += 1
    return nova_tarefa

@app.delete("/tarefas/{tarefa_id}",response_model=Tarefa)
def excluir_tarefa(tarefa_id:int):
    for index, tarefa in enumerate(tarefas):
        if tarefa.id == tarefa_id:
            del tarefas[index]
            return tarefa
    raise HTTPException(status_code=404,detail="Tarefa não localizada")