"""
Exercício 2: Analisador de Números
Escreva um programa que:
1. Receba um número do usuário.
2. Verifique se é par ou ímpar.
3. Informe se é positivo, negativo ou zero.
4. Calcule seu quadrado."""

numero = int(input('Informe um numero: '))

par_impar = 'Par' if numero % 2 == 0 else 'Impar'
positivo_negativo_zero = 'Positivo' if numero > 0 else 'Negativo' if numero < 0 else 'Zero'

print(f'O numero informado é {par_impar}')
print(f'O numero informado é {positivo_negativo_zero}')
print(f"O numero {numero} elevado ao quadrado é: {numero ** 2}")

