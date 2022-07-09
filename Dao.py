import mysql.connector
from mysql.connector import errorcode

def connection():
    try:
        db_connect = mysql.connector.connect(host='localhost', user='root', password='', database='Jamegao')
        print('Conexão sucedida!')
        return db_connect
    except mysql.connector.Error as erro:
        if erro.errno == errorcode.ER_BAD_DB_ERROR:
            print('Banco de dados não existe!, {}'.format(erro))
        else:
            print(erro)
    else:
        db_connect.close()