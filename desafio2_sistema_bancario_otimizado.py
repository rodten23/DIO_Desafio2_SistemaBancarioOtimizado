menu = '''
=================================================================
                     Que bom ter você aqui!                       
  O Banco ROSAMM está sempre pronto a ajudar com usas finanças.
=================================================================

Por favor, digite a opção desejada:

[D] Depositar   -   [E] Ver Extrato

[S] Sacar       -   [X] Sair do Sistema\n
'''

SALDO_INICIAL = 0
saldo = SALDO_INICIAL

saques_feitos_dia = 0
LIMITE_SAQUES = 3

LIMITE_VALOR_SAQUE = 500

extrato = ''

def mostrar_extrato():
    return

def cadastrar_cliente():
    return

def cadastrar_conta():
    return

def depositar():
    return

def sacar():
    return

def sair():
    return


while True:

    opcao = input(menu)

    if opcao == 'd':
        print('\nFAZER DEPÓSITO (aceitamos apenas notas):')
        valor_deposito = float(input('\nPor favor, qual valor será depositado? => '))
        while True:
            if valor_deposito < 2:
                valor_deposito = float(input('\nInfelizmente não aceitamos moedas.\nFavor, informe novamente o valor a ser depositado => '))
            else:
                saldo += valor_deposito
                extrato += f'\nDepósito de R$ {valor_deposito:.2f}  (Saldo de R$ {saldo:.2f})'
                break

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
