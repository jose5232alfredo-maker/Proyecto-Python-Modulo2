
# Bienvenido al programa de validacion de palabras y cuadrantes en el plano cartesiano, craeremos un programa que permita al usuario ingresar datos 
# y validar en un plano cartesiano 
# Primeramente vamos a agregar nombres a los cuadrantes para visualizar mejor y evitar un errro de ubicasion

CUADRANTE = (
    "Cuadrante 1", #indice 0: (Y>0, X>0) 
    "Cuadrante 2", #indice 1: (Y>0, X<0)
    "Cuadrante 3", #indice 2: (Y<0, X<0)
    "Cuadrante 4"  #indice 3: (Y<0, X>0)
)

# Ahora vamos a crear una funcion para evaluar la longuitud de una palabra y validar si tiene entre 4 y 8 caracteres

def evaluar_palabra ():
    """
    Solicitamos una palabra al usuario y guarda todos los intentos en una lista .
    Se usa una lista por que es una coleccion ordenada y mutable, ademas de que se puede agregar o eliminar elementos.
    """
    
    # Creamos una lista vacia para almacenar los intentos del usuario y tener un registro de los intentos
    
    historial_palabras = []
    
    while True:
        palabra = input("Ingrese una palabra:(entre 4 y 8 caracteres) ").strip()
        
        # Almacenamos en una lista todos los intentos del ususario 
        
        historial_palabras.append(palabra) 
        
        longitud = len(palabra)

        if 4 <= longitud <= 8:
            print("Palabra Correcta")
            break
        elif longitud < 4:
            print(f"Faltan letras para completar(Su palabra solo tiene {longitud} letras, se requieren minimo 4 para continuar)")
        else:
            print(f"Ahora sobran letras(Su palabra tiene {longitud} letras, solo debe tener 8 como maximo)")


# Se mostrara el historial de las palabras ingresadas por el usuario al final del programa
# Es importate tener un listado de control asi el usuario vera sus errores 

    print("Historial de palabras ingresadas:")
    for i, palabra in enumerate(historial_palabras, start=1):
        print(f"{i}. {palabra}")
    print("Gracias por participar en la actividad de validacion de palabras.")

    
# Ahora pediremos al usuario que ingrese las coordenadas de "X" y "Y" 
# Se validara los datos ingresados por el usuario y se mostrara en que cuadrante se encuentra el punto ingresado 


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

# Ahora vamos a determinar los cuadrantes de "Y" y "X" si son positivos o negativos, con datso precisos y sin errores

def evaluar_cuadrante():
    """
    Evalua los valores de X y Y para determinar en que cuadrante se encuentra
    """
    x = solicitar_coordenada("X")
    y = solicitar_coordenada("Y")
    
    if x > 0 and y > 0:
        cuadrante = CUADRANTE  [1] # primer cuadrante
    elif x < 0 and y > 0:
        cuadrante = CUADRANTE  [2] # segundo cuadrante
    elif x < 0 and y < 0:
        cuadrante = CUADRANTE  [3] # tercer cuadrante  
    elif x > 0 and y < 0:
        cuadrante = CUADRANTE  [4] # cuarto cuadrante 
    print(f"El punto se encuentra en el cuadrante: {cuadrante}")

# Ahora vamos a ejecutar las funciones de los cuadrantes y longuitud de la palabra, que sean correctas y sin errores

if __name__ == "__main__":
    print("Validacion de la palabra correctamente")
    evaluar_palabra () 
    
    print("Validacion de los cuadrantes de X y Y en el plano cartesiano")
    evaluar_cuadrante ()

