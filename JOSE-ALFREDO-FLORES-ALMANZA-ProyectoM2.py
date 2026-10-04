# Ahora vamos a terminar con el modulo 2 de este curso, fue un proceso especial y muy interesante

# PROYECTO FINAL DEL MODULO 2: CONSOLIDADO DE RETOS ( BIFURCASION, CICLOS Y COLECCIONES )

# Descripcion: se usa el script que integra dos funcipnalidades princiales interactivas
# Validacion de longuitud de una palabra ingresadapor el usuario
# Identificacion del cuadrante en el plano cartesiano usando tuplas e indices

# Se crean nombres para los cuadrantes asi se evita que se modifiquen o se pierda la informacion

CUADRANTE = (
    "Cuadrante 1", #indice 0: (Y>0, X>0)
    "Cuadrante 2", #indice 1: (Y>0, X<0)
    "Cuadrante 3", #indice 2: (Y<0, X<0)
    "Cuadrante 4"  #indice 3: (Y<0, X>0)
)
def evaluar_palabra():
    """
    Solicita una palabra al usuario y valida su longitud, asegurando que tenga entre 4 y 8 caracteres al igual se almacena en una lista.
    
    """
    historial_palabras = []  # Lista para almacenar las palabras ingresadas por el usuario
    print("\nValidacion de la palabra correctamente")
    
    while True:
        palabra = input("Ingrese una palabra (Entre 4 y 8 letras en la palabra): ").strip()
        longitud = len(palabra)
        historial_palabras.append(palabra)  # Agrega la palabra al historial

        if 4 <= longitud <= 8:
            print("Palabra Correcta")
            break
        elif longitud < 4:
            print(f"Faltan letras para completar(Su palabra solo tiene {longitud} letras, se requieren minimo 4 para continuar)")
            print(f"intenta de nuevo")
        else:
            print(f"Ahora sobran letras(Su palabra tiene {longitud} letras, solo debe tener 8 como maximo)")
            print(f"intenta de nuevo")  
            
    print("\nHistorial de palabras ingresadas:")
    for i, palabra in enumerate(historial_palabras, start=1):
        print(f"intento {i}. {palabra}")
    print("----------------\n")
    
def solicitar_coordenada(nombre_eje):
    """
    Pide una coordenada al usuario y no permite valores no numéricos ni cero.
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

def evaluar_cuadrante():
    """
    Evalua los valores de X y Y para determinar en que cuadrante se encuentra
    """
    print("\nValidacion de los cuadrantes de X y Y en el plano cartesiano")
    x = solicitar_coordenada("X")
    y = solicitar_coordenada("Y")
    
    if x > 0 and y > 0:
        cuadrante = CUADRANTE[0]  # primer cuadrante
    elif x < 0 and y > 0:
        cuadrante = CUADRANTE[1]  # segundo cuadrante
    elif x < 0 and y < 0:
        cuadrante = CUADRANTE[2]  # tercer cuadrante
    elif x > 0 and y < 0:
        cuadrante = CUADRANTE[3]  # cuarto cuadrante 
        
    print(f"\nResultado:El punto ({x}, {y}) se encuentra en el cuadrante: {cuadrante}.\n")
    
def mostrar_menu():
    """
    Muestra un menú interactivo para que el usuario elija entre validar una palabra o determinar el cuadrante.
    """
    while True:
        print("==========================================")
        print(" MENU PRINCIPAL - PROYECTO FINAL MODULO 2 ")
        print("==========================================")
        print("Seleccione una opción:")
        print("1. Validar la longitud de una palabra")
        print("2. Determinar el cuadrante de un punto (X, Y)")
        print("3. Salir")
        
        opcion = input("Ingrese el número de la opción deseada: ").strip()
        
        if opcion == "1":
            evaluar_palabra()
        elif opcion == "2":
            evaluar_cuadrante()
        elif opcion == "3":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.\n")
            
if __name__ == "__main__":
    mostrar_menu()  
        
        