# import Adafruit_DHT
# import RPi.GPIO as GPIO
import time
import math as mt
import numpy as np


class Classifier():
    def __init__(self,frio,calor):
        # self.DHTSensor = Adafruit_DHT.DHT11
        # self.KY015 = 4
        self.frio=frio
        self.calor=calor

    
    def NB_classifier(self,test):

        #HUMEDAD PROMEDIO EN QUE SE SIENTE FRIO/CALOR
        hum_mean_0 = 23
        hum_var_0 = 64
        hum_mean_1 = 16
        hum_var_1 = 49
        #TEMPERATURA PROMEDIO EN QUE SE SIENTE FRIO O CALOR
        temp_mean_0 = self.frio #13
        temp_var_0 = 5
        temp_mean_1 = self.calor #24
        temp_var_1 = 4
        #VALORES PARA FRIO
        mean_0 = [hum_mean_0, temp_mean_0]
        var_0 = [hum_var_0, temp_var_0]
        #VALORES PARA CALOR
        mean_1 = [hum_mean_1, temp_mean_1]
        var_1 = [hum_var_1, temp_var_1]
        #CONSIDERO INVIERNO
        prior_0 = 0.65
        prior_1 = 0.35

        p_frio = 1
        for n in range(len(test)):
            p_frio *= (mt.exp(-((test[n]-mean_0[n])**2)/(2*var_0[n])))/((2*mt.pi*(var_0[n]))**0.5)
        p_frio *= prior_0

        p_calor = 1
        for n in range(len(test)):
            p_calor *= (mt.exp(-((test[n]-mean_1[n])**2)/(2*var_1[n])))/((2*mt.pi*(var_1[n]))**0.5)
        p_calor *= prior_1

        return p_frio/(p_frio + p_calor)

    def resp(self):
        #CLASE 0: FRIO (ABRIGARSE)
        #CLASE 1: CALOR (NO ABRIGARSE)
        
        # read = Adafruit_DHT.read_retry(self.DHTSensor, self.KY015)
        read=(30,10)
        p_frio = self.NB_classifier(read)

        return read, p_frio
    