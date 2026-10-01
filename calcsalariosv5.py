def calcular_despesas():
    print('\nBom dia, cliente. essa é a calculadora de despesas, criada por Vinícius Frank.')
    print('Na primeira linha, ponha o salario, na segunda sua luz, na terceira, sua agua, na quarta, sua internet,')
    print('Na quinta, ponha suas outras despesas')
    https://www.onlinegdb.com/#editor_1
    renda = float(input('Digite seu Salário total: '))
    luz = float(input('Digite sua Conta de luz: '))
    agua = float(input('Digite sua Conta de Àgua: '))
    internet = float(input('Digite sua conta de internet: '))
    despesasgeral = float(input('Digite suas outras Despesas: '))
    
    despesas = luz + agua + internet + despesasgeral
    sobra = renda - despesas
    porcentagem_gastos = (despesas / renda) * 100
    lazer = sobra * 0.20
    investimentos = sobra * 0.40
    reserva = sobra * 0.40

    print(f'\nSalário: {renda:.2f} R$')
    print(f'Gastos: {despesas:.2f} R$')
    print(f'Saldo: {sobra:.2f} R$')

    if porcentagem_gastos < 20:
        print('Você economiza muito bem. Deveria guardar seus lucros em uma poupança.')
    elif porcentagem_gastos == 100:
        print('Você gastou tudo que ganhou. Melhore seus gastos!')
    elif porcentagem_gastos < 100:
        print('Você economizou Bem! continue assim!')
    else:
        print('Seu saldo ficou no negativo. que pena. Melhore na próxima!')
        
    if porcentagem_gastos < 100:
        print('\nComo usar seu Dinheiro:')
        print(f'Gaste em Investimentos: {investimentos:.2f} R$')
        print(f'Guarde esse dinheiro: {reserva:.2f} R$')
        print(f'Use esse Dinheiro como quiser: {lazer:.2f} R$')


def simular_investimentos():
    print('\nOnde deseja Investir?')
    print('1- Poupança (0,5% ao mês)')
    print('2- CDB (0,8% ao mês)')
    print('3- Ações (1,2% ao mês)')
 
    local = int(input('Escolha a opção: '))
    opcao_valida = True
    
    if local == 1:
        taxa = 0.005
        nome = 'Poupança'
    elif local == 2:
        taxa = 0.008
        nome = 'CDB'
    elif local == 3:
        taxa = 0.012
        nome = 'Ações'
    else:
        print('Opção Inválida')
        opcao_valida = False

    if opcao_valida:
        salario = float(input('Digite a quantidade que irá investir: '))
        meses = int(input('Digite quantos meses Você deixará o dinheiro: '))
        
        for i in range(meses):
            salario = salario * (1 + taxa)
     
        print(f'\nInvestindo em {nome} por {meses} meses:')
        print(f'Seu dinheiro total final será: {salario:.2f} R$')


# --- LOOP PRINCIPAL DO PROGRAMA ---
cwhile = True

while cwhile:
    print('\n----MENU----')
    print('1: Calcular despesas')
    print('2: Simulador de investimentos')
    print('3: Sair')
    secao = int(input('Escolha sua seção: '))

    if secao == 1:
        calcular_despesas()  # Chama a função de despesas
    elif secao == 2:
        simular_investimentos()  # Chama a função de investimentos
    elif secao == 3:
        print('Saindo do programa. Até logo!')
        cwhile = False
    else:
        print('Seção inválida. Tente novamente.')
