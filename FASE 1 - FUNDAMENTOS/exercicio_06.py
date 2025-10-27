"""
Exercício 6: Calculadora de IMC
# Calcule o Índice de Massa Corporal
# IMC = peso / (altura ** 2)
"""


def classificar_imc():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    imc = peso / (altura ** 2)

    print(f"\nSeu IMC é: {imc:.2f}")

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    elif imc < 35:
        classificacao = "Obesidade Grau I"
    elif imc < 40:
        classificacao = "Obesidade Grau II"
    else:
        classificacao = "Obesidade Grau III"

    print(f"Classificação: {classificacao}")

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura ** 2)

print(f"O IMC calculado é: {imc:.2f}")
classificar_imc()