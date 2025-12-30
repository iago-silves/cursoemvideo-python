def valor_aluguel_carro(km_percorridos, dias_alugados):
    carro_por_dia_real = dias_alugados * 60
    km_rodados_real = km_percorridos * 0.15

    return carro_por_dia_real + km_rodados_real


valor_aluguel = valor_aluguel_carro(60, 2)

print(f"O valor total do aluguel: {valor_aluguel}.")