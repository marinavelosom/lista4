import math

data = [24, 27, 26, 29, 33, 21, 18, 24, 23, 34,
        17, 15, 19, 23, 25, 29, 36, 19, 18, 22]

nivel_confianca = 0.99

desvio_padrao = 4.3

amostra = len(data)

# z critico para 99% de confiança
z = 2.576

margem_de_erro = z * desvio_padrao / math.sqrt(amostra)

print(f"Margem de erro: {margem_de_erro:.2f} minutos")