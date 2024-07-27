import math

data = [30, 26, 33, 26, 26, 33, 31, 31, 21, 37,
        27, 20, 34, 35, 30, 24, 38, 34, 39, 31,
        22, 30, 23, 23, 31, 44, 31, 33, 33, 26,
        27, 28, 25, 35, 23, 32, 29, 31, 25, 27]

nivel_confianca = 0.95

desvio_padrao = 7.9

n = len(data)

media_amostra = sum(data) / n

variancia_amostra = sum((x - media_amostra) ** 2 for x in data) / (n - 1)

desvio_padrao_amostra = math.sqrt(variancia_amostra)

# t critico para 95% de confiança
t = 1.96

margem_de_erro = t * desvio_padrao / math.sqrt(n)

print(f"Margem de erro: {margem_de_erro:.2f} horas")