porcao_inteira = input("Digite um número flutuante: ").strip()

try:
    float(porcao_inteira)
except ValueError:
    print("Erro: digite um valor flutuante.")

if porcao_inteira in " ":
    print("Erro: contém espaços.")

elif porcao_inteira.isalpha():
    print("Erro: digite um valor válido.")

for i in porcao_inteira:
    if i in ".":
        break

    print(f"A parte inteira do número {porcao_inteira} é {i}", end="")


# versão corrigita:

# valor = input("Digite um número flutuante: ").strip()

# try:
#     numero = float(valor)
#     parte_inteira = int(numero)
#     print(f"A parte inteira do número {numero} é {parte_inteira}")
# except ValueError:
#     print("Erro: digite um valor flutuante válido.")
