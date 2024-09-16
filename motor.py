import time
from machine import Pin, PWM

# Definindo os pinos GPIO para a ponte H e o motor DC
in1 = Pin(15, Pin.OUT)
in2 = Pin(14, Pin.OUT)
ena = PWM(Pin(13))  # PWM para controle de velocidade
ena.freq(1000)      # Frequência de PWM
ena.duty_u16(32768) # 50% de duty cycle para velocidade média

def abrir_cofre():
    # Ativar motor para abrir o cofre
    print("Abrindo o cofre...")
    in1.value(1)  # Sentido de rotação 1
    in2.value(0)
    time.sleep(5)  # Mantém o motor ativo por 5 segundos (ajustar conforme necessário)
    parar_motor()

def fechar_cofre():
    # Inverter o motor para fechar o cofre
    print("Fechando o cofre...")
    in1.value(0)  # Sentido de rotação inverso
    in2.value(1)
    time.sleep(5)  # Tempo para fechar o cofre
    parar_motor()

def parar_motor():
    # Desativar o motor
    in1.value(0)
    in2.value(0)
    print("Motor parado.")
