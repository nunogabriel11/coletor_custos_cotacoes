import pandas as pd

############################################################################
# DATASETS
############################################################################

linhas_10_41 = list(range(10, 41))
linhas_10_42 = list(range(10, 42))
linhas_10_48 = list(range(10, 48))
linhas_10_43 = list(range(10, 43))
linhas_10_46 = list(range(10, 46))
linhas_10_49 = list(range(10, 49))
linhas_11_47 = list(range(11, 47))
linhas_11_40 = list(range(11, 40))
linhas_11_41 = list(range(11, 41))
linhas_11_46 = list(range(11, 46))

# Overseas 

OVS_CL1_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/OVS_CL1Tarifario Porto - Armazem.xlsx',skiprows=lambda x: x not in linhas_10_43)
OVS_CL1_LISBOA_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/OVS_CL1Tarifario Lisboa - Armazem.xlsx',skiprows=lambda x: x not in linhas_11_41)
OVS_CL1_PORTO_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/OVS_CL1Tabela de distribuição_Porto_Ponto A_B.xlsx',skiprows=lambda x: x not in linhas_10_48)
OVS_CL1_LISBOA_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/OVS_CL1Tabela de distribuição_Lisboa_Ponto A_B.xlsx',skiprows=lambda x: x not in linhas_11_46)

# RoadFreight

RDF_CL1_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/RDF_CL1Tarifario Porto - Armazem.xlsx',skiprows=lambda x: x not in linhas_10_43)
RDF_CL1_LISBOA_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/RDF_CL1Tarifario Lisboa - Armazem.xlsx',skiprows=lambda x: x not in linhas_11_41)
RDF_CL1_PORTO_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/RDF_CL1Tabela de distribuição_Porto_Ponto A_B.xlsx',skiprows=lambda x: x not in linhas_10_48)
RDF_CL1_LISBOA_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/RDF_CL1Tabela de distribuição_Lisboa_Ponto A_B.xlsx',skiprows=lambda x: x not in linhas_11_46)
RDF_CL2_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/RDF_CL2Tabela de distribuição.xlsx',skiprows=lambda x: x not in linhas_10_46)


# Distribuição

# - CAFES5F
DST_CL1_PORTO_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL1Tabela de distribuição_Porto_Ponto A_B.xlsx', skiprows=lambda x: x not in linhas_10_48)
DST_CL1_LISBOA_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL1Tabela de distribuição_Lisboa_Ponto A_B.xlsx', skiprows=lambda x: x not in linhas_11_46)
DST_CL2_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL2Tabela de distribuição_2024.xlsx', skiprows=lambda x: x not in linhas_10_42)
DST_CL3_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL3Tarifario Porto - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_10_42)
DST_CL3_LISBOA_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL3Tarifario Lisboa - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_11_40)
DST_CL3_PORTO_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL3Tabela de distribuição_Porto_Ponto A_B.xlsx', skiprows=lambda x: x not in linhas_10_48)
DST_CL3_LISBOA_A_B =  pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL3Tabela de distribuição_Lisboa_Ponto A_B.xlsx', skiprows=lambda x: x not in linhas_11_46)
DST_CL4_PORTO_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL4Tabela de distribuição_Porto_Ponto A_F.xlsx', skiprows=lambda x: x not in linhas_10_48)
DST_CL4_LISBOA_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL4Tabela de distribuição_Lisboa_Ponto A_F.xlsx', skiprows=lambda x: x not in linhas_11_46)
DST_CL5_PORTO_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL5Tabela de distribuição_Porto_Ponto A_B.xlsx', skiprows=lambda x: x not in linhas_10_48)
DST_CL5_LISBOA_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL5Tabela de distribuição_Lisboa_Ponto A_B.xlsx', skiprows=lambda x: x not in linhas_11_46)
DST_CL6_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL6Tarifario Porto - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_10_43)
DST_CL7_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL7Table distribution_Oporto_2024.xlsx', skiprows=lambda x: x not in linhas_10_49)
DST_CL7_LISBOA_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL7Table distribution_Lisbon_2024.xlsx', skiprows=lambda x: x not in linhas_11_47)
DST_CL8_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL8Tarifario Porto - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_10_42)
DST_CL9_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL9Tarifario Porto - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_10_42)
DST_CL9_LISBOA_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL9Tabela distribuição_Lisboa_2024.xlsx', skiprows=lambda x: x not in linhas_11_47)
DST_CL9_PORTO_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL9Tabela de distribuição_Porto_Ponto A_B.xlsx', skiprows=lambda x: x not in linhas_10_48)
DST_CL9_LISBOA_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL9Tabela de distribuição_Lisboa_Ponto A_B.xlsx', skiprows=lambda x: x not in linhas_11_46)
DST_CL10_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL10Tabela de distribuição 2024.xlsx', skiprows=lambda x: x not in linhas_10_43)
DST_CL11_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL11Tabela de distribuição_Porto_2024.xlsx', skiprows=lambda x: x not in linhas_10_49)
DST_CL12_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL12Tarifario Porto - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_10_42)
DST_CL12_LISBOA_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL12Tarifario Lisboa - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_11_40)
DST_CL12_PORTO_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL12Tabela de distribuição_Porto_Ponto A_B.xlsx', skiprows=lambda x: x not in linhas_10_48)
DST_CL12_LISBOA_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL12Tabela de distribuição_Lisboa_Ponto A_B.xlsx', skiprows=lambda x: x not in linhas_11_46)
DST_CL13_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL13Tarifario Porto - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_10_42)
DST_CL13_LISBOA_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL13Tarifario Lisboa - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_11_40)
DST_CL13_PORTO_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL13Tabela de distribuição_Porto_Ponto A_B.xlsx', skiprows=lambda x: x not in linhas_10_48)
DST_CL13_LISBOA_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL13Tabela de distribuição_Lisboa_Ponto A_B.xlsx', skiprows=lambda x: x not in linhas_11_40)
DST_CL14_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL14Tabela distribuição_Porto_2024.xlsx', skiprows=lambda x: x not in linhas_10_48)
DST_CL14_LISBOA_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL14Tabela distribuição_Lisboa_2024.xlsx', skiprows=lambda x: x not in linhas_11_47)
DST_CL15_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL15Tarifario Porto_2024.xlsx', skiprows=lambda x: x not in linhas_10_42)
DST_CL16_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL16Tarifario Porto - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_10_42)
DST_CL17_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL17Tabela de distribuição_Porto_Restantes códigos.xlsx', skiprows=lambda x: x not in linhas_10_42)
DST_CL17_LISBOA_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL17Tarifario Lisboa - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_11_40)
DST_CL18_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL18Tarifario Porto - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_10_42)
DST_CL18_LISBOA_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL18Tarifario Lisboa - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_11_40)
DST_CL18_PORTO_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL18Tabela de distribuição_Porto_Ponto A_B.xlsx', skiprows=lambda x: x not in linhas_10_48)
DST_CL18_LISBOA_A_B = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/DST_CL18Tabela de distribuição_Lisboa_Ponto A_B.xlsx', skiprows=lambda x: x not in linhas_11_46)


# Gestão de Stocks

GS_CL1_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/GS_CL1Tarifario Porto - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_10_43)
GS_CL2_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/GS_CL2Tarifario Porto - 2024.xlsx', skiprows=lambda x: x not in linhas_10_43)
GS_CL3_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/GS_CL3Tarifario Porto - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_10_43)
GS_CL4_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/GS_CL4Tarifario Porto - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_10_43)
GS_CL5_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/GS_CL5Tabela de distribuição_2024.xlsx', skiprows=lambda x: x not in linhas_10_42)
GS_CL6_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/GS_CL6Tabela de distribuição 2024.xlsx', skiprows=lambda x: x not in linhas_10_41)
GS_CL7_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/GS_CL7National distribution_2024.xlsx', skiprows=lambda x: x not in linhas_10_42)
GS_CL8_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/GS_CL8Tabela de distribuição 2024.xlsx', skiprows=lambda x: x not in linhas_10_41)
GS_CL9_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/GS_CL9Tabela distribuição_Porto_2024.xlsx', skiprows=lambda x: x not in linhas_10_48)
GS_CL9_LISBOA_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/GS_CL9Tabela distribuição_Lisboa_2024.xlsx', skiprows=lambda x: x not in linhas_11_47)
GS_CL10_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/GS_CL10Tabela de distribuição 2024.xlsx', skiprows=lambda x: x not in linhas_10_41)
GS_CL11_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/GS_CL11Table Distribution_2024.xlsx', skiprows=lambda x: x not in linhas_10_43)
GS_CL12_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/GS_CL12Tarifario Porto - GERAL 2024.xlsx', skiprows=lambda x: x not in linhas_10_43)
GS_CL13_PORTO_ARM = pd.read_excel(r'C:/Users/Nuno Gabriel/Desktop/Executável - Teste sem cronometragens/xls-files/GS_CL13Tabela de distribuição 2024.xlsx', skiprows=lambda x: x not in linhas_10_41)