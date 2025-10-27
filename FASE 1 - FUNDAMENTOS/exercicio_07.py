"""
Exercício 7: Validador de Email Simples
# Verifica se tem @ e .
"""

def valida_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False

email = input('Informe um email: ')
# print(f"Este e-mail é valido: {valida_email(email)}")
print("Este e-mail é valido: {}".format(valida_email(email)))