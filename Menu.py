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
        '2. Consultar Jamegões\n'                        +
        '3. Consultar Atalhos\n'                         +
        '4. Editar Jamegão\n'                            +
        '5. Desativar Jamegão\n'                         +
        '6. Escolher outro arquivo\n'                    +
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
            print('Escolha uma Jamegão consultar')
            jameg = input()
            Crud.consujoin(jameg)
        elif this.opcao == 3:
            print('Qual atalho deseja abrir?')
            Crud.consutodoatal()
            print('Informe a pasta e Subpasta: ')
            atal = input()
            Crud.joinfiles(atal)
            novjame = input()
            Crud.atualijame(novjame, jameg)
        elif this.opcao == 4:
            print('Escolha uma Jamegão para editar')
            Crud.consutodo()
            jameg = input()
            print('Informe o novo nome do Jamegão')
        elif this.opcao == 5:
            Crud.consutodo()
            print('Escolha um Jamegão para desativar:')
            jameg = input()
            Crud.excluirjame(jameg)
        elif this.opcao == 6:
            Crud.abrirpasta()
            pegarvo()
            print('Informe o nome do novo Jamego: ')
            jameg = input()
            Crud.inserijame(jameg)
