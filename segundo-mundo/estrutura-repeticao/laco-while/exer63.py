quantidade = int(input("Digite quantos termos da sequência: "))

anterior = 0
atual = 1
contador = 0

while contador < quantidade:
    print(anterior, end=" → ")
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    contador += 1

print("FIM")
