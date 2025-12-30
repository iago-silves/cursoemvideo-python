nome = input("digite seu nome completo: ").strip()

remover_espacos = nome.replace(" ", "")
contar_letras = len(remover_espacos)

letras_primeiro_nome = nome.split()[0]

print(
    f"O nome em maiúsculas: {nome.upper()}\n"
    f"O nome em minúsculas: {nome.lower()}\n"
    f"A quantidade de letras ao todo: {contar_letras}\n"
    f"A quantidade de letras do primeiro nome: {len(letras_primeiro_nome)}"
)