palavra = input("Digite um nome: ").strip().lower()

palavra_sem_espacos = palavra.replace(" ", "")
palavra_reversa = palavra_sem_espacos[::-1]

if palavra_sem_espacos == palavra_reversa:
    resultado = f"A palavra {palavra} é um palíndromos."
else:
    resultado = f"A palavra {palavra} não é um palíndromos."

print(resultado)
    