def dinheiro_em_real_br(valor_real):
    return valor_real / 5.5


dinheiro_carteira = float(input("Digite quanto dinheiro tem disponivel em real (BR): "))

print(f"Valor em dólar: {dinheiro_em_real_br(dinheiro_carteira)}")