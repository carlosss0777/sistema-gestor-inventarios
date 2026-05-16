# Validaciones globales

# Validacion de indice 
def validar_indice(indice, size):
    if not indice or indice.strip() == "":
        raise ValueError("El indice no puede estar vacio")
    
    try:
        indice_int = int(indice)
    except:
        raise ValueError("El indice debe ser numerico")
    
    if indice_int < 0 or indice_int > size:
        raise ValueError("Indice no valido")
    
    return indice_int - 1