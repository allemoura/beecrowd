# -*- coding: utf-8 -*-
#entradas
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

#calcula notas com pesos
a = nota1 * 0.2
b = nota2 * 0.3
c = nota3 * 0.5

#calcula e imprime media
media = a + b + c
print("MEDIA = {:.1f}".format(media))
