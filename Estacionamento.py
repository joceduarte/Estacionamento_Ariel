'''
Desenvolva uma aplicação Python que utilize ao menos 2 coleções e funções, para que seja possível 
realizar o cadastro de veículos em um estacionamento com o seguinte menu:
1 - Estacionar veículo
2 - Retirar veículo
3 - Veículos estacionados
4 - Está estacionado?
0 - Sair
Deve gravar a placa do veículo que será a chave, marca, modelo, cor e proprietário.
'''
estacionar = {}

def menu():
    print('---Bem Vindo ao Estacionamento---')
    print('1 - Estacionar Veiculo - ')
    print('2 - Retirar o veiculo -')
    print('3 - Veiculos no Estacionamento - ')
    print('4 - O veiculo está estacionado ?')
    print('0 - Sair - ')

def Estacionar_Veiculo(estacionar):
    placa = input('Digite a Placa do Veiculo: ').upper()
    if placa in estacionar:
        print('Veiculo Estacionado!')
        return
    
    marca = input('Digite a Marca do Veiculo: ')
    modelo = input('Informe o modelo do Veiculo: ')
    cor = input('Digite a Cor do Veiculo: ')
    proprietario = input('Informe o nome do proprietario: ')
    
    veiculo = { 
        'marca': marca,
        'modelo': modelo,
        'cor' : cor,
        'proprietario' : proprietario,
        }


    estacionar[placa] = veiculo 
    print('-' * 40)
    print(f'Veiculo {placa} esta estacionado!')
    print('-' * 40)


def Retirar_o_veiculo(estacionar):
    placa = input('Digite a placa do veiculo para a Retirada: ')
    if placa in estacionar:
        del estacionar[placa]
        print('-' * 40)
        print(f'O Veiculo {placa} foi retirado do estacionamento!')
        print('-' * 40)
    else:
        print('Veiculo nao se encontra no estacionamento! tentar novamente...')


def veiculos_estacionados(estacionar):
    if estacionar:
        print('Veiculos no estacionamento: ')
        print('-' * 40)
        for placa, veiculo in estacionar.items():
            print(f'Placa: {placa}')
            print(f'Marca: {veiculo['marca']}')
            print(f'Modelo: {veiculo['modelo']}')
            print(f'Cor: {veiculo['cor']}')
            print(f'Proprietario: {veiculo['proprietario']}')
            print('-' * 40)
    else: 
        print('Veiculo não encontrado no estacionamento!!!')


def veiculo_estacionado(estacionar):
    placa = input('Digite a placa do Veiculo: ').upper()
    if placa in estacionar:
        print('-' * 40)
        print(f'Veiculo {placa} esta Estacionado!')
        print('-' * 40)
    else:
        print(f'Veiculo {placa} não esta no estacionamento.')




def main():
    
    carro_inicial = {
        'marca': 'HIUNDAY',
        'modelo': 'Sonata',
        'cor': 'Preto',
        'proprietario': 'Jocemar Duarte'
    }
    estacionar['ABC-123'] = carro_inicial
    while True:
        menu()
        opcao = input('Escolha uma opção para informação desejado: ')
        
        if opcao == '1':
            Estacionar_Veiculo(estacionar)
        elif opcao == '2':
            Retirar_o_veiculo(estacionar)
        elif opcao == '3':
            veiculos_estacionados(estacionar)
        elif opcao == '4':
            veiculo_estacionado(estacionar)
        elif opcao == '0':
            confirmar = input('Desejar sair? (S/N): ').upper()
            if confirmar == 'S':
                print('-' * 40)
                print('Volte Sempre! E boa Viagem...')
                print('-' * 40)
                break
        else:
            print('-' * 40)
            print('Opção não valida, Tente Novamente!')
            print('-' * 40)



if __name__=='__main__':
    main()