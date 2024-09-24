from tabelas_excel import GS_CL1_PORTO_ARM, GS_CL2_PORTO_ARM, GS_CL3_PORTO_ARM, GS_CL4_PORTO_ARM, GS_CL5_PORTO_ARM, GS_CL6_PORTO_ARM, GS_CL7_PORTO_ARM, GS_CL8_PORTO_ARM, GS_CL9_PORTO_ARM, GS_CL9_LISBOA_ARM, GS_CL10_PORTO_ARM, GS_CL11_PORTO_ARM, GS_CL12_PORTO_ARM, GS_CL13_PORTO_ARM
from selecao_tabelas import sem_exc, com_exc
from cores import verde, amarelo, azul, roxo, ciano, vermelho, cinza, laranja, term
from descricao_carga import info_carga
from cw_ldm import taxavel_estrado


def gestao_de_stocks():
    while True:
        print(f'''              {vermelho}Menu Gestão de Stocks{term}         
            {ciano}[1] GS_CL1
            [2] GS_CL2
            [3] GS_CL3
            [4] GS_CL4
            [5] GS_CL5
            [6] GS_CL6
            [7] GS_CL7
            [8] GS_CL8
            [9] GS_CL9
            [10] GS_CL10
            [11] GS_CL11
            [12] GS_CL12
            [13] GS_CL13
            [14] Sair de Gestão de Stocks{term}''')

        escolha = input(f"{laranja}Selecione uma opção: {term}")

        if escolha == '1':
            print("Selecionou o Cliente GS_CL1")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = GS_CL1_PORTO_ARM
                nome_cliente = "GS_CL1_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente GS_CL1 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente GS_CL1 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente GS_CL1 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

        elif escolha == '2':
            print("Selecionou o Cliente GS_CL2")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = GS_CL2_PORTO_ARM
                nome_cliente = "GS_CL2_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente GS_CL2 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente GS_CL2 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente GS_CL2 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

        elif escolha == '3':
            print("Selecionou o Cliente GS_CL3")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = GS_CL3_PORTO_ARM
                nome_cliente = "GS_CL3_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente GS_CL3 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente GS_CL3 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente GS_CL3 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue
        elif escolha == '4':
            print("Selecionou o Cliente GS_CL4")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = GS_CL4_PORTO_ARM
                nome_cliente = "GS_CL4_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente GS_CL4 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente GS_CL4 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente GS_CL4 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue
        elif escolha == '5':
            print("Selecionou o Cliente GS_CL5")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = GS_CL5_PORTO_ARM
                nome_cliente = "GS_CL5_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente GS_CL5 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente GS_CL5 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente GS_CL5 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

        elif escolha == '6':
            print("Selecionou o Cliente GS_CL6")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = GS_CL6_PORTO_ARM
                nome_cliente = "GS_CL6_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente GS_CL6 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente GS_CL6 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente GS_CL6 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

        elif escolha == '7':
            print("Selecionou o Cliente GS_CL7")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = GS_CL7_PORTO_ARM
                nome_cliente = "GS_CL7_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente GS_CL7 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente GS_CL7 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente GS_CL7 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

        elif escolha == '8':
            print("Selecionou o Cliente GS_CL8")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = GS_CL8_PORTO_ARM
                nome_cliente = "GS_CL8_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente GS_CL8 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente GS_CL8 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente GS_CL8 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

        elif escolha == '9':
            print("Selecionou o Cliente GS_CL9")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = GS_CL9_PORTO_ARM
                nome_cliente = "GS_CL9_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                tabela = GS_CL9_LISBOA_ARM
                nome_cliente = "GS_CL9_LISBOA_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente GS_CL9 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente GS_CL9 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

        elif escolha == '10':
            print("Selecionou o Cliente GS_CL10")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = GS_CL10_PORTO_ARM
                nome_cliente = "GS_CL10_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente GS_CL10 não tem tabelas para Armazém em Lisboa.")
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente GS_CL10 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente GS_CL10 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

        elif escolha == '11':
            print("Selecionou o Cliente GS_CL11")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = GS_CL11_PORTO_ARM
                nome_cliente = "GS_CL11_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente GS_CL11 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente GS_CL11 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente GS_CL11 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

        elif escolha == '12':
            print("Selecionou o Cliente GS_CL12")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = GS_CL12_PORTO_ARM
                nome_cliente = "GS_CL12_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente GS_CL12 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente GS_CL12 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente GS_CL12 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

        elif escolha == '13':
            print("Selecionou o Cliente GS_CL13")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = GS_CL13_PORTO_ARM
                nome_cliente = "GS_CL13_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente GS_CL13 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente GS_CL13 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente GS_CL13 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue
            
        elif escolha == '14':
            break
        else:
            print("Opção inválida! Tente novamente.")