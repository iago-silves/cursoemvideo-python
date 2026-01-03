primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

decimo_termo = 10
prog_aritmetrica = 0

while prog_aritmetrica < decimo_termo:
    print(f"{primeiro_termo}", end=" → ")

    primeiro_termo += razao
    prog_aritmetrica += 1

print("Acabouu!")