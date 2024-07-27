import math

media_amostral = 12.9
media_hipotese_nula = 13
desvio_padrao = 0.19
tamanho_amostra = 32
nivel_significancia = 0.01

# estatística z
z = (media_amostral - media_hipotese_nula) / (desvio_padrao / math.sqrt(tamanho_amostra))

# para 1% de significancia
z_critico = 2.33

print(f'Estatistica z: {z}')
print(f'Z critico para significancia de {nivel_significancia}: {z_critico}')

# H0 -> tm <= 13s
# HA -> tm > 13s
if z > z_critico:
    print("Rejeitamos a hipotese nula. Ou seja, tempo médio é maior que 13s")
else:
    print("Nao rejeitamos a hipotese nula. Ou seja, de fato tempo medio eh menor ou igual a 13s")


