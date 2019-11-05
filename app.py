#!/usr/bin/python3
# -*- coding: utf-8 -*-
import signal
import sys
import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

led = 4
buzzer = 18

INTERVAL = 0.2

CODES = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}

def dit():
    GPIO.output(led, GPIO.HIGH)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(INTERVAL)
    GPIO.output(led, GPIO.LOW)
    GPIO.output(buzzer, GPIO.LOW)

def dah():
    GPIO.output(led, GPIO.HIGH)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(INTERVAL * 3)
    GPIO.output(led, GPIO.LOW)
    GPIO.output(buzzer, GPIO.LOW)

def morse(msg):
    words = msg.split(' ')

    for word in words:
        time.sleep(INTERVAL * 7)

        for key in word:
            time.sleep(INTERVAL * 3)

            code = CODES[key]

            for c in code:
                if c == '.':
                    dit()
                else:
                    dah()

                time.sleep(INTERVAL)
 
def processData(client, userdata, message):
    topic = str(message.topic)
    msg = str(message.payload.decode('utf-8'))
    print('Received message: {0}'.format(msg))
    morse(msg)

try:
    print('Starting...')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(buzzer, GPIO.OUT)

    client = mqtt.Client('NodePI')
    client.connect('test.mosquitto.org', 1883)
    client.subscribe('NodeJS')
    client.on_message = processData
    client.loop_start()

    while True:
        pass

except KeyboardInterrupt as e:
    print('Cya!')
except Exception as e:
    print('Error: {0}.'.format(e))
finally:
    print('\nQuitting...')
    GPIO.cleanup()
    sys.exit(0)

