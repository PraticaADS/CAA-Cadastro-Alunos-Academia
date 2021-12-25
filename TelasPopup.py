import getpass
from sys import maxsize
from tkinter.constants import CENTER
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import ButtonMenu, Window, popup
import bd

msg = ""

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Popup


def janela_popup():
    sg.theme(str(bd.tema))
    popup = [
        [sg.Text(msg)],
        [sg.Button(button_text='  Sair  ', key='ok_conf_cad', border_width=3)]
    ]

    return sg.Window('Tela popup', layout=popup, finalize=True, modal=True, keep_on_top=True)

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Popup ok cadastro


def janela_popup_ok_cadasto():
    sg.theme(str(bd.tema))
    popup = [
        [sg.Text(msg)],
        [sg.Button(button_text='  Sair  ',
                   key='popup_ok_cadasto', border_width=3)]
    ]

    return sg.Window('Tela popup', layout=popup, finalize=True, modal=True, keep_on_top=True)

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Popup delete aluno


def janela_popup_del(msg):
    sg.theme(str(bd.tema))
    popupdel = [
        [sg.Text(msg)],
        [sg.Button('SIM', border_width=3), sg.Button('NÃO', border_width=3)],
    ]

    return sg.Window('Tela popup Delete', layout=popupdel, finalize=True, modal=True, keep_on_top=True)

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Popup delete plano


def janela_popup_delplano(msg):
    sg.theme(str(bd.tema))
    popupdel = [
        [sg.Text(msg)],
        [sg.Button('SIM', key='simplano', border_width=3),
         sg.Button('NÃO', key='naoplano', border_width=3)],

    ]

    return sg.Window('Tela popup Delete', layout=popupdel, finalize=True, modal=True, keep_on_top=True)

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Popup delete instrutor


def janela_popup_delinstrutor(msg):
    sg.theme(str(bd.tema))
    popupdel = [
        [sg.Text(msg)],
        [sg.Button('SIM', key='siminstrutor', border_width=3),
         sg.Button('NÃO', key='naoinstrutor', border_width=3)],

    ]

    return sg.Window('Tela popup Delete', layout=popupdel, finalize=True, modal=True, keep_on_top=True)

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Popup update aluno


def janela_popup_upl(msg):
    sg.theme(str(bd.tema))
    pop_upl = [
        [sg.Text(msg)],
        [sg.Button('SIM.', border_width=3), sg.Button('NÃO.', border_width=3)]
    ]

    return sg.Window('Tela popup upgrade', layout=pop_upl, finalize=True, modal=True, keep_on_top=True)

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# poupup update plano


def janela_popup_uplplano(msg):
    sg.theme(str(bd.tema))
    pop_upl = [
        [sg.Text(msg)],
        [sg.Button('SIM.', key='simaltplano', border_width=3),
         sg.Button('NÃO.', key='naoaltplano', border_width=3)]
    ]
    return sg.Window('Tela popup upgrade plano', layout=pop_upl, finalize=True, modal=True, keep_on_top=True)

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# poupup update instrutor


def janela_popup_uplinstrutor(msg):
    sg.theme(str(bd.tema))
    pop_upl = [
        [sg.Text(msg)],
        [sg.Button('SIM.', key='simaltinstrutor', border_width=3),
         sg.Button('NÃO.', key='naoaltinstrutor', border_width=3)]
    ]
    return sg.Window('Tela popup upgrade Instrutor', layout=pop_upl, finalize=True, modal=True, keep_on_top=True)

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# poupup ok


def janela_popup_ok(msg):
    sg.theme(str(bd.tema))
    pop_OK = [
        [sg.Text("Registros encontratos")],
        [sg.Text(msg)]
    ]

    return sg.Window('Tela popup ok', layout=pop_OK, finalize=True, modal=True, keep_on_top=True)
