from datetime import datetime, date
from dateutil.relativedelta import relativedelta

def idade_alistamento_militar(data_nascimento):
    data_inicial = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
    return relativedelta(date.today(), data_inicial)

data_nascimento = input("Digite a sua data de nascimento (dd/mm/aa): ").strip()

alistamento_militar = idade_alistamento_militar(data_nascimento).years

if alistamento_militar < 18:
    print("Ainda não chegou a hora do alistamento.")
elif alistamento_militar == 18:
    print("É a hora exata de se alistar.")
else:
    print("Já passou do tempo do alistamento.")

