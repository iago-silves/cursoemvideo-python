primeiro = int(input("Digite um número: "))
segundo = int(input("Digite um número: "))

if primeiro > segundo:
    print("O primeiro valor é maior.")
elif segundo < primeiro:
    print("O segundo valor é maior.")
else:
    print("Não existe valor maior, os dois são iguais.")