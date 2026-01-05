from random import randint

def regra_game(jogador, cpu):
    if jogador % 2 == 0:
        return "vitoria jogador!"
    return "vitoria cpu!"

vitorias = 0

while(True):
    try:
        jogador = int(input("Digite um número: "))
        cpu = randint(0, 11)

        vitoria = regra_game(jogador, cpu)

        if vitoria == "vitoria jogador!":
            print("PARABÉNS!!! GANHOUUUU!")
            vitorias += 1

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

print(f"TOTAL DE VITÓRIAS: {vitorias}.")