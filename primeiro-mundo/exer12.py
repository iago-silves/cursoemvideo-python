def calcular_desconto(nome, preco, desconto_aplicado=0.05):
    return {
        "nome": nome,
        "preco_atualizado": preco - (preco * desconto_aplicado)
    }

nome_produto = input("Digite o nome do produto: ").title().strip()
preco_produto = float(input("Digite o preco do produto: "))

desconto_produto = calcular_desconto(nome_produto, preco_produto)

print(
    f"O produto {desconto_produto['nome']} está com preço atual de {desconto_produto['preco_atualizado']}."
)