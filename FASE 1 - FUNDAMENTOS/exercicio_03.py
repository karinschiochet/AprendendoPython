"""
Exercício 3: Gerenciador de Listas
Crie um programa que:
1. Permita ao usuário adicionar 5 itens a uma lista.
2. Ordene a lista.
3. Remova o último elemento.
4. Imprima a lista resultante.
"""

lista = []

print("Digite 5 itens:")
for i in range(5):
    item = input(f"Item {i+1}:  ")
    lista.append(item)

lista.sort()
print("lista ordenada:", lista)
lista.pop()
print("lista final: ", lista)

