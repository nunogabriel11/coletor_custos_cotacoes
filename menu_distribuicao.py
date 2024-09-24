from tabelas_excel import DST_CL1_PORTO_A_B, DST_CL1_LISBOA_A_B, DST_CL14_PORTO_ARM, DST_CL14_LISBOA_ARM, DST_CL2_PORTO_ARM, DST_CL3_PORTO_ARM, DST_CL3_LISBOA_ARM, DST_CL3_PORTO_A_B, DST_CL3_LISBOA_A_B, DST_CL10_PORTO_ARM, DST_CL4_PORTO_A_B, DST_CL4_LISBOA_A_B, DST_CL5_PORTO_A_B, DST_CL5_LISBOA_A_B, DST_CL6_PORTO_ARM, DST_CL7_PORTO_ARM, DST_CL7_LISBOA_ARM, DST_CL8_PORTO_ARM, DST_CL9_PORTO_ARM, DST_CL9_LISBOA_ARM, DST_CL9_PORTO_A_B, DST_CL9_LISBOA_A_B, DST_CL11_PORTO_ARM, DST_CL12_PORTO_ARM, DST_CL12_LISBOA_ARM, DST_CL12_PORTO_A_B, DST_CL12_LISBOA_A_B, DST_CL13_PORTO_ARM, DST_CL13_LISBOA_ARM, DST_CL13_PORTO_A_B, DST_CL13_LISBOA_A_B, DST_CL15_PORTO_ARM, DST_CL16_PORTO_ARM, DST_CL17_PORTO_ARM, DST_CL17_LISBOA_ARM, DST_CL18_PORTO_ARM, DST_CL18_LISBOA_ARM, DST_CL18_PORTO_A_B, DST_CL18_LISBOA_A_B
from selecao_tabelas import com_exc, sem_exc
from cores import verde, amarelo, azul, roxo, ciano, vermelho, cinza, laranja, term
from descricao_carga import info_carga
from cw_ldm import taxavel_estrado


def distribuicao():
    while True:
        print(f'''              {vermelho}Menu Distribuição{term}       
            {ciano}[1] DST_CL1
            [2] DST_CL2
            [3] DST_CL3
            [4] DST_CL4
            [5] DST_CL5
            [6] DST_CL6 
            [7] DST_CL7
            [8] DST_CL8
            [9] DST_CL9
            [10] DST_CL10
            [11] DST_CL11
            [12] DST_CL12
            [13] DST_CL13
            [14] DST_CL14
            [15] DST_CL15
            [16] DST_CL16
            [17] DST_CL17
            [18] DST_CL18
            [19] Sair de Distribuição{term}''')

        escolha = input(f"{laranja}Selecione uma opção: {term}")


        if escolha == '1':
            print("Selecionou o Cliente DST_CL1")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                print("O Cliente DST_CL1 não tem tabelas para Armazém.")
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente DST_CL1 não tem tabelas para Armazém.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                tabela = DST_CL1_PORTO_A_B
                nome_cliente = "DST_CL1_PORTO_A_B"
                taxavel = 300   
                metro_estrado = 1750  
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                tabela = DST_CL1_LISBOA_A_B
                nome_cliente = "DST_CL1_LISBOA_A_B"
                taxavel = 300  
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue
        elif escolha == '2':
            print("Selecionou o Cliente DST_CL2")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = DST_CL2_PORTO_ARM
                nome_cliente = "DST_CL2_PORTO_ARM"
                taxavel = 333   
                metro_estrado = 1750  
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente DST_CL2 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente DST_CL2 não tem tabelas para zonas A - B.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente DST_CL2 não tem tabelas para zonas A - B.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue
        elif escolha == '3':
            print("Selecionou o Cliente DST_CL3")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = DST_CL3_PORTO_ARM
                nome_cliente = "DST_CL3_PORTO_ARM"
                taxavel = 333 
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                tabela = DST_CL3_LISBOA_ARM
                nome_cliente = "DST_CL3_LISBOA_ARM"
                taxavel = 333   
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "OUTROS" and zona == "PORTO":
                tabela = DST_CL3_PORTO_A_B
                nome_cliente = "DST_CL3_PORTO_A_B"
                taxavel = 300  
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                tabela = DST_CL3_LISBOA_A_B
                nome_cliente = "DST_CL3_LISBOA_A_B"
                taxavel = 300  
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

        elif escolha == '4':
            print("Selecionou o Cliente DST_CL4")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                print("O Cliente DST_CL4 não tem tabelas para Armazém no Porto.")
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                tabela = DST_CL4_PORTO_A_B
                nome_cliente = "DST_CL4_PORTO_A_B"
                taxavel = 300   
                metro_estrado = 1750   
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                tabela = DST_CL4_LISBOA_A_B
                nome_cliente = "DST_CL4_LISBOA_A_B"
                taxavel = 300   
                metro_estrado = 1750   
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue
        elif escolha == '5':
            print("Selecionou o Cliente DST_CL5")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                print("O Cliente DST_CL5 não tem tabelas para Armazém no Porto.")
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente DST_CL5 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                tabela = DST_CL5_PORTO_A_B
                nome_cliente = "DST_CL5_PORTO_A_B"
                taxavel = 300   
                metro_estrado = 1750  
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                tabela = DST_CL5_LISBOA_A_B
                nome_cliente = "DST_CL5_LISBOA_A_B"
                taxavel = 300   
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue
        elif escolha == '6':
            print("Selecionou o Cliente DST_CL6")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = DST_CL6_PORTO_ARM
                nome_cliente = "DST_CL6_PORTO_ARM"
                taxavel = 333   
                metro_estrado = 1750   
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente DST_CL6 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente DST_CL6 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente DST_CL6 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue
        elif escolha == '7':
            print("Selecionou o Cliente DST_CL7")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = DST_CL7_PORTO_ARM
                nome_cliente = "DST_CL7_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750   
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                tabela = DST_CL7_LISBOA_ARM
                nome_cliente = "DST_CL7_LISBOA_ARM"
                taxavel = 333
                metro_estrado = 1750  
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente DST_CL7 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente DST_CL7 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue
        elif escolha == '8':
            print("Selecionou o Cliente DST_CL8")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = DST_CL8_PORTO_ARM
                nome_cliente = "DST_CL8_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente DST_CL8 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente DST_CL8 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente DST_CL8 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

        elif escolha == '9':
            print("Selecionou a DST_CL9")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = DST_CL9_PORTO_ARM
                nome_cliente = "DST_CL9_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                tabela = DST_CL9_LISBOA_ARM
                nome_cliente = "DST_CL9_LISBOA_ARM"
                taxavel = 333
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "OUTROS" and zona == "PORTO":
                tabela = DST_CL9_PORTO_A_B
                nome_cliente = "DST_CL9_PORTO_A_B"
                taxavel = 300   
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                tabela = DST_CL9_LISBOA_A_B
                nome_cliente = "DST_CL9_LISBOA_A_B"
                taxavel = 300   
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

        elif escolha == '10':
            print("Selecionou o Cliente DST_CL10")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = DST_CL10_PORTO_ARM
                nome_cliente = "DST_CL10_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente DST_CL10 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente DST_CL10 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente DST_CL10 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

        elif escolha == '11':
            print("Selecionou o Cliente DST_CL11")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = DST_CL11_PORTO_ARM
                nome_cliente = "DST_CL11_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente DST_CL11 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente DST_CL11 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente DST_CL11 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue

        elif escolha == '12':
            print("Selecionou o Cliente DST_CL12")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = DST_CL12_PORTO_ARM
                nome_cliente = "DST_CL12_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750   
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                tabela = DST_CL12_LISBOA_ARM
                nome_cliente = "DST_CL12_LISBOA_ARM"
                taxavel = 333
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "OUTROS" and zona == "PORTO":
                tabela = DST_CL12_PORTO_A_B
                nome_cliente = "DST_CL12_PORTO_A_B"
                taxavel = 300   
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                tabela = DST_CL12_LISBOA_A_B
                nome_cliente = "DST_CL12_LISBOA_A_B"
                taxavel = 300   
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue
        elif escolha == '13':
            print("Selecionou o Cliente DST_CL13")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = DST_CL13_PORTO_ARM
                nome_cliente = "DST_CL13_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                tabela = DST_CL13_LISBOA_ARM
                nome_cliente = "DST_CL13_LISBOA_ARM"
                taxavel = 333
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "OUTROS" and zona == "PORTO":
                tabela = DST_CL13_PORTO_A_B
                nome_cliente = "DST_CL13_PORTO_A_B"
                taxavel = 300  
                metro_estrado = 1750   
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                tabela = DST_CL13_LISBOA_A_B
                nome_cliente = "DST_CL13_LISBOA_A_B"
                taxavel = 300   
                metro_estrado = 1750  
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue
        elif escolha == '14':
            print("Selecionou o Cliente DST_CL14")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = DST_CL14_PORTO_ARM
                nome_cliente = "DST_CL14_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                tabela = DST_CL14_LISBOA_ARM
                nome_cliente = "DST_CL14_LISBOA_ARM"
                taxavel = 333
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente DST_CL14 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente DST_CL14 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue
        elif escolha == '15':
            print("Selecionou o Cliente DST_CL15")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = DST_CL15_PORTO_ARM
                nome_cliente = "DST_CL15_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750   
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente DST_CL15 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente DST_CL15 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente DST_CL15 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue
        elif escolha == '16':
            print("Selecionou o Cliente DST_CL16")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = DST_CL16_PORTO_ARM
                nome_cliente = "DST_CL16_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750  
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                print("O Cliente DST_CL16 não tem tabelas para Armazém em Lisboa.")
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente DST_CL16 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente DST_CL16 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue
        elif escolha == '17':
            print("Selecionou o Cliente DST_CL17")                    
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = DST_CL17_PORTO_ARM
                nome_cliente = "DST_CL17_PORTO_ARM"
                taxavel = 300   
                metro_estrado = 1750   
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                tabela = DST_CL17_LISBOA_ARM
                nome_cliente = "DST_CL17_LISBOA_ARM"
                taxavel = 300   
                metro_estrado = 1750   
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "OUTROS" and zona == "PORTO":
                print("O Cliente DST_CL17 não tem tabelas para zonas A - B no Porto.")
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                print("O Cliente DST_CL17 não tem tabelas para zonas A - B em Lisboa.")
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue
        elif escolha == '18':
            print("Selecionou o Cliente DST_CL18")
            cp, peso, comp, larg, alt, origem_destino, zona, sobreponivel = info_carga()

            if origem_destino == "ARMAZEM" and zona == "PORTO":
                tabela = DST_CL18_PORTO_ARM
                nome_cliente = "DST_CL18_PORTO_ARM"
                taxavel = 333
                metro_estrado = 1750   
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "ARMAZEM" and zona == "LISBOA":
                tabela = DST_CL18_LISBOA_ARM
                nome_cliente = "DST_CL18_LISBOA_ARM"
                taxavel = 333
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado)
            elif origem_destino == "OUTROS" and zona == "PORTO":
                tabela = DST_CL18_PORTO_A_B
                nome_cliente = "DST_CL18_PORTO_A_B"
                taxavel = 300   
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            elif origem_destino == "OUTROS" and zona == "LISBOA":
                tabela = DST_CL18_LISBOA_A_B
                nome_cliente = "DST_CL18_LISBOA_A_B"
                taxavel = 300   
                metro_estrado = 1750    
                peso = taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado)
                com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente)
            else:
                print("Opção de origem/destino ou zona inválida.")
                continue
        elif escolha == '19':
            break
        else:
            print("Opção inválida! Tente novamente.")