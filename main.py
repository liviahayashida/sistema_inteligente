from machine import Pin      # Importa a classe Pin para controlar GPIOs(pinos em microcontroladores)
from dht import DHT22        # Importa o driver específico para o sensor DHT22
from utime import sleep      # Importa a função sleep para introduzir pausas

# Inicializa o sensor DHT22 na porta digital GP15
sensor = DHT22(Pin(16))      
# Inicializa o sensor PIR (movimento) na porta GP14 como entrada
pir = Pin(14, Pin.IN)  # Configura o pino 14 como entrada

# Inicializa os pinos digitais GP2, GP3 e GP4 como saídas para controlar os LEDs
led_verde = Pin(12, Pin.OUT)
led_amarelo = Pin(10, Pin.OUT)
led_vermelho = Pin(3, Pin.OUT)

# Define uma função para garantir que todos os LEDs estejam desligados
def leds_off():
    led_verde.off()
    led_amarelo.off()
    led_vermelho.off()

while True: # Loop principal
    # 1- Leitura dos Sensores
    sensor.measure()              # Solicita a medição ao sensor DHT22 (temperatura e umidade)
    temp = sensor.temperature()   # Armazena o valor da temperatura em °C
    movimento = pir.value()       # Lê o estado do sensor PIR (0=sem movimento, 1=movimento)

    # 2- Exibição no Console
    print(f"Temperatura: {temp}°C | Movimento: {movimento}")

    # 3- Lógica de Sinalização
    leds_off()  # Garante que todos os LEDs estejam desligados antes de ligar o estado atual

    if movimento == 0:
        # CONDIÇÃO 1: Sem movimento (ambiente inativo)
        # Acende o LED Verde (sinalizando que está tudo "normal" ou inativo)
        led_verde.on()

    else:
        # CONDIÇÃO 2: Movimento detectado (pessoas ativas)
        
        # Subcondição A: Temperatura ideal
        if temp < 26:
            # Temperatura abaixo de 26°C → OK
            led_verde.on()

        # Subcondição B: Temperatura de atenção
        elif 26 <= temp <= 28:
            # Temperatura entre 26°C e 28°C → Atenção
            led_amarelo.on()

        # Subcondição C: Temperatura de alerta/perigo
        elif temp > 28:
            # Temperatura acima de 28°C → Perigo/Alerta
            
            # Pisca o LED Vermelho rapidamente
            led_vermelho.on()
            sleep(0.3)
            led_vermelho.off()
            sleep(0.3)
            # Pula o 'sleep(1)' final e reinicia o loop 'while True', 
            # garantindo que o pisca-pisca continue rapidamente.
            continue 

    # Pausa de 1 segundo (usada apenas se não estiver piscando o LED Vermelho)
    sleep(1)