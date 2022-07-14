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
        
def consujoin(nome):
    try:
        sql = "SELECT (atal) FROM Atalho WHERE jameg = '{}'".format(nome)
        con.execute(sql)
        for (atal) in con:
            print('Atalho: {}'.format(atal))
    except Exception as erro:
        print(erro)

def consuljoin2(nome):
    try:
        sql = "SELECT (atal), (jameg) as Jamegoes from Jamegoes"
        sql2 = "inner join Atalho"
        sql3 = "on cod_jameg = cod_atal"
        con.execute(sql, sql2, sql3)
        for (atal, jameg) in con:
            print('Atalho: {} , JAmeg: {}'.format(atal, nome))
    except Exception as erro:
        print(erro)

def consudois(nome):
    try:
        tentei = "SELECT Jamegoes.* , Atalho.* FROM Jamegoes FULL OUTER JOIN Jamegoes ON Jamegoes.jameg = Atalho.atal"
        sql = "select * from Jamegoes where jameg = '{}'".format(nome)
        sql2 = "select * from Atalho where atal = '{}'".format(nome)
        con.execute(tentei)
        for (nome, nome2) in con:
            print("Jameg: {}" , "Atalho: {}".format(nome, nome2))
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
    path = r'C:\Users\calve\Documents'
    cami = os.path.join(path, r'\Users\calve\Documents', atal)
    print(cami)
