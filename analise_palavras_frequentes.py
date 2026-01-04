import re
from collections import Counter

def palavras_mais_comuns(arq_txt):
    with open(arq_txt, 'r', encoding='utf-8') as arq_aberto:
       texto = arq_aberto.read().lower()

    palavras = re.findall(r'\b[a-zA-Z]{2,}\b', texto)

    artigos_definidos = {"o", "a", "os", "as", "que", "de", "da", "das", "do", "dos", "e", "um", "uns", "uma", "umas", "não"}
    palavras = [cada_palavra for cada_palavra in palavras if cada_palavra not in artigos_definidos]

    frequencia_palavras = Counter(palavras)
    palavras_mais_frequentes = frequencia_palavras.most_common(10)

    for palavra, frequencia in palavras_mais_frequentes:
        print(f'{palavra}: {frequencia}')

    return palavras_mais_frequentes

arq_txt = 'MemóriasPostumasDeBrasCubas.txt'
palavras_mais_comuns(arq_txt)
