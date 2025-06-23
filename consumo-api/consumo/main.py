
import requests, json

if __name__ == "__main__":
    url = "http://127.0.0.1:8000"
    req = requests.get(f"{url}/livros")
    print(req.text) 
    livro = {
        "titulo": "sei la doido",
        "ano": 2025,
        "edicao": 1
    }
    req = requests.post(f"{url}/livros", json = livro)
    print(req.status_code)
    print(req.text)

    pesquisa = "livro" 
    req = requests.get(f"{url}/livros/{pesquisa}")
    print(req.status_code)
    print(req.text)

    r = requests.delete(f"{url}/livros/{pesquisa}")
    print(r.status_code)