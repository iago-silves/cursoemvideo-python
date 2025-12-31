def calculo_imc(peso, altura):
    if altura <= 0 or peso <= 0:
        return "Erro: peso ou alturas inválidas."
    
    imc = peso / (altura * altura)

    if imc < 18.5:
        return "Abaixo do peso."
    elif imc < 25:
        return "Peso ideal."
    elif imc < 30:
        return "Obesidade."
    else:
        return "obesidade mórbida."

print(calculo_imc(50, 1.63))