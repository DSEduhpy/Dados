from lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #nome: Nome do arquivo / 'rt: Texto = Arquivo em texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # wt+: Cria um arquivo de texto e coloca o nome
        a.close()
    except:
        print('\033[31mHouve um erro na criação de um arquivo!\033[m')
    else:
        print(f'\033[1;32mArquivo {nome} criado com sucesso!\033m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>3} anos')
    finally:
        a.close() # Para fechar o arquivo, usa o comando digitado.

def cadastrar(arq, nome = '<desconhecido>', idade = 0):
    try:
        a = open(arq, 'at') # O 'at', vai criar o arquivo com o nome e a idade 
    except:
        print('\033[1;31mHouve um ERRO na abertura o arquivo"\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n') #a.write = Para escrever no arquivo:
        except:
            print('\033[1;31mHouve um ERRO ao escrever no arquivo!\033[m')
        else:
            print(f'\033[1;32mNovo registro de {nome} cadastrado!\033[m')
            a.close()



