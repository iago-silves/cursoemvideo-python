numero = int(input("Digite um número inteiro: "))

binario = []

while numero > 0:
    resto = numero % 2
    binario.append(resto)
    numero = numero // 2

print(binario[::-1])