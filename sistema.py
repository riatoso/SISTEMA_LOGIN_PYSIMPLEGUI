from conexao_banco import nova_conexao as conectar
import pymysql


class Login:
    def cadastrar(self, nome, usuario, senha):
        if conectar() != 0:
            inserir = f"""insert into login.usuario (nome, usuario ,senha) 
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
                            lista = [i[1], i[2], i[3], i[0], i[4]]
                            # print(i)
                            return lista
                except pymysql.err.IntegrityError as intg:
                    return lista
                except:
                    return lista

    def update(self, idf, cpf, cargo, telefone, datacad):
        if conectar() != 0:
            altera = f"""update usuario set cpf='{cpf}', cargo='{cargo}', telefone='{telefone}',datacad='{datacad}'
                        where id = '{idf}'"""
            with conectar() as conexao:
                try:
                    cursor = conexao.cursor()
                    cursor.execute(altera)
                    conexao.commit()
                    return 1
                except pymysql.err.IntegrityError as err1:
                    return 2
                except:
                    return 0

