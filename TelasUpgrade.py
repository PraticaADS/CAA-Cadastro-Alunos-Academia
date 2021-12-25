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
# Alterar Cadastro instrutor
def janela_cad_instrutor_alt():
    sg.theme(str(bd.tema))
    cadastros = [
        [sg.Text("Nome completo"), sg.Input(
            nomec, key='nomepinstrutor', expand_x=True, disabled=True)],
        [sg.Text("Sexo"), sg.Input(sexo, size=(20, 30), key='sexoinstrutor', disabled=True),
            sg.Text("Data Mov."), sg.Input(datem, key='dateminstrutor', disabled=True, size=(20, 30), expand_x=True)],
        [sg.Text("Altura"), sg.Input(altura, key='alturainstrutor', size=(8, 30)), sg.Text("Data nascimento"),
            sg.Input(datan, key='dataninstrutor', size=(10, 30), disabled=True), sg.Button("Data Nascimento", key='datainstrutor', expand_x=True, disabled=True, border_width=3)],
        [sg.Text("Peso"), sg.Input(peso, key='pesoinstrutor', size=(8, 30)),
            sg.Input(imc, key='imcinstrutor', disabled=True, size=(8, 30),
                     visible=False), sg.Text("              Status Instrutor"),
            sg.Combo(values=status, key='statusinstrutor', size=(20, 30), expand_x=True, default_value="ATIVO", readonly=True)],


        [sg.Button('Alterar', key='alt_cad_instrutor', border_width=3),
         sg.Button('  Sair  ', border_width=3)]
    ]
    return sg.Window('Tela Alterar Cadastro de Instrutor', layout=cadastros, finalize=True, modal=True, keep_on_top=True)

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Alterar cadastro de planos


def janela_cad_plano_alt():
    sg.theme(str(bd.tema))
    cad_plano = [
        [sg.Text("Nome plano"), sg.Input(
            nomec, key='nomeplano', disabled=True, expand_x=True)],
        [sg.Text("Codigo Plano"), sg.Input(
            user, key='codplano', disabled=True)],
        [sg.Text("Status plano"), sg.Combo(
            status, key='statusplano', readonly=True, size=(15, 10))],
        [sg.Button('Alterar', key='alt_cad_plano', border_width=3),
         sg.Button('  Sair  ', border_width=3)]
    ]
    return sg.Window('Alteração Cadastro de plano', layout=cad_plano, finalize=True, modal=True, keep_on_top=True)

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Tela Altera cadastro aluno


def janela_cadastro_alt():
    sg.theme(str(bd.tema))
    cadastros = [
        [sg.Text("Nome completo"), sg.Input(
            nomec, key='nomec_alt', size=(45, 10), disabled=True, expand_x=True)],
        [sg.Text("CPF"), sg.Input(cpf, key='cpf_alt', size=(20, 30), expand_x=False, disabled=True), sg.Text(
            "Data Mov."), sg.Input(datem, key='datem_alt', disabled=True, size=(20, 30), expand_x=True)],
        [sg.Text("Sexo"), sg.Input(sexo, disabled=True, size=(20, 30), key='sexo_alt'),
            sg.Text("Data nascimento"), sg.Input(datan, key='datan_alt', size=(15, 30), disabled=True, expand_x=True)],
        [sg.Text("Altura"), sg.Input(altura, key='altura_alt', size=(8, 30)), sg.Text("Peso"), sg.Input(peso, key='peso_alt', size=(8, 30)), sg.Input(imc, key='imc_alt', disabled=True, size=(8, 30), visible=False), sg.Text("Status"),
            sg.Combo(values=status, key='status_alt', size=(
                20, 30), expand_x=True, default_value="ATIVO", readonly=True)
         ],
        [sg.Text("Plano "), sg.Combo(values=plano, key='plano_alt',
                                     size=(20, 30), expand_x=False, default_value="..........", readonly=True),
            sg.Text("Instrutor "), sg.Combo(values=nomep, key='nomep', size=(20, 30), expand_x=True, default_value="..........", readonly=True)],

        [sg.Button('Aterar', key='alt_cad_aluno', border_width=3),
         sg.Button('  Sair  ', border_width=3)]
    ]
    return sg.Window('Alteração de Cadastro de Aluno', layout=cadastros, finalize=True, modal=True, keep_on_top=True)


# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Tela Atualizações Alunos
def ativos():
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
            "Delete", key="delete", expand_x=True, border_width=3),
         sg.Combo(values=status, size=(10, 30), key='talterar', default_value="ATIVO", readonly=True, visible=False), sg.Button(
            "Alterar", key='altera', expand_x=True, border_width=3), sg.Input(key='inp_pesquisa'), sg.Button("Pesquisa", key='bt_pesquisa', expand_x=True, border_width=3),
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
    window = sg.Window('Atualizações Alunos', layout=layout, finalize=True,
                       resizable=True, size=(0, 0), location=(-1, -1), modal=True)
    window.maximize()
    return window


# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Tela Atualizações Planos
def ativosplanos():
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
            "Delete", key="deleteplano", expand_x=True, border_width=3),
         sg.Combo(values=status, size=(10, 30), key='talterarplano', default_value="ATIVO", readonly=True, visible=False), sg.Button(
            "Alterar", key='alteraplano', expand_x=True), sg.Input(user, key='inp_pesquisaplano'), sg.Button("Pesquisa", key='bt_pesquisaplano', expand_x=True, border_width=3),
         ]]
    window = sg.Window('Atualização de planos', layout=layout, finalize=True,
                       resizable=True, size=(0, 0), location=(-1, -1), modal=True)
    window.maximize()
    return window


# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Atualizações Instrutores
def ativosinstrutor():
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
            "Delete", key="deleteinstrutor", expand_x=True, disabled=False, border_width=3),
         sg.Combo(values=status, size=(10, 30), key='talterarinstrutor', default_value="ATIVO", disabled=False, readonly=True, visible=False), sg.Button(
            "Alterar", key='alterainstrutor', expand_x=False, border_width=3), sg.Input(user, key='inp_pesquisainstrutor', disabled=False), sg.Button("Pesquisa", key='bt_pesquisainstrutor', expand_x=True, disabled=False, border_width=3),
         ]]
    window = sg.Window('Atualização de Instrutor', layout=layout, finalize=True,
                       resizable=True, size=(0, 0), location=(-1, -1), modal=True)
    window.maximize()
    return window
