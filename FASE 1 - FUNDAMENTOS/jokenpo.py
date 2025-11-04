import tkinter as tk
import random
from tkinter import Button, LabelFrame, Label

def escolheu_pedra():
    jokenpo(escolha_usuario='pedra')

def escolheu_papel():
    jokenpo(escolha_usuario='papel')

def escolheu_tesoura():
    jokenpo(escolha_usuario='tesoura')

def jokenpo(escolha_usuario):
    escolha_computador = random.choice(['pedra', 'papel', 'tesoura'])

    if escolha_usuario == escolha_computador:
        mensagem = f'''
            Você: {escolha_usuario.upper()}
            Eu: {escolha_computador.upper()}
            
            Resultado: Empate!!!
        '''
    elif(escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
            (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
            (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        mensagem = f'''
            Você: {escolha_usuario.upper()}
            Eu: {escolha_computador.upper()}
            
            Resultado: Você ganhou!!!
        '''
    else:
        mensagem = f'''
            Você: {escolha_usuario.upper()}
            Eu: {escolha_computador.upper()}

            Resultado: O Computador ganhou!!!
        '''

    resultado.config(text=mensagem)

janela = tk.Tk()

frame = LabelFrame(janela, text='Qual a sua escolha?', padx=10, pady=10)
frame.pack(padx=10, pady=10)

Button(frame, text='Pedra', command=escolheu_pedra).grid(row=1, column=0)
Button(frame, text='Papel', command=escolheu_papel).grid(row=1, column=1)
Button(frame, text='Tesoura', command=escolheu_tesoura).grid(row=1, column=2)

resultado = Label(frame, padx=10, pady=10, justify=tk.LEFT)
resultado.grid(row=2, column=0, columnspan=3)

janela.title("Pedra, Papel ou Tesoura")
janela.geometry("500x200+200+200")

janela.mainloop()
