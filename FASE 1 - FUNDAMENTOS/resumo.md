# 🐍 Tipos de Dados e Operadores em Python - Guia Completo

Conceito:
Variáveis são "containers" para armazenar dados. Python tem tipagem dinâmica (não declaramos o tipo).

## 📊 Tipos de Dados Fundamentais
1. Números Inteiros (int)
`
idade = 25
quantidade = -10
ano = 2024
numero_grande = 1_000_000  # Python ignora underscores (apenas para legibilidade)
print(type(idade))  # <class 'int'>
`

2. Números Decimais (float)
`
preco = 19.99
altura = 1.75
temperatura = -5.5
nota_cientifica = 2.5e-3  # 0.0025
print(type(preco))  # <class 'float'>
`

3. Texto (str)
`
#Diferentes formas de criar strings
nome = "João"
sobrenome = 'Silva'
frase = """Texto
com múltiplas
linhas"""
cidade = '''São Paulo'''
#######
#Operações com strings
nome_completo = nome + " " + sobrenome  # Concatenação
repeticao = "Python " * 3  # "Python Python Python "
tamanho = len(nome)  # 4
print(type(nome))  # <class 'str'>
`

4. Booleanos (bool)
`
#Valores booleanos
verdadeiro = True
falso = False
#######
#Resultados de comparações
maior_de_idade = idade >= 18  # True ou False
tem_nome = bool(nome)  # True se nome não for vazio
print(type(verdadeiro))  # <class 'bool'>
`

🔄 Conversão entre Tipos (Type Casting)

#### Conversão explícita
texto_para_numero = int("123")        # 123 (int)
decimal_para_inteiro = int(3.99)      # 3 (trunca, não arredonda)
numero_para_texto = str(456)          # "456"
float_para_texto = str(3.14)          # "3.14"
numero_para_bool = bool(1)            # True
texto_vazio_para_bool = bool("")      # False

##### Conversão implícita (Python faz automaticamente)
resultado = 5 + 2.5  # 7.5 (int + float = float)

🧮 Operadores Aritméticos

Operadores Básicos
`
a = 10
b = 3
soma = a + b           # 13
subtracao = a - b      # 7
multiplicacao = a * b  # 30
divisao = a / b        # 3.333... (sempre retorna float)
`

Operadores Avançados
`
divisao_inteira = a // b    # 3 (descarta a parte decimal)
resto_divisao = a % b       # 1 (resto da divisão)
potencia = a ** b           # 1000 (10 elevado a 3)
raiz_quadrada = a ** 0.5    # 3.162... (raiz quadrada de 10)
#######
#Operadores com strings
texto1 = "Hello"
texto2 = "World"
concatenacao = texto1 + " " + texto2  # "Hello World"
repeticao = texto1 * 3                # "HelloHelloHello"
`

⚖️ Operadores de Comparação

Sempre retornam True ou False
`
x = 10
y = 5
igual = x == y           # False
diferente = x != y       # True
maior_que = x > y        # True
menor_que = x < y        # False
maior_igual = x >= y     # True
menor_igual = x <= y     # False
#######
#Comparação de strings (ordem alfabética)
"abc" == "abc"     # True
"abc" == "ABC"     # False (case-sensitive)
"apple" < "banana" # True
`

🔌 Operadores Lógicos

and (E lógico)
`
#Ambos devem ser True
tem_idade = idade >= 18
tem_renda = True
pode_financiar = tem_idade and tem_renda  # True apenas se AMBOS forem True
#######
#Tabela verdade do AND
True and True    # True
True and False   # False
False and True   # False
False and False  # False
`
or (OU lógico)
`
#Pelo menos um deve ser True
tem_cartao = False
tem_dinheiro = True
pode_comprar = tem_cartao or tem_dinheiro  # True se PELO MENOS UM for True
#######
#Tabela verdade do OR
True or True    # True
True or False   # True
False or True   # True
False or False  # False`

not (NEGAÇÃO lógica)
`
#Inverte o valor booleano
chovendo = True
nao_chovendo = not chovendo  # False
#######
#Tabela verdade do NOT
not True   # False
not False  # True
`
🎯 Operadores de Identidade e Associação
is e is not (Identidade)
`
#Verificam se são o MESMO objeto na memória
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1
#######
print(lista1 is lista2)     # False (objetos diferentes)
print(lista1 is lista3)     # True (mesmo objeto)
print(lista1 is not lista2) # True`

in e not in (Associação)
`
#Verificam se um elemento está em uma sequência
frutas = ["maçã", "banana", "laranja"]
texto = "Python é incrível"
#######
print("banana" in frutas)        # True
print("uva" not in frutas)       # True
print("Python" in texto)         # True
print("java" not in texto)       # True
`

📝 Operadores de Atribuição
Atribuição Simples
`
x = 10
nome = "Ana"
`
Atribuição Composta
`
contador = 5
contador += 3   # Equivale a: contador = contador + 3 → 8
contador -= 2   # Equivale a: contador = contador - 2 → 6
contador *= 2   # Equivale a: contador = contador * 2 → 12
contador /= 3   # Equivale a: contador = contador / 3 → 4.0
contador //= 2  # Equivale a: contador = contador // 2 → 2.0
contador %= 3   # Equivale a: contador = contador % 3 → 2.0
`

🎪 Precedência de Operadores

Ordem de avaliação (do mais prioritário para o menos):

1. () - Parênteses
2. ** - Exponenciação
3. *, /, //, % - Multiplicação, Divisão, etc.
4. +, - - Adição e Subtração
5. ==, !=, >, <, >=, <= - Comparação
6. not - Negação
7. and - E lógico
8. or - OU lógico

`
resultado = 5 + 3 * 2 ** 2  # 5 + (3 * (2^2)) = 5 + 12 = 17
resultado2 = (5 + 3) * 2 ** 2  # 8 * 4 = 32
`

💡 Dicas Importantes
1. Use parênteses para deixar a ordem clara
2. Teste tipos com type() quando necessário
3. Converta inputs sempre que precisar fazer cálculos
4. Use == para comparação, = é apenas para atribuição
5. Cuidado com comparações de floats devido a imprecisões


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

