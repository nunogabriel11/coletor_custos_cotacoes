from tabelas_excel import OVS_CL1_PORTO_ARM, OVS_CL1_LISBOA_ARM, OVS_CL1_PORTO_A_B, OVS_CL1_LISBOA_A_B
from selecao_tabelas import sem_exc, com_exc
from cores import verde, amarelo, term, vermelho, ciano, laranja
from descricao_carga import info_carga
from cw_ldm import taxavel_estrado

def overseas():
    while True:
        print(f'''              {vermelho}Menu Overseas{term}        
            {ciano}[1] Cliente OVS_CL1
            [2] Sair de Overseas{term}''')

        escolha = input(f"{laranja}Selecione uma opção: {term}")

        if escolha == "1":
            print("Selecionou o Cliente OVS_CL1")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = OVS_CL1_PORTO_ARM
                nome_cliente = "OVS_CL1_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                tabela = OVS_CL1_LISBOA_ARM
                nome_cliente = "OVS_CL1_LISBOA_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "OUTROS" and zona == "PORTO":
                tabela = OVS_CL1_PORTO_A_B
                nome_cliente = "OVS_CL1_PORTO_A_B"
                taxavel = 300
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                tabela = OVS_CL1_LISBOA_A_B
                nome_cliente = "OVS_CL1_LISBOA_A_B"
                taxavel = 300
                metro_estrado = 1500
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

            


        elif escolha == "2":
            break
        else:
            print("Opção inválida! Tente novamente.")
