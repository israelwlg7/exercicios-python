import requests

cep = input("Digite o CEP: ")
url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url)
dados = resposta.json()

print("\n📍 Endereço encontrado:")
print(f"Rua: {dados.get('logradouro')}")
print(f"Bairro: {dados.get('bairro')}")
print(f"Cidade: {dados.get('localidade')}")
print(f"Estado: {dados.get('uf')}")