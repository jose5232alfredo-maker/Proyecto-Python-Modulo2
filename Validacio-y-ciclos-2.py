# Nuevamente daremos ejecusion al codigo similar anterior,pero esta ves agrgando el bucle de while y forzar al usuario a infresar el dato correctamente
# Ademas de implementar este dato en el plano cartesiano si es "0", marcara error o si falta un dato, 


def evaluar_palabra ():
    """
    Solicitamos una palabra asta que cumpla con la longuitud de un string y valida si tiene entre 4 y 8.
    """
    while True:
        palabra = input("Ingrese una palabra: ").strip()
        longitud = len(palabra)

        if 4 <= longitud <= 8:
            print("Palabra Correcta")
            break
        elif longitud < 4:
            print(f"Faltan letras para completar(Su palabra solo tiene {longitud} letras, se requieren minimo 4 para continuar)")
        else:
            print(f"Ahora sobran letras(Su palabra tiene {longitud} letras, solo debe tener 8 como maximo)")


# Daremos el bucle while sobre las coordenadas asi el usuario no ingrese valores no numericos y se le pedira que ingrese nuevamente el valor de X y Y

def solicitar_coordenada(nombre_eje):
    """
    Pide una coordenada al usuario y no permitir valores no numéricos.
    """
    while True:
        try:
            val = float(input(f"Ingrese el valor de {nombre_eje}: "))
            if val == 0:
                print("Error: El valor no puede ser 0. Intente nuevamente.")
            else:
                return val
        except ValueError:
            print(f"Error: Ingrese un valor numérico válido para {nombre_eje}.")

# Ahora vamos a determinar los cuadrantes de "Y" y "X" si son positivos o negativos 

def evaluar_cuadrante():
    """
    Evalua los valores de X y Y para determinar en que cuadrante se encuentra
    """
    x = solicitar_coordenada("X")
    y = solicitar_coordenada("Y")
    
    if x > 0 and y > 0:
        print("El punto se encuentra en el primer cuadrante")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el segundo cuadrante")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el tercer cuadrante")
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuarto cuadrante")

# Ahora vamos a ejecutar las funciones de los cuadrantes y longuitud de la palabra

if __name__ == "__main__":
    print("Validacion de la palabra correctamente")
    evaluar_palabra () 
    
    print("Validacion de los cuadrantes de X y Y en el plano cartesiano")
    evaluar_cuadrante ()



