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

