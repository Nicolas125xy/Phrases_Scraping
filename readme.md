
# Web Scraping de um site de Frases 
## Este projeto é um script em Python que realiza a busca de frases em um site de pensamentos e citações chamado Pensador.com. O script utiliza as bibliotecas requests e BeautifulSoup para realizar a busca e extrair as frases encontradas.

# Como utilizar
## Para utilizar o script, basta executá-lo e digitar a palavra-chave que deseja buscar. O script irá exibir as frases encontradas em formato de texto no console.

# Dependências
## Para executar o script, é necessário ter as bibliotecas requests e BeautifulSoup instaladas. Você pode instalá-las utilizando o pip:

```
pip install requests 
pip install beautifulsoup4

```
# Funcionamento
## O script utiliza a função requests.get() para enviar uma solicitação GET para a página de busca do Pensador.com, passando a palavra-chave como parâmetro. Em seguida, ele analisa o conteúdo HTML da resposta utilizando a biblioteca BeautifulSoup. Por fim, ele encontra todos os elementos com a classe 'frase fr' e imprime as frases encontradas.

# Exemplo de uso

```
Pesquisar: amor

Buscando resultados...

Amor é a poesia dos sentidos, a sabedoria das paixões, a guerra das atrações e a paz dos desejos. - Voltaire
-------------------------------------------------

Amor é o único tesouro que não perde valor ao ser dividido. - Antoine de Saint-Exupéry
-------------------------------------------------

````
# Limitações
## O script só busca frases na primeira página de resultados do Pensador.com. Se houver mais frases disponíveis, você precisará modificar o script para buscar as próximas páginas.

# Licença
## Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
