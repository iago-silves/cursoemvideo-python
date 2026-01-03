contador = 0
soma = 0

while(True):
    try:
        numero = int(input("Digite um número (Para parar: 999): "))

        if numero != 999:
            contador += 1
            soma += numero
        
        else:
            print("Finalizando...")
            break

    except ValueError:
        print("Erro: Digite valores validos!")
        continue

print(f"A quantidade de números digitados: {contador}.\n"
      f"A soma de todos números digitados: {soma}.")