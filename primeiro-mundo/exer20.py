from random import randint

lista_alunos = [
    "Iago Silvestre", "Eduardo Basborsa", "Lucas Gabriel", "João Vitor"
]

print("== Ordem de apresentação ==")

for i in lista_alunos:
    aluno = lista_alunos[randint(0, 4)]

    print(f"- {aluno}")


# from random import shuffle

# lista_alunos = [
#     "Iago Silvestre", "Eduardo Basborsa", "Lucas Gabriel", "João Vitor"
# ]

# shuffle(lista_alunos)

# print("== Ordem de apresentação ==")

# for aluno in lista_alunos:
#     print(f"- {aluno}")
