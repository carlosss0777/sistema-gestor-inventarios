# Funciones auxiliares y utilidades

import os
import time

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
    
def pausa():
    time.sleep(1)
    
def pausaLarga():
    time.sleep(2)