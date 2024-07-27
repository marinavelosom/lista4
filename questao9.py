import math

s1 = [
    125.302, 125.364, 129.491, 119.026, 130.156, 127.737, 104.935, 155.090, 119.950,
    135.941, 110.225, 133.981, 108.729, 138.692, 101.700, 128.676, 127.857, 121.650,
    112.271, 98.488, 130.685, 131.733, 120.388, 107.406, 105.687, 110.473, 115.235,
    129.847, 92.796, 155.956
]

s2 = [
    121.232, 127.403, 147.043, 150.086, 152.947, 153.124, 140.478, 149.328, 154.216,
    145.887, 128.966, 144.881, 139.455, 148.278, 130.305, 137.399, 133.041, 152.535,
    138.691, 140.942, 145.377, 136.206, 126.793, 154.545, 138.180, 152.801, 128.337,
    136.467, 157.890, 141.825, 151.294, 113.529, 148.484, 139.141, 150.223, 138.821,
    134.362, 143.290, 130.566, 121.223, 151.899, 151.412, 134.970, 134.963, 145.848,
    147.644, 123.404, 137.720, 148.617, 144.529
]

tam_amostra_s1 = len(s1)
tam_amostra_s2 = len(s2)

media_s1 = sum(s1) / tam_amostra_s1
media_s2 = sum(s2) / tam_amostra_s2

variancia_s1 = sum((x - media_s1) ** 2 for x in s1) / (tam_amostra_s1 - 1)
variancia_s2 = sum((x - media_s2) ** 2 for x in s2) / (tam_amostra_s2 - 1)

variancia_combinada = ((tam_amostra_s1 - 1) * variancia_s1 + (tam_amostra_s2 - 1) * variancia_s2) / (tam_amostra_s1 + tam_amostra_s2 - 2)

t = (media_s1 - media_s2) / math.sqrt(variancia_combinada * (1/tam_amostra_s1 + 1/tam_amostra_s2))

graus_de_liberdade = tam_amostra_s1 + tam_amostra_s2 - 2
t_critico = 1.96 

print("Media s1:", media_s1)
print("Media s2:", media_s2)
print("Variancia s1:", variancia_s1)
print("Variancia s2:", variancia_s2)
print("T:", t)
print("T critico:", t_critico)

if abs(t) > t_critico:
    print("Rejeitamos a hipotese nula. Os desempenhos dos servidores sao significativamente diferentes.")
else:
    print("Nao rejeitamos a hipotese nula. Os desempenhos dos servidores sao equivalentes.")
