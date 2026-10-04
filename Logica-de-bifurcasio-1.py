# En esta actividad aremos la solicitud para determinar la longitud de un script
# En otra peticion para determinar los cuadrantes de "Y" y "X" si son positivos o negativos

def evaluar_palabra (palabra):
    """
    Evalua la longuitud de un string y valida si tiene entre 4 y 8.
    """
    longitud = len(palabra)
    
    if 4 <= longitud <= 8:
        print("Palabra Correcta")
    elif longitud < 4:
        print(f"Faltan letras para completar(Su palabra solo tiene {longitud} letras, se requieren minimo 4 para continuar)")
    else:
        print(f"Ahora sobran letras(Su palabra tiene {longitud} letras, solo debe tener 8 como maximo)")


# Ahora vamos a determinar los cuadrantes de "Y" y "X" si son positivos o negativos 

def evaluar_cuadrante(x, y):
    """
    Evalua los valores de X y Y para determinar en que cuadrante se encuentra
    """
    if x > 0 and y > 0:
        print("El punto se encuentra en el primer cuadrante")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el segundo cuadrante")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el tercer cuadrante")
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuarto cuadrante")
    else:
        print("El punto se encuentra sobre uno de los ejes") 
        
        
# Ahora vamos a ejecutar las funciones de los cuadrantes y longuitud de la palabra

if __name__ == "__main__":
    print("Validacion de la palabra correctamente")
    entrada_palabra = input("Ingrese una palabra: ").strip()
    evaluar_palabra(entrada_palabra) 
    
    print("\nValidacion de los cuadrantes de X y Y en el plano cartesiano")
    try:
        x = float(input("Ingrese el valor de X: "))
        y = float(input("Ingrese el valor de Y: "))
        evaluar_cuadrante(x, y)
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos para X y Y.")
        
