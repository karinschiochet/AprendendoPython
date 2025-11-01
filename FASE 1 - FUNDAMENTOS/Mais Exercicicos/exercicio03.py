"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

"""
import math
tamanho = float(input("Tamanho a ser pintado em metros quadrados: "))

valor_lata = 80.00
litros_por_metro = 1.0 / 3.0
litros_necessarios = tamanho * litros_por_metro
latas_necessarias = math.ceil(litros_necessarios / 18.00)

print(f"Foi necessário {latas_necessarias} latas de tinta, custando R$ {latas_necessarias * valor_lata:.2f}")
