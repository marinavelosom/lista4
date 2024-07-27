import math

custo_medio = 2650

desvio_padrao = 425

amostra = 50

nivel_confianca = 95

alpha = 1 - nivel_confianca / 100

z_critico = 1.96

margem_de_erro = z_critico * desvio_padrao / math.sqrt(amostra)

limite_inferior = custo_medio - margem_de_erro

limite_superior = custo_medio + margem_de_erro

print(f"Intervalo de confianca (95%): US$ {limite_inferior:.4f} - US$ {limite_superior:.4f}")
