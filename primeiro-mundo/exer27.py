nome = input("digite seu nome completo: ").strip()

primeiro_nome = nome.split()[0]
ultimo_nome = nome.split()[-1]

print(
    f"Primeiro nome: {primeiro_nome}\n"
    f"Ultimo nome: {ultimo_nome}"
)