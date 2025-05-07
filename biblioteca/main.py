from fastapi import FastAPI, HTTPException, Form, Request
from models import Usuario,Livro,Biblioteca,Emprestimo
from typing import List

#uvicorn main:app RODA O APP   

app = FastAPI()

usuarios: List[Usuario] = []
livros: List[Livro] = []
bibliotecas: List[Biblioteca] = []
emprestimos: List[Emprestimo] = []

#############
###USUARIO###
#############

@app.get("/user/",response_model=List[Usuario])
def listar_usuarios():
    return usuarios

@app.post('/user/',response_model=Usuario)
def novo_usuario(usuario:Usuario):
    usuarios.append(usuario)
    return usuario

@app.delete("/user/{username}",response_model=Usuario)
def excluir_usuario(username:str):
    for index, usuario in enumerate(usuarios):
        if usuario.username == username:
            del usuarios[index]
            return usuario
    raise HTTPException(status_code=404,detail="Usuario não localizado")

### LIVROS

@app.get("/livro/",response_model=List[Livro])
def listar_livros():
    return Livro

@app.post('/livro/',response_model=Livro)
def novo_livro(livro:Livro):
    livros.append(livro)
    return livro

@app.delete("/livro/{titulo}",response_model=Livro)
def excluir_livro(titulo:str):
    for index, livro in enumerate(livros):
        if livro.titulo == titulo:
            del livros[index]
            return livro
    raise HTTPException(status_code=404,detail="Livro não localizado")

### BIBLIOTECA

@app.get("/biblioteca/",response_model=List[Biblioteca])
def listar_bibliotecas():
    return biblioteca

@app.post('/biblioteca/',response_model=Biblioteca)
def nova_biblioteca(biblioteca:Biblioteca):
    biblioteca.append(biblioteca)
    return biblioteca

@app.delete("/biblioteca/{nome}",response_model=Biblioteca)
def excluir_biblioteca(nome:str):
    for index, biblioteca in enumerate(biblioteca):
        if biblioteca.nome == nome:
            del biblioteca[index]
            return biblioteca
    raise HTTPException(status_code=404,detail="Biblioteca não localizada")

## EMPRESTIMO

@app.get("/emprestimo/",response_model=List[Emprestimo])
def listar_emprestimos():
    return emprestimos

@app.post('/emprestimo/',response_model=Emprestimo)
def novo_emprestimo(emprestimo:Emprestimo):
    emprestimos.append(emprestimo)
    return emprestimo

@app.delete("/emprestimo/{username}",response_model=Emprestimo)
def excluir_tarefa(username:str):
    for index, emprestimo in enumerate(emprestimos):
        if emprestimo.username == username:
            del emprestimos[index]
            return emprestimo
    raise HTTPException(status_code=404,detail="Emprestimo não localizado")