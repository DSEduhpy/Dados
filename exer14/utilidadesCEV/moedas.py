def metade(v=0, formato=False):

    res = v / 2
    return res if not formato else moeda(res)


def dobro(v=0, formato=False):
    """
    Calcula o dobro de um valor numérico.

    Args:
        v (float, optional): Valor a ser dobrado. Defaults to 0.
        formato (bool, optional): 
            Se True, retorna o resultado formatado como moeda. 
            Se False, retorna apenas o número. Defaults to False.

    Returns:
        float | str: O dobro do valor, formatado ou não.
    """
    res = v * 2
    return res if not formato else moeda(res)


def aumento(v=0, taxa = 22, formato=False):
    res = v + (v * 22 / 100)
    return res if not formato else moeda(res) 


def diminuir(v=0, taxa=13, formato=False):
    res = v - (v * 13 / 100)
    return res if not formato else moeda(res)


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.',',' )


def resumo(v=0, taxaa=13, taxar=5):
    print('-'*36)
    print('RESUMO DOS VALORES'.center(36))
    print('-'*36)
    print(f'Analisando o valor: \t{moeda(v)}')
    print(f'Dobro de {moeda(v)}: \t{dobro(v, True)}')
    print(f'Metade de {moeda(v)}: \t{metade(v, True)}')
    print(f'Aumento de {taxaa}%: \t{aumento(v, taxaa, True)}')
    print(f'Redução de {taxar}%: \t{diminuir(v, taxar, True)}')    
    print('-'*36)



'''
código: .center() -> PARA CENTRAALIZAR
'''