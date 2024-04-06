# -*- coding: utf-8 -*-
# Enquanto não for informado um conjunto de coordenadas de saída e destino igual a (0, 0, 0, 0)
while True:
    # Lê as coordenadas de entrada
    entrada = input().split()
    x_inicial, y_inicial, x_destino, y_destino = int(
        entrada[0]), int(entrada[1]), int(entrada[2]), int(entrada[3])
    # Se as coordenadas forem (0, 0, 0, 0), encerra o loop
    if x_inicial == 0 and y_inicial == 0 and x_destino == 0 and y_destino == 0:
        break
    # Verifica se a dama já está na casa de destino
    if x_inicial == x_destino and y_inicial == y_destino:
        print("0")
    # Verifica se a dama pode chegar em um movimento
    elif (x_inicial == x_destino or y_inicial == y_destino) or ((x_destino - x_inicial) == abs(y_destino - y_inicial) or abs(x_destino - x_inicial) == abs(y_destino - y_inicial) or abs(x_destino - x_inicial) == (y_destino - y_inicial) or (x_destino - x_inicial) == (y_destino - y_inicial)):
        print("1")
    # Caso contrário, são necessários pelo menos dois movimentos
    else:
        print("2")
