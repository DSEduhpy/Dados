from utilidadesCEV import moedas
from utilidadesCEV import dados

preco = dados.leiadinheiro('Digite o preço: R$')
moedas.resumo(preco, 10, 20)