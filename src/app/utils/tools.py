# Funciones auxiliares y utilidades

import os
import time

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
    
def pausa():
    time.sleep(1)
    
def pausaLarga():
    time.sleep(2)
    
def detener():
    input("\nPresiona ENTER para continuar")
    
def mensaje_error(e):
    print("\n------------------------------------------------------------")
    print(f"ERROR: {e}")
    print("Intenta nuevamente...")
    print("------------------------------------------------------------\n")