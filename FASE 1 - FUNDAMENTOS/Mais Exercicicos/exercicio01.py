limite = 50
multa = 4.00

peso = int(input("Digite o peso do peixe: "))

excesso = (peso - limite) if peso > limite else 0
multa = excesso * multa

if excesso > 0:
    print(f"O peixe excedeu o limite de {limite}kg e foi multado em R${multa:.2f}")
else:
    print("Não foi multado")