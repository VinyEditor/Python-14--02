import requests

login = input("Digite o Login: ")

url = f"(https://api.github.com/users/{login})"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    login = data['login']
    repositorios = data['repositorios']
    seguidores = data['seguidores']
    print(f"Login: {login}")
    print(f"Qtd de repositórios: {repositorios}")
    print(f"Qtd de seguidores: {seguidores}")
else:
    print("Login não encontrado.")