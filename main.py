from datetime import datetime
from datetime import date
import time
import bd
import PySimpleGUI as sg
import TelasCadastros as tc
import TelasConsulta as tcs
import TelasMenu as tm
import TelasPopup as tp
import TelasUpgrade as tu

from validate_docbr import CPF
cpf = CPF()

# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# VARIAVES JANELAS
janela1 = tm.janela_login()
janela2 = None
janela3 = None
janela4 = None
janela5 = None
# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================

# FUNÇÕES LIMPA CAMPOS


def limpaadm():
    window.find_element('senha').Update('')
    window.find_element('nome').Update('')
    window.find_element('nome').SetFocus()


def limpacampos():
    window.find_element('nomec').Update('')
    window.find_element('altura').Update('')
    window.find_element('peso').Update('')
    window.find_element('datan').Update('')
    window.find_element('sexo').Update('')


def limpacamposinstrutor():

    window.find_element('nomep').Update('')
    window.find_element('altura').Update('')
    window.find_element('peso').Update('')
    window.find_element('datan').Update('')
    window.find_element('sexo').Update('')


def limpacamposinstrutor2():
    tc.nomec = ""
    tc.sexo = ""
    tc.altura = ""
    tc.datan = ""
    # t.datem = ""
    tc.peso = ""
    tc.status = ""


def limpaadmcad():
    window.find_element('nomeadm').Update('')
    window.find_element('user').Update('')
    window.find_element('passs').Update('')
    window.find_element('passss').Update('')


def limpaadmsenha():
    window.find_element('passs').Update('')
    window.find_element('passss').Update('')


def limpaplano():
    window.find_element('nomeplano').Update('')
    window.find_element('codplano').Update('')


# ===================================================================
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ===================================================================
# Loop telas rodando
while True:
    window, eventos, valores = sg.read_all_windows()
    if window == janela1 and eventos == sg.WIN_CLOSED:
        janela1.close()
        break
    if window == janela2 and eventos == sg.WIN_CLOSED:
        janela2.close()
        break
    if window == janela3 and eventos == sg.WIN_CLOSED:
        janela3.close()

    if window == janela4 and eventos == sg.WIN_CLOSED:
        janela4.close()

    if window == janela1 and eventos == '  Sair  ':
        janela1.close()
        break

    if window == janela2 and eventos == 'ok_conf_cad':
        janela2.close()
        # break

    if window == janela2 and eventos == '  Sair  ':
        janela2.close()
    if window == janela3 and eventos == '  Sair  ':
        janela3.close()
    if window == janela4 and eventos == 'popup_ok_cadasto':
        janela4.close()
        janela3.close()

    if window == janela4 and eventos == 'ok_conf_cad':
        janela4.close()

    if window == janela5 and eventos == 'ok_conf_cad':
        janela5.close()

    if window == janela1 and eventos == sg.WIN_CLOSED:
        janela1.close()
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # TELA LOGIN - ENTRAR
    if window == janela1 and eventos == 'Entrar':
        dadoslidos = bd.retlogin(valores['nome'])
        statement = f"SELECT user from admin WHERE user='{valores['nome']}' AND passs = '{valores['senha']}';"
        bd.c.execute(statement)
        if not bd.c.fetchone():
            limpaadm()
            tp.msg = "Dados não conferem, favor tentar novamente"
            janela2 = tp.janela_popup()

        else:
            bd.escolha = valores['escolha']

            if bd.escolha == "Blue":
                #bd.tema = "SystemDefault"
                bd.tema = "Material1"
            if bd.escolha == "Escuro":
                bd.tema = "SandyBeach"
            if dadoslidos[0][0] == "Master":
                janela1.close()
                janela2 = tm.janelamenuadm()

            if dadoslidos[0][0] == "Escrita":
                janela1.close()
                janela2 = tm.janelamenuescrita()

            if dadoslidos[0][0] == "Leitura":
                janela1.close()
                janela2 = tm.janelamenueleitura()
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Cadastro de aluno
    if window == janela2 and eventos == 'Aluno':
        tc.nomec = ""
        tc.cpf = ""
        tc.altura = ""
        tc.peso = ""
        tc.datan = ""
        tc.sexo = ["MASCULINO", "FEMENINO"]
        tc.status = ["ATIVO", "INATIVO"]

        lista_sem_plano = bd.listaplano()
        resultado_listaplano = [''.join(i) for i in lista_sem_plano]
        tc.plano = resultado_listaplano

        #tc.plano = bd.listaplano()
        lista_sem_ = bd.listainstrutor()
        resultado_lista = [''.join(i) for i in lista_sem_]
        tc.nomep = resultado_lista
        janela3 = tc.janela_cadastro()

    if window == janela3 and eventos == 'cad_aluno':

        st_cpf = cpf.validate(str(valores['cpf']))
        if valores['nomec'] == "" or valores['sexo'] == "" or valores['altura'] == "" or valores['datan'] == "" or valores['peso'] == "" or valores['status'] == "" or valores['plano'] == "" or valores['nomep'] == "":
            tp.msg = "Favor prencher todos os campos corretamente"
            janela4 = tp.janela_popup()
        elif st_cpf == False:
            new_cpf_one = cpf.generate()  # gera cpf valido
            window.find_element('cpf').Update(new_cpf_one)  # gera cpf valido
            tp.msg = "Favor colocar um cpf valido, para fins de teste caso não preencha o sistema gera um automaticamente"
            janela4 = tp.janela_popup()

        else:

            if bd.lista_cpf(valores['cpf']) != []:
                tp.msg = "Ja tem um cadastro com esse CPF, para fins de teste caso não preencha o sistema gera um automaticamente"
                janela4 = tp.janela_popup()
                new_cpf_one = cpf.generate()  # gera cpf valido
                window.find_element('cpf').Update(
                    new_cpf_one)  # gera cpf valid
            else:
                try:
                    p_peso_alt = float(valores['peso'].replace(',', '.'))
                    alt_alt = float(valores['altura'].replace(',', '.'))
                    peso_altura = p_peso_alt / (alt_alt*alt_alt)
                    valores['imc'] = round(peso_altura, 2)
                    valores['datem'] = tc.datem

                    bd.cadastrardados(valores['nomec'].upper(), valores['cpf'], valores['datem'], valores['sexo'].upper(
                    ), valores['altura'], valores['datan'], valores['peso'], valores['imc'], valores['status'].upper(), valores['plano'], valores['nomep'])
                    bd.cadastrardados_h(valores['nomec'].upper(), valores['cpf'], valores['datem'], valores['sexo'].upper(
                    ), valores['altura'], valores['datan'], valores['peso'], valores['imc'], valores['status'].upper(), valores['plano'], valores['nomep'])
                    limpacampos()
                    ehNumero = True
                    tp.msg = "Dados Cadastrados com sucesso"
                    janela4 = tp.janela_popup_ok_cadasto()
                except ValueError:
                    tp.msg = "Valores invalidos, Favor usar apenas numeros para os campos peso e altura"
                    janela4 = tp.janela_popup()

    if eventos == 'data':
        
        janela4 = sg.popup_get_date(start_year=1980, month_names=[
                                    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"])
        if janela4:
            month, day, year = janela4
            window['datan'].update(f"{day:0>2d}/{month:0>2d}/{year}")
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Cadastro de instrutor
    if window == janela2 and eventos == 'Instrutor':
        janela3 = tc.janela_cadastro_instrutor()

    if window == janela3 and eventos == 'cad_instrutor':

        if valores['nomep'] == "" or valores['sexo'] == "" or valores['altura'] == "" or valores['datan'] == "" or valores['peso'] == "" or valores['status'] == "":
            tp.msg = "Favor prencher todos os campos"
            janela4 = tp.janela_popup()
        else:
            #bd.cadastrardados_instrutor(valores['nomep'].upper().replace(" ", "_"), valores['sexo'].upper(), valores['altura'].upper(), valores['datan'], valores['peso'], valores['status'].upper())
            bd.cadastrardados_instrutor(valores['nomep'].upper(), valores['sexo'].upper(
            ), valores['altura'].upper(), valores['datan'], valores['peso'], valores['status'].upper())
            limpacamposinstrutor()
            tp.msg = "Dados Cadastrados com sucesso"
            janela4 = tp.janela_popup_ok_cadasto()
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Cadastro de Operador
    if window == janela2 and eventos == 'Cadastro User':
        janela3 = tc.janela_cad_admin()
    if window == janela3 and eventos == 'Cadastrarr':
        if valores['nomeadm'] == "" or valores['user'] == "" or valores['passs'] == "" or valores['passss'] == "" or valores['previlegio'] == "":
            tp.msg = "Favor prencher todos os campos"
            janela4 = tp.janela_popup()
        else:
            if valores['passs'] == valores['passss']:
                bd.cadastraruser(valores['nomeadm'].upper(
                ), valores['user'].upper(), valores['passs'], valores['passss'], valores['previlegio'])
                limpaadmcad()
                tp.msg = "Dados Cadastrados com sucesso"
                janela4 = tp.janela_popup_ok_cadasto()
            else:
                limpaadmsenha()
                tp.msg = "Senhas diferentes"
                janela4 = tp.janela_popup()

    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Cadastro de plano
    if window == janela2 and eventos == 'Plano':
        janela3 = tc.janela_cad_plano()

    if window == janela3 and eventos == 'Cadastrarrr':
        if valores['nomeplano'] == "" or valores['codplano'] == "":
            tp.msg = "Favor prencher todos os campos"
            janela4 = tp.janela_popup()
        else:
            bd.cadastrarplanos(
                valores['nomeplano'].upper(), valores['codplano'].upper(), valores['statusplano'].upper())
            limpaplano()
            tp.msg = "Dados Cadastrados com sucesso"
            janela4 = tp.janela_popup()

    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Atualizações de cadastro de aluno
    if window == janela2 and eventos == 'Alunos':
        tu.plano = bd.listaplano()
        tu.nomep = bd.listainstrutor()
        # tu.plano.append("TODOS")
        # tu.nomep.append("TODOS")

        lista_sem_plano = bd.listaplano()
        resultado_listaplano = [''.join(i) for i in lista_sem_plano]
        tu.plano = resultado_listaplano
        tu.plano.append("TODOS")

        lista_sem_ = bd.listainstrutor()
        resultado_lista = [''.join(i) for i in lista_sem_]
        tu.nomep = resultado_lista
        tu.nomep.append("TODOS")

        tu.ret_plano = tu.plano
        tu.ret_instrutor = tu.nomep
        janela3 = tu.ativos()
        tu.i = 0
        listado = False
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Consulta Cadastro de Alunos
    if window == janela2 and eventos == 'Consulta Alunos':
        tcs.plano = bd.listaplano()
        tcs.nomep = bd.listainstrutor()
        # tu.plano.append("TODOS")
        # tu.nomep.append("TODOS")

        lista_sem_plano = bd.listaplano()
        resultado_listaplano = [''.join(i) for i in lista_sem_plano]
        tcs.plano = resultado_listaplano
        tcs.plano.append("TODOS")

        lista_sem_ = bd.listainstrutor()
        resultado_lista = [''.join(i) for i in lista_sem_]
        tcs.nomep = resultado_lista
        tcs.nomep.append("TODOS")

        tcs.ret_plano = tcs.plano
        tcs.ret_instrutor = tcs.nomep
        janela3 = tcs.ativos_consulta()
        tcs.i = 0
        listado = False

    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Lista todos alunos
    if window == janela3 and eventos == 'listardados':
        listado = True
        dados_lidos = bd.lista()
        window.find_element('lido').Update(dados_lidos)
        row_colors = ((0, 'white'))
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Lista Alunos Ativos
    if window == janela3 and eventos == 'ativos':
        listado = True
        criterio = "ATIVO"
        dados_lidos = bd.listacrit(criterio)
        window.find_element('lido').Update(dados_lidos)
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Lsita Alunos inativos
    if window == janela3 and eventos == 'inativos':  # lista alunos inativos
        listado = True
        criterio = "INATIVO"
        dados_lidos = bd.listacrit(criterio)
        window.find_element('lido').Update(dados_lidos)
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Delata Alunos cadastrado
    if window == janela3 and eventos == 'delete':  # deleta selecionado

        if listado == False:
            tp.msg = "Favor Lista e depois selecionar um Aluno a ser deletado!"
            janela4 = tp.janela_popup_ok(tp.msg)

        else:
            vl_lido = valores['lido']
            soma = sum(vl_lido)
            x_d_lido = dados_lidos
            if x_d_lido != []:
                y_d_lido = x_d_lido[soma][1]
                tu.a_peso = y_d_lido
                tp.msg = "Confirmar alt_alterar exclusão do aluno " + \
                    x_d_lido[soma][2]
                janela4 = tp.janela_popup_del(tp.msg)
            else:
                tp.msg = "Favor Lista e depois selecionar um Aluno a ser deletado!"
                janela4 = tp.janela_popup_ok(tp.msg)

    if window == janela4 and eventos == 'SIM':
        bd.deletesel(y_d_lido)
        window = janela3
        bd.lista()
        dados_lidos = bd.lista()
        window.find_element('lido').Update(dados_lidos)
        janela4.close()
        window.find_element('lido').Update(dados_lidos)
    if window == janela4 and eventos == 'NÃO':
        janela4.close()
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Alterar cadastro de alunos
    if window == janela3 and eventos == 'altera':  # alterar status
        if listado == False:
            tp.msg = "Favor Lista e depois selecionar um Aluno a ser Alterado!"
            janela4 = tp.janela_popup_ok(tp.msg)
        else:
            bd.conection = bd.sqlite3.connect('bd.db')
            bd.c = bd.conection.cursor()
            ld_lido = valores['lido']
            if ld_lido != []:
                d_mov = datetime.now().strftime("%data_n_alt/%m/%Y %H:%M:%S")
                soma = sum(ld_lido)
                x_d_lido = dados_lidos
                cond = x_d_lido[soma][1]
                nv_val_alterar = valores['talterar']
                tu.nomec = x_d_lido[soma][2]
                tu.cpf = x_d_lido[soma][3]
                tu.sexo = x_d_lido[soma][4]
                tu.altura = x_d_lido[soma][5]
                tu.datan = x_d_lido[soma][6]
                # t.datem      #x_d_lido[soma][1]#
                tu.datem = x_d_lido[soma][1]
                tu.peso = x_d_lido[soma][7]
                tu.status = tu.status
                d_mov = tc.datem
                nome_c = tc.nomec
                c_p_f = tc.cpf
                s_sexo = tc.sexo
                alt_alterar = tc.altura
                data_n_alt = tc.datan
                peso_alterado = tc.peso
                stat_alterado = tc.status
                lista_sem_plano = bd.listaplano()
                resultado_listaplano = [''.join(i) for i in lista_sem_plano]
                tu.plano = resultado_listaplano
                lista_sem_ = bd.listainstrutor()
                resultado_lista = [''.join(i) for i in lista_sem_]
                tu.nomep = resultado_lista
                p_plano_alt = tu.status
                p_peso_alt = tu.nomep
                list1 = list(p_peso_alt)
                janela4 = tu.janela_cadastro_alt()
            else:
                tp.msg = "Favor Lista e depois selecionar um Aluno a ser deletado!"
                janela4 = tp.janela_popup_ok(tp.msg)

    if window == janela4 and eventos == 'alt_cad_aluno':
        bd.conection = bd.sqlite3.connect('bd.db')
        bd.c = bd.conection.cursor()
        d_mov = tu.datem
        nome_c = tu.nomec
        c_p_f = tu.cpf
        s_sexo = valores['sexo_alt']
        alt_alterar = valores['altura_alt']
        data_n_alt = valores['datan_alt']
        peso_alterado = valores['peso_alt']
        stat_alterado = valores['status_alt']
        p_plano_alt = valores['plano_alt']
        pers_alterado = valores['nomep']

        p_peso_alt = float(valores['peso_alt'].replace(',', '.'))
        alt_alt = float(valores['altura_alt'].replace(',', '.'))
        peso_altura = p_peso_alt / (alt_alt*alt_alt)
        imc_atual = valores['imc_alt'] = round(peso_altura, 2)

        if valores['plano_alt'] == ".........." or valores['nomep'] == "..........":
            tp.msg = "Favor preencher todos os campos"
            janela5 = tp.janela_popup()

        else:
            tp.msg = "Tem Certeza?"
            janela5 = tp.janela_popup_upl(tp.msg)

    if window == janela5 and eventos == 'SIM.':
        bd.upl_novo(alt_alterar, peso_alterado, stat_alterado,
                    imc_atual, p_plano_alt, pers_alterado, d_mov)
        bd.cadastrardados_h(nome_c, c_p_f, d_mov, s_sexo, alt_alterar, data_n_alt,
                            peso_alterado, imc_atual, stat_alterado, p_plano_alt, pers_alterado)
        window = janela3
        janela5.close()
        janela4.close()
        dados_lidos = bd.lista()
        window.find_element('lido').Update(dados_lidos)
        limpacamposinstrutor2()

    if window == janela5 and eventos == 'NÃO.':
        limpacamposinstrutor2()
        janela5.close()
        janela4.close()
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Pesquisa por nome aluno
    if window == janela3 and eventos == 'bt_pesquisa':
        pesquisa = valores['inp_pesquisa']
        pesquisa2 = "%"
        pesquisa3 = pesquisa2 + pesquisa + pesquisa2
        dados_lidos = bd.listacrit(pesquisa3)
        dados_lidos = bd.pesquisa(pesquisa3)
        if dados_lidos == []:
            tp.msg = "Sem dados de retorno para sua pesquisa"
            janela4 = tp.janela_popup()
        else:
            window.find_element('lido').Update(dados_lidos)
            ld_lido = dados_lidos[0][1]
            cond = ld_lido
            nv_val_alterar = valores['talterar']
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Filtos alunos
    if window == janela3 and eventos == 'bt_filtro':
        if valores['f_sexo'] == "TODOS":
            valores['f_sexo'] = "%"
            dados_lidos = bd.listacrit_filtros(
                valores['f_status'], valores['f_sexo'], valores['f_imcm'], valores['f_imc'], valores['b_plano'], valores['b_instrutor'])
            window.find_element('lido').Update(dados_lidos)

        if valores['f_status'] == "TODOS":
            valores['f_status'] = "%"
            dados_lidos = bd.listacrit_filtros(
                valores['f_status'], valores['f_sexo'], valores['f_imcm'], valores['f_imc'], valores['b_plano'], valores['b_instrutor'])
            window.find_element('lido').Update(dados_lidos)

        if valores['b_plano'] == "TODOS":
            valores['b_plano'] = "%"
            dados_lidos = bd.listacrit_filtros(
                valores['f_status'], valores['f_sexo'], valores['f_imcm'], valores['f_imc'], valores['b_plano'], valores['b_instrutor'])
            window.find_element('lido').Update(dados_lidos)

        if valores['b_instrutor'] == "TODOS":
            valores['b_instrutor'] = "%"
            dados_lidos = bd.listacrit_filtros(
                valores['f_status'], valores['f_sexo'], valores['f_imcm'], valores['f_imc'], valores['b_plano'], valores['b_instrutor'])
            window.find_element('lido').Update(dados_lidos)

            tm.reg = bd.listacrit_filtros_qtd(
                valores['f_status'], valores['f_sexo'], valores['f_imcm'], valores['f_imc'], valores['b_plano'], valores['b_instrutor'])
            msg = tm.reg[0][0]
            window.find_element('qdt_reg').Update(tm.reg[0][0])
        else:
            dados_lidos = bd.listacrit_filtros(
                valores['f_status'], valores['f_sexo'], valores['f_imcm'], valores['f_imc'], valores['b_plano'], valores['b_instrutor'])
            window.find_element('lido').Update(dados_lidos)

            tm.reg = bd.listacrit_filtros_qtd(
                valores['f_status'], valores['f_sexo'], valores['f_imcm'], valores['f_imc'], valores['b_plano'], valores['b_instrutor'])
            msg = tm.reg[0][0]
            window.find_element('qdt_reg').Update(tm.reg[0][0])

    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Atualizaçõs Planos
    if window == janela2 and eventos == 'Consulta Planos':
        janela3 = tcs.ativosplanos_consulta()
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Atualizaçõs Planos
    if window == janela2 and eventos == 'Planos':
        janela3 = tu.ativosplanos()
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Lista todos os planos
    if window == janela3 and eventos == 'listardadosplano':

        dados_lidosplano = bd.pesquisaplano()
        window.find_element('lidoplano').Update(dados_lidosplano)
        row_colors = ((0, 'white'))
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Lista planos ativos
    if window == janela3 and eventos == 'ativosplano':
        critplano = "ATIVO"
        dados_lidosplano = bd.listacritplano(critplano)
        window.find_element('lidoplano').Update(dados_lidosplano)
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Lista Planos inativos
    if window == janela3 and eventos == 'inativosplano':
        critplano = "INATIVO"
        dados_lidosplano = bd.listacritplano(critplano)
        window.find_element('lidoplano').Update(dados_lidosplano)
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Delete plano
    if window == janela3 and eventos == 'deleteplano':  # deleta selecionado
        vl_lido = valores['lidoplano']
        if vl_lido != []:
            soma = sum(vl_lido)
            x_d_lido = dados_lidosplano
            y_d_lido = x_d_lido[soma][1]
            tu.a_peso = y_d_lido
            tp.msg = "Confirmar alt_alterar exclusão do Plano " + \
                x_d_lido[soma][2]
            janela4 = tp.janela_popup_delplano(tp.msg)
        else:
            tp.msg = "Favor Lista e depois selecionar o plano ser deletado!"
            janela4 = tp.janela_popup_ok(tp.msg)
    if window == janela4 and eventos == 'simplano':
        bd.deleteselplano(y_d_lido)
        window = janela3
        bd.pesquisaplano()
        dados_lidosplano = bd.pesquisaplano()
        window.find_element('lidoplano').Update(dados_lidosplano)
        janela4.close()

    if window == janela4 and eventos == 'naoplano':
        janela4.close()
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
     # Alterar cadastro de planos
    if window == janela3 and eventos == 'alteraplano':  # alterar status
        bd.conection = bd.sqlite3.connect('bd.db')
        bd.c = bd.conection.cursor()
        ld_lido = valores['lidoplano']
        if ld_lido != []:
            soma = sum(ld_lido)
            x_d_lido = dados_lidosplano
            tu.nomec = x_d_lido[soma][1]
            tu.user = x_d_lido[soma][2]
            tu.statusplano = x_d_lido[soma][3]
            janela4 = tu.janela_cad_plano_alt()
        else:
            tp.msg = "Favor Lista e depois selecionar um Plano a ser deletado!"
            janela4 = tp.janela_popup_ok(tp.msg)
    if window == janela4 and eventos == 'alt_cad_plano':
        bd.conection = bd.sqlite3.connect('bd.db')
        bd.c = bd.conection.cursor()
        d_mov = tu.datem
        nome_c = tu.nomec  # esse usar
        u_user = tu.user  # esse usar
        stp = valores['statusplano']
        tp.msg = "Tem Certeza?"
        janela5 = tp.janela_popup_uplplano(tp.msg)
    if window == janela5 and eventos == 'simaltplano':
        bd.upl_novoplano(stp, nome_c)
        window = janela3
        janela5.close()
        janela4.close()
        dados_lidos = bd.pesquisaplano()
        window.find_element('lidoplano').Update(dados_lidos)
    if window == janela5 and eventos == 'naoaltplano':
        janela5.close()
        janela4.close()

    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Pesquisa por nome plano
    if window == janela3 and eventos == 'bt_pesquisaplano':
        pesquisaPlano = valores['inp_pesquisaplano']
        pesquisa2 = "%"
        pesquisa_plano = pesquisa2 + pesquisaPlano + pesquisa2
        dados_lidos_pes_plano = bd.listacrit(pesquisa_plano)
        dados_lidos_pes_plano = bd.pesquisa_plano(pesquisa_plano)
        if dados_lidos_pes_plano == []:
            tp.msg = "Sem dados de retorno para sua pesquisa"
            janela4 = tp.janela_popup()
        else:
            window.find_element('lidoplano').Update(dados_lidos_pes_plano)
            ld_lidoplano = dados_lidos_pes_plano[0][1]
            cond = ld_lidoplano
            nv_val_alterarplano = valores['talterarplano']
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Consulta instrutores
    if window == janela2 and eventos == 'Consulta Instrutores':
        janela3 = tcs.ativosinstrutor_consulta()
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Atualizações instrutores
    if window == janela2 and eventos == 'Instrutores':
        janela3 = tu.ativosinstrutor()
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Lista todos os instrutores
    if window == janela3 and eventos == 'listardadosinstrutor':
        dados_lidosinstrutor = bd.pesquisainstrutor()
        window.find_element('lidoinstrutor').Update(dados_lidosinstrutor)
        row_colors = ((0, 'white'))
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Lista instrutores ativos
    if window == janela3 and eventos == 'ativosinstrutor':
        critinstrutor = "ATIVO"
        dados_lidosinstrutor = bd.listacritinstrutor(critinstrutor)
        window.find_element('lidoinstrutor').Update(dados_lidosinstrutor)
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Lista instrutores inativos
    if window == janela3 and eventos == 'inativosinstrutor':
        critinstrutor = "INATIVO"
        dados_lidosinstrutor = bd.listacritinstrutor(critinstrutor)
        window.find_element('lidoinstrutor').Update(dados_lidosinstrutor)
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Alterar cadastro de instrutor
    if window == janela3 and eventos == 'alterainstrutor':  # alterar status
        bd.conection = bd.sqlite3.connect('bd.db')
        bd.c = bd.conection.cursor()
        ld_lido = valores['lidoinstrutor']
        if ld_lido != []:
            soma = sum(ld_lido)
            x_d_lido = dados_lidosinstrutor
            tu.nomec = x_d_lido[soma][1]
            tu.sexo = x_d_lido[soma][2]
            tu.altura = x_d_lido[soma][3]
            tu.datan = x_d_lido[soma][4]
            tu.peso = x_d_lido[soma][5]
            tu.statusinstrutor = x_d_lido[soma][6]
            janela4 = tu.janela_cad_instrutor_alt()
        else:
            tp.msg = "Favor Lista e depois selecionar um instrutor a ser deletado!"
            janela4 = tp.janela_popup_ok(tp.msg)
    if window == janela4 and eventos == 'alt_cad_instrutor':
        bd.conection = bd.sqlite3.connect('bd.db')
        bd.c = bd.conection.cursor()
        nome_c = tu.nomec
        at = valores['alturainstrutor']
        p_peso_alt = valores['pesoinstrutor']
        stp = valores['statusinstrutor']
        tp.msg = "Tem Certeza?"
        janela5 = tp.janela_popup_uplinstrutor(tp.msg)
    if window == janela5 and eventos == 'simaltinstrutor':
        bd.upl_novoinstrutor(at, p_peso_alt, stp, nome_c)
        window = janela3
        janela5.close()
        janela4.close()
        dados_lidos = bd.pesquisainstrutor()
        window.find_element('lidoinstrutor').Update(dados_lidos)
    if window == janela5 and eventos == 'naoaltinstrutor':
        janela5.close()
        janela4.close()
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Delete instrutor
    if window == janela3 and eventos == 'deleteinstrutor':  # deleta instrutor
        ldinstrutor = valores['lidoinstrutor']
        if ldinstrutor != []:
            soma = sum(ldinstrutor)
            x_d_lido = dados_lidosinstrutor

            y_d_lido = x_d_lido[soma][1]
            tp.msg = "Confirmar alt_alterar exclusão do instrutor: "+y_d_lido
            janela4 = tp.janela_popup_delinstrutor(tp.msg)
        else:
            tp.msg = "Favor Lista e depois selecionar o instrutor ser deletado!"
            janela4 = tp.janela_popup_ok(tp.msg)
    if window == janela4 and eventos == 'siminstrutor':
        bd.deleteselinstrutor(y_d_lido)
        window = janela3
        bd.pesquisainstrutor()
        dados_lidosinstrutor = bd.pesquisainstrutor()
        window.find_element('lidoinstrutor').Update(dados_lidosinstrutor)
        janela4.close()

    if window == janela4 and eventos == 'naoinstrutor':
        janela4.close()
        dados_lidosinstrutor = bd.pesquisainstrutor()
        # window.find_element('lidoinstrutor').Update(dados_lidosinstrutor)
        row_colors = ((0, 'white'))
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
    # Pesquisa por nome instrutor
    if window == janela3 and eventos == 'bt_pesquisainstrutor':
        pesquisainstrutor = valores['inp_pesquisainstrutor']
        pesquisa2 = "%"
        pesquisa_instrutor = pesquisa2 + pesquisainstrutor + pesquisa2
        dados_lidos_pes_instrutor = bd.listacrit(pesquisa_instrutor)
        dados_lidos_pes_instrutor = bd.pesquisa_instrutor(pesquisa_instrutor)
        if dados_lidos_pes_instrutor == []:
            tp.msg = "Sem dados de retorno para sua pesquisa"
            janela4 = tp.janela_popup()
        else:
            window.find_element('lidoinstrutor').Update(
                dados_lidos_pes_instrutor)
            ld_lidoinstrutor = dados_lidos_pes_instrutor[0][1]
            cond = ld_lidoinstrutor
            nv_val_alterarinstrutor = valores['talterarinstrutor']
    # ===================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ===================================================================
