numero = int(input("Digite um número: "))

quantidade_divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        quantidade_divisores += 1

print(f"O numero {numero} foi divido {quantidade_divisores} vezes.")

if quantidade_divisores == 2:
    print(f"Ele é primo!")