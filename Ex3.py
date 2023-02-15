import requests

# Definindo as URLs para consumir as cotações
urls = {
    'USD': 'https://economia.awesomeapi.com.br/json/last/USD-BRL',
    'EUR': 'https://economia.awesomeapi.com.br/json/last/EUR-BRL',
    'BTC': 'https://economia.awesomeapi.com.br/json/last/BTC-BRL'
}

# Função para converter o valor de Real para outras moedas
def converter_real(valor, destino):
    url = urls[destino]
    response = requests.get(url)
    data = response.json()
    cotacao = float(data[destino]['bid'])
    valor_convertido = valor / cotacao
    return valor_convertido

# Perguntando ao usuário qual a moeda de destino
moeda_destino = input("Digite a moeda de destino (USD, EUR, BTC): ")

# Perguntando ao usuário o valor em Real
valor_real = float(input("Digite o valor em Real: "))

# Convertendo o valor de Real para a moeda de destino
valor_convertido = converter_real(valor_real, moeda_destino)

# Imprimindo o valor convertido
print(f"O valor convertido para {moeda_destino} é: {valor_convertido:.2f}")