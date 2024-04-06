# -*- coding: utf-8 -*-
# Função para verificar se três medidas formam um triângulo
def eh_triangulo(A, B, C):
    # Verifica se a medida A é menor que a soma das medidas B e C
    # e se A é maior que a diferença entre B e C
    return (abs(B - C) < A < (B + C))


# Lê as medidas A, B e C do triângulo
A, B, C = map(float, input().split())

# Verifica se todas as combinações de medidas formam um triângulo
if eh_triangulo(A, B, C) and eh_triangulo(B, C, A) and eh_triangulo(C, A, B):
    # Se sim, imprime o perímetro do triângulo com uma casa decimal
    print("Perimetro = {:.1f}".format(A + B + C))
else:
    # Se não, imprime a área do triângulo com uma casa decimal
    print("Area = {:.1f}".format(((A + B) * C) / 2.0))
