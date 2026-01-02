"""
Exercício Python 48: Faça um programa que calcule 
a soma entre todos os números que são múltiplos de 
três e que se encontram no intervalo de 1 até 500.
"""
quantidade = 0
somar_todos = 0

for i in range(1, 500 + 1):
    soma_algarismos = sum(int(j) for j in str(i))
    
    if soma_algarismos % 3 == 0:
        quantidade += 1
        somar_todos += i
        
print(f"Quantidade: {quantidade}")
print(f"Soma: {somar_todos}")