total_compras = 0
produto_caro = 0
produto_barato = 0
nome_produto_barato = ""
controler = 0

while(True):
    try:
        nome_produto = input("Digite o nome do produto: ").strip().title()
        valor_produto = float(input("Digite o preço do produto: "))

        continuar = input("Deseja continuar (SIM/NÂO): ").strip().lower()

        if continuar not in ("sim", "s", "n", "nao", "não"):
            print("Erro: Opção inválida!")
            continue

        controler += 1

        if controler == 1:
            produto_caro = valor_produto
            produto_barato = valor_produto

            if produto_barato:
                nome_produto_barato = nome_produto
        else:
            if valor_produto > produto_caro:
                produto_caro = valor_produto
            
            if valor_produto < produto_barato:
                produto_barato = valor_produto
                nome_produto_barato = nome_produto

        total_compras += valor_produto


        if continuar in ("n", "nao", "não"):
            print("Finalizando programa!")
            break

    except ValueError:
        print("Erro: Valor inválido, tente novamente!")
        continue 

print(f"O total da compra foi: R$ {total_compras}\n"
      f"O produto mais barato foi {nome_produto_barato} que custa {produto_barato}")