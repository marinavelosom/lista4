import math

PL1 = [17, 16, 21, 14, 18, 24, 16, 14, 21, 23, 11, 18, 13, 18, 15]
PL2 = [18, 14, 19, 11, 23, 21, 10, 13, 19, 24, 15, 20, 21, 21, 16]

tam_amostras = len(PL1)

# diferença de tempos de implementacao para cada programador
diferencas = [PL1[i] - PL2[i] for i in range(tam_amostras)]

media_diferencas = sum(diferencas) / tam_amostras

variancia_diferencas = sum((x - media_diferencas) ** 2 for x in diferencas) / (tam_amostras - 1)

t = media_diferencas / math.sqrt(variancia_diferencas / tam_amostras)

# para 95% de confiança e 14 graus de liberdade
t_critico = 2.145  

print("Diferencas:", diferencas)
print("Media das diferencas:", media_diferencas)
print("Variancia das diferencas:", variancia_diferencas)
print("Valor t calculado:", t)
print("Valor critico para 95% de confianca:", t_critico)

# H0: nao há diferença significativa no desempenho das duas linguagens de programação (a média das diferenças é zero)
# HA: há uma diferença significativa no desempenho das duas linguagens de programação (a média das diferenças é diferente zero)

if abs(t) > t_critico:
    print("Rejeitamos a hipotese nula. Ha evidencias para apoiar uma diferença no desempenho das linguagens.")
else:
    print("Nao rejeitamos a hipotese nula. Nao ha evidencias para apoiar uma diferenca no desempenho das linguagens.")

