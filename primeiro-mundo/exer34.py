def calcular_salario_aumento(salario):
    if salario > 1250:
        return salario + (salario * 0.1)
    return salario + (salario * 0.15)

print(calcular_salario_aumento(1250))
print(calcular_salario_aumento(1512))
print(calcular_salario_aumento(1000))