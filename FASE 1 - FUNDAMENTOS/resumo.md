1. Variáveis e Tipos de Dados
Conceito:
Variáveis são "containers" para armazenar dados. Python tem tipagem dinâmica (não declaramos o tipo).

Tipos Básicos:
int: Números inteiros (-3, 0, 42)
float: Números decimais (3.14, -0.001)
str: Texto ("Olá", 'Python')
bool: Valores lógicos (True ou False)

Exemplo:
idade = 30                    # int
altura = 1.75                 # float
nome = "Maria"                # str
estudante = True              # bool

2. Operadores
Aritméticos: +, -, *, /, // (divisão inteira), % (resto), ** (potência)
Comparação: ==, !=, >, <, >=, <=
Lógicos: and, or, not

Exemplo:
a = 10
b = 3
soma = a + b          # 13
divisao_inteira = a // b  # 3
eh_maior = a > b      # True
logico = (a > 5) and (b < 5)  # True

3. Estruturas Condicionais
Conceito: Execute blocos de código com base em condições.

Exemplo:
nota = 85

if nota >= 90:
    print("A")
elif nota >= 70:
    print("B")
else:
    print("C")

4. Loops
for: Itera sobre sequências (lista, string, etc.).
while: Repete enquanto uma condição for verdadeira.

Exemplo:
# For
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

# While
contador = 0
while contador < 3:
    print(contador)
    contador += 1

5. Funções
Conceito: Blocos de código reutilizáveis.

Exemplo:
def calcular_area_retangulo(base, altura):
    area = base * altura
    return area

resultado = calcular_area_retangulo(5, 3)  # 15

6. Estruturas de Dados
Listas: Mutáveis [1, 2, 3]
Tuplas: Imutáveis (1, 2, 3)
Dicionários: Pares chave-valor {"nome": "João", "idade": 25}

Exemplo:
frutas = ["maçã", "banana", "laranja"]  # Lista
coordenadas = (4, 5)                    # Tupla
pessoa = {"nome": "Carlos", "idade": 30} # Dicionário

7. Input/Output
print(): Saída de dados.
input(): Entrada de dados (sempre retorna string).

Exemplo:
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))  # Convertendo para int
print(f"Olá {nome}, você tem {idade} anos.")

