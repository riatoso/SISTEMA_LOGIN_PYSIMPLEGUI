import PySimpleGUI as sg
from sistema import Login
from datetime import datetime
import criptografia_senha
from valida import Valida

if __name__ == "__main__":

    def login():
        sg.theme("DarkTeal12")
        layout = [
            [sg.Text("Digite o nome do usuario.", size=30)],
            [sg.Input(key="usuario", size=15), ],
            [sg.Text("Digite a senha.", size=30)],
            [sg.Input(key="senha", password_char="*", size=15)],
            [sg.Button('Login', size=20)],
            [sg.Button('Cadastrar', disabled=False, size=20)],
        ]
        return sg.Window("Login", icon="login.ico", size=(200, 190), layout=layout, finalize=True)


    def cadastrar_login():
        sg.theme("DarkTeal12")
        layout = [
            [sg.Text("Nome do funcionário.", size=20)],
            [sg.Input(key="nome", size=45)],
            [sg.Text("Login do usuario.", size=20)],
            [sg.Input(key="usuario", size=15)],
            [sg.Text("Senha.", size=20)],
            [sg.Input(key="senha", password_char="*", size=15)],
            [sg.Text("Redigite a senha.", size=20)],
            [sg.Input(key="resenha", password_char="*", size=15)],
            [sg.Button('Cadastrar', disabled=False, size=20), sg.Button('Voltar ao login', size=20)],
        ]
        return sg.Window('Cadastro de login.', icon="login.ico", size=(350, 250), layout=layout, finalize=True)


    def pre_sistema():
        hoje = datetime.now()
        sg.theme("DarkTeal12")
        layout = [
            [sg.Text("Complete seus dados.", size=20)],
            [sg.Text("ID do funcionário.", size=20)],
            [sg.Input(key="id", size=4)],
            [sg.Text(f"{40 * '--'}", size=45)],
            [sg.Text("Nome do funcionário.", size=20)],
            [sg.Input(key="nome", disabled=True, size=45)],
            [sg.Text(" * CPF. Apenas números EX: 02321445611.", size=40)],
            [sg.Input(key="cpf", size=15)],
            [sg.Text(" * Telefone. Apenas números EX: 16991220890.", size=40)],
            [sg.Input(key="telefone", size=15)],
            [sg.Text(" * Selecione o cargo a ser cadastrado.", size=20)],
            [sg.Listbox(values=['Analista', 'Gerencia', 'Suporte'], default_values=["Analista"], size=(30, 3),
                        key='cargo')],
            [sg.Text("Data do cadastro.", size=15)],
            [sg.Input(f"{hoje.strftime('%d/%m/%Y')}", key="data", disabled=True, size=10)],
            [sg.Button('Cadastrar', disabled=False, size=20), sg.Button("Finalizar", size=20)],
            [sg.Text("Campos com '*' são obrigatorios.", text_color="Red", size=35)],
        ]
        return sg.Window('Pré cadastro sistema integrado.', size=(350, 460), icon="login.ico", layout=layout,
                         finalize=True)


    def in_sistema():
        sg.theme("DarkTeal12")
        layout = [
            [sg.Text("CRIE SEU SISTEMA AQUI.", size=20)],
            [sg.Button('Cadastrar', disabled=False, size=20), sg.Button("Finalizar", size=20)],
        ]
        return sg.Window('Sistema integrado.', size=(380, 70), icon="login.ico", layout=layout, finalize=True)


    def executa():
        janela1, janela2, janela3, janela4 = login(), None, None, None
        while True:
            window, events, values = sg.read_all_windows()
            if events == janela1 and sg.WINDOW_CLOSED:
                break
            if window == janela1 and events == "Cadastrar":
                janela1.hide()
                janela2 = cadastrar_login()
                continue
            if window == janela2 and events == "Voltar ao login":
                janela1.un_hide()
                janela2.hide()
                continue
            ############################################
            if window == janela1 and events == "Login":
                usuario = values["usuario"]
                senha = values["senha"]
                verifica = Login()
                if len(usuario) == 0:
                    sg.popup_no_titlebar("DIGITE UM NOME DE USUARIO!", background_color="silver")
                    continue
                else:
                    lista = verifica.buscar(usuario)
                    if lista:
                        if lista[4]:
                            sg.popup_no_border("Acesso ao sistema", background_color="silver")
                            janela1.hide()
                            janela4 = in_sistema()
                            continue
                        else:
                            if usuario == lista[0] and senha == criptografia_senha.descriptografa(lista[2]):
                                janela1.hide()
                                sg.popup_no_border("Acesso ao sistema liberado.",
                                                   f"Bem vindo {lista[1]} ao pré cadastro!",
                                                   background_color="silver")
                                janela3 = pre_sistema()
                                janela3["id"].update(f"{lista[3]}")
                                janela3["nome"].update(f"{lista[1]}")
                                continue
                            else:
                                sg.popup_no_titlebar("NOME DE USUARIO OU SENHAS INCORRETOS.", background_color="silver")
                                janela1["usuario"].update("")
                                janela1["senha"].update("")
                                janela1["usuario"].set_focus()
                                continue
                    if not lista:
                        sg.popup_no_titlebar("USUARIO NÃO CADASTRADO", background_color="silver")
                        janela1["usuario"].update("")
                        janela1["senha"].update("")
                        janela1["usuario"].set_focus()
                        continue
            ###########################################
            if window == janela2 and events == "Cadastrar":
                nome = values["nome"]
                usuario = values["usuario"]
                senha = values["senha"]
                resenha = values["resenha"]
                usuario = usuario.lower()
                nome = nome.title()
                if len(usuario) == 0:
                    sg.popup_no_titlebar("Nome de usuario não pode ser VAZIO!", background_color="silver")
                    continue
                if senha == resenha:
                    senha = criptografia_senha.criptografa(senha)
                    cadastro = Login()
                    valida = cadastro.cadastrar(nome, usuario, senha)
                    if valida == 0:
                        sg.popup_no_titlebar("ERRO DE CADASTRO, POR FAVOR REDEFINA.", background_color="silver")
                        continue
                    if valida == 2:
                        sg.popup_no_titlebar("USUARIO JA CADASTRADO!", background_color="silver")
                        continue
                    else:
                        sg.popup_no_titlebar("CADASTRO EFETUADO COM SUCESSO.", background_color="silver")
                        janela2["nome"].update("")
                        janela2["usuario"].update("")
                        janela2["senha"].update("")
                        janela2["resenha"].update("")
                        janela2["nome"].set_focus()
                        continue
                else:
                    sg.popup_no_titlebar("Senhas não conferem!", "REDIGITE AS MESMAS", background_color="silver")
                    janela2["senha"].update("")
                    janela2["resenha"].update("")
                    janela2["senha"].set_focus()
                    continue
            ############################################
            if window == janela3 and events == "Cadastrar":
                pre = Login()
                idf = values["id"]
                telefone = values["telefone"]
                cargo = values["cargo"]
                data = values["data"]
                cpf = values["cpf"]

                if len(cpf) != 11:
                    sg.popup_no_titlebar("CPF precisa ter 11 numeros.", background_color="silver")
                    janela3["cpf"].update("")
                    janela3["cpf"].set_focus()
                    continue
                elif len(telefone) != 11:
                    sg.popup_no_titlebar("Telefone precisa ter 11 numeros.", background_color="silver")
                    janela3["telefone"].update("")
                    janela3["telefone"].set_focus()
                    continue
                elif not cpf:
                    sg.popup_no_titlebar("CPF não pode ser vazio.", background_color="silver")
                    janela3["cpf"].update("")
                    janela3["cpf"].set_focus()
                    continue
                elif not telefone:
                    sg.popup_no_titlebar("Telefone não pode ser vazio.", background_color="silver")
                    janela3["telefone"].update("")
                    janela3["telefone"].set_focus()
                    continue
                elif not cargo:
                    sg.popup_no_titlebar("Telefone não pode ser vazio.", background_color="silver")
                    continue
                elif len(telefone) == 11 and len(cpf) == 11:
                    t = Valida()
                    t_valida = t.v_telefone(telefone)
                    c_valida = t.v_cpf(cpf)
                    if t_valida != 0 and c_valida == 0:
                        sg.popup_no_titlebar("CPF não pode conter letras.", "REDIGITE",background_color="silver")
                        janela3["cpf"].update("")
                        janela3["cpf"].set_focus()
                        continue
                    if t_valida == 0 and c_valida != 0:
                        sg.popup_no_titlebar("Telefone não pode conter letras.", "REDIGITE",background_color="silver")
                        janela3["telefone"].update("")
                        janela3["telefone"].set_focus()
                        continue
                    else:
                        telefone = t_valida
                        sg.popup_no_titlebar(f"Seu Telefone - {telefone}", background_color="silver")
                        cpf = c_valida
                        sg.popup_no_titlebar(f"Seu CPF - {cpf}", background_color="silver")
                        data = f"{data[6:10]}/{data[3:5]}/{data[0:2]}"
                        cargo = cargo[0]
                        insere = pre.update(int(idf), cpf, cargo, telefone, data)
                        if insere == 2:
                            sg.popup_no_titlebar("CPF ja existe no sistema.", "REDIGITE", background_color="silver")
                            janela3["cpf"].update("")
                            janela3["cpf"].set_focus()
                            continue
                        else:
                            sg.popup_no_titlebar("Dados inseridos com sucesso.", background_color="silver")
                            break
            ##############################################
            if window == janela4 and events == "Cadastrar":
                sg.popup_no_titlebar("Botão Cadastrar.", background_color="silver")
                continue
            if window == janela3 and events == "Finalizar":
                sg.popup_no_titlebar("Saindo do sistema.", background_color="silver")
                break
            ###############################################
            if window == janela4 and events == "Finalizar":
                sg.popup_no_titlebar("Saindo do sistema.", background_color="silver")
                break
            if window == janela1 or window == janela2 or window == janela3 or window == janela4:
                if events == sg.WINDOW_CLOSED:
                    break


    executa()
