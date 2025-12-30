variavel = input("Digite uma variavel: ")

print(
      f"O tipo da variavel: {type(variavel)}\n"
      f"Contém espaços: {variavel.isspace()}\n"
      f"Trata-se de valor númerico: {variavel.isnumeric()}\n"
      f"Trata-se de uma letra: {variavel.isalpha()}\n"
      f"Trata-se de um dado alfanumerico: {variavel.isalnum()}\n"
      f"Contém letras maisculas: {variavel.isupper()}\n"
      f"Contém letras minusculas: {variavel.islower()}\n"
      )