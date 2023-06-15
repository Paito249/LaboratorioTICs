import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import math as mt
import numpy as np

DHTSensor = Adafruit_DHT.DHT11
KY015 = 4

#CLASE 0: FRIO (ABRIGARSE)
#CLASE 1: CALOR (NO ABRIGARSE)

#CONSIDERO INVIERNO
prior_0 = 0.75
prior_1 = 0.25


#HUMEDAD PROMEDIO EN QUE SE SIENTE FRIO/CALOR
hum_mean_0 = 25
hum_var_0 = 64
hum_mean_1 = 10
hum_var_1 = 49

#TEMPERATURA PROMEDIO EN QUE SE SIENTE FRIO O CALOR
temp_mean_0 = int(input('Temperatura promedio en que le da frio: ')) #13
temp_var_0 = 2
temp_mean_1 = int(input('Temperatura promedio en que le da calor: ')) #24
temp_var_1 = 4


#VALORES PARA FRIO
mean_0 = [hum_mean_0, temp_mean_0]
var_0 = [hum_var_0, temp_var_0]

#VALORES PARA CALOR
mean_1 = [hum_mean_1, temp_mean_1]
var_1 = [hum_var_1, temp_var_1]

#CLASIFICADOR NAIVE BAYES CONSIDERANDO GAUSSIANIDAD DE LAS VARIABLES
def NB_classifier(test, clase = 0):
    if clase == 0:
        global prior_0, mean_0, var_0
        a = 1
        for n in range(len(test)):
            a *= (mt.exp(-((test[n]-mean_0[n])**2)/(2*var_0[n])))/((2*mt.pi*(var_0[n]))**0.5)
        return a*prior_0
    elif clase == 1:
        global prior_1, mean_1, var_1
        a = 1
        for n in range(len(test)):
            a *= (mt.exp(-((test[n]-mean_1[n])**2)/(2*var_1[n])))/((2*mt.pi*(var_1[n]))**0.5)
        return a*prior_1
h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, KY015)

test = [h, t]
print(f'Temp: {t}; Humedad: {h}')
p_frio = NB_classifier(test, clase=0)
p_calor = NB_classifier(test, clase=1)
p = p_frio/(p_frio + p_calor)
print(f'La probabilidad de que sientas frio es de un {np.round(100*p,2)}%')
if p > 0.5: print('LLEVA CHALECO!!')
else: print('Si eres team verano, es tu dia de suerte ;)')
