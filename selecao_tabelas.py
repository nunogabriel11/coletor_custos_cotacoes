import pandas as pd
import time
#from cronometro import iniciar_tempo, pagar_e_registar
from cores import verde, amarelo, azul, roxo, ciano, vermelho, cinza, laranja, term
#from cronometro import iniciar_tempo, pagar_e_registar, start_time


############################################################################
# FUNÇÕES PARA OS DATASETS
############################################################################



def sem_exc(cp, peso, comp, larg, alt, tabela, nome_cliente, taxavel, metro_estrado):  # Sem excedente

        # ENCONTRAR A COLUNA DO CÓDIGO POSTAL INSERIDO #
    col = 3  # Início da 1ª coluna

    verificacao = False  # Variável para verificação da existência do código postal

    while col <= (len(tabela.iloc[0]) - 1):
        for lin in range(0, 20):  # Limite alto por segurança (0, 20)
            if pd.isna(tabela.iloc[lin, col]) and isinstance(tabela.iloc[lin, col], float) or isinstance(tabela.iloc[lin, col], float):
                break
            else:
                if len(str(tabela.iloc[lin, col])) < 10:  # Necessário para os casos em que é só um CP e não intervalo
                    if cp == int(tabela.iloc[lin, col]):
                        coluna = col
                        verificacao = True
                        break
                else:
                    if cp >= int(tabela.iloc[lin, col][:4]) and cp <= int(tabela.iloc[lin, col][-4:]):
                        coluna = col
                        verificacao = True
                        break
        col += 1

    if not verificacao:
        print(f'Cliente: {nome_cliente} ')
        print(f"O Código Postal {cp} não existe na tabela.")
        return

    if verificacao:

                ### Encontrar o peso selecionado em cada tabela dos clientes

        for c in range(0, 20):
            if not pd.isna(tabela.iloc[c, 2]) and isinstance(tabela.iloc[c, 2], float):
                inicio_linha = c
                break

        fim_linha = len(tabela["A"])

        for lin_p in range(inicio_linha, fim_linha):
            if peso <= 3000 and peso >= int(tabela.iloc[lin_p, 0]) and peso <= int(tabela.iloc[lin_p, 2]):
                linha = lin_p
                break

                        ### Obtenção do Custo

        if peso > 3000:
            print('_*_*' * 10)
            print(f'{vermelho}Cliente:{term} {nome_cliente}')
            print(f"{amarelo}Peso Excedido.{term}")
            print('_*_*' * 10)
            #nome_clientes.append(str(tabela))
            #custo_clientes.append("Peso Excedido.")

            #pagar_e_registar("Armazem")   # Parar cronometragem após receber custo
            #iniciar_tempo()            # Começar nova cronometragem

        else:
            print('_*_*' * 10)
            #print(f'Cliente: {str(tabela)} ')
            print(f'{vermelho}Cliente:{term} {nome_cliente}')
            print(f'{azul}Custo:{term} {verde}{round(tabela.iloc[linha, coluna], 2)} € {term}')
            print('_*_*' * 10)
            #ome_clientes.append(str(tabela))
            #custo_clientes.append(round(tabela.iloc[linha, coluna], 2))

            #pagar_e_registar("Armazem")   # Parar cronometragem após receber custo
            #iniciar_tempo()            # Começar nova cronometragem



def com_exc(cp, peso, comp, larg, alt, tabela, nome_cliente):   # Com excedente


    # ENCONTRAR A COLUNA DO CÓDIGO POSTAL INSERIDO #
    col = 3  #Início da 1ª coluna

    verificacao = False       # Variável para verificação da existência do código postal

    while col <= (len(tabela.iloc[0])-1):
        for lin in range(0,20):    # Limite alto por segurança (0, 20)
            if pd.isna(tabela.iloc[lin, col]) and isinstance(tabela.iloc[lin, col], float) or isinstance(tabela.iloc[lin, col], float):  # Identificação de que terminou os codigos postais dessa linha
                break
                
            else:
                if len(str(tabela.iloc[lin,col])) < 10:      # Necessário para os casos em que é só um CP e não intervalo. O Python assume como "int" (não há "len" de "int")
                    if cp == int(tabela.iloc[lin,col]):
                        coluna = col
                        verificacao = True    # Encontrado o código postal
                        break                 # O ciclo termina pois foi encontrada a coluna
                else:
                    if cp >= int(tabela.iloc[lin,col][:4]) and cp <= int(tabela.iloc[lin,col][-4:]):
                        coluna = col
                        verificacao = True   # Encontrado o código postal
                        break                # O ciclo termina pois foi encontrada a coluna
        
        col = col + 1


    ### Em caso de o codigo postal não existir
    if verificacao == False:
        print(f'{vermelho}Cliente:{term} {nome_cliente}')
        print(f"{amarelo}O Código Postal {cp} não existe na tabela.{term}")


    #################################################################### ENCONTRAR A LINHA DO PESO INSERIDO (SEM VERIFICAÇÃO DO PESO TAXÁVEL - CBM X 333) #################################################################### 

    if verificacao == True:
        for c in range(0,20):
                if not pd.isna(tabela.iloc[c,2]) and isinstance(tabela.iloc[c, 2], float):
                    #print(c)
                    inicio_linha = c
                    break

        fim_linha = len(tabela["A"])
                
        for lin_p in range (inicio_linha, fim_linha-1):    
                
                if peso<= 4000 and peso >= int(tabela.iloc[lin_p,0]) and peso <= int(tabela.iloc[lin_p,2]):
                    #print(f'Linha: {lin_p}')
                    #print(f'Inicio: {TRANSITEX_LISBOA_ARM.iloc[lin_p,0]}, Fim: {TRANSITEX_LISBOA_ARM.iloc[lin_p,2]}')
                    linha = lin_p



    #################################################################### CUSTO OBTIDO #################################################################### 
        if peso > 4000:
            custo = (tabela.iloc[fim_linha-2, coluna]) + (tabela.iloc[fim_linha-1, coluna]*(peso-4000))                   # Custo total com o EXCEDENTE 
            print('_*_*'*10)
            print(f'{vermelho}Cliente:{term} {nome_cliente} ')
            print(f'{azul}Custo:{term} {verde}{float(round(custo, 2))} €{term}')
            print('_*_*'*10)

            #pagar_e_registar("Ponto_A_B")   # Parar cronometragem após receber custo
            #iniciar_tempo()            # Começar nova cronometragem
            
            
        else:
            print('_*_*'*10)
            print(f'{vermelho}Cliente:{term} {nome_cliente} ')
            print(f'{azul}Custo:{term} {verde}{round(tabela.iloc[linha, coluna], 2)} €{term}')
            print('_*_*'*10)

            #pagar_e_registar("Ponto_A_B")   # Parar cronometragem após receber custo
            #iniciar_tempo()            # Começar nova cronometragem