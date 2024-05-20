import random
import PySimpleGUI as sg
import os

class Passgen:
    def __init__(self):
        # LAYOUT
        sg.theme('Black')

        # Aba principal
        layout_principal = [
            [sg.Text('Site/Software', size=(15, 1)), sg.Input(key='Site', size=(20, 1))],
            [sg.Text('Email/Usuário', size=(15, 1)), sg.Input(key="Usuario", size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(range(1, 31)), key="Total_chars", default_value=1, size=(3, 1))],
            [sg.Button('Gerar senha')]
        ]

        # Aba de senhas criadas
        layout_senhas_criadas = [
            [sg.Text('Senhas criadas')],
            [sg.Output(size=(50, 10), key='senhas_criadas_output')]
        ]

        # Tabs
        layout = [
            [sg.TabGroup([[sg.Tab('Gerador de Senhas', layout_principal), sg.Tab('Senhas Criadas', layout_senhas_criadas)]])]
        ]

        # Janela
        self.janela = sg.Window("Gerador de senhas", layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar senha':
                nova_senha = self.gerar_senha(valores['Total_chars'])
                site = valores['Site']
                usuario = valores['Usuario']
                # Atualizar a aba de senhas criadas
                self.janela['senhas_criadas_output'].print(f"Site/Software: {site}\nEmail/Usuário: {usuario}\nSenha: {nova_senha}\n")

    def gerar_senha(self, tamanho):
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@$%^&*()'
        rnd = random.SystemRandom()
        senha = ''.join(rnd.choice(chars) for i in range(tamanho))
        return senha

# Cria e inicia o gerador de senhas
gen = Passgen()
gen.Iniciar()