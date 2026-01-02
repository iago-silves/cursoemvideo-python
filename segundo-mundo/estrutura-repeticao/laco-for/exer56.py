"""
Exercício Python 56: Desenvolva um programa que leia o nome, 
idade e sexo de 4 pessoas. No final do programa, mostre: a média 
de idade do grupo, qual é o nome do homem mais velho e quantas 
mulheres têm menos de 20 anos.

"""
def linha(separador="-+", quantidade=20):
    print(separador * quantidade)

quantidade_pessoas = 4
idade_total = 0
sexo_feminino_menos_20 = 0

homem_mais_velho_idade = 0
nome_homem_mais_velho = ""


for i in range(0, quantidade_pessoas):
    nome = input(f"Digite o nome da {i + 1}ª pessoa: ").strip().title()
    sexo = input(f"Digite o sexo (M/F) da {i + 1}ª pessoa: ").strip().title()

    if sexo not in "MF":
        print("Erro: Digite um sexo existente!")
        continue

    try:
        idade = int(input(f"Digite a idade da {i + 1}ª pessoa: "))

        homem_mais_velho = idade

        if sexo == "F" and idade < 20:
            sexo_feminino_menos_20 += 1

        if sexo == "M" and idade > homem_mais_velho_idade:
            homem_mais_velho_idade = idade
            nome_homem_mais_velho = nome

        
        idade_total += idade

    except ValueError:
        print("Erro: Certissifique que a idade foi digitada corretamente!")
        continue
    

    
    
media_das_idades = idade_total / quantidade_pessoas

print(f"A média da idade do grupo: {media_das_idades:.1f}.\n"
      f"O nome do homem mais velo: {nome_homem_mais_velho}.\n"
      f"A quantidade de mulheres com menos de 20 anos: {sexo_feminino_menos_20}.")