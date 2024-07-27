import math

media_amostral = 20695
media_hipotese_nula = 21500
desvio_padrao = 2250
tamanho_amostra = 25
nivel_significancia = 0.05

# estatística z
z = (media_amostral - media_hipotese_nula) / (desvio_padrao / math.sqrt(tamanho_amostra))

# para 95% de confianca
z_critico = 1.96

print(f'Estatistica z: {z:.4f}')
print(f'Z critico para significancia de {nivel_significancia} (bilateral): {z_critico}')

if abs(z) > z_critico:
    print("Rejeitamos a hipótese nula. A informacao pode estar incorreta.")
else:
    print("Nao rejeitamos a hipotese nula. Nao ha evidencias suficientes para afirmar que a informacao esta incorreta.")
