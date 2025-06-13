# Guia de uso
## 1. Ejecutar el *broker*
Abre una terminal (*cmd*)
~~~bash
python broker.py
~~~
Se mostrara como resultado:
~~~bash
[broker] Escuchando en 0.0.0.0:14000...
~~~
## 2. Ejecutar una o más suscripciones
Abre una terminal y ejecuta un suscriptor o más
~~~bash
python subscriber.py
~~~
Cuando se te pida escribe el tema (*topic*), por ejemplo:
~~~bash
Tema a suscribirse: Deportes
~~~
El sistema mantendra la conexion abierta esperando mensaje del *broker*
## 3. Ejecutar una o más publicaciones
En otra terminal:
~~~bash
python publisher.py
~~~
Envia un mensaje en este formato:
~~~bash
deportes: ¡El America ganó 15-8!
~~~
Todos los *suscriptores* suscritos a *deportes* recibiran:
~~~bash
[deportes] !El Pumas ganó 5-0!
~~~