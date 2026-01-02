"""
Exercício Python 50: Desenvolva um programa que 
leia seis números inteiros e mostre a soma apenas 
daqueles que forem pares. Se o valor digitado 
for ímpar, desconsidere-o
"""
soma_pares = 0

for _ in range(0, 6):
    num = int(input("Digite um número:"))
    
    if num % 2 == 0:
        soma_pares += num
        
print(f"Soma dos pares: {soma_pares}")