import requests
from bs4 import BeautifulSoup

url = 'https://statusinvest.com.br/fundos-imobiliarios/mxrf11'
response = requests.get(url)

# verificação de solicitação
if response.status_code == 200:
    html = response.text

else:
    print('falha ao obter a página. Status code:', response.status_code)