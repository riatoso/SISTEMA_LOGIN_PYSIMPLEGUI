from conexao_banco import nova_conexao as conectar
import pymysql


class Login:
    def cadastrar(self, nome, usuario, senha):
        if conectar() != 0:
            inserir = f"""INSERT INTO login.usuario (nome, usuario ,senha) 
                        values ('{nome}', '{usuario}', '{senha}')"""
            with conectar() as conexao:
                try:
                    cursor = conexao.cursor()
                    cursor.execute(inserir)
                    conexao.commit()
                    return 1
                except pymysql.err.IntegrityError as intg:
                    return 2
                except:
                    return 0

    def buscar(self, usuario):
        if conectar() != 0:
            seleciona = f"select * from login.usuario where usuario = '{usuario}'"
            with conectar() as conexao:
                try:
                    cursor = conexao.cursor()
                    cursor.execute(seleciona)
                    if not cursor:
                        lista = []
                        return lista
                    else:
                        for i in cursor:
                            lista = [i[1], i[2], i[3]]
                            # print(i)
                            return lista
                except pymysql.err.IntegrityError as intg:
                    return lista
                except:
                    return lista

