import sys

COMISSAO_MEDICA_HABITUAL = 0.6
CUSTO_CONSULTA = 35
PAGAMENTO_WELLS_POR_CONSULTA = 10
PAGAMENTO_MEDICO_POR_CONSULTA = 25 * 0.6
NUMERO_CONSULTAS_PARA_BONUS = 300
PAYMENT_BONUS = 0.05
PAGAMENTO_MEDICO_POR_CONSULTA_BONUS = PAGAMENTO_MEDICO_POR_CONSULTA * PAYMENT_BONUS

def readArray():
    try:
        a = input().split(" ")
    except:
        sys.exit(0)
    for i in range(0, len(a)):
        a[i] = int(a[i])
    return a;

def obterValoresPagosAosMedicos(numeroConsultasMes):
    valoresMedicos = []

    nextMonthHasBonus = False
    for i in range(0, len(numeroConsultasMes) - 2, 3):
        for j in range(i, i + 3):
            payment = numeroConsultasMes[j] * PAGAMENTO_MEDICO_POR_CONSULTA
            if (nextMonthHasBonus):
                valoresMedicos.append(payment + payment * PAYMENT_BONUS)
            else:
                valoresMedicos.append(payment)
        numeroConsultasTrimestre = numeroConsultasMes[i] + numeroConsultasMes[i + 1] + numeroConsultasMes[i + 2]
        if (numeroConsultasTrimestre > 300):
            nextMonthHasBonus = True
        else:
            nextMonthHasBonus = False
        
    return valoresMedicos
    
    

def main():
    numeroConsultasMes = readArray()
    valoresMedicos = obterValoresPagosAosMedicos(numeroConsultasMes)
    print(valoresMedicos)
    

if __name__ == "__main__":
    main()
    
# 100 200 300 50 100 150 200 300 400 15 12 120 230 320 410 151 220 230