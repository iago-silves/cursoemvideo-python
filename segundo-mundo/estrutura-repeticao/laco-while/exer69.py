sexo_feminino_menos_20 = 0
maiores_de_18 = 0
homens = 0

while(True):
    try:
        sexo = input(f"Digite o sexo (M/F) da pessoa: ").strip().upper()

        if sexo not in ("M", "F"):
            print("Erro: Digite um sexo existente!")
            continue

        idade = int(input(f"Digite a idade da pessoa: "))

        if sexo == "F" and idade < 20:
            sexo_feminino_menos_20 += 1
        
        if idade > 18:
            maiores_de_18 += 1
        
        if sexo == "M":
            homens += 1
            
        continuar = input("Deseja continuar (SIM/NÃO): ").lower().strip()

        if continuar not in ("sim", "s", "n", "nao", "não"):
            print("Erro: Opção inválida!")
            continue

        if continuar in ("n", "nao", "não"):
            print("Finalizando programa!")
            break

    except ValueError:
        print("Erro: Digite números válidos!")
        continue 


print(f"Mulheres com menos de 20 anos: {sexo_feminino_menos_20}.\n"
      f"A quantidade de maiores de idade: {maiores_de_18}.\n"
      f"A quantidade de homens cadastrados: {homens}.")