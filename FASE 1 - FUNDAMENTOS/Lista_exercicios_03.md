🧪 Exercícios Práticos

📝 **Exercício 1:** Calculadora de Operações Básicas

Enunciado: Crie uma função chamada calculadora que recebe dois números e uma operação (+, -, *, /) como parâmetros 
e retorna o resultado da operação.

O que esperar:
`print(calculadora(10, 5, '+'))  # Deve retornar 15
print(calculadora(10, 5, '-'))  # Deve retornar 5
print(calculadora(10, 5, '*'))  # Deve retornar 50
print(calculadora(10, 5, '/'))  # Deve retornar 2.0`

📝 **Exercício 2:** Verificador de Número Primo
Enunciado: Crie uma função eh_primo que recebe um número inteiro e 
retorna True se o número for primo, e False caso contrário.

O que esperar:
`print(eh_primo(7))   # Deve retornar True
print(eh_primo(10))  # Deve retornar False
print(eh_primo(2))   # Deve retornar True
print(eh_primo(1))   # Deve retornar False`

📝 **Exercício 3:** Contador de Caracteres
Enunciado: Crie uma função contar_caracteres que recebe 
uma string e retorna um dicionário com a contagem de cada caractere.

O que esperar:
`print(contar_caracteres("python"))
#Deve retornar: {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
print(contar_caracteres("banana"))
#Deve retornar: {'b': 1, 'a': 3, 'n': 2}`

📝 **Exercício 4:** Gerador de Senha Aleatória
Enunciado: Crie uma função gerar_senha que recebe um tamanho (padrão 8) e 
retorna uma senha aleatória contendo letras maiúsculas, minúsculas, números e símbolos.

O que esperar:
`print(gerar_senha(8))   # Deve retornar algo como: "A3b#9zM!"
print(gerar_senha(12))  # Deve retornar algo como: "xY8$kL2#pQ9*"`

📝 **Exercício 5:** Validador de CPF
Enunciado: Crie uma função validar_cpf que recebe uma string com um CPF e 
retorna True se for válido, False caso contrário. Use o algoritmo de validação de CPF brasileiro.

O que esperar:
`print(validar_cpf("123.456.789-09"))  # Deve retornar False
print(validar_cpf("111.444.777-35"))  # Deve retornar True`

📝 **Exercício 6:** Calculadora de Juros Compostos
Enunciado: Crie uma função calcular_juros_compostos que recebe capital inicial, 
taxa de juros (em %), tempo (em meses) e retorna o montante final.

O que esperar:
`print(calcular_juros_compostos(1000, 1, 12))  # ≈ 1126.82
print(calcular_juros_compostos(500, 2, 6))    # ≈ 563.08`

📝 **Exercício 7:** Ordenador de Lista Personalizado
Enunciado: Crie uma função ordenar_personalizado que recebe 
uma lista e uma string com o critério ("crescente", "decrescente", "par_impar") e retorna a lista ordenada.

O que esperar:
`print(ordenar_personalizado([3, 1, 4, 2], "crescente"))    # [1, 2, 3, 4]
print(ordenar_personalizado([3, 1, 4, 2], "decrescente"))  # [4, 3, 2, 1]
print(ordenar_personalizado([3, 1, 4, 2], "par_impar"))    # [2, 4, 1, 3] (pares primeiro)`

📝 **Exercício 8:** Tradutor de Código Morse
Enunciado: Crie uma função para_morse que recebe uma string e retorna a versão em código Morse.

O que esperar:
`print(para_morse("SOS"))        # Deve retornar "... --- ..."
print(para_morse("PYTHON"))     # Deve retornar ".--. -.-- - .... --- -."`

📝 **Exercício 9:** Gerenciador de Tarefas
Enunciado: Crie funções para um gerenciador 
de tarefas: adicionar_tarefa, listar_tarefas, marcar_concluida, remover_tarefa. 
Use uma lista global para armazenar as tarefas.

O que esperar:
`adicionar_tarefa("Estudar Python")
adicionar_tarefa("Fazer exercícios")
listar_tarefas()  # Deve mostrar ambas as tarefas
marcar_concluida(0)
listar_tarefas()  # Deve mostrar a primeira como concluída`

📝 **Exercício 10:** Calculadora de Estatísticas
Enunciado: Crie uma função estatisticas que recebe uma lista de números e 
retorna um dicionário com: média, mediana, moda, valor máximo e mínimo.

O que esperar:
`print(estatisticas([1, 2, 3, 4, 5]))
#Deve retornar: {'media': 3.0, 'mediana': 3, 'moda': None, 'max': 5, 'min': 1}
print(estatisticas([1, 2, 2, 3, 4]))
#Deve retornar: {'media': 2.4, 'mediana': 2, 'moda': 2, 'max': 4, 'min': 1}`

📝 **Exercício 11:** Validador de Data
Enunciado: Crie uma função validar_data que recebe uma string no formato "dd/mm/aaaa" e 
retorna True se for uma data válida, False caso contrário.

O que esperar:
`print(validar_data("29/02/2020"))  # True (ano bissexto)
print(validar_data("29/02/2021"))  # False
print(validar_data("32/01/2023"))  # False`

📝 **Exercício 12:** Compactador de String
Enunciado: Crie uma função compactar_string que recebe uma string e retorna uma versão compactada 
onde sequências de caracteres repetidos são substituídas pelo caractere seguido do número de repetições.

O que esperar:
`print(compactar_string("aaabbbcccaaa"))  # "a3b3c3a3"
print(compactar_string("abcde"))         # "a1b1c1d1e1"`

📝 **Exercício 13:** Jogo da Forca
Enunciado: Crie uma função jogo_da_forca que implemente o jogo da forca. 
A função deve receber a palavra secreta e permitir que o usuário tente adivinhar letras.

O que esperar:
`Palavra: _ _ _ _ _
Tentativas restantes: 6
Digite uma letra: a
Palavra: _ a _ a _`

📝 **Exercício 14:** Conversor de Número Romano
Enunciado: Crie uma função romano_para_decimal que converte números romanos para decimal.

O que esperar:
`print(romano_para_decimal("XIV"))     # 14
print(romano_para_decimal("MMXXIII")) # 2023
print(romano_para_decimal("IX"))      # 9`

📝 **Exercício 15:** Sistema de Biblioteca
Enunciado: Crie funções para gerenciar uma biblioteca: adicionar_livro, emprestar_livro, devolver_livro, listar_livros_disponiveis. Cada livro deve ter título, autor e status (disponível/emprestado).

O que esperar:
`adicionar_livro("Dom Casmurro", "Machado de Assis")
adicionar_livro("1984", "George Orwell")
emprestar_livro("Dom Casmurro")
listar_livros_disponiveis()  # Deve mostrar apenas "1984"`

**Exercício 16:** Verificador de Palíndromo
eh_palindromo(texto)

**Exercício 17:** Gerador de E-mail Corporativo
gerar_email(nome, sobrenome, dominio="empresa.com")
