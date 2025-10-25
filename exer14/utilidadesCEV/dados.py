def leiadinheiro(msg):
    válido = False
    while not válido:
        entrada = input(msg).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO! \"{entrada}\" é um valor inválido!\033[m')
        else:
            válido = True
            return float(entrada)
