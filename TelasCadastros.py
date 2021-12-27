import getpass
from sys import maxsize
from tkinter.constants import CENTER
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import ButtonMenu, Window, popup
import bd

from datetime import datetime
import calendar as cal
fnt = 'Arial 12'


nomec = ""
cpf = ""
cpf_listado = ""
nomep = ""
altura = ""
peso = ""
datan = ""
sexo = ["MASCULINO", "FEMENINO"]
nome = ""
status = ["ATIVO", "INATIVO"]
senha = ""
imc = ""
user = ""
passs = ""
passss = ""
datem = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
plano = []
previlegio = ["Leitura", "Escrita"]

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Cadastro de aluno


def janela_cadastro():
    sg.theme(str(bd.tema))
    cadastros = [
        [sg.Text("Nome completo"), sg.Input(
            nomec, key='nomec', expand_x=True)],
        [sg.Text("CPF"), sg.Input(cpf, key='cpf', size=(20, 30), expand_x=False), sg.Text(
            "    Sexo"), sg.Combo(values=sexo, size=(20, 30), key='sexo', readonly=True, expand_x=True)],
        [sg.Text("Data Mov."), sg.Input(datem, key='datem', disabled=True, size=(
            20, 30), expand_x=True), sg.Text("Altura"), sg.Input(altura, key='altura', size=(8, 30))],
        [sg.Text("Data nascimento"),
            sg.Input(datan, key='datan', size=(10, 30), disabled=True), sg.Button("Escolher Data Nascimento", key='data', expand_x=True, border_width=3)],
        [sg.Text("Peso"), sg.Input(peso, key='peso', size=(8, 30)),
            sg.Input(imc, key='imc', disabled=True, size=(8, 30),
                     visible=False), sg.Text("              Status"),
            sg.Combo(values=status, key='status', size=(20, 30), expand_x=True, default_value="ATIVO", readonly=True)],
        [sg.Text("Plano"), sg.Combo(values=plano, key='plano', size=(20, 30), expand_x=False, readonly=True), sg.Text("Instrutor"),
            sg.Combo(values=nomep, key='nomep', size=(20, 30), expand_x=False, readonly=True)],

        [sg.Button('Cadastrar', key='cad_aluno', border_width=3),
         sg.Button('  Sair  ', border_width=3)]
    ]
    return sg.Window('Cadastro de aluno', layout=cadastros, finalize=True, modal=True, keep_on_top=True)

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Cadastro instrutor


def janela_cadastro_instrutor():
    sg.theme(str(bd.tema))
    cadastros = [
        [sg.Text("Nome completo"), sg.Input(
            nomec, key='nomep', expand_x=True)],
        [sg.Text("Sexo"), sg.Combo(values=sexo, size=(20, 30), key='sexo', readonly=True),
            sg.Text("Data Mov."), sg.Input(datem, key='datem', disabled=True, size=(20, 30), expand_x=True)],
        [sg.Text("Altura"), sg.Input(altura, key='altura', size=(8, 30)), sg.Text("Data nascimento"),
            sg.Input(datan, key='datan', size=(10, 30), disabled=True), sg.Button("Data Nascimento", key='data', expand_x=True)],
        [sg.Text("Peso"), sg.Input(peso, key='peso', size=(8, 30)),
            sg.Input(imc, key='imc', disabled=True, size=(8, 30),
                     visible=False), sg.Text("              Status"),
            sg.Combo(values=status, key='status', size=(20, 30), expand_x=True, default_value="ATIVO", readonly=True)],

        [sg.Button('Cadastrar', key='cad_instrutor', border_width=3),
         sg.Button('  Sair  ', border_width=3)]
    ]
    return sg.Window('Cadastro de nstrutor', layout=cadastros, finalize=True, modal=True, keep_on_top=True)

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Tela Cadastro adm


def janela_cad_admin():
    sg.theme(str(bd.tema))
    cad_admin = [
        [sg.Text("Favor digitar o seu nome completo"),
         sg.Input(nomec, key='nomeadm', expand_x=True)],
        [sg.Text("Digite seu usuario"), sg.Input(user, key='user', size=(15, 30)), sg.Text("Digite sua senha"), sg.Input(passs, key='passs', size=(10, 30), password_char='*'), sg.Text("Repira a senha"), sg.Input(
            passss, key='passss', password_char='*', size=(10, 30))],

        [sg.Text("Previlegio"), sg.Combo(
            previlegio, s=(10, 30), key='previlegio', readonly=True), sg.Button('Cadastrar', key='Cadastrarr', border_width=3), sg.Button('  Sair  ', border_width=3)],


    ]
    return sg.Window('Cadastro de Funcionario', layout=cad_admin, finalize=True, modal=True, keep_on_top=True)

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Cadastro de plano


def janela_cad_plano():
    sg.theme(str(bd.tema))
    cad_plano = [
        [sg.Text("Nome plano"), sg.Input(
            nomec, key='nomeplano', expand_x=True)],
        [sg.Text("Codigo Plano"), sg.Input(user, key='codplano', size=(15, 30)), sg.Text("Status plano"), sg.Input(
            "ATIVO", key='statusplano', size=(15, 30), disabled=True)],

        [sg.Button('Cadastrar', key='Cadastrarrr', border_width=3),
         sg.Button('  Sair  ', border_width=3)]
    ]
    return sg.Window('Cadastro de plano', layout=cad_plano, finalize=True, modal=True, keep_on_top=True)
