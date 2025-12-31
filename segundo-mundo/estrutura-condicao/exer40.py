def situacao_aluno(nota_aluno):
    if nota_aluno < 0 or nota_aluno > 10:
        return "Nota inválida."
    
    if nota_aluno < 5:
        return "Reprovado."
    elif nota_aluno < 7:
        return "Recuperação."
    else:
        return "Aprovado."
    

print(situacao_aluno(10))