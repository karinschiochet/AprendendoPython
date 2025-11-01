"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato,

Faça um programa que nos dê:
* salário bruto.
* quanto pagou ao INSS.
* quanto pagou ao sindicato.
* o salário líquido.

calcule os descontos e o salário líquido, conforme mostrado abaixo:

+ Salário Bruto: R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato (5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.

"""

valor_por_hora = float(input("Quanto ganha por hora trabalhada: "))
quantidade_horas_trabalhadas = int(input("Quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_por_hora * quantidade_horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print(f"""
+ Salário Bruto: R$ {salario_bruto:.2f}
- IR (11%) : R$ {ir:.2f}
- INSS (8%) : R$ {inss:.2f}
- Sindicato (5%) : R$ {sindicato:.2f}
= Salário Liquido : R$ {salario_liquido:.2f}
""")
