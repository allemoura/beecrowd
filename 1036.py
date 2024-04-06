# -*- coding: utf-8 -*-
# link questão: https://judge.beecrowd.com/pt/problems/view/1036
import math
# recebe valores de entrada
nums = input().split()

# separa os valores
a, b, c = float(nums[0]), float(nums[1]), float(nums[2])
# se a = 0 não é possivel calcular as raízes
if a == 0:
    print("Impossivel calcular")
else:
    # calcula o valor das raízes
    cont = b**2 - (4 * a * c)

    # se o count menor que 0, significa que não foi possivel calcular as raízes
    if cont < 0:
        print("Impossivel calcular")
    else:
        # calcula o valor de Bhaskara
        delta = math.sqrt(cont)
        r1 = (-(b) + delta)/(2 * a)
        r2 = (-(b) - delta)/(2 * a)

        # imprime os valores de R1 e R2 encontrados
        print("R1 = {:.5f}".format(r1))
        print("R2 = {:.5f}".format(r2))
