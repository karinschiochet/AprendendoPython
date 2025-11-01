📚 Listas, Tuplas e Dicionários em Python - Guia Completo
Vamos explorar as três estruturas de dados mais importantes do Python!

🧩 1. LISTAS
Conceito:
Listas são coleções ordenadas, mutáveis e que permitem elementos duplicados.

Características:
✅ Ordenada (mantém a ordem de inserção)

✅ Mutável (pode ser alterada após criação)

✅ Permite elementos duplicados

✅ Pode conter diferentes tipos de dados

Sintaxe:
minha_lista = [elemento1, elemento2, elemento3]

Operações Principais:
Criação e Acesso:
`# Criando listas
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
mista = [1, "texto", 3.14, True]
vazia = []
#######
#Acessando elementos
print(frutas[0])    # "maçã" (primeiro elemento)
print(frutas[-1])   # "laranja" (último elemento)
print(frutas[1:3])  # ["banana", "laranja"] (slice)`

Modificando Listas:
`
frutas = ["maçã", "banana", "laranja"]
#######
#Adicionando elementos
frutas.append("uva")           # Adiciona no final
frutas.insert(1, "morango")    # Insere na posição 1
frutas.extend(["kiwi", "pêssego"])  # Adiciona múltiplos
#######
#Removendo elementos
frutas.remove("banana")        # Remove pelo valor
frutas.pop(1)                  # Remove pelo índice e retorna
frutas.pop()                   # Remove o último
del frutas[0]                  # Remove pelo índice
#######
#Modificando
frutas[1] = "abacaxi"          # Altera elemento
`

Métodos Úteis:
`
numeros = [3, 1, 4, 1, 5, 9, 2]
#######
print(len(numeros))            # 7 - tamanho da lista
print(numeros.count(1))        # 2 - conta ocorrências
print(numeros.index(4))        # 2 - índice do elemento
#######
numeros.sort()                 # Ordena a lista
numeros.reverse()              # Inverte a ordem
copia = numeros.copy()         # Cria cópia
numeros.clear()                # Esvazia a lista
`

List Comprehension:
`#Criar lista com padrão
quadrados = [x**2 for x in range(5)]          # [0, 1, 4, 9, 16]
pares = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
#######
#Transformar elementos
nomes = ["ana", "joão", "maria"]
maiusculos = [nome.upper() for nome in nomes]  # ["ANA", "JOÃO", "MARIA"]`

🔒 2. TUPLAS
Conceito:
Tuplas são coleções ordenadas, imutáveis e que permitem elementos duplicados.

Características:
✅ Ordenada (mantém a ordem)

❌ IMUTÁVEL (não pode ser alterada após criação)

✅ Permite elementos duplicados

✅ Mais eficiente que listas para dados fixos

Sintaxe:
`minha_tupla = (elemento1, elemento2, elemento3)
#ou sem parênteses
minha_tupla = elemento1, elemento2, elemento3
`
Operações Principais:
Criação e Acesso:
`
#Criando tuplas
coordenadas = (4, 5)
cores = ("vermelho", "verde", "azil")
um_elemento = (1,)              # IMPORTANTE: vírgula necessária
vazia = ()
#######
#Acessando elementos (igual às listas)
print(coordenadas[0])           # 4
print(cores[1:])                # ("verde", "azil")
`

Métodos Disponíveis:
`
numeros = (1, 2, 2, 3, 4, 2)
#######
print(numeros.count(2))         # 3 - conta ocorrências
print(numeros.index(3))         # 3 - índice do elemento
print(len(numeros))             # 6 - tamanho
`

Desempacotamento:
`
#Desempacotar tupla
ponto = (10, 20)
x, y = ponto                    # x = 10, y = 20
#######
#Trocar valores sem variável temporária
a, b = 5, 10
a, b = b, a                     # a = 10, b = 5
#######
#Retornar múltiplos valores de função
def operacoes(a, b):
    return a + b, a - b, a * b
#######
soma, diferenca, produto = operacoes(10, 5)`

🗂️ 3. DICIONÁRIOS
Conceito:
Dicionários são coleções não ordenadas (até Python 3.6), mutáveis e indexadas por chaves únicas.

Características:
✅ Chave-Valor (pares)
✅ Mutável
✅ Chaves devem ser únicas e imutáveis
✅ Valores podem ser de qualquer tipo

Sintaxe:
`meu_dict = {
    "chave1": "valor1",
    "chave2": "valor2"
}`

Operações Principais:
Criação e Acesso:
`
#Criando dicionários
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}
#######
produto = dict(nome="Notebook", preco=2500, estoque=10)
#######
#Acessando valores
print(pessoa["nome"])           # "João"
print(pessoa.get("idade"))      # 30
print(pessoa.get("email", "Não informado"))  # Valor padrão
`

Modificando Dicionários:
`
pessoa = {"nome": "Maria", "idade": 25}
#######
#Adicionando/alterando
pessoa["idade"] = 26            # Altera valor
pessoa["email"] = "maria@email.com"  # Adiciona novo
pessoa.update({"cidade": "Rio", "idade": 27})  # Múltiplas
#######
#Removendo
email = pessoa.pop("email")     # Remove e retorna valor
del pessoa["cidade"]            # Remove
pessoa.clear()                  # Esvazia dicionário
`

Métodos Úteis:
`
pessoa = {"nome": "Carlos", "idade": 35, "cidade": "Belo Horizonte"}
#######
print(pessoa.keys())            # dict_keys(['nome', 'idade', 'cidade'])
print(pessoa.values())          # dict_values(['Carlos', 35, 'Belo Horizonte'])
print(pessoa.items())           # dict_items([('nome', 'Carlos'), ...])
#######
print("nome" in pessoa)         # True - verifica chave
print(len(pessoa))              # 3 - número de pares
`

Iterando sobre Dicionários:
`
aluno = {"nome": "Ana", "nota1": 8.5, "nota2": 7.0, "nota3": 9.0}
#######
#Por chaves
for chave in aluno:
    print(f"{chave}: {aluno[chave]}")
#######
#Por itens (chave e valor)
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
#######
#Apenas valores
for valor in aluno.values():
    print(valor)
`

Dictionary Comprehension:
`
#Criar dicionário com padrão
quadrados = {x: x**2 for x in range(5)}        # {0:0, 1:1, 2:4, 3:9, 4:16}
#######
#Filtrar elementos
notas = {"mat": 8, "port": 6, "cien": 9, "hist": 5}
aprovados = {materia: nota for materia, nota in notas.items() if nota >= 7}
#{'mat': 8, 'cien': 9}
`

🔄 Comparação entre as Estruturas
Característica	    Listas	    Tuplas	    Dicionários
Ordenada	        ✅ Sim	    ✅ Sim	    ❌ Não (até 3.6) / ✅ Sim (3.7+)
Mutável	            ✅ Sim	    ❌ Não	    ✅ Sim
Indexação	        Por índice	Por índice	Por chave
Permite duplicatas	✅ Sim	    ✅ Sim	    ❌ Chaves: Não / ✅ Valores: Sim
Uso comum	        Dados que mudam	Dados fixos	Dados nomeados
