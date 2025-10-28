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


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[m{item}')
        c += 1
    print(linha())
    opc = leiaInt('\033[1;32mSua opção:\033[m ')
    return opc