"""
Exercício Python 041: A Confederação
Nacional de Natação precisa de um programa 
que leia o ano de nascimento de um atleta 
e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""

def classificar_atletas(idade):
    if idade < 0 or idade > 120:
        return f"Erro: idade digite inválida."
        
    if idade <= 9:
        return "MIRIM"
    elif idade <= 14:
        return "INFANTIL"
    elif idade <= 19:
        return "JÚNIOR"
    elif idade <= 25:
        return "SÊNIOR"
    else:
        return "MASTER"

idade = classificar_atletas(30) 
       
print(idade)