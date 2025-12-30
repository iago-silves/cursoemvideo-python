# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input("Digite seu nome: ").title().strip()

print("Boboca!" if nome == "Lucas" else "Seja bem-vindo!")