from pydantic import BaseModel
from datetime import datetime
from typing import List

class Usuario(BaseModel):
    username:str
    password:str
    data_criacao:datetime

class Livro(BaseModel):
    titulo:str
    ano:int
    edicao:int

class Biblioteca(BaseModel):
    nome:str
    acervo: List[Livro]
    usuarios: List[Usuario] #Tava escrito usuario, sem S, mudei pra fazer mais sentido

class Emprestimo(BaseModel):
    usuario:Usuario
    livro:Livro
    data_emprestimo:datetime
    data_devolucao:datetime