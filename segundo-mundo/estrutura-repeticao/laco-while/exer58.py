from random import randint

quantidade_tentativas = 0

while(True):
    try:
        computador_pense = randint(0, 10)

        adivinhar_numero = int(input("Digite o número digitado pelo computador: "))

        quantidade_tentativas += 1

        if computador_pense != adivinhar_numero:
            resultado = "ERROUUU!"
        else: 
            resultado = "ACERTOUU!"
            break

        print(resultado)

        continuar = input("Deseja continuar (s/n): ").strip().lower()

        if continuar not in ("s", "n"):
            print("Erro: opção inválida!")
            continue
    
    except ValueError:
        print("Erro: Digite um número válido.")


print(f"A quantidade de tentativas: {quantidade_tentativas}.")