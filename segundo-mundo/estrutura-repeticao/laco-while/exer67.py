while(True):
    try:
        numero = int(input("Digite um número: "))

        for i in range(0, 10 + 1):
            print(f"{i} x {numero} = {i * numero}")

        continuar = input("Deseja continuar (SIM/NÃO): ").lower().strip()

        if continuar not in ("sim", "s", "n", "nao", "não"):
            print("Erro: Opção inválida!")
            continue

        if continuar in ("n", "nao", "não"):
            print("Finalizando programa!")
            break

    except ValueError:
        print("Erro: Digite números válidos!")
        continue