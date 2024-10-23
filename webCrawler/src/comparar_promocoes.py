from datetime import datetime

def comparar_promocoes(antigas, novas):
    antigas_set = {(promo['nome'], promo['preco']) for promo in antigas}

    novas_promocoes = [promo for promo in novas if (promo['nome'], promo['preco']) not in antigas_set]

    removidas_promocoes = [promo for promo in antigas if (promo['nome'], promo['preco']) not in {(p['nome'], p['preco']) for p in novas}]

    relatorio = {
        "data_consulta": datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        "numero_promocoes_obtidas": len(novas),
        "novas_promocoes": len(novas_promocoes),
        "promocoes_removidas": len(removidas_promocoes),
        "erros": [] #todo - log de erro no relatorio?
    }

    return relatorio