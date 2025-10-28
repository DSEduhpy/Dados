from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'dseduh.txt'
 
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['\033[36mVer pessoas cadastradas\33[36m', '\033[36mNovo cadastro\033[36m', '\033[36mSair do sistema\033[m'])
    if resp == 1:
        # Ler arquivo criado:
        lerArquivo(arq)


    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = input('Digite o nome: ')
        idade = leiaInt('Digite a idade: ')
        cadastrar(arq, nome, idade)
        
    elif resp == 3:
        cabeçalho('\033[35mFinalizando o sistema...\033[m')
        sleep(1)
        cabeçalho('\033[34mObrigado! Volte sempre!\033[m')
        break
    else:
        print('\033[1;31mERROR: Digite uma opção válida!\033[m')
        sleep(2)