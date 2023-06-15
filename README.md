# Laboratorio TICs

Integrantes: Giovanni Castiglioni y Paola Silva.

Este repositorio tiene como objetivo, documentar y almacenar el avance realizado por el grupo para el proyecto de EL5207 Laboratorio de Tecnologías de Información y Comunicaciones de la FCFM

Descripción del tema.
Sensor: DHT11 Sensor de Temperatura y Humedad

![image](https://github.com/Paito249/LaboratorioTICs/assets/90465211/e4b8a410-7198-466e-98e5-aa9a3dd2e03f)

La conexión queda resulta directamente, pues el sensor cuenta con solo 3 pins correspondientes 
a 5V, ground y data. Existe una versión del sensor (que no tiene la placa negra 
apreciable en la imagen) que cuenta con 4 pins, pero hay uno que no se usa, y los 3 
restantes son equivalentes a los ya mencionados tras una conexión a través de una resistencia de 4.7kOhms entre los pins Data y VCC. Así, “Data” puede conectarse a cualquier pin de I/O para entregar la información a la RPI.
restantes son equivalentes a los ya mencionados tras una conexión a través de una resistencia de 4.7kOhms entre los pins Data y VCC. Así, “Data” puede conectarse a 
Luego la información se procesa mediante código programado Python usando la librería Adafruit dentro de la RPI.

El circuito resultante se presenta a continuación.

![Imagen de WhatsApp 2023-05-12 a las 16 34 47](https://github.com/Paito249/LaboratorioTICs/assets/90465211/7ce8bd03-8a47-4fdc-9e77-6bae5d3907fa)


Se eligió dar un sentido específico a este proyecto, de manera que a través de las mediciones realizadas por el sensor se determina si el usuario necesita llevar consigo chaleco o no, con el objetivo de mostrar la estrecha relación que pueden llegar a tener la vida cotidiana con la simbiosis entre modelos matemáticos de estimación y tecnologías IoT.


Los resultados obtenidos por medio del código empleado se ilustran a continuación:

![Imagen de WhatsApp 2023-05-12 a las 16 47 44](https://github.com/Paito249/LaboratorioTICs/assets/90465211/18d1cad2-d434-429b-b0ab-39dab52f1146)


Se considera pendiente:
*Terminar la conexión del servidor y probar que los resultados impresos en este correspondan a lo solicitado.
*Calibrar el sensor, para lo cual se hará uso de un termómetro higrómetro ambiental.


Se adjunta Figma del diseño del servidor web: https://www.figma.com/proto/hqCxPPQXd284caSbmxza9Y/Untitled?type=design&node-id=1-2&scaling=contain&page-id=0%3A1&starting-point-node-id=1%3A2

Este diseño fue el implementado a través de los distintos archivos que se listan a continuación:

* index.html
* estilos.css
* proyecto_lab_copy.py
* app.py

Dando como resultado la siguiente pantalla:
![image](https://github.com/Paito249/LaboratorioTICs/assets/90465211/502caf87-6594-4bf9-8ca2-d8c23fb4fe06)

Donde en los campos se ingresan los valores de frio y calor, como resultado el servidor arroja el mensaje de si debes llevar chaleco o no.

![image](https://github.com/Paito249/LaboratorioTICs/assets/90465211/3515d24b-196d-4ec9-86cf-5fabd6cd6234)


