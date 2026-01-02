peso = []

for i in range(0, 5):
    peso_pessoa = float(input(f"Digite o peso da {i + 1}º pessoa: "))

    peso.append(peso_pessoa)
    
maior = max(peso)
menor = min(peso)

print(f"Maior peso: {maior}.\n"
      f"Menor peso: {menor}.")
