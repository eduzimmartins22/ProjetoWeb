from datetime import datetime
import os

def comparar_promocoes(antigas, novas):
    novas_promocoes = []
    removidas_promocoes = []

    #promoções novas
    for promo_nova in novas:
        encontrada = False
        for promo_antiga in antigas:
            if (promo_nova['nome'] == promo_antiga['nome'] and 
                promo_nova['preco'] == promo_antiga['preco']):
                encontrada = True
                break
        if not encontrada:
            novas_promocoes.append(promo_nova)

    #promoções removidas
    for promo_antiga in antigas:
        encontrada = False
        for promo_nova in novas:
            if (promo_antiga['nome'] == promo_nova['nome'] and 
                promo_antiga['preco'] == promo_nova['preco']):
                encontrada = True
                break
        if not encontrada:
            removidas_promocoes.append(promo_antiga)

    relatorio = {
        "data_consulta": datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        "numero_promocoes_obtidas": len(novas),
        "novas_promocoes": len(novas_promocoes),
        "promocoes_removidas": len(removidas_promocoes),
        "erros": [] #todo - log de erro no relatorio?
    }

    return relatorio

def encontrar_arquivo_mais_recente(pasta):
    arquivos = [f for f in os.listdir(pasta) if f.startswith('promocoes-') and f.endswith('.json')]
    
    if not arquivos:
        return None

    arquivo_mais_recente = None
    data_mais_recente = None

    for arquivo in arquivos:
        partes_nome = arquivo.replace('promocoes-', '').replace('.json', '').split('-')
        dia, mes, ano = int(partes_nome[0]), int(partes_nome[1]), int(partes_nome[2])
        data_arquivo = datetime(ano, mes, dia)

        if data_mais_recente is None or data_arquivo > data_mais_recente:
            data_mais_recente = data_arquivo
            arquivo_mais_recente = arquivo

    return os.path.join(pasta, arquivo_mais_recente)