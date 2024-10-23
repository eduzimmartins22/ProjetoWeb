import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from comparar_promocoes import comparar_promocoes
import os

response = requests.get("https://www.guiaserra.com.br/promocoes")
conteudo = response.content
soup = BeautifulSoup(conteudo, "html.parser")


items = soup.find("section", class_="padding-side")
promocoes_novas = []
imagens_capturadas = set() 


if items:
    for item in items.find_all("div", class_="column-two-to-one-v4 margin-bottom40"):
        promocao = {}


        nome = item.find("p", class_="discount-title")
        promocao['nome'] = nome.get_text(strip=True) if nome else "Nome indisponível"


        preco = item.find('span', class_='span-price')
        promocao['preco'] = preco.get_text(strip=True).replace('\xa0', '') if preco else "Preço indisponível"


        imagem = item.find('img', class_='product')
        if imagem:

            imagem_src = (
                imagem.get('data-src') or  
                imagem.get('data-lazy') or  
                imagem.get('src') 
            )


            if imagem_src and imagem_src.startswith("http") and imagem_src.endswith(('.jpg', '.png', '.webp')):
                if imagem_src not in imagens_capturadas:  
                    promocao['imagem'] = imagem_src
                    imagens_capturadas.add(imagem_src) 
                else:
                    promocao['imagem'] = "Imagem duplicada"
            else:
                promocao['imagem'] = "Imagem inválida ou indisponível"
        else:
            promocao['imagem'] = "Imagem indisponível"


        promocoes_novas.append(promocao)


data_hoje = datetime.now().strftime('%d-%m-%Y')
nome_arquivo_json = f'promocoes-' + data_hoje + '.json'


caminho_pasta_relatorios = 'Buscas'
if not os.path.exists(caminho_pasta_relatorios):
    os.makedirs(caminho_pasta_relatorios)


caminho_arquivo_json = os.path.join(caminho_pasta_relatorios, nome_arquivo_json)


try:
    with open(caminho_arquivo_json, 'r', encoding='utf-8') as f:
        promocoes_antigas = json.load(f).get('promocoes', [])
except FileNotFoundError:
    promocoes_antigas = []


relatorio = comparar_promocoes(promocoes_antigas, promocoes_novas)


conteudo_final = {
    "relatorio": relatorio,
    "promocoes": promocoes_novas
}


with open(caminho_arquivo_json, 'w', encoding='utf-8') as f:
    json.dump(conteudo_final, f, ensure_ascii=False, indent=4)

print("Promoções salvas no arquivo " + nome_arquivo_json)