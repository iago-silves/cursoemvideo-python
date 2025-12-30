def calcular_preco_passagem(distancia):
    if distancia <= 200:
        return distancia * 0.5
    
    return distancia * 0.45


print(calcular_preco_passagem(200))
print(calcular_preco_passagem(300))