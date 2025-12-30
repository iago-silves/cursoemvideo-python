from random import randint

computador_pense = randint(0, 5)

adivinhar_numero = int(input("Digite o número digitado pelo computador: "))

print(computador_pense == adivinhar_numero)