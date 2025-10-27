"""
Exercício 4: Dicionário de Contatos
Desenvolva um sistema simples de contatos onde:
1. O usuário pode adicionar nome e telefone.
2. Consulte contatos pelo nome.
3. Liste todos os contatos.
"""

contatos = {}

opcao = ""

while opcao != "0":
    opcao = input(
        "1 - Adicionar contato\n"
        "2 - Consultar contato\n"
        "3 - Listar contatos\n"
        "0 - Sair\n"
        "Informe a opção desejada: ")
    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        contatos[nome] = telefone
        print("Contato adicionado com sucesso!")
    elif opcao == "2":
        nome = input("Nome: ")
        if nome in contatos:
            print(f"Telefone: {contatos[nome]}")
        else:
            print(f"O nome {nome} não foi encontrado.")
    elif opcao == "3":
        for nome, telefone in contatos.items():
            print(f"{nome}: {telefone}")
    elif opcao == "0":
        break

print("Saindo...")