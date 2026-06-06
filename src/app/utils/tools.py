# Funciones auxiliares y utilidades

import os
import time

def limpiar_pantalla():
    """
    Limpia la pantalla de la consola. 
    """
    os.system("cls" if os.name == "nt" else "clear")
    
def pausa():
    """
    Pausa breve
    """
    time.sleep(1)
    
def pausaLarga():
    """
    Pausa larga
    """
    time.sleep(2)
    
def detener():
    """
    Detiene la ejecución y espera a que el usuario presione ENTER
    """
    input("\nPresiona ENTER para continuar")
    
def mensaje_error(e):
    """
    Muestra un mensaje de error con el detalle del error y una invitación a intentar nuevamente.
    """
    print("\n------------------------------------------------------------")
    print(f"ERROR: {e}")
    print("Intenta nuevamente...")
    print("------------------------------------------------------------\n")