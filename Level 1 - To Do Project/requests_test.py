import requests

url = str("https://www.example.com")

response = requests.get(url).status_code

print(f'O site {url} retornou o seguinte status_code: {response}')
