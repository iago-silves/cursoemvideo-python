from math import sqrt

def calcular_hipotenusa(cateto_adjacente, cateto_oposto):
    hipotenusa = (cateto_adjacente * cateto_adjacente) + (cateto_oposto * cateto_oposto)

    return sqrt(hipotenusa)


print(f"O valor da hiponusa: {calcular_hipotenusa(3, 4)}")