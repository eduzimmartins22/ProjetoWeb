import requests
from bs4 import BeautifulSoup
import json


response = requests.get("https://www.guiaserra.com.br/promocoes")
conteudo = response.content
soup = BeautifulSoup(conteudo, "html.parser")


items = soup.find("section", class_="padding-side")
promocoes = []
imagens_capturadas = set() 


if items:
    for item in items.find_all("div", class_="column-two-to-one-v4 margin-bottom40"):
        promocao = {}


        nome = item.find("p", class_="discount-title")
        promocao['nome'] = nome.get_text(strip=True) if nome else "Nome indisponível"


        preco = item.find('span', class_='span-price')
        promocao['preco'] = preco.get_text(strip=True) if preco else "Preço indisponível"


        imagem = item.find('img', class_='product')
        if imagem:

            imagem_src = (
                imagem.get('data-src') or  
                imagem.get('data-lazy') or  
                imagem.get('src') 
            )


            print(f"Tentando capturar imagem: {imagem_src}")


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


        promocoes.append(promocao)


with open('promocoes.json', 'w', encoding='utf-8') as f:
    json.dump(promocoes, f, ensure_ascii=False, indent=4)

print("Promoções salvas no arquivos Json")