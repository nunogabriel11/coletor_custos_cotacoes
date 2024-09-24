### A FAZER: ###
# DONE - Substituir o menu de cada setor pelas tabelas adequadas
# DONE - Fazer lista das tabelas necessárias em falta
# DONE - Inserir Dataset OVS + código para experimentar
# DONE - Fazer o mesmo para restantes setores
# DONE Reestruturar tabelas que dão para alterar
# DONE - Falar com o Pedro / Paulo sobre tabelas que são diferentes para criar estrutura base igual às outras
# DONE Inserir novos Datasets (Ver caderno WrLg perguntas e respostas Pedro Lira)
# DONE - Na tabela à parte dos clientes de cada setor, colocar os casos específicos com alteração de cw e ldm (diferentes de 333,33 e 1750)
# DONE - Ver questão dos "ldm". Tentar colocar como base 1750 associado a uma variável, e para os casos especiais, alterar o valor da variável para essa tabela específica
# DONE - Fazer o mesmo para "cw"
# DONE - Quando o cd não existe, está a retribuir o dataset (Corrigir)
# DONE - Fazer Manutenção preventiva ou Execução defensiva nas variáveis de entrada.
# DONE NÃO ESQUECER DE CRIAR CÓDIGO E TABELAS IGUAIS, MUDAR O NOME DOS CLIENTES E APLICAR UMA TAXA ALEATÓRIA ENTRE 0.7 E 1.3 PARA OS CUSTOS OU TEMPOS (FAZER RANDOM E APLICAR)
# DONE Colocar fator de LDM e de CBM fixo para cada tabela (pode-se colocar print para o utilizador saber qual o valor dessa tabela- titulo de curiosidade)
# - Colocar comentários em cada ficheiro .py para facilitar compreensão
# - Resolver problema de tipos de cargas (paletes, caixas, tubos, número) - mudar código e tese



######################################################################################
# MENU PRINCIPAL
######################################################################################

from colorama import Fore, Style, init
from menu_distribuicao import distribuicao
from menu_gestao_de_stocks import gestao_de_stocks
from menu_overseas import overseas
from menu_roadfreight import roadfreight
from cores import laranja
#import time
#from cronometro import iniciar_tempo, wb


init(autoreset=True) # Iniciar a biblioteca de cores (colorama)

def menu_principal():
    #iniciar_tempo()

    while True:
        print(f''' {Fore.RED}Menu Principal{Style.RESET_ALL}          
        {Fore.CYAN}[1] Distribuição
        [2] Gestão de Stocks
        [3] Overseas
        [4] RoadFreight
        [5] Sair do programa{Style.RESET_ALL} ''')

        escolha = input(f"{laranja}Selecione uma opção: {Style.RESET_ALL}")

        if escolha == '1':
            distribuicao()
        elif escolha == '2':
            gestao_de_stocks()
        elif escolha == '3':
            overseas()
        elif escolha == '4':
            roadfreight()
        elif escolha == '5':
            print(f"{Fore.RED}Fim do programa...{Style.RESET_ALL}")
            #wb.save("./excel_tempos/tempos.xlsx")  # Guardar a cronometragem
            break
        else:
            print(f"{Fore.MAGENTA}Opção inválida! Tente novamente.{Style.RESET_ALL}")

if __name__ == "__main__":
    menu_principal()
