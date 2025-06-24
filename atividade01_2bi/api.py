import requests
url = "http://127.0.0.1:8000"

def listar():
    req = requests.get(f"{url}/livros")
    return req.text

def pesquisar():
    livro = input('Informe o titulo do livro: ')
    req = requests.get(f"{url}/livros/{livro}")
    print(type(req.text))
    if req.text == '{"detail":"Não localizado"}':
        return "Livro não encontrado"
    return req.text

def cadastrar():
    titulo = (input('Insira o título do livro: '))
    ano = (input('Insira o ano do livro: '))
    while not ano.isnumeric():
        print('insira um NÚMERO')
        ano = (input('Insira o ano do livro: '))
    
    edicao = input('Insira a edição: ')
    while not edicao.isnumeric():
        print('insira um NÚMERO')
        edicao = (input('Insira o ano do edição: '))

    livro = {"titulo": titulo,
             "ano": ano,
             "edicao":edicao}

    req = requests.post(f"{url}/livros", json=livro)
    return req

def deletar():
    titulo = (input("Título do livro a ser deletado: "))
    req = requests.delete(f"{url}/livros/{titulo}")
    return req

if __name__ == "__main__":
    while True:
        print('Q q tu quer?')
        print('1 - Listar todos os livros')
        print('2 - Pesquisar livro')
        print('3 - Cadastrar livro')
        print('4 - Deletar livro')
        print('5 - Finalizar')
        
        escolha = input('Ação: ')
        if escolha not in ["1","2","3","4","5"]:
            print('-----------------------------')
            print('Escolha uma opção válida')
            print('-----------------------------')
        else:
            if escolha == "1":
                resp = listar()
            elif escolha == "2":
                resp = pesquisar()
            elif escolha == "3":
                resp = cadastrar()
            elif escolha == "4":
                resp = deletar()
            else:
                break
            print(resp)


            
