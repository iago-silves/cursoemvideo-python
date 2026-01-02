def verificar_sexo(sexo):
    while(True):
        if sexo not in ("M", "F"):
            return "Erro: Dado inválido!"
        return "Dados cadastrados com sucesso!"




print(verificar_sexo("M"))
print(verificar_sexo("F"))
print(verificar_sexo("j"))
print(verificar_sexo("k"))
print(verificar_sexo("l"))
print(verificar_sexo("F"))