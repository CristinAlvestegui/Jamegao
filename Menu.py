import this
import Crud

this.opcao = -1

def pegarvo():
    print('Por favor informe o caminho do arquivo ou pasta')
    atal = input()
    Crud.inseriatal(atal)
    

#def jamegarfile(jameg=atal):
    #print('Informe o nome do Jamego que deseja consultar: ')
    #jameg = input()
    #jameg.open(atal)

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
            Crud.abrirpasta()
            pegarvo()
            print('Informe o nome do novo Jamego: ')
            jameg = input()
            Crud.inserijame(jameg)
        elif this.opcao == 2:
            Crud.consutodo()
        elif this.opcao == 3:
            print('Escolha uma Jamegão para editar')
            Crud.consutodo()
            jameg = input()
            print('Informe o novo nome do Jamegão')
            novjame = input()
            Crud.atualijame(novjame, jameg)
        elif this.opcao == 4:
            print('Simplesmente não :(')
            jameg = input()
            Crud.excluirjame(jameg)
        elif this.opcao == 5:
            Crud.abrirpasta()
            pegarvo()
            print('Informe o nome do novo Jamego: ')
            jameg = input()
            Crud.inserijame(jameg)
