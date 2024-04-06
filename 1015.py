# -*- coding: utf-8 -*-
import math
# recebe entradas
entrada1 = input().split()
entrada2 = input().split()

# separa os valores
x1, y1 = float(entrada1[0]), float(entrada1[1])
x2, y2 = float(entrada2[0]), float(entrada2[1])

# soma os valores internor da raiz quadrada
soma = ((x2 - x1)**2) + ((y2-y1)**2)
# calcula a raiz quadrada e imprime o valor
distancia = math.sqrt(soma)
print("{:.4f}".format(distancia))
