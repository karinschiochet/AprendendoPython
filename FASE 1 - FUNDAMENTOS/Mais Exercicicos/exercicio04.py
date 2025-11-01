"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao utilizador as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

* comprar apenas latas de 18 litros;
* comprar apenas galões de 3,6 litros;
* misturar latas e galões, de forma que o desperdício de tinta seja menor.
* Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
from math import ceil
tamanho = float(input("Tamanho a ser pintado em metros quadrados: "))

cobertura_tinta = 1.0 / 6.0
latao_quantidade = 18.00
latao_valor = 80.00
galao_quantidade = 3.60
galao_valor = 25.00

litros_necessarios = tamanho * cobertura_tinta
litros_necessarios += litros_necessarios * 0.10
latas_necessarias = ceil(litros_necessarios / latao_quantidade)
galoes_necessarios = ceil(litros_necessarios / galao_quantidade)

if litros_necessarios >= latao_quantidade:
    latas = litros_necessarios / latao_quantidade
    latas_restantes = litros_necessarios % latao_quantidade
    galoes = ceil(latas_restantes / galao_quantidade)

    print(f"""
    Litros necessários: {litros_necessarios} 
    Quantidade de Latas: {latas_necessarias} | Custo: {latas_necessarias * latao_valor}
    Quantidade de Galões: {galoes_necessarios} | Custo: {galoes_necessarios * galao_valor}
    Latas: {latas} | Galão: {galoes} | Custo: {latas * latao_valor + galoes * galao_valor}
    """)