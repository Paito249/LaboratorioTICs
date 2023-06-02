# Laboratorio TICs

Integrantes: Giovanni Castiglioni y Paola Silva.

Este repositorio tiene como objetivo, documentar y resguardar el avance realizado por el grupo para el trabajo de Laboratorio de Tecnologías de la información y comunicaciones de la FCFM

Descripción del tema.
Sensor: DHT11 Sensor de Temperatura y Humedad

![image](https://github.com/Paito249/LaboratorioTICs/assets/90465211/e4b8a410-7198-466e-98e5-aa9a3dd2e03f)

La conexión es bastante directa, pues el sensor tiene solo 3 pins, correspondientes 
a 5V, ground y data. Existe una versión del sensor (que no tiene la placa negra 
apreciable en la imagen) que cuenta con 4 pins, pero hay uno que no se usa, y los 3 
restantes son equivalentes a los ya mencionados. Así, “data” puede conectarse a 
cualquier pin de I/O para entregar la información a la RPI.
Luego la información de procesa con Python usando la librería Adafruit

El circuito resultante se presenta a continuación.

![Imagen de WhatsApp 2023-05-12 a las 16 34 47](https://github.com/Paito249/LaboratorioTICs/assets/90465211/7ce8bd03-8a47-4fdc-9e77-6bae5d3907fa)


Se eligió dar un sentido específico a este proyecto, de manera que a tráves de las mediciones realizadas por el sensor se determina si el usuario necesita llevar consigo chaleco o no.


La salida del código empleado se ilustra a continuación.

![Imagen de WhatsApp 2023-05-12 a las 16 47 44](https://github.com/Paito249/LaboratorioTICs/assets/90465211/18d1cad2-d434-429b-b0ab-39dab52f1146)


Se considera pendiente:
*Terminar la conexión del servidor y probar que los resultados impresos en este correspondan a lo solicitado.
*Calibrar el sensor, para lo cual se hará uso de un termómetro higrómetro ambiental.
