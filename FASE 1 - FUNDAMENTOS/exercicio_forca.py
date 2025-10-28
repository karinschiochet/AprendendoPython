"""
📝 **Exercício 13:** Jogo da Forca

Enunciado: Crie uma função jogo_da_forca que implemente o jogo da forca.
A função deve receber a palavra secreta e permitir que o utilizador tente adivinhar letras.

O que esperar:
Palavra: _ _ _ _ _
Tentativas restantes: 6
Digite uma letra: a
Palavra: _ a _ a _
"""

def jogo_da_forca(palavra: str):
    palavra_secreta = list(palavra.strip())
    tamanho = len(palavra_secreta)
    letras_acertadas = ['_' for _ in range(tamanho)]
    tentativas = 6
    while tentativas != 0:
        print(f'Palavra: {" ".join(letras_acertadas)}')
        print(f'Tentativas restantes: {tentativas}')
        tentativas -= 1
        letra = input('Digite uma letra: ').lower()
        if letra in palavra_secreta:
            for i in range(tamanho):
                if palavra_secreta[i] == letra:
                    letras_acertadas[i] = letra
            if '_' not in letras_acertadas:
                print('Parabéns, você acertou!!!')
                break
        if tentativas == 0:
            print(f'Você perdeu!!! A palavra era {palavra}')


jogo_da_forca('abacate')