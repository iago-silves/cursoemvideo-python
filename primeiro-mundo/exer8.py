def conversor_medidas(valor_metros):
    return {
        "centimetros": valor_metros * 100,
        "milimetros": valor_metros * 1000
    }

valor_metros = int(input("Digite um valor em metros: "))

print(conversor_medidas(valor_metros))