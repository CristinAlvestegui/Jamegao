import this
import Crud

this.opcao = -1

def pegArvo():
    print('Por favor informe o caminho do arquivo ou pasta')
    atal = input()
    Crud.InserirAtal(atal)
    executar()
    

def jamegarFile(jameg=atal):
    print('Informe o nome do Jamego que deseja consultar: ')
    jameg = input()
    jameg.open(atal)

def menu():
    print('\nEscolha umas das alternativas abaixo: \n\n' +
        '1. Cadastrar Jamegão\n'                         +
        '2. Consultar Jamegão\n'                         +
        '3. Editar Jamegão\n'                            +
        '4. Desativar Jamegão\n'                         +
        '5. Escolher outro arquivo\n'                    +
        '0. Sair\n')
    this.opcao = int(input())


def executar():
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            print('Informe o nome do novo Jamego: ')
            jameg = input()
            Crud.inseriJame(jameg)
        elif this.opcao == 2:
            print('Informe o nome do Jamego que deseja consultar: ')
            jameg = input()
            Crud.consuJame(jameg)
            Crud.consuAltal(atal)
        elif this.opcao == 3:
            print('Informe o nome que deseja atualizar: ')
            jameg = input()
            Crud.atualiJame(jameg)
        elif this.opcao == 4:
            print('Simplesmente não :(')
            jameg = input()
            Crud.excluirJame(jameg)
        elif this.opcao == 5:
            Crud.abrirPasta()
            pegArvo()
