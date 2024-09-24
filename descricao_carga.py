from cores import verde, amarelo, azul, roxo, ciano, vermelho, cinza, laranja, term

############################################################################
# QUESTÕES DE DESCRIÇÃO DA CARGA
############################################################################

# Vavriaveis globais para ter acesso no ficheiro "cronometro.py"

origem_destino = sobreponivel = zona = "1"


def info_carga():

    global origem_destino
    global sobreponivel
    global zona
    
    while True:
        try:
            cp = int(input(f"{verde}Insira o código postal entre 1000 e 8999: {term}"))
            if 1000 <= cp <= 8999:
                break
            else:
                print(f"{amarelo}Dados inválidos! O código postal deve estar entre 1000 e 8999.{term}")
        except ValueError:
            print(f"{amarelo}Dados inválidos! Por favor, insira um valor inteiro para o código postal.{term}")

    while True:                # Para facilitar, as variáveis "peso", "comp", "larg" e "alt" dizem respeito à carga completa do cliente (conjuntos de caixas/paletes completas)
        try:
            peso = int(input(f"{verde}Insira o Peso da carga (Kgs): {term}"))
            break
        except ValueError:
            print(f"{amarelo}Dados inválidos! Por favor, insira um valor inteiro para o peso.{term}")

    while True:
        try:
            comp = float(input(f"{verde}Insira o comprimento da carga (m): {term}"))
            break
        except ValueError:
            print(f"{amarelo}Dados inválidos! Por favor, insira um valor numérico para o comprimento.{term}")

    while True:
        try:
            larg = float(input(f"{verde}Insira a largura da carga (m): {term}"))
            break
        except ValueError:
            print(f"{amarelo}Dados inválidos! Por favor, insira um valor numérico para a largura.{term}")

    while True:
        try:
            alt = float(input(f"{verde}Insira a altura da carga (m): {term}"))
            break
        except ValueError:
            print(f"{amarelo}Dados inválidos! Por favor, insira um valor numérico para a altura.{term}")

    sobreponivel = ""
    while True:
        sobreponivel = input(f"{verde}A carga é sobreponível? Sim / Não {term}").upper().strip()[0]
        if sobreponivel in 'SN':
            break
        else:
            print(f"{amarelo}Dados inválidos! Por favor, insira Sim ou Não{term}")

    while True:
        origem_destino = input(f"{verde}A origem / destino é um armazem ou um ponto genérico? (Armazem ou Outros){term}: ").upper().strip()
        if origem_destino in {'ARMAZEM', 'OUTROS'}:
            break
        else:
            print(f"{amarelo}Dados inválidos! Por favor, insira 'ARMAZEM' ou 'OUTROS'.{term}")

    while True:
        zona = input(f"{verde}Insira a zona: PORTO / LISBOA: {term}").upper().strip()
        if zona in {'PORTO', 'LISBOA'}:
            break
        else:
            print(f"{amarelo}Dados inválidos! Por favor, insira 'PORTO' ou 'LISBOA'.{term}")

    return cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel


def getInputs():
    return origem_destino, sobreponivel, zona