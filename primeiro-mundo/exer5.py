def sucessor_antecessor(numero):
    return f"O antecessor: {numero - 1} e o sucessor: {numero + 1}."

try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro...")

print(sucessor_antecessor(numero))