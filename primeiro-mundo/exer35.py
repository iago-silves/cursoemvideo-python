primeiro = int(input("Digite um número: "))
segundo = int(input("Digite um número: "))
terceiro = int(input("Digite um número: "))

maior = primeiro
soma_lados = segundo + terceiro

if segundo > maior:
    maior = segundo
    soma_lados = primeiro + terceiro

if terceiro > maior:
    maior = terceiro
    soma_lados = primeiro + segundo


if soma_lados > maior:
    print("Forma triangulo...")

else:
    print("Não forma triangulo...")