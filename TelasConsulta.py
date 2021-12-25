# @title Texto de título padrão { display-mode: "code" }


from tkinter.constants import CENTER
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import ButtonMenu, Window, popup
import bd

from datetime import datetime
import calendar as cal
fnt = 'Arial 12'


nomec = ""
nomep = ""
cpf = ""
altura = ""
peso = ""
datan = ""
sexo = ["MASCULINO", "FEMENINO"]
status = ["ATIVO", "INATIVO"]
imc = ""
user = ""
datem = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
plano = []
ret_plano = []
ret_instrutor = []


# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Consulta Alunos
def ativos_consulta():
    sg.theme(str(bd.tema))
    i = ""
    dados_lidos = [["", "", "", "", "", "", "", ""]]
    layout = [
        [sg.Table(
            key='lido',
            col_widths=[2, 13, 25, 10, 10, 6, 10, 5, 5, 8, 12, 23],
            values=dados_lidos,
            headings=["ID", "Data Mov.", "Nome", "CPF", "Sexo", "Altura",
                      "Dt Nascimento", "Peso", "IMC", "Status", "Plano", "Instrutor"],
            # row_colors=[(i,cor)],
            row_colors=[(i, 'red', 'green')],  # for i in range(0,  19)],
            justification='left',
            max_col_width=20,
            auto_size_columns=False,
            # background_color='#aaaaaa',
            header_background_color='#aaaaaa',
            alternating_row_color='#E0F2F7',
            expand_x=True,
            expand_y=True,
            # def_col_width=15,
            text_color='black',

        )],
        [sg.Text('')],
        [sg.Button("Listar Todos", key="listardados", expand_x=True, border_width=3), sg.Button("Ativos", key="ativos", expand_x=True, border_width=3),
         sg.Button("Inativos", key="inativos", expand_x=True, border_width=3), sg.Button(
            "Delete", key="delete", expand_x=True, border_width=3, disabled=True),
         sg.Combo(values=status, size=(10, 30), key='talterar', default_value="ATIVO", readonly=True, disabled=True, visible=False), sg.Button(
            "Alterar", key='altera', expand_x=True, border_width=3, disabled=True), sg.Input(key='inp_pesquisa'), sg.Button("Pesquisa", key='bt_pesquisa', expand_x=True, border_width=3),
         ],
        [sg.Text('F i l t r a r  D a d o s===========================================================================================================================================================')],
        [sg.Text('Status'), sg.Combo(("ATIVO", "INATIVO", "TODOS"), default_value="TODOS", size=(8, 30), key='f_status', readonly=True),
         sg.Text('  Sexo'),
         sg.Combo(values=("MASCULINO", "FEMENINO", "TODOS"), default_value="TODOS", size=(
             15, 30), key='f_sexo', change_submits=True, readonly=True),
         sg.Text("  Imc >="), sg.Input(key='f_imcm', size=(
             5, 30), default_text=1), sg.Text("  Imc <="),
         sg.Input(key='f_imc', size=(5, 30),
                  default_text=100), sg.Text("  Plano"),
         sg.Combo(values=ret_plano, key='b_plano', size=(25, 30),
                  default_value="TODOS", readonly=True), sg.Text("  Instrutor"),
         sg.Combo(values=ret_instrutor, key='b_instrutor',
                  size=(40, 30), default_value="TODOS", readonly=True),
         sg.Button(" Filtrar dados", key='bt_filtro', border_width=3)],
        [sg.Text("Total de Registos da consuta", font=30), sg.Input(
            key='qdt_reg', size=(5, 30), disabled=True, justification='center', font=30)],

        [sg.Text('=========================================================================================================================================================================')]
    ]
    window = sg.Window('Consulta Alunos', layout=layout, finalize=True,
                       resizable=True, size=(0, 0), location=(-1, -1), modal=True)
    window.maximize()
    return window


# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Tela consulta Planos
def ativosplanos_consulta():
    sg.theme(str(bd.tema))
    i = ""
    dados_lidosplano = [["", "", "", "", "", "", "", ""]]
    layout = [
        [sg.Table(
            key='lidoplano',
            col_widths=[10, 10],
            values=dados_lidosplano,
            headings=["ID", "Nome Plano", "Cod. Plano", "Status Plano"],
            # row_colors=[(i,cor)],
            row_colors=[(i, 'red', 'green')],  # for i in range(0,  19)],
            justification='left',
            max_col_width=20,
            auto_size_columns=False,
            # background_color='#aaaaaa',
            header_background_color='#aaaaaa',
            alternating_row_color='#E0F2F7',
            expand_x=True,
            expand_y=True,
            # def_col_width=15,
            text_color='black',

        )],
        [sg.Text('')],
        [sg.Button("Listar Todos", key="listardadosplano", expand_x=True, border_width=3), sg.Button("Ativos", key="ativosplano", expand_x=True, disabled=False, border_width=3),
         sg.Button("Inativos", key="inativosplano", expand_x=True, disabled=False, border_width=3), sg.Button(
            "Delete", key="deleteplano", expand_x=True, border_width=3, disabled=True),
         sg.Combo(values=status, size=(10, 30), key='talterarplano', default_value="ATIVO", readonly=True, disabled=True, visible=False), sg.Button(
            "Alterar", key='alteraplano', expand_x=True, disabled=True), sg.Input(user, key='inp_pesquisaplano'), sg.Button("Pesquisa", key='bt_pesquisaplano', expand_x=True, border_width=3),
         ]]
    window = sg.Window('Consulta de planos', layout=layout, finalize=True,
                       resizable=True, size=(0, 0), location=(-1, -1), modal=True)
    window.maximize()
    return window


# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Consulta instrutores
def ativosinstrutor_consulta():
    sg.theme(str(bd.tema))
    i = ""
    dados_lidosinstrutor = [["", "", "", "", "", "", "", ""]]
    layout = [
        [sg.Table(
            key='lidoinstrutor',
            col_widths=[10, 10, 10, 10, 10, 10, 10],
            values=dados_lidosinstrutor,
            headings=["ID", "Nome Instrutor", "Sexo", "Altura",
                      "Data de nascimento", "Peso", "Status"],
            # row_colors=[(i,cor)],
            row_colors=[(i, 'red', 'green')],  # for i in range(0,  19)],
            justification='left',
            max_col_width=20,
            auto_size_columns=False,
            # background_color='#aaaaaa',
            header_background_color='#aaaaaa',
            alternating_row_color='#E0F2F7',
            expand_x=True,
            expand_y=True,
            # def_col_width=15,
            text_color='black',

        )],
        [sg.Text('')],
        [sg.Button("Listar Todos", key="listardadosinstrutor", expand_x=True, border_width=3), sg.Button("Ativos", key="ativosinstrutor", expand_x=True, disabled=False, border_width=3),
         sg.Button("Inativos", key="inativosinstrutor", expand_x=True, disabled=False, border_width=3), sg.Button(
            "Delete", key="deleteinstrutor", expand_x=True, disabled=True, border_width=3),
         sg.Combo(values=status, size=(10, 30), key='talterarinstrutor', default_value="ATIVO", disabled=True, readonly=True, visible=False), sg.Button(
            "Alterar", key='alterainstrutor', expand_x=False, border_width=3, disabled=True), sg.Input(user, key='inp_pesquisainstrutor', disabled=False), sg.Button("Pesquisa", key='bt_pesquisainstrutor', expand_x=True, disabled=False, border_width=3),
         ]]
    window = sg.Window('Consulta de Instrutor', layout=layout, finalize=True,
                       resizable=True, size=(0, 0), location=(-1, -1), modal=True)
    window.maximize()
    return window
