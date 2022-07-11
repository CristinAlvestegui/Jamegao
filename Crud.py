import Dao
import os


db_connect = Dao.connection()
con = db_connect.cursor()

def inserijame(nome):
    try:
        sql = "insert into Jamegoes(jameg) values('{}')".format(nome)
        con.execute(sql)
        db_connect.commit()
        print("{} Inserido".format(con.rowcount))
    except Exception as erro:
            print(erro)
            
def inseriatal(nome):
    try:
        sql = "insert into Atalho(atal) values('{}')".format(nome)
        con.execute(sql)
        db_connect.commit()
        print("{} Inserido".format(con.rowcount))
    except Exception as erro:
            print(erro)

def consujame(nome):
    try:
        sql = "select * from Jamegoes where jameg = '{}'".format(nome)
        con.execute(sql)
        for(jameg) in con:
            print("jameg: {}".format(nome))
    except Exception as erro:
        print(erro)
        
def consuatal(nome):
    try:
        sql = "select * from Atalho where atal = '{}'".format(nome)
        con.execute(sql)
        for(atal) in con:
            print("jameg: {}".format(nome))
    except Exception as erro:
        print(erro)

def atualijame(nome,novoNome):
    try:
        sql = "update Jamegoes set {} = '{}' where jameg = '{}'".format(nome, novoNome)
        con.execute(sql)
        db_connect.commit()
        print('{} Atualizado!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def excluirjame(nome):
    try:
        sql = "delete from Jamegoes where jameg = '{}'".format(nome)
        con.execute(sql)
        db_connect.commit()
        print('{} Excluido!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def abripasta():
    print('\nBem-vindo ao seu diretorio!\n' +
            '\nEscolha um arquivo: ')
    arvo ='C:\\Users\\cristina.asubieta\\Documents\\' #'C:\\Users\\calve\\Documents'
    for (root, dirs, files) in os.walk(arvo):
        print(root)
        print(dirs)
        print(files)
        print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')


