def pagar_produto(forma_pagamento, preco):
    if preco <= 0:
        return "Erro: Preco inválido."
    
    if forma_pagamento == "dinheiro":
        return preco - (preco * 0.1)
    elif forma_pagamento == "cartao_credito_vista":
        return preco - (preco * 0.05)
    elif forma_pagamento == "cartao_credito_parcelar_2":
        return preco
    elif forma_pagamento == "cartao_credito_parcelar_3":
        return preco + (preco * 0.2)
    else:
        return "Erro: forma de pagamento inválida."

print(pagar_produto("dinheiro", 200))
print(pagar_produto("cartao_credito_vista", 200))
print(pagar_produto("cartao_credito_parcelar_2", 200))
print(pagar_produto("cartao_credito_parcelar_3", 200))
print(pagar_produto("xerecard", 200))