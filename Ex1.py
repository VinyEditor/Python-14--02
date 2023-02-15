import requests

cep = input("Digite o CEP desejado (somente números): ")

url = f"https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    logradouro = data['logradouro']
    bairro = data['bairro']
    cidade = data['localidade']
    print(f"Logradouro: {logradouro}")
    print(f"Bairro: {bairro}")
    print(f"Cidade: {cidade}")
else:
    print("Não foi possível obter as informações desse CEP.")