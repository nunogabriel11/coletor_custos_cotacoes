from cores import verde, amarelo, term

def taxavel_estrado(comp, larg, alt, taxavel, peso, sobreponivel, metro_estrado):
    cw = comp * larg * alt * taxavel  # Cálculo do Peso Taxável

    if sobreponivel in "S":
        if cw > peso:
            print(f"CW: {cw}")
            peso = cw
            print(f"{verde}Considerado o peso taxável (cw) de: {peso} Kgs")
        else:
            print(f"{verde}Considerado o peso real de: {peso} Kgs")
    else:

        # Código existente para cálculos de LDM
        while True:
            try:
                larg_veiculo = float(input(f"{verde}Largura do veículo:{term} "))
                break
            except ValueError:
                print(f"{amarelo}Dados inválidos! Por favor, insira um valor numérico para a largura do veículo.{term}")

        while True:
            try:
                n_paletes = float(input(f"{verde}Número de paletes: {term}"))
                break
            except ValueError:
                print(f"{amarelo}Dados inválidos! Por favor, insira um valor numérico para o número de paletes.{term}")

        while True:
            try:
                larg_pal = float(input(f"{verde}Largura de cada palete: {term}"))
                break
            except ValueError:
                print(f"{amarelo}Dados inválidos! Por favor, insira um valor numérico para o número de paletes.{term}")

        while True:
            try:
                comp_pal = float(input(f"{verde}Comprimento de cada palete: {term}"))
                break
            except ValueError:
                print(f"{amarelo}Dados inválidos! Por favor, insira um valor numérico para o número de paletes.{term}")

        n_pal_larg_veiculo = larg_veiculo / larg_pal

        ldm_c = ldm_i = ldm_t = 0

        if n_paletes > n_pal_larg_veiculo:
            filas_necessarias = n_paletes / n_pal_larg_veiculo
            filas_completas = int(filas_necessarias)

            if filas_necessarias - filas_completas == 0:
                ldm_t = ldm_c = comp_pal * filas_completas
                print(f"Total de {ldm_t} LDM")
            else:
                n_paletes_em_falta = n_paletes - (int(n_pal_larg_veiculo) * filas_completas)
                ldm_i = comp_pal * ((larg_pal * n_paletes_em_falta) / larg_veiculo)
                ldm_c = comp_pal * filas_completas
                ldm_t = ldm_i + ldm_c
                print(f"Total de {ldm_t} LDM")
        elif n_paletes == n_pal_larg_veiculo:
            filas_completas = int(n_paletes / n_pal_larg_veiculo)
            ldm_c = comp_pal * filas_completas
            print(f"{filas_completas} filas completas com um total de {ldm_c} LDM.")
        else:
            ldm_t = ldm_i = comp_pal * ((larg_pal * n_paletes) / larg_veiculo)
            print(f"1 fila com {ldm_t} ldm.")

        ldm = round(ldm_t * metro_estrado, 2)

        if cw > peso and cw > ldm:
            peso = cw
            print(f"Considerado o peso taxável (cw) de: {peso} Kgs")
        elif ldm > peso and ldm > cw:
            peso = ldm
            print(f"Considerado o peso de metros de estrado (ldm) de: {peso} Kgs")
        else:
            print(f"Considerado o peso real de: {peso} Kgs")

    return peso
