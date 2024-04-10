import requests
from bs4 import BeautifulSoup

# URL de pesquisa e texto pesquisado
search_url = 'https://www.pensador.com/busca.php'
search_text = input('\nPesquisar: ')
print('\nBuscando resultados...\n')

# Parâmetros da pesquisa
params = {'q': search_text}

# Enviar solicitação GET para o site Pensador
response = requests.get(search_url, params=params)

# Verificar se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Analisar o conteúdo HTML da resposta
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar todos os elementos <p> com a classe 'frase fr'
    frases = soup.find_all('p', class_='frase fr')
    
    # Extrair e imprimir as frases encontradas
    for frase in frases:
        print(frase.text)
        print('-' * 50)  # Linha de separação entre as frases
        print()  # Adiciona uma linha em branco após cada frase
else:
    print('Falha ao acessar a página de resultados:', response.status_code)
