def emprestimo_bancario(valor_casa, salario_comprador, anos_pagar):
    parecela_mes = valor_casa / (anos_pagar * 12)
    valor_pagar_comprador = salario_comprador * 0.3

    if valor_pagar_comprador < parecela_mes:
        return "desaprovado."
    return "aprovado."
    
print(emprestimo_bancario(250000, 1000, 20))