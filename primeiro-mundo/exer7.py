def media_aluno(nota1, nota2):
    return (nota1 + nota2) / 2

nome = input("Digite o nome do aluno: ").title().strip()

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

print(
    f"Aluno: {nome}\n"
    f"Média: {media_aluno(nota1, nota2)}"
)