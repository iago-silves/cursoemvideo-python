from random import randint

lista_alunos = [
    "Iago Silvestre", "Eduardo Basborsa", "Lucas Gabriel", "João Vitor"
]

aluno_sorteado = lista_alunos[randint(0, 4)]

print(f"Aluno sorteado: {aluno_sorteado}.")