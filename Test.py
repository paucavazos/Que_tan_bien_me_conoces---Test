#La biblioteca os permite trabajar con archivos y carpetas. (Consultar referencias).
import os

#Para que el programa funcione correctamente, el  archivo de código "Test.py" y los archivos de texto "test.txt" y "resultados.txt" deben estar en la misma carpeta. Lo que 
#hacen estas siguientes 3 líneas de código es identificar dónde está guardado "Test.py", así, en caso de que el usuario llegue a cambiar de carpeta alguno(s) de estos 3 
#archivos, al momento de correr el programa y guardar la información en los archivos de texto, automáticamente "aparece(n)" el (los) otro(s) ahí mismo. Es decir, no puedes 
#seperar este trío de archivos.

carpeta = os.path.dirname(os.path.abspath(__file__))
#Esta línea obtiene la ubicación de la carpeta donde se encuentra guardado el archivo de Python, para que el programa pueda localizar los demás archivos desde esa misma 
#carpeta.
# - __file__: indica el archivo de Python que se está ejecutando.
# - os.path.abspath(): obtiene la dirección completa de ese archivo.
# - os.path.dirname(): obtiene la dirección de la carpeta donde se encuentra el archivo.
# - carpeta: es la variable donde se guarda esa dirección.

ruta_test = os.path.join(carpeta, "test.txt")
#Esta línea sirve para crear la ruta completa del archivo test.txt, uniendo la ubicación de la carpeta con el nombre del archivo. El resultado se guarda en la variable
#ruta_test.
# - ruta_test: variable donde se guarda la ruta del archivo.
# - os.path.join(): función que une dos partes de una ruta.
# - carpeta: variable que contiene la ubicación de la carpeta donde está el código.
# - "test.txt": nombre del archivo que se quiere localizar.

ruta_resultados = os.path.join(carpeta, "resultados.txt")
#Esta línea crea la ruta completa del archivo resultados.txt, uniendo la ubicación de la carpeta con el nombre del archivo. El resultado se guarda en la variable 
#ruta_resultados.
# - ruta_resultados: variable donde se guarda la ruta del archivo.
# - os.path.join(): función que une dos partes de una ruta.
# - carpeta: variable que contiene la ubicación de la carpeta donde está el código.
# - "resultados.txt": nombre del archivo que se quiere localizar.

#La siguiente función calcula el porcentaje de tu calificación dividiendo las preguntas correctas entre el total de preguntas y luego multiplica por 100.
def calcular_calificacion(preguntas, correctas):
    calificacion = (correctas / preguntas) * 100
    return calificacion

#Con ese reultado que dio en la primera función, se ejecuta esta función:
def mostrar_resultado(calificacion):
    print("\nTu calificacion es:", round(calificacion, 2), "%") #Redondea la calificación a 2 decimales... \n se utiliza para dar un salto de línea.

    #Dependiendo tu calificación, se muestra en pantalla un texto diferente.
    if calificacion >= 90:
        print("¡Me conoces muchisimo!")
    elif calificacion >= 70:
        print("¡Me conoces bien!")
    elif calificacion >= 50:
        print("Me conoces más o menos.")
    else:
        print("Tenemos que convivir más.")


#Esta función, como su nombre lo indica, es para CREAR el test. Pide el nombre del creador del test, el número de preguntas que tendrá el test, las preguntas, las opciones y
#la opción correcta.

def crear_test():
    nombre = input("¿Como te llamas? ").strip().capitalize() #Se eliminan espacios en blanco al principio, y si el usuario escribió su nombre como "ana" o "ANA", solo 
    #se pone la primera letra en mayúsculas --> Ana.

    #Este bloque solicita al usuario la cantidad de preguntas y convierte su respuesta a un número entero. Si escribe algo que no sea un número válido, muestra un mensaje de
    #error y termina la función.

    # - try: intenta ejecutar el código.
    # - preguntas: variable donde se guarda la cantidad de preguntas.
    # - input(): función que solicita información al usuario.
    # - int(): función que convierte la respuesta en un número entero.
    # - except ValueError: detecta si ocurre un error al convertir el dato.
    try: #(Consultar referencias)
        preguntas = int(input("¿Cuantas preguntas tendra el test? "))
    except ValueError: #(Consultar referencias)
        print("Debes escribir un numero entero.")
        return

    if preguntas <= 0:
        print("El test debe tener al menos una pregunta.")
        return

    test = [] # Lista vacía que será llenada.

    for numero in range(preguntas): # Ciclo que se repetirá la cantidad de veces que corresponda al número de preguntas que haya en el test.
        print("\nPregunta", numero + 1) # Suma 1 para que la numeración comience en 1 y no 0.

        pregunta = input("Escribe la pregunta: ").strip()
        opcion1 = input("Opcion A: ").strip()
        opcion2 = input("Opcion B: ").strip()
        opcion3 = input("Opcion C: ").strip()
        opcion4 = input("Opcion D: ").strip()

        correcta = input(
            "Letra de la respuesta correcta: "
        ).strip().upper() # De esta manera, así el usuario ponga la opción correcta en minúscula, ésta se pondrá automáticamente en mayúscula.

        while correcta not in ["A", "B", "C", "D"]: # Mientras el usuario escriba algo más que no sea A, B, C o D, se le obligará a usar una de estas letras para continuar.
            print("Selecciona A, B, C o D.")
            correcta = input(
                "Letra de la respuesta correcta: "
            ).strip().upper()

        test.append([
            pregunta, opcion1, opcion2,
            opcion3, opcion4, correcta
        ]) # A la lista se le van agregando preguntas, opciones, y opciones correctas.

    archivo = open(ruta_test, "w") # Se abre el archivo test.txt en modo escritura para guardar la información del test. El archivo abierto se guarda en la variable 
    #archivo.

    archivo.write(nombre + "\n") # Se escribe el nombre del usuario en el archivo test.txt, agregando un salto de línea después del nombre.
    archivo.write(str(preguntas) + "\n") # Se escribe la cantidad de preguntas en el archivo test.txt, convirtiéndola primero en texto y agregando un salto de línea.

    # Estos ciclos recorren la lista test y escriben cada uno de sus datos en el archivo, agregando un salto de línea después de cada uno.
    for pregunta in test:
        for dato in pregunta:
            archivo.write(dato + "\n")

    archivo.close() # Se cierra el archivo.

    print("\n¡Tu test se ha guardado correctamente!")

# Esta función es para RESPONDER un test.
def responder_test():

    if not os.path.exists(ruta_test): # Esta condición verifica si el archivo ubicado en ruta_test no existe, para realizar una acción en caso de que no se encuentre. 
        # os.path.exists(): función que verifica si existe un archivo o carpeta.
        print("\nNo existe ningún test. Primero debes crear uno.")
        return # Simplemente termina la ejecución de la función.

    archivo = open(ruta_test, "r") # Se abre el archivo test.txt en modo lectura para poder consultar la información que contiene.
    datos = archivo.readlines() # Esta línea lee todas las líneas del archivo y las guarda en la variable datos como una lista.
    archivo.close()

    if len(datos) < 2: # Verificar si la lista datos tiene menos de dos elementos, para comprobar que el archivo contenga la información necesaria.
        print("\nEl archivo del test esta vacío o incompleto.")
        return

    try: # intenta ejecutar el código.
        preguntas = int(datos[1].strip())
    except ValueError: # Detecta si ocurre un error al convertir el dato.
        print("\nEl archivo contiene datos incorrectos.")
        return

    if preguntas <= 0 or len(datos) != 2 + preguntas * 6: # Verificar que la cantidad de preguntas sea mayor que cero y que el archivo tenga la cantidad de datos esperada. 
        #Si alguna de estas condiciones no se cumple, se ejecuta el bloque correspondiente.
        # 2 + preguntas * 6: calcula la cantidad de líneas que debería tener el archivo: dos datos iniciales (nombre del creador del test, y cantidad de preguntas) y seis
        #por cada pregunta (pregunta, opción 1, opción 2, opción 3, opción 4, opción correcta).
        print("\nEl archivo del test está incompleto o tiene errores.")
        return

    nombre = datos[0].strip() # obtiene el nombre guardado en la primera posición de la lista datos, elimina los espacios y saltos de línea de los extremos y lo guarda en 
    #la variable nombre.
    
    test = [] # Lista vacía que será llenada.

    for numero in range(preguntas):
        posicion = 2 + numero * 6 # Calcula la posición de la lista datos donde comienza la información de cada pregunta y guarda el resultado en la variable posicion.

        test.append([
            datos[posicion].strip(),
            datos[posicion + 1].strip(),
            datos[posicion + 2].strip(),
            datos[posicion + 3].strip(),
            datos[posicion + 4].strip(),
            datos[posicion + 5].strip().upper()
        ]) # Se obtienen los seis datos de cada pregunta del archivo y los agrega como una lista dentro de test, eliminando los espacios y saltos de línea. También 
        #convierte la respuesta correcta a mayúsculas.

    participante = input("\n¿Cuál es tu nombre? ").strip().capitalize() # Se pide el nombre de quien responderá el quiz.
    correctas = 0 # Contador

    print("\nTest de", nombre) # Nombre del creador del test.

    # Este ciclo recorre todas las preguntas del test y muestra en pantalla cada pregunta junto con sus cuatro opciones de respuesta (A, B, C y D).
    for numero in range(preguntas):
        print("\n" + test[numero][0])
        print("A)", test[numero][1])
        print("B)", test[numero][2])
        print("C)", test[numero][3])
        print("D)", test[numero][4])

        respuesta = input("Tu respuesta: ").strip().upper() #Se pide la respuesta al usuario.

        while respuesta not in ["A", "B", "C", "D"]:
            print("Selecciona A, B, C o D.")
            respuesta = input("Tu respuesta: ").strip().upper()

        if respuesta == test[numero][5]: #Si la respuesta es correcta se suma 1 al contador.
            correctas = correctas + 1

    calificacion = calcular_calificacion(preguntas, correctas) # Se manda a llamar la función de calcular_calificación

    # Estas líneas muestran en pantalla los resultados del test, indicando el nombre del participante y la cantidad de respuestas correctas que obtuvo.
    print("\nResultados de", participante)
    print("Respuestas correctas:", correctas, "de", preguntas)

    mostrar_resultado(calificacion)

    archivo = open(ruta_resultados, "a") # Esta línea abre el archivo resultados.txt en modo añadir, para guardar nuevos resultados sin borrar los que ya estaban registrados.

    archivo.write(
        participante + " - "
        + str(round(calificacion, 2)) + "%\n"
    ) # Se escribe el nombre del participante junto a su puntaje.

    archivo.close()

    print("\nTu resultado se ha guardado correctamente.")

# Este ciclo mantiene el menú del programa en funcionamiento, mostrando las tres opciones disponibles: crear un test, responder un test o salir.
while True:
    print("\n¿QUÉ TANTO ME CONOCES?")
    print("\n1. Crear un test")
    print("2. Responder un test")
    print("3. Salir")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        crear_test()

    elif opcion == "2":
        responder_test()

    elif opcion == "3":
        print("\n¡Gracias por utilizar el programa!")
        break # te permite salirte del ciclo.

    else:
        print("\nOpción no válida. Intenta nuevamente.")
