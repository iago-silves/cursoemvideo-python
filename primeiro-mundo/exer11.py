largula = float(input("Digite a largura em metros (m²) da parede: "))
altura = float(input("Digite a altura em metros (m²) da parede: "))

# Um litro de tinta pinta 2 metros
area_ser_pintada = largula * altura

# Quantidade necessaria de tinta
quantidade_tinta = (area_ser_pintada / 2)

print(f"A quantidade de tinta necessária para pintar uma área de {area_ser_pintada} é {quantidade_tinta} litros.")