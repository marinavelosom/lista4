import math

data = [
    186.4978, 306.4696, 246.8279, 242.3109, 227.8811, 278.1708, 249.6557, 253.292, 208.1038, 238.7719,
    232.57, 262.5679, 229.2001, 256.1409, 221.9513, 268.2424, 257.8084, 201.4026, 266.9491, 230.4371,
    216.5795, 178.5637, 215.9115, 220.0037, 275.9563, 221.868, 246.065, 180.2109, 189.6811, 229.2552,
    226.0516, 214.7398, 228.1066, 261.5842, 292.2176, 226.7751, 200.2462, 243.5119, 241.9945, 195.8083,
    162.6561, 196.4679, 203.9529, 257.2282, 231.6957, 214.5121, 239.846, 216.7897, 274.2512, 211.2262,
    251.6661, 204.5006, 239.5076, 223.1867, 214.8416, 193.993, 255.3547, 216.7973, 216.0063, 249.4203
]

amostra_atual = len(data)

media = sum(data) / amostra_atual

desvio_padrao = math.sqrt(sum((x - media) ** 2 for x in data) / (amostra_atual - 1))

# para 99% de confianca
z_critico = 2.576

# erro absoluto 
E = 5

amostras_necessarias = (z_critico * desvio_padrao / E) ** 2

# arredonda para cima 
amostras_necessarias = math.ceil(amostras_necessarias)

medidas_adicionais = amostras_necessarias - amostra_atual
print(f"Medidas adicionais necessarias: {medidas_adicionais}")

