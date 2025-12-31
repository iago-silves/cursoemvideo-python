from random import randint

jokenpo = [
    "papel",
    "tesoura",
    "pedra"
]

def logica_ganhar(cpu, player):
    if player == "papel" and cpu == "pedra":
        return "Vitória do player!"
    
    elif player == "pedra" and cpu == "tesoura":
        return "Vitória do player!"
    
    elif player == "tesoura" and cpu == "papel":
        return "Vitória do player!"
    
    elif player == "tesoura" and cpu == "pedra":
        return "Vitória da cpu!"

    elif player == "papel" and cpu == "tesoura":
        return "Vitória da cpu!"
    elif player == "pedra" and cpu == "papel":
        return "Vitória da cpu!"
    
    else:
        return "Empate!"

while(True):
    cpu = randint(0, 2)
    player = input("Digite (papel, pedra ou tesoura): ").lower().strip()

    if player not in jokenpo:
        print("Erro: digite uma opção válida.")
    
    vencedor = logica_ganhar(jokenpo[cpu], player)

    print(vencedor)

    continuar = input("Deseja continuar (sim/não): ").lower().strip()

    if continuar != "sim" and continuar != "não":
        print("Erro: digite uma opção válida.")
    
    if continuar == "não":
        break
