def salario_funcionario(salario_atual, aumento_proporcionado=0.15):
    return salario_atual + (salario_atual * aumento_proporcionado)

salario = float(input("Digite seu salario atual: "))

aumento_salarial = salario_funcionario(salario)

print(f"O seu salário sofreu uma auteração de 15%: {aumento_salarial}.")