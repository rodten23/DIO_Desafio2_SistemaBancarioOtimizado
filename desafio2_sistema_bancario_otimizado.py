menu = '''
=================================================================
                     Que bom ter você aqui!                       
  O Banco ROSAMM está sempre pronto a ajudar com usas finanças.
=================================================================

Por favor, digite a opção desejada:

[D] Depositar   -   [E] Ver Extrato

[S] Sacar       -   [X] Sair do Sistema\n
'''
clientes = []

contas = []

SALDO_INICIAL = 0
saldo = SALDO_INICIAL

saques_feitos_dia = 0
LIMITE_SAQUES = 3

LIMITE_VALOR_SAQUE = 500

extrato = ''

def mostrar_extrato(saldo, extrato):
    # Função extrato deve receber os argumentos por posição e nome (positional only e keyword only)
    # Argumento posicional: saldo e argumento nomeado: extrato
    return

def formatar_data_nascimento(data_nascimento):
    data_nasc_formatada = f'{data_nascimento[0:2]}/{data_nascimento[2:4]}/{data_nascimento[4:8]}'
    return data_nasc_formatada

def cadastrar_cliente():
    nome = input('Por favor, digite o seu nome completo: ')
    data_nascimento = int(input('Qual sua data de nascimento? (com 8 dígitos): '))
    data_nasc_formato_8 = formatar_data_nascimento(data_nascimento)
    cpf = int(input('Agora digite o seu CPF (apenas números): '))
    logradouro = input('Agora vamos cadastrar seu endereço residencial.\nPor favor, digite o logradouro (rua, avenida, travessa): ')
    numero = int(input('Digite o número da residência: '))
    bairro = input('Agora pode inserir o seu bairro: ')
    cidade = input('Qual sua cidade: ')
    sigla_estado = input('Por fim, informe a sigla do seu estado: ')
    endereço = f'{logradouro}, {numero} - {bairro} - {cidade}/{sigla_estado}'

    while cpf in clientes:
        break

    return

def cadastrar_conta():
    # Deve-se ter uma lista de contas, onde cada conta é composta por agência, número da conta e usuário.
    # O número das contas é sequencial, iniciando em 1.
    # O número da agência é fixo: "0001". Cada usuário pode ter mais de uma conta, cada conta pertence a somente um usuário.
    return

def depositar(saldo, valor_deposito, extrato):
    # Função de depósito deve receber os argumentos apenas por posição (positional only)
    while True:
        if valor_deposito < 2:
            valor_deposito = float(input('\nInfelizmente não aceitamos moedas.\nFavor, informe novamente o valor a ser depositado => '))
        else:
            saldo += valor_deposito
            extrato += f'\nDepósito de R$ {valor_deposito:.2f}  (Saldo de R$ {saldo:.2f})'
            break

    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limites_saques):
    # Função de saque deve receber argumentos apenas por nome (keyword only)
    return saldo, extrato

def sair():
    return


while True:

    opcao = input(menu)

    if opcao == 'd':
        print('\nFAZER DEPÓSITO (aceitamos apenas notas):')
        valor_deposito = float(input('\nPor favor, qual valor será depositado? => '))
        deposito, nova_linha_extrato = depositar(saldo, valor_deposito, extrato)
        saldo += deposito
        extrato += nova_linha_extrato

    elif opcao == 's':
        print(f'\nEFETUAR SAQUE (disponibilizamos apenas notas)\nLimites: até {LIMITE_SAQUES} saques diários totalizando até R$ {LIMITE_VALOR_SAQUE:.2f} por saque.')
        
        if saques_feitos_dia == LIMITE_SAQUES:
            print(f'Você atingiu o limite diário de {LIMITE_SAQUES} saques.\nNovos saques poderão ser feitos no próximo dia útil.\n')
        
        else:
            valor_saque = float(input('\nPor favor, quanto você quer sacar?\nOu digite 0 para voltar ao menu principal\n=> '))
            while True:
                if valor_saque == 0:
                    break
                elif valor_saque < 2:
                    valor_saque = float(input('\nInfelizmente não disponibilizamos moedas.\nFavor, informe novamente o valor que deseja sacar ou digite 0 para voltar=> '))
                elif valor_saque > saldo:
                    valor_saque = float(input('\nVocê não tem saldo suficiente.\nFavor, informe novamente o valor que deseja sacar ou digite 0 para voltar=> '))
                elif valor_saque > LIMITE_VALOR_SAQUE:
                    valor_saque = float(input(f'\nCada saque pode ser de no máximo R$ {LIMITE_VALOR_SAQUE:.2f}.\nFavor, informe novamente o valor que deseja sacar ou digite 0 para voltar=> '))         
                else:
                    saldo -= valor_saque
                    saques_feitos_dia += 1
                    extrato += f'\nSaque de R$ {valor_saque:.2f}  (Saldo de R$ {saldo:.2f})'
                    break

    elif opcao == 'e':
        print('\nEXIBIR EXTRATO')
        print(f'\nSaldo inicial => R$ {SALDO_INICIAL:.2f}')
        
        if extrato == '':
            print('\nAinda não foram feitos depósitos ou saques para esta conta.')
        else:
            print(extrato)
        input('\nPressione qualquer tecla para voltar ao menu anterior: ')
        
    elif opcao == 'x':
        print('\nSaindo do Sistema...\n')
        break

    else:
        print('\nOperação inválida! Por favor, selecione novamente a operação desejada.\n')
