primeiro = int(input("Digite um número: "))
segundo = int(input("Digite um número: "))
terceiro = int(input("Digite um número: "))

maior = primeiro
menor = primeiro

if segundo > maior:
    maior = segundo
if segundo < menor:
    menor = segundo

if terceiro > maior:
    maior = terceiro
if terceiro < menor:
    menor = terceiro

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
