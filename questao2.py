import math

amostra = [24, 27, 26, 29, 33, 21, 18, 24, 23, 34,
        17, 15, 19, 23, 25, 29, 36, 19, 18, 22]

sigma = 4.3
n = len(amostra)
confiança = 0.99

media_amostral = sum(amostra) / n

alpha = 1 - confiança
z_critico = 2.575  

erro_padrao = sigma / math.sqrt(n)

margem_erro = z_critico * erro_padrao
limite_inferior = media_amostral - margem_erro
limite_superior = media_amostral + margem_erro

print("Media amostral:", media_amostral)
print("Erro padrao:", erro_padrao)
print("Margem de erro:", margem_erro)
print("Intervalo de confianca de 99%: ({:.2f}, {:.2f})".format(limite_inferior, limite_superior))
