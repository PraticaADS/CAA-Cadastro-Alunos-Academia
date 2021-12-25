# @title Texto de título padrão { display-mode: "code" }

import getpass
from sys import maxsize
from tkinter.constants import CENTER
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import ButtonMenu, Window, popup
import bd

from datetime import datetime
import calendar as cal
fnt = 'Arial 12'


nome = ""
senha = ""
tema = "Claro", "Escuro"

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Tela Login


def janela_login():
    sg.theme("SystemDefault")
    login = [
        [sg.Text("Digite seu usuario"), sg.Input(
            nome, key='nome', focus=True)],
        [sg.Text("Digite sua senha  "), sg.Input(senha, key='senha', password_char='*')
         ], [sg.Text("Tema                  "), sg.Combo(default_value="Claro", values=tema, size=(20, 30), key='escolha', readonly=True, expand_x=False)],
        [sg.Text("=====================================================================")],
        [sg.Text("     "), sg.Button('Entrar', expand_x=True, border_width=3, ), sg.Text(
            "     "), sg.Button('  Sair  ', expand_x=True, border_width=3), sg.Text("     "), ]
    ]

    return sg.Window('Tela Login', layout=login, finalize=True, size=(300, 150))


# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Tela menu principal adm
def janelamenuadm():
    # sg.theme('BluePurple')
    sg.theme(str(bd.tema))

    # ------ Menu Definition ------ #
    menu_def = [['Cadastro', ['Aluno', 'Plano', 'Instrutor']],
                ['Atualizações', ['Alunos', 'Planos', 'Instrutores']],
                ['Consultas', ['Consulta Alunos',
                               'Consulta Planos', 'Consulta Instrutores']],
                ['Ajuda', ['Help', 'About...']],
                ['Admin', ['Cadastro User']]]

    # ------ GUI Defintion ------ #
    frame_layout = [
        [sg.T('Text inside of a frame')],
        [sg.CB('Check 1'), sg.CB('Check 2')],
    ]
    login = [
        [sg.Menu(menu_def,)],
        #[sg.Output(size=(100, 30))]
        [sg.Image('background.png', expand_x=True, expand_y=True)]
    ]

    # return sg.Window('Menu Principal', layout=login, finalize=True,size=(1300, 650))
    # return sg.Window('Menu Principal', layout=login, finalize=True, size=(1200, 650))
    window = sg.Window('Menu Principal', layout=login, finalize=True,
                       resizable=True, size=(0, 0), location=(-1, -1), modal=True)
    window.maximize()
    return window
    #window = sg.Window('Window Title', layout, resizable = True, finalize=True)

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Tela menu principal escrita


def janelamenuescrita():
    sg.theme('BluePurple')
    # ------ Menu Definition ------ #
    menu_def = [['Cadastro', ['Aluno', 'Plano', 'Instrutor']],
                ['Atualizações', ['Alunos', 'Planos', 'Instrutores']],
                ['Consultas', ['Consulta Alunos',
                               'Consulta Planos', 'Consulta Instrutores']],
                ['Ajuda', ['Help', 'About...']],
                ['!Admin', ['Cadastro User']]]

    # ------ GUI Defintion ------ #
    frame_layout = [
        [sg.T('Text inside of a frame')],
        [sg.CB('Check 1'), sg.CB('Check 2')],
    ]
    login = [
        [sg.Menu(menu_def,)],
        [sg.Image('background.png', expand_x=True, expand_y=True)]
    ]

    # return sg.Window('Menu Principal', layout=login, finalize=True,size=(1300, 650))
    window = sg.Window('Menu Principal', layout=login, finalize=True,
                       resizable=True, size=(0, 0), location=(-1, -1), modal=True)
    window.maximize()
    return window

    # menu user leitura
# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Tela menu principal leitura


def janelamenueleitura():
    sg.theme('BluePurple')
    # ------ Menu Definition ------ #
    menu_def = [['!Cadastro', ['Aluno', 'Plano', 'Instrutor']],
                ['!Atualizações', ['Alunos', 'Planos', 'Instrutores']],
                ['Consultas', ['Consulta Alunos',
                               'Consulta Planos', 'Consulta Instrutores']],
                ['Ajuda', ['Help', 'About...']],
                ['!Admin', ['Cadastro User']]]

    # ------ GUI Defintion ------ #
    frame_layout = [
        [sg.T('Text inside of a frame')],
        [sg.CB('Check 1'), sg.CB('Check 2')],
    ]
    login = [
        [sg.Menu(menu_def, )],
        [sg.Image('background.png', expand_x=True, expand_y=True)]
    ]

    # return sg.Window('Menu Principal', layout=login, finalize=True,size=(1300, 650))
    window = sg.Window('Menu Principal', layout=login, finalize=True,
                       resizable=True, size=(0, 0), location=(-1, -1), modal=True)
    window.maximize()
    return window
