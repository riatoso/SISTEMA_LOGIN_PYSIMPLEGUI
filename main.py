import PySimpleGUI as sg
from sistema import Login
from datetime import datetime
import criptografia_senha

if __name__ == "__main__":
    hoje = datetime.now()


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


    def cadastrar():
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
            [sg.Button('Cadastrar', disabled=False, size=20), sg.Button('Voltar ao Login', size=20)],
        ]
        return sg.Window('Cadastro de login.', icon="login.ico", layout=layout, finalize=True)


    def menu_sistema():
        sg.theme("DarkTeal12")
        layout = [
            [sg.Text("Nome do funcionário.", size=20)],
            [sg.Input(key="nome", disabled=True, size=45)],
            [sg.Text("CPF.", size=20)],
            [sg.Input(key="cpf", size=15)],
            [sg.Text("Telefone.", size=20)],
            [sg.Input(key="telefone", size=15)],
            [sg.Text("Cargo.", size=20)],
            [sg.Input(key="cargo", size=15)],
            [sg.Text("Data do cadastro.", size=15)],
            [sg.Input(f"{hoje.strftime('%d/%m/%Y')}", key="data", disabled=True, size=10)],
            [sg.Button('Cadastrar', disabled=False, size=20), sg.Button("Finalizar", size=20)],
        ]
        return sg.Window('Sistema Principal.', icon="login.ico", layout=layout, finalize=True)


    def sistema():
        janela1, janela2, janela3 = login(), None, None
        while True:
            window, events, values = sg.read_all_windows()
            if events == janela1 and sg.WINDOW_CLOSED:
                break
            if window == janela1 and events == "Cadastrar":
                janela1.hide()
                janela2 = cadastrar()
                continue
            if window == janela2 and events == "Voltar ao Login":
                janela2.hide()
                janela1.un_hide()
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
                        if usuario == lista[0] and senha == criptografia_senha.descriptografa(lista[2]):
                            janela1.hide()
                            sg.popup_no_border("Acesso ao sistema liberado.", f"Bem vindo {lista[1]} ao sistema!",
                                               background_color="silver")
                            janela3 = menu_sistema()
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
                sg.popup_no_titlebar("Inserindo dados.", background_color="silver")
                continue
            if window == janela3 and events == "Finalizar":
                sg.popup_no_titlebar("Saindo do sistema.", background_color="silver")
                break
            if window == janela1 or window == janela2 or window == janela3:
                if events == sg.WINDOW_CLOSED:
                    break


    sistema()
