import random
import time

def exercicio_1():
    print('Iniciando...')
    time.sleep(2)
    for i in range(1,21):
        temperatura = random.randint(20,120)
        time.sleep(1)
        if temperatura > 80:
            print(f'Temperatura {i}: alta {temperatura} C°') 

def exercicio_2():
    print('Iniciando...')
    time.sleep(2)
    for i in range(1,21):
        velocidade = random.uniform(0,3)
        print('Velocidade:',round(velocidade,2))
        time.sleep(1)
        if velocidade < 0.5:
            print('ALERTA: Velocidade Baixa')

def exercicio_3():
    print('Iniciando...')
    time.sleep(2)
    for i in range(1,21):
        kWh = random.uniform(200,1000)
        time.sleep(1)
        if kWh > 700:
            print('ALERTA: Consumo alto')
            print(f'Consumo {i}:',round(kWh,2))

def exercicio_4():
    print('Iniciando...')
    time.sleep(2)
    for i in range(1,21):
        ph = random.randint(1,10)
        print(f'ph {i}:{ph}')
        time.sleep(1)
        if ph < 6 or ph > 8:
            print('ALERTA: ph fora do padrão')
    
def exercicio_5():
    print('Iniciando...')
    time.sleep(2)
    for i in range(1,21):
        temperatura = random.randint(0,15)
        time.sleep(1)
        if temperatura > 10:
            print(f'ALERTA!\nTemperatura {i}: alta {temperatura} C°') 

def exercicio_6():
    print('Iniciando...')
    time.sleep(2)
    for i in range(1,21):
        porcentagem = random.randint(1,100)
        time.sleep(1)
        if porcentagem < 20 or porcentagem > 90:
            print(f'{porcentagem}%: PERIGO')
        else:
             print(f'{porcentagem}%: Dentro do limite')


def exercicio_7():
    print('Iniciando...')
    time.sleep(2)
    for i in range(1,21):
        vibracao = random.uniform(1,12)
        time.sleep(1)
        if vibracao > 10:
            print(f'Vibração acima do limite: {vibracao:.2f}')
        else:
            print(f'Vibração dentro do limite: {vibracao:.2f}')

def exercicio_8():
    print('Iniciando...')
    time.sleep(2)
    for i in range(1,21):
        pressao = random.randint(200,1000)
        print(f'Pressão {i}: {pressao} ')
        time.sleep(1)
        if pressao > 700:
            print(f'ALERTA! \n Temperatura {i}: alta {pressao} C°') 
        else:
            print(f'Pressão {i}: Dentro do limite {pressao} C°')

def exercicio_9():
    producao = []
    for i in range(1,21):
        producao.append(random.randint(1,20))
    media = sum(producao) / len(producao)
    if media > 10:
        print(f'A média foi atingida com {media:0f} motores feitos por hora.')
    else:
        print(f'A média de motores não foi atingida.\nA média foi de {media:.0f} motores produzidos por hora.')
           
def exercicio_10():
    print('Iniciando...')
    time.sleep(2)
    for i in range(1,21):
        temperatura = random.randint(20,120)
        time.sleep(1)
        if temperatura > 80:
            print(f'Temperatura {i}: alta {temperatura:.2f} C°\nDesligamento forçado!')

def exercicio_11():
    print('Iniciando...')
    time.sleep(2)
    cont = 0
    for i in range(1,21):
        leitura = random.randint(1,2)
        time.sleep(1)
        if leitura == 2:
            print(f'Falha na maquina {i}. ')
        else:
            print(f'Maquina {i} operando normalmente.')

def exercicio_12():
    print('Iniciando...')
    time.sleep(2)
    cont = 0
    for i in range(1,21):
        leitura = random.randint(1,3)
        time.sleep(1)
        if leitura == 1:
            print(f'Alerta na maquina {i}! ')
        elif leitura == 2:
            print(f'Maquina {i} Critica!')
        else:
            print(f'Maquina {i} operando normalmente!') 
        
def exercicio_13():
    print('Iniciando...')
    time.sleep(2)
    for i in range(1,21):
        temperatura = random.randint(20,50)
        pressao = random.randint(200,1000)
        print(f'Pressão {i}: {pressao} ')
        time.sleep(1)
        if temperatura > 35:
            print(f'Temperatura {i}: alta {temperatura} C°') 
        else:
            print(f'Temperatura {i}: agradavel {temperatura} C°')

def exercicio_14():
    print('Iniciando...')
    time.sleep(2)
    dados = []
    for i in range(1,21):
        dados.append(random.randint(1,10))
    media = sum(dados) / len (dados)
    print(f'Historico dos dados:\n{dados}')

    time.sleep(1)
    print(f'A media dos dados foi: {media}')

def exercicio_15():
    print('Iniciando...')
    time.sleep(2)
    for i in range(1,101):
        dado = random.randint(1,2)
        time.sleep(1)
        if dado == 2:
            print(f'Dado {i} critico!')

def exercicio_16():
    print('Iniciando...')
    time.sleep(2)
    for i in range(1,21):
        print(f'Enviando dado {i} para a nuvem')
        time.sleep(2)
        print(f'Dado {i} enviado.')
def exercicio_17():
    print('Iniciando...')
    time.sleep(2)
    notas = []
    for i in range(4):
        notas.append(random.randint(0,10))
    media = sum(notas) / len(notas)
    maximo = max(notas)
    minimo = min(notas)
    time.sleep(1)
    print('media',media)
    time.sleep(1)
    print('maximo',maximo)
    time.sleep(1)
    print('minimo',minimo)

def exercicio_18():
    print('Iniciando...')
    time.sleep(2)
    for i in range(1, 21):
        leitura_vibracao = random.uniform(1, 10)
        time.sleep(1)
        print(f'Leitura {i}: {leitura_vibracao:.2f} mm/s')
        if leitura_vibracao > 8:
            print('ALERTA: Anomalia detectada! Risco de falha no equipamento.')

def exercicio_19():
    print('Iniciando...')
    time.sleep(2)
    meta_esperada = 50
    for i in range(1, 21):
        producao_real = random.randint(30, 60)
        time.sleep(1)
        eficiencia = (producao_real / meta_esperada) * 100
        print(f'Hora {i} - Eficiência: {eficiencia:.2f}% (Produzido: {producao_real}/{meta_esperada})')
        time.sleep(1)
        if eficiencia < 80:
            print('ALERTA: Desempenho crítico. Eficiência abaixo de 80% da meta!')
        elif eficiencia >= 100:
            print('Sucesso: Meta atingida ou superada!')
        else:
            print('Atenção: Produção abaixo da meta, mas dentro do limite aceitável.')

def exercicio_20():
    print('Iniciando...')
    time.sleep(2)
    
    banco_de_dados = [] 
    
    for i in range(1, 21):
        temperatura = random.randint(30, 110)
        vibracao = random.uniform(1, 12)
        time.sleep(1)
        if temperatura >= 90 or vibracao >= 9:
            status = "CRÍTICO - Parada Recomendada"
        elif temperatura >= 75 or vibracao >= 6:
            status = "ALERTA - Inspeção Necessária"
        else:
            status = "NORMAL - Operando"
            
        print(f'[SUPERVISÓRIO] Leitura {i} | Temp: {temperatura}C° | Vibração: {vibracao:.2f} | Status: {status}')
        time.sleep(1)

        banco_de_dados.append({
            'leitura': i,
            'temperatura': temperatura,
            'vibracao': vibracao,
            'status': status
        })

    print('\n' + '='*40)
    print(' DASHBOARD DE DESEMPENHO (RELATÓRIO FINAL)')
    print('='*40)
    time.sleep(2)
    
    total_leituras = len(banco_de_dados)
    leituras_normais = sum(1 for registro in banco_de_dados if "NORMAL" in registro['status'])
    leituras_alerta = sum(1 for registro in banco_de_dados if "ALERTA" in registro['status'])
    leituras_criticas = sum(1 for registro in banco_de_dados if "CRÍTICO" in registro['status'])
    
    print(f'Total de Amostras: {total_leituras}')
    print(f'-> Operação Normal: {leituras_normais}')
    print(f'-> Ocorrências de Alerta: {leituras_alerta}')
    print(f'-> Ocorrências Críticas: {leituras_criticas}')
    print('='*40 + '\n')

def master():
    exercicio_1()
    exercicio_2()
    exercicio_3()
    exercicio_4()
    exercicio_5()
    exercicio_6()
    exercicio_7()
    exercicio_8()
    exercicio_9()
    exercicio_10()
    exercicio_11()
    exercicio_12()
    exercicio_13()
    exercicio_14()
    exercicio_15()
    exercicio_16()
    exercicio_17()
    exercicio_18()
    exercicio_19()
exercicio_20()

master()    


