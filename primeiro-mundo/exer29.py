def velocidade_carro(velocidade):
    if velocidade > 80:
        multa = (velocidade - 80) * 7

    return f"O valor da multa: {multa}"


print(velocidade_carro(110))