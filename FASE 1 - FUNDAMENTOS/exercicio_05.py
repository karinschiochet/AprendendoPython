"""
Exercício 5: Validador de Senha
Crie uma função que:
1. Receba uma senha.
2. Verifique se tem pelo menos 8 caracteres.
3. Contenha pelo menos um número e uma letra maiúscula.
4. Retorne True ou False.
"""

def valida_senha(senha):
    tamanho = True if len(senha) >= 8 else False
    tem_numero = False
    tem_maiuscula = False
    tem_caracteres_especiais = False
    caracter_especial = ['@', '#', '$', '%', '&', '*', '_', '=']
    if tamanho:
        for i in senha:
            if i.isdigit():
                tem_numero = True
            elif i.isupper():
                tem_maiuscula = True
            elif i in caracter_especial:
                tem_caracteres_especiais = True
        if tem_numero and tem_maiuscula and tem_caracteres_especiais:
            return True
        else:
            return False
    else:
        return False

senha = input("Digite sua senha: ")
print("Senha é válida? ", valida_senha(senha))
