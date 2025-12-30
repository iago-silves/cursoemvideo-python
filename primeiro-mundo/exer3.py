def somarDoisNumeros(a, b):
    return a + b

try:
    primeiro = int(input("Digite um número: "))
    segundo = int(input("Digite outro número: "))
except:
    print("Erro...")

print(f"O resultado da soma: {somarDoisNumeros(primeiro, segundo)}")