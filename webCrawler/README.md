# Projeto: Consulta de Promoções na Serra

Este projeto tem como objetivo realizar a consulta automatizada das promoções no site [guiaserra.com.br](https://www.guiaserra.com.br), coletando informações atualizadas sobre promoções disponíveis na região da Serra diariamente.

## Funcionalidades

- Acessa automaticamente a parte de promoções do site [guiaserra.com.br/promocoes](https://www.guiaserra.com.br/promocoes).
- Faz a extração dos dados de promoções usando `BeautifulSoup4`.
- Realiza requisições HTTP para obter as páginas de interesse com a biblioteca `requests`.
- Salva as promoções encontradas na busca em um arquivo `.json`
- Exibe as promoções disponíveis de forma organizada.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
    - [`beautifulsoup4`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): para análise e extração de dados HTML.
    - [`requests`](https://docs.python-requests.org/en/master/): para realizar requisições HTTP e acessar o site.