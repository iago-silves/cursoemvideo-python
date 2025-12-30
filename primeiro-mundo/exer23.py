def digitos_separados(unidade=0, dezena=0, centena=0, milhar=0):
    return {
        "unidade": unidade,
        "dezena": dezena,
        "centena": centena,
        "milhar": milhar
    }

try:
    numero = input("Digite um número: ")

    numero_inteiro = int(numero)

    if numero_inteiro < 0 or numero_inteiro > 9999:
        print("Erro: digite um número de 0 a 9999...")

    digitos_numericos = digitos_separados(str(numero_inteiro)[0], str(numero_inteiro)[1], str(numero_inteiro)[2], str(numero_inteiro)[3])


    print(
        f"Unidade: {digitos_numericos['unidade']}\n"
        f"Dezena: {digitos_numericos['dezena']}\n"
        f"Centena: {digitos_numericos['centena']}\n"
        f"Milhar: {digitos_numericos['milhar']}"
    )

except ValueError:
    print("Erro: digite um número válido...")


# try:
#     numero = int(input("Digite um número de 0 a 9999: "))

#     if numero < 0 or numero > 9999:
#         print("Erro: digite um número de 0 a 9999.")
#     else:
#         unidade = numero % 10
#         dezena = (numero // 10) % 10
#         centena = (numero // 100) % 10
#         milhar = numero // 1000

#         print(
#             f"Unidade: {unidade}\n"
#             f"Dezena: {dezena}\n"
#             f"Centena: {centena}\n"
#             f"Milhar: {milhar}"
#         )

# except ValueError:
#     print("Erro: digite um número válido.")
