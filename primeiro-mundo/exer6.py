from math import sqrt

def dobroTriploRaizQuadrada(numero):
    return f"dobro: {numero * 2}\n triplo: {numero * 3}\n raiz quadrada: {sqrt(numero)}."

numero = int(input("Digite um numero: "))

print(f"O {dobroTriploRaizQuadrada(numero)}")