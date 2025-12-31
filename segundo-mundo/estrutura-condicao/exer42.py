primeiro = int(input("Digite um número: "))
segundo = int(input("Digite um número: "))
terceiro = int(input("Digite um número: "))

maior = primeiro
soma_lados = segundo + terceiro

if segundo > maior:
    maior = segundo
    soma_lados = primeiro + terceiro

if terceiro > maior:
    maior = terceiro
    soma_lados = primeiro + segundo

forma_triagulo = soma_lados > maior

if forma_triagulo:
    equilatero = primeiro == segundo and primeiro == terceiro and segundo == terceiro
    isosceles = primeiro == segundo and primeiro != terceiro or primeiro == terceiro and primeiro != segundo or segundo == terceiro and terceiro != primeiro
    
    if equilatero:
        resultado = "Equilatero."
    elif isosceles:
        resultado = "Isosceles."
    else:
        resultado = "Escaleno."
    
    print(resultado)
    
else:
    print("Não forma triangulo...")