cidade_santo = input("Digite o nome da sua cidade: ").strip().lower()

if "santo" in cidade_santo:
    resultado = "verdadeiro."
else:
    resultado = "falso."

print(resultado)