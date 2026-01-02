funcionar = True

while(funcionar):
    while(True):
        try:
            num1 = int(input("Digite um numero: "))
            num2 = int(input("Digite outro numero: "))
            break

        except ValueError:
            print("Erro: digite um número válido!")
            continue
    
    while(True):
        print(
            "\nMenu:\n"
            "1. Somar\n"
            "2. Multiplicar\n"
            "3. Maior valor\n"
            "4. Novos números\n"
            "5. Sair do programa\n"
        )

        opcao = input("Escolha uma opção: ").lower().strip()

        if opcao not in ("1", "2", "3", "4", "5"):
            print("Erro: opção inválida!")
            continue

        if opcao == "1":
            resultado = num1 + num2

        elif opcao == "2":
            resultado = num1 * num2

        elif opcao == "3":

            if num1 > num2:
                resultado = num1
            else:
                resultado = num2
            
        elif opcao == "4":
            print("== Escolha novamente os numeros ==")
            break

        else:
            print("Obrigado por usar este programa!")
            funcionar = False
        
        print(resultado)
