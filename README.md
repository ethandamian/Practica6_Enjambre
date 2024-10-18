# Practica6_Enjambre
## Integrantes de equipo:
- Aguirre Morales Gael Alejandro(319165704)
- Fernández Blancas Melissa Lizbeth (319281778)
- Sánchez Salmerón Ethan Damian (319122323)
- Sánchez Nava Rodrigo (319222571)
- Lopez Carrillo Alan Ignacio (420014760)

## Acerca de los programas
Se realizaron 4 juegos para esta práctica:
- 4 en linea
- Ahorcado
- Piedra papel o tijera
- Gato
Cada juego fue realizado en python con sockets y pygame, siguiendo una estructura Servidor -> (Cliente, Network) donde Network se encarga de conectar cada cliente al servidor, y el cliente realiza las acciones de un jugador. 

## Requisitos

Para correr cada juego, se necesita tener instalado **pygame**, con el comando
  ```bash
  pip instal pygame
  ```

## Como jugar

Cada juego se ejecuta de la misma manera:
1. Primero hay que moverse a la carpeta del juego
```bash
cd CarpetaDelJuego
```
  Las carpetas de los juegos son:
  - Ahorcado
  - Conecta4
  - Gato
  - RockPaperScissors

2. Hay que inicializar el servidor con
```bash
python Servidor.py
```
3. Una vez Inicializado, conectamos el cliente al servidor, que es el jugador que va a competir con una IA en cada juego (excepto para el juego de Ahorcado)
```bash
python Cliente.py
```
### Ahorcado
Para jugar el ahorcado, al conectar un cliente, se tendrá esta vista
![image](https://github.com/user-attachments/assets/8778e0fb-750e-473a-9017-209daf153667)

Solo hay que escribir una letra con el teclado e intentar adivinar la palabra. **Solo se tiene 10 intentos por palabra**
</br>
Si se acaban los intentos y no se adivinó la palabra, se podrá volver a intentar con otra palabra, dando click al boton "Reiniciar"
![image](https://github.com/user-attachments/assets/65fed1c8-2e6a-41b7-8c39-7d7307dcedf9)

Mismo caso si la palabra es adivinada
![image](https://github.com/user-attachments/assets/59244be9-cd8b-4e07-b4f3-93689d7a31de)




### Conecta 4

Para este juego, cuando nos conectamos con un cliente, tendremos esta vista
![image](https://github.com/user-attachments/assets/ce545839-8411-491c-9c3d-ae09b1631e97)

Y para realizar un movimiento, solo hay que dar click en alguna de las columnas del tablero. Se jugará con una IA, que usa (intenta xd) un algoritmo **MinMax** para la predicción de los movimientos. 
![image](https://github.com/user-attachments/assets/f01f900a-c86f-47ad-9001-048907c42994)

Una vez que alguno de los jugadores conecte 4 fichas en horizontal, vertical o en diagonal, se anuncia el ganador y se puede volver a jugar dando click en el boton de "Reiniciar"
![image](https://github.com/user-attachments/assets/f7cfea0f-abc7-4130-80d8-a6fc0f03824b)


### Piedra papel o tijera

Cuando se conecta un cliente al servidor, se abre esta venta del juego
![image](https://github.com/user-attachments/assets/28d5f6f3-1d89-44e6-a36a-6839e3995e69)

Simplemente hay que elegir un movimiento entre "Rock", "Scissors" o "Paper", dando click en su respectivo botón. Se jugará contra una IA que lo único que hace es tomar una opción al azar de estas tres, y realizar ese movimiento. Si se le gana a la IA, se anuncia el ganador, si se pierde o se empata, igual. En los tres casos, el juego se reincia sólo y se vuelve a jugar. 
![image](https://github.com/user-attachments/assets/a2f9f885-ddee-4d1d-934d-68bca55c802c)

![image](https://github.com/user-attachments/assets/9001765e-5c7c-4d4b-b842-c3204e7444c6)


### Gato 
El juego inicia en esta ventana 

![image](https://github.com/user-attachments/assets/39a300e5-e0e9-40f5-b14c-d218f46c9ba5)

Jugamos como "X" contra la IA que es "O". Simplemente hay que dar click en una de las celdas a la que queremos tirar y la IA va a realizar un **MinMax** para decidir su movimiento. 
Gana el jugador que conecte tres de sus "X" o "O" de forma horizontal, vertical o en diagonal. El ganador será anunciado y se podrá reiniciar el juego con el botón de "Reiniciar", lo mismo si hay un empate, es decir, que el tablero se llenó y nadie conectó sus respectivas "fichas". 

![image](https://github.com/user-attachments/assets/cbf89a9e-d48b-4a22-abb5-8e69b6743ad7)

![image](https://github.com/user-attachments/assets/c4e00b64-8cbb-4df2-8fd4-f09443c117c0)


>[!NOTE]
> Ejecutamos varias veces el juego (mas de 10) y no fuimos capaces de ganarle a la IA, al parecer piensa mucho jajajj

