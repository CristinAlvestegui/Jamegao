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
    
def consutodo():
    try:
        sql = 'select * from Jamegoes'
        con.execute(sql)
        for(jameg) in con:
            print("Jameg: {}".format(jameg))
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

def abrirpasta():
    arvo = 'C:\\Users\\calve\\Documents\\'
    print('\nBem-vindo ao seu diretorio!\n')
    for arvo, dirs, files in os.walk(arvo):
        if not dirs:
            print('A pasta: ', arvo, 'não possui subpastas')
        else:
            print('A pasta: ', arvo, 'possui as subpastas:')
            for sub in dirs:
                print('\t\t', sub)
        if not files:
            print('\t não possui arquivos')
            print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')
        else:
            print('\t e os arquivos: ')
            for files in files:
                print('\t\t', files)

def pegarvo():
    print('Por favor informe a subpasta e o nome do arquivo:')
    atal = input()
    inseriatal(atal)
    Menu.executar()

def joinfiles():
    os.path.join('r', '' + arvo, 'r', '' + atal)
