primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
decimo_termo = 10

prog_aritmetrica = primeiro_termo + (decimo_termo - 1) * razao

for i in range(primeiro_termo, prog_aritmetrica + 1, razao):
    print(f"{i}", end=" → ")
print("ACABOUUU")