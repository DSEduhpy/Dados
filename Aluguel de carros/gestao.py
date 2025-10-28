
from time import sleep
print('='*11)
print('\033[1;36mBem - vindo à locadora de carros!\033[m ')
print('='*11)
print('\033[32mO que deseja fazer?\033[m')

carros = { 1:('Fiat Mobi Like 1.0', 95),
2: ('Chevrolet Onix 1.0', 120),
3: ('Hyundai HB20 1.0 Comfort', 130),
4: ('Volkswagen Polo 1.0 TSI', 150),          
5: ('Jeep Renegade 1.3 Turbo', 220),
6: ('Volkswagen T-Cross 1.0', 210),
7: ('Toyota Corolla 2.0', 280),
8: ('Honda HR-V Touring 1.5 Turbo', 300)}

alugados = []

while True:
    print(f'\033[1;33mDISPONÍVEIS: {len(carros)}\033[m   |   \033[1;31mALUGADOS: {len(alugados)}\033[m')
    print('-='*10)
    
    opcao = int(input('''\033[33m1 - \033[34mMostrar portifólio\033[m 
\033[33m2 - \033[34mAlugar um carro\033[m
\033[33m3 - \033[34mDevolver um carro\033[m 
'''))
    print('-='*17)
    
    if opcao == 1:
        for c, v in carros.items():
            print(f'\033[35m{c:<3} \033[1;36m{v[0]:<30}\033[m')
        print('-='*17)

        resp = int(input('''\033[1;32m1  -  Continuar  |  2  -  Sair\033[m 
'''))
        if resp == 2:
            print()
            print('\033[32mSaindo do Portifólio...\033[m')
            sleep(1)
            print('\033[33m<<< Volte sempre! >>>\033[m')
            break
        else:
            continue

    elif opcao == 2:
        print('\033[35m[ ALUGAR ] Dê uma olhada em nosso portifólio\033[m')
        for c, v in carros.items():
            print(f'\033[35m{c:<3} {v[0]:<30} \033[36mR${v[1]:>7},00 / diária\033[m')
        print('-'*70)
        escolha = int(input('\033[1;33mEscolha o código do carro: \033[m'))
        if escolha not in carros:
            print('\033[31mCódigo inválido!\033[m')
            continue
        aluguel = int(input('\033[32mQuantos dias você quer alugar? \033[m'))
        valor = carros[escolha][1] * aluguel
        print(f'\033[32mVocê escolheu o carro \033[1;36m{carros[escolha][0]} \033[32malugando por \033[1;33m{aluguel} \033[32mdias.\033[m')
        print(f'\033[34mO aluguel saiu por \033[35mR${valor:.2f}.')
        print('\033[34mDeseja alugar? \033[m')
        cont = int(input('\033[35m0 - SIM | 1 - NÃO    \033[m'))
        if cont == 0:
            alugados.append((escolha, carros[escolha]))
            if escolha in carros:
                del carros[escolha]
            print('\033[1;34mParabéns! Você fez a sua melhor escolha!\033[m ')
        else:
            continue
        print()
    
    if opcao == 3:
        if not alugados:
            print('\033[31mNão tem nenhum carro alugado!\033[m ')
            print('='*10)
        else:
            print('\033[33mQual carro você quer devolver?\033[m')
            for i, (c,v) in enumerate(alugados):
                print(f'\033[35m[{i+1}] -> {v[0]}\033[m')
            devolver = int(input('\033[1;32mEscolha o código que queira devolver. \033[m')) - 1
            if 0 <= devolver < len(alugados):
                c , v = alugados.pop(devolver)
                carros[c] = v
                print(f'\033[1;32mO carro {v[0]} foi devolvido com sucesso!\033[m')
            else:
                print('\033[1;31mOpção inválida!\033[m ')
                