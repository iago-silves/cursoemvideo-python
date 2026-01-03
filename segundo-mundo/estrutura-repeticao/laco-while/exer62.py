primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

total_termos = 0
termos_mostrar = 10

while termos_mostrar != 0:
    contador = 0

    while contador < termos_mostrar:
        print(primeiro_termo, end=" → ")
        primeiro_termo += razao
        contador += 1
        total_termos += 1

    print("\nPausa!")
    termos_mostrar = int(input("Quantos termos deseja mostrar a mais? "))

print(f"A quantidade de termos mostrados é: {total_termos}")
