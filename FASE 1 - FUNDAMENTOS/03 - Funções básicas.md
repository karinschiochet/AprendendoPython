🎯 Funções em Python - Guia Completo

📚 O que são Funções?
Conceito:
Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas ajudam a:

* Organizar o código
* Evitar repetição
* Facilitar a manutenção
* Dividir problemas complexos em partes menores

🏗️ Criando Funções Básicas
Sintaxe Básica:
`def nome_da_funcao(parametros):
    # código da função
    return valor  # opcional`

📋 Exemplos Detalhados
Exemplo 1: Função Simples sem Parâmetros
`
def cumprimentar():
    print("Olá, seja bem-vindo!")
#######
#Chamando a função
cumprimentar()  # Output: Olá, seja bem-vindo!
cumprimentar()  # Podemos chamar quantas vezes quisermos!
`

Exemplo 2: Função com Parâmetros
`
def cumprimentar_pessoa(nome):
    print(f"Olá {nome}, seja bem-vindo!")
#######
#Chamadas diferentes
cumprimentar_pessoa("Alice")      # Olá Alice, seja bem-vindo!
cumprimentar_pessoa("Carlos")     # Olá Carlos, seja bem-vindo!
`

Exemplo 3: Função com Múltiplos Parâmetros
`
def apresentar_pessoa(nome, idade, cidade):
    print(f"Esta é {nome}, tem {idade} anos e mora em {cidade}.")
#######
apresentar_pessoa("Maria", 25, "São Paulo")
#Output: Esta é Maria, tem 25 anos e mora em São Paulo.
`

Exemplo 4: Função com Retorno
`
def somar(a, b):
    resultado = a + b
    return resultado
#######
#Armazenando o resultado
soma = somar(5, 3)
print(soma)  # 8
#######
#Usando diretamente
print(somar(10, 20))  # 30`

Exemplo 5: Função com Múltiplos Retornos
`
def calcular_operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    return soma, subtracao, multiplicacao, divisao
#######
#Recebendo todos os resultados
resultados = calcular_operacoes(10, 2)
print(resultados)  # (12, 8, 20, 5.0)
#######
#Desempacotando os resultados
s, sub, mult, div = calcular_operacoes(10, 2)
print(f"Soma: {s}")           # Soma: 12
print(f"Subtração: {sub}")    # Subtração: 8
print(f"Multiplicação: {mult}") # Multiplicação: 20
print(f"Divisão: {div}")      # Divisão: 5.0`

🎛️ Tipos de Parâmetros
1. Parâmetros Posicionais
`def criar_usuario(nome, email, idade):
    usuario = {
        "nome": nome,
        "email": email,
        "idade": idade
    }
    return usuario
#######
#Os argumentos devem estar na ordem correta
usuario1 = criar_usuario("Ana", "ana@email.com", 30)
`
2. Parâmetros Nomeados (Keyword Arguments)
`
#Podemos especificar os parâmetros pelo nome
usuario2 = criar_usuario(idade=25, nome="Carlos", email="carlos@email.com")`

3. Parâmetros com Valores Padrão
`
def cumprimentar_com_horario(nome, horario="dia"):
    print(f"Bom {horario}, {nome}!")
#######
#Usando valor padrão
cumprimentar_com_horario("Maria")           # Bom dia, Maria!
#######
#Sobrescrevendo o valor padrão
cumprimentar_com_horario("João", "tarde")   # Bom tarde, João!
cumprimentar_com_horario("Ana", "noite")    # Bom noite, Ana!`

4. Parâmetros Arbitrários (*args)
`
def somar_tudo(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total
#######
print(somar_tudo(1, 2, 3))        # 6
print(somar_tudo(10, 20, 30, 40)) # 100
print(somar_tudo(5))              # 5
`
5. Parâmetros Arbitrários Nomeados (kwargs)**
`
def criar_perfil(**informacoes):
    perfil = {}
    for chave, valor in informacoes.items():
        perfil[chave] = valor
    return perfil
#######
perfil1 = criar_perfil(nome="Ana", idade=25, cidade="Rio")
perfil2 = criar_perfil(nome="Lucas", profissao="Engenheiro")
#######
print(perfil1)  # {'nome': 'Ana', 'idade': 25, 'cidade': 'Rio'}
print(perfil2)  # {'nome': 'Lucas', 'profissao': 'Engenheiro'}`

🔄 Escopo de Variáveis
Variáveis Locais vs Globais
`variavel_global = "Eu sou global"
#######
def funcao_exemplo():
    variavel_local = "Eu sou local"
    print(variavel_local)   # Acessa a variável local
    print(variavel_global)  # Acessa a variável global
#######
funcao_exemplo()
#print(variavel_local)  # ERRO! variável_local não existe fora da função`

Modificando Variável Global (não recomendado)
`contador = 0
def incrementar():
    global contador  # Declara que vamos usar a variável global
    contador += 1
#######
print(f"Antes: {contador}")  # Antes: 0
incrementar()
print(f"Depois: {contador}") # Depois: 1`

🎪 Funções como Cidadãos de Primeira Classe

Funções podem ser atribuídas a variáveis
`def multiplicar(a, b):
    return a * b
#######
#Atribuindo função a uma variável
minha_funcao = multiplicar
print(minha_funcao(5, 3))  # 15`

Funções podem ser passadas como argumentos
`def aplicar_operacao(a, b, operacao):
    return operacao(a, b)
#######
def somar(x, y):
    return x + y
#######
def subtrair(x, y):
    return x - y
#######
print(aplicar_operacao(10, 5, somar))     # 15
print(aplicar_operacao(10, 5, subtrair))  # 5`

💡 Boas Práticas com Funções
1. Nomes Descritivos
2. Funções Pequenas e Específicas
3. Documentação com Docstrings
4. Valores Padrão Apropriados

🎯 Próximos Passos

* Pratique criando funções para problemas do dia a dia
* Experimente com diferentes tipos de parâmetros
* Combine funções para construir programas mais complexos
* Estude funções built-in do Python como map(), filter(), e reduce()