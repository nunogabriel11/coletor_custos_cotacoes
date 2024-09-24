from tabelas_excel import RDF_CL1_PORTO_ARM, RDF_CL1_LISBOA_ARM, RDF_CL1_PORTO_A_B, RDF_CL1_LISBOA_A_B, RDF_CL2_ARM
from selecao_tabelas import sem_exc, com_exc
from cores import verde, amarelo, azul, roxo, ciano, vermelho, cinza, laranja, term
from descricao_carga import info_carga
from cw_ldm import taxavel_estrado


def roadfreight():
    while True:
        print(f'''              {vermelho}Menu RoadFreight{term}         
            {ciano}[1] Cliente RDF_CL1
            [2] Cliente RDF_CL2
            [3] Sair de RoadFreight{term}''')

        escolha = input(f"{laranja}Selecione uma opção: {term}")

        if escolha == '1':
            print("Selecionou o Cliente RDF_CL2")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = RDF_CL1_PORTO_ARM
                nome_cliente = "RDF_CL1_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                tabela = RDF_CL1_LISBOA_ARM
                nome_cliente = "RDF_CL1_LISBOA_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "OUTROS" and zona == "PORTO":
                tabela = RDF_CL1_PORTO_A_B
                nome_cliente = "RDF_CL1_PORTO_A_B"
                taxavel = 300
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                tabela = RDF_CL1_LISBOA_A_B
                nome_cliente = "RDF_CL1_LISBOA_A_B"
                taxavel = 300
                metro_estrado = 1500
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

        elif escolha == "2":
            print("Selecionou o Cliente RDF_CL2")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = RDF_CL2_ARM
                nome_cliente = "RDF_CL2_ARM"
                taxavel = 250
                metro_estrado = 1500
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                tabela = RDF_CL2_ARM
                nome_cliente = "RDF_CL2_ARM"
                taxavel = 250
                metro_estrado = 1500
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente GS_CL1 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente RDF_CL2 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue



        elif escolha == '3':
            break
        else:
            print("Opção inválida! Tente novamente.")