contador = 0
soma = 0
maior = 0
menor = 0

while(True):
    try:
        numero = int(input("Digite um número (Para parar: 999): "))

        if numero != 999:
            contador += 1
            soma += numero
        
        else:
            print("Finalizando...")
            break

        if contador == 1:
            maior = numero
            menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
    
    except ValueError:
        print("Erro: Digite valores validos!")
        continue

media = soma / contador if contador > 0 else 0

print(f"A media: {media}.\n"
      f"O maior: {maior} e o menor: {menor}.")