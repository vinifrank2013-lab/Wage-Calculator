
import json


despesas = {}


def salvar_despesas():
    with open("dados.json", "w") as arquivo:
        json.dump(despesas, arquivo)


def carregar_dados():
    global despesas

    try:
        with open("dados.json", "r") as arquivo:
            despesas = json.load(arquivo)
    except FileNotFoundError:
        despesas = {}


def ver_despesas():
    print("Vamos ver as suas despesas!")

    for despesa, valor in despesas.items():
        print(f"Despesa: {despesa}")
        print(f"Valor: {valor:.2f} R$")


def calcular_despesas():
    print('\nBom dia, cliente. essa é a calculadora de despesas, criada por Vinícius Frank.')
    print("Escreva o seu número de despesas abaixo")
    nDespesas = int(input())

    for despesa in range(nDespesas):
        print("Qual o nome de sua despesa")
        nomedespesa = input()

        print("Qual o valor dessa despesa")
        valordespesa = float(input())

        despesas[nomedespesa] = valordespesa

    salvar_despesas()

    print("Me fale o seu salário mensal embaixo:")
    renda = float(input())

    total_despesas = sum(despesas.values())

    sobra = renda - total_despesas
    porcentagem_gastos = (total_despesas / renda) * 100
    lazer = sobra * 0.20
    investimentos = sobra * 0.40
    reserva = sobra * 0.40

    print(f'\nSalário: {renda:.2f} R$')
    print(f'Gastos: {total_despesas:.2f} R$')
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


def adicionar_meta():
    print("Fale o nome da sua meta:")
    nome_meta = input()

    print("Fale o Preço dessa meta")
    preço_meta = float(input())

    print("Fale quanto irá gastar por mes nessa meta:")
    gasto_pormes_meta = float(input())

    tempo_meta = preço_meta / gasto_pormes_meta

    tempo_meta = int(tempo_meta)

    print(f"Você demorará {tempo_meta} meses pra atingir a sua meta")


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

carregar_dados()

cwhile = True

while cwhile:
    print('\n----MENU----')
    print('1: Calcular despesas')
    print('2: Ver despesas')
    print('3: Calcular tempo pra metas')
    print('4: Simulador de investimentos')
    print('5: Sair')

    secao = int(input('Escolha sua seção: '))

    if secao == 1:
        calcular_despesas()

    elif secao == 2:
        ver_despesas()

    elif secao == 3:
        adicionar_meta()

    elif secao == 4:
        simular_investimentos()

    elif secao == 5:
        print("Tchau! Venha novamente")
        break

    else:
        print('Seção inválida. Tente Novamente.')