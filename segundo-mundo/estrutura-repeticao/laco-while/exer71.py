try:
    valor = int(input("Digite um valor para saque: "))

    if valor <= 0:
        print("Valor inválido.")
        
    else:
        cedulas_50 = 0
        cedulas_20 = 0
        cedulas_10 = 0
        cedulas_1 = 0

        while valor >= 50:
            valor -= 50
            cedulas_50 += 1

        while valor >= 20:
            valor -= 20
            cedulas_20 += 1

        while valor >= 10:
            valor -= 10
            cedulas_10 += 1

        while valor >= 1:
            valor -= 1
            cedulas_1 += 1

        print("Cédulas entregues:")
        if cedulas_50 > 0:
            print(f"{cedulas_50} nota(s) de R$50")
        if cedulas_20 > 0:
            print(f"{cedulas_20} nota(s) de R$20")
        if cedulas_10 > 0:
            print(f"{cedulas_10} nota(s) de R$10")
        if cedulas_1 > 0:
            print(f"{cedulas_1} nota(s) de R$1")

except ValueError:
    print("Erro: Digite um valor válido!")
