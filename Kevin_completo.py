import RPi.GPIO as GPIO
import time

IN1 = 23
IN2 = 24
EN1 = 25

IN3 = 27
IN4 = 22
EN2 = 17

SENSOR_IZQ = 18
SENSOR_DER = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(EN1, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(EN2, GPIO.OUT)
GPIO.setup(SENSOR_IZQ, GPIO.IN)
GPIO.setup(SENSOR_DER, GPIO.IN)

p1 = GPIO.PWM(EN1, 50)
p2 = GPIO.PWM(EN2, 50)
p1.start(0)
p2.start(0)

velocidad = 100

def avanzar():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    p1.ChangeDutyCycle(velocidad)
    p2.ChangeDutyCycle(velocidad)

def detener():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    p1.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)

def girar_izquierda():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    p1.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(velocidad)

def girar_derecha():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    p1.ChangeDutyCycle(velocidad)
    p2.ChangeDutyCycle(0)

try:
    estado_anterior = None
    while True:
        izq = GPIO.input(SENSOR_IZQ)
        der = GPIO.input(SENSOR_DER)

        if izq == 1 and der == 1:
            if estado_anterior != "RECTO":
                print("→ Avanzando recto")
                estado_anterior = "RECTO"
            avanzar()

        elif izq == 1 and der == 0:
            if estado_anterior != "IZQUIERDA":
                print("↺ Girando izquierda")
                estado_anterior = "IZQUIERDA"
            girar_izquierda()

        elif izq == 0 and der == 1:
            if estado_anterior != "DERECHA":
                print("↻ Girando derecha")
                estado_anterior = "DERECHA"
            girar_derecha()

        else:
            if estado_anterior != "PARADO":
                print("■ Parado (fuera de línea)")
                estado_anterior = "PARADO"
            detener()

        time.sleep(0.05)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nPrograma terminado.")
