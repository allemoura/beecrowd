# -*- coding: utf-8 -*-
# link questão: https://judge.beecrowd.com/pt/problems/view/1089
def contar_picos(amostras):
    picos = 0
    n = len(amostras)

    # Itera sobre todas as amostras
    for i in range(n):
        # Define os índices dos elementos anterior e posterior ao elemento atual
        if i == 0:
            prev = n - 1  # O último elemento é anterior ao primeiro
        else:
            prev = i - 1

        if i == n - 1:
            next = 0  # O primeiro elemento é posterior ao último
        else:
            next = i + 1

        # Verifica se o elemento atual é um pico
        if (amostras[i] > amostras[prev] and amostras[i] > amostras[next]) or \
           (amostras[i] < amostras[prev] and amostras[i] < amostras[next]):
            picos += 1

    return picos


# Código para ler as amostras e calcular o número de picos
while True:
    n = int(input())
    if n == 0:
        break

    amostras = list(map(int, input().split()))

    print(contar_picos(amostras))
