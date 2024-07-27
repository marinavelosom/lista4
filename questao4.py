import math

data = [
    18.41, 16.91, 16.83, 17.72, 15.54, 15.56, 18.01, 19.11, 19.79, 18.32,
    18.65, 20.71, 20.66, 21.04, 21.74, 22.13, 21.96, 22.16, 22.86, 20.86,
    20.74, 22.05, 21.42, 22.34, 22.83, 24.34, 17.97, 14.47, 19.06, 18.42,
    20.85, 21.43, 21.97, 21.81
]

desvio_padrao = 2.62

amostra = len(data)

media = sum(data) / amostra

# z criticos para 90% e 99% de confiança
z_90 = 1.645
z_99 = 2.576

# calcula intervalo de confiança
def intervalo_confianca(media, desvio_padrao, amostra, z):
    margem_de_erro = z * desvio_padrao / math.sqrt(amostra)
    limite_inferior = media - margem_de_erro
    limite_superior = media + margem_de_erro
    return limite_inferior, limite_superior

# 90%
ic_90 = intervalo_confianca(media, desvio_padrao, amostra, z_90)
print(f"Intervalo de confianca (90%): US$ {ic_90[0]:.2f} - US$ {ic_90[1]:.2f}")

# 99%
ic_99 = intervalo_confianca(media, desvio_padrao, amostra, z_99)
print(f"Intervalo de confianca (99%): US$ {ic_99[0]:.2f} - US$ {ic_99[1]:.2f}")
