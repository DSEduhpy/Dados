from exer14.utilidadesCEV import dados


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número inteiro!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar os dados\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            if n.is_integer():
                print('\033[1;31mError! Digite um número real válido!\033[m')
                continue
        except (ValueError, TypeError):
            print('\033[31mErro no dado! Digite novamente!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar o número.\033[m ')
            return 0
        else:
            return n


n1 = leiaInt('Digite um número inteiro: ')
n2 = dados.leiadinheiro('Digite um número real: ')
print(f'Os valores digitados foram {n1} e {n2}')
