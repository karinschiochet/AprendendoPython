🔄 Estruturas Condicionais e Loops em Python - Guia Completo
Vamos explorar como controlar o fluxo do seu programa com condições e repetições!

🎯 Estruturas Condicionais (if/elif/else)

**Conceito Fundamental:**
As estruturas condicionais permitem que seu programa tome decisões baseadas em condições.

Sintaxe Básica:
`if condicao1:
    # Executa se condicao1 for True
elif condicao2:
    # Executa se condicao1 for False E condicao2 for True
else:
    # Executa se todas as condições forem False`

📋 Exemplos Detalhados

Exemplo 1: Verificação Básica de Idade
`idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade!")
    print("Pode votar e dirigir.")
elif idade >= 16:
    print("Você é adolescente.")
    print("Pode votar, mas não dirigir.")
else:
    print("Você é menor de idade.")
    print("Não pode votar nem dirigir.")`

Exemplo 2: Sistema de Notas
`nota = float(input("Digite sua nota (0-100): "))
#######
if nota >= 90:
    conceito = "A"
    mensagem = "Excelente!"
elif nota >= 80:
    conceito = "B"
    mensagem = "Muito bom!"
elif nota >= 70:
    conceito = "C" 
    mensagem = "Bom!"
elif nota >= 60:
    conceito = "D"
    mensagem = "Precisa melhorar."
else:
    conceito = "F"
    mensagem = "Reprovado."
#######
print(f"Conceito: {conceito}")
print(f"Mensagem: {mensagem}")`

Exemplo 3: Múltiplas Condições com Operadores Lógicos
`tem_carteira = True
tem_carro = False
idade = 17
#######
#Usando and, or, not
if idade >= 18 and tem_carteira:
    print("Pode dirigir legalmente!")
elif idade >= 16 and tem_carteira and tem_carro:
    print("Pode praticar com supervisão")
else:
    print("Não pode dirigir")
#######
#Verificando se NÃO tem algo
if not tem_carro:
    print("Você precisa de um carro para dirigir")`

Exemplo 4: Condições Aninhadas
`numero = int(input("Digite um número: "))
#######
if numero > 0:
    print("Número positivo")
    if numero % 2 == 0:
        print("e par")
    else:
        print("e ímpar")
elif numero < 0:
    print("Número negativo")
else:
    print("Número zero")`

Exemplo 5: Condição em Uma Linha (Operador Ternário)
`idade = 20
status = "maior" if idade >= 18 else "menor"
print(f"Você é {status} de idade")
#######
#Equivale a:
if idade >= 18:
    status = "maior"
else:
    status = "menor"`

🔁 Loops (for e while)

**Conceito:**
Loops permitem repetir blocos de código múltiplas vezes.

🔄 Loop FOR

Quando usar: Quando você sabe quantas vezes quer repetir ou quer iterar sobre uma sequência.
Sintaxe:
`for variavel in sequencia:
    # código a repetir`

Exemplos com FOR:
Exemplo 1: Iterando sobre uma Lista
`frutas = ["maçã", "banana", "laranja", "uva"]
#######
print("Lista de frutas:")
for fruta in frutas:
    print(f"- {fruta}")
#######
#Com enumerate para pegar índice e valor
for indice, fruta in enumerate(frutas):
    print(f"Fruta {indice + 1}: {fruta}")`

Exemplo 2: Usando range()
`# range(stop) - 0 até stop-1
print("Contagem de 0 a 4:")
for i in range(5):
    print(i)
#######
#range(start, stop) - start até stop-1  
print("\nContagem de 2 a 6:")
for i in range(2, 7):
    print(i)
#######
#range(start, stop, step) - com passo
print("\nNúmeros pares de 0 a 10:")
for i in range(0, 11, 2):
    print(i)
#######
print("\nContagem regressiva de 5 a 1:")
for i in range(5, 0, -1):
    print(i)`

Exemplo 3: Iterando sobre String
`palavra = "Python"
#######
print("Letras da palavra:")
for letra in palavra:
    print(letra)
#######
#Com índice
for indice, letra in enumerate(palavra):
    print(f"Posição {indice}: '{letra}'")`

Exemplo 4: Iterando sobre Dicionário
`pessoa = {
    "nome": "Carlos",
    "idade": 25,
    "cidade": "São Paulo"
}
#######
print("Informações da pessoa:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
#######
#Apenas chaves
for chave in pessoa.keys():
    print(chave)
#######
#Apenas valores
for valor in pessoa.values():
    print(valor)`

🔁 Loop WHILE

Quando usar: Quando você quer repetir enquanto uma condição for verdadeira (número de repetições desconhecido).
Sintaxe:
`while condicao:
    # código a repetir`

Exemplos com WHILE:

Exemplo 1: Contador Básico
`contador = 1
#######
while contador <= 5:
    print(f"Contagem: {contador}")
    contador += 1  # IMPORTANTE: Não esqueça de atualizar a variável!
#######
print("Fim da contagem!")`

Exemplo 2: Menu Interativo
`opcao = ""
#######
while opcao != "sair":
    print("\n=== MENU ===")
    print("1 - Cadastrar")
    print("2 - Listar") 
    print("sair - Sair")
    #######
    opcao = input("Escolha uma opção: ").lower()
    #######
    if opcao == "1":
        print("Cadastrando...")
    elif opcao == "2":
        print("Listando...")
    elif opcao == "sair":
        print("Saindo do sistema...")
    else:
        print("Opção inválida!")`

Exemplo 3: Validação de Entrada
`numero_valido = False
#######
while not numero_valido:
    try:
        numero = int(input("Digite um número entre 1 e 10: "))
        if 1 <= numero <= 10:
            numero_valido = True
            print(f"Número válido: {numero}")
        else:
            print("Número fora do intervalo!")
    except ValueError:
        print("Por favor, digite um número inteiro!")`


Exemplo 4: Loop Infinito Controlado
`import time
#######
contador = 0
executando = True
#######
while executando:
    print(f"Executando... ciclo {contador + 1}")
    contador += 1
    #######
    if contador >= 5:
        executando = False
    #######
    time.sleep(1)  # Pausa de 1 segundo
#######
print("Loop finalizado!")`

🎪 Controle de Loops: break e continue

**break:** Sai completamente do loop
**continue:** Pula para a próxima iteração

Exemplo 1: Usando break
`print("Procurando o número 5:")
for i in range(1, 11):
    if i == 5:
        print("Número 5 encontrado! Parando...")
        break
    print(i)`

Exemplo 2: Usando continue
`print("Números ímpares de 1 a 10:")
for i in range(1, 11):
    if i % 2 == 0:  # Se for par
        continue    # Pula para a próxima iteração
    print(i)`

Exemplo 3: break com while
`while True:  # Loop infinito
    senha = input("Digite a senha: ")
    #######
    if senha == "python123":
        print("Acesso concedido!")
        break
    else:
        print("Senha incorreta! Tente novamente.")`