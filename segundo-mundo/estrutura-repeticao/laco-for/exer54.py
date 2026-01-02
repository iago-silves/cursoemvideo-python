from datetime import date

def maioridade_pessoa(data_nascimento):
    ano_atual = date.today().year
    return ano_atual - data_nascimento

quantidade_maior_idade = 0
quantidade_menor_idade = 0

for i in range(0, 7):
    data_nascimento = int(input(f"Digite a sua data de nascimento da {i + 1}º pessoa: ")).strip()
    
    idade_pessoa = maioridade_pessoa(data_nascimento)

    if idade_pessoa >= 18:
        quantidade_maior_idade += 1
    else:
        quantidade_menor_idade += 1

print(f"A quantidade de pessoas maiores de idade é: {quantidade_maior_idade}.\n"
      f"A quantidade de pessoas menores de idade é: {quantidade_menor_idade}.")