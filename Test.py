
import os


def calcular_calificacion(preguntas, correctas):
    calificacion = (correctas / preguntas) * 100
    return calificacion


def mostrar_resultado(calificacion):
    print("\nTu calificacion es:", round(calificacion, 2), "%")

    if calificacion >= 90:
        print("¡Me conoces muchisimo!")
    elif calificacion >= 70:
        print("¡Me conoces bien!")
    elif calificacion >= 50:
        print("Me conoces más o menos.")
    else:
        print("Tenemos que convivir mas.")


def crear_test():
    nombre = input("¿Como te llamas? ").strip().capitalize()

    try:
        preguntas = int(input("¿Cuantas preguntas tendra el test? "))
    except ValueError:
        print("Debes escribir un numero entero.")
        return

    if preguntas <= 0:
        print("El test debe tener al menos una pregunta.")
        return

    test = []

    for numero in range(preguntas):
        print("\nPregunta", numero + 1)

        pregunta = input("Escribe la pregunta: ").strip()
        opcion1 = input("Opcion A: ").strip()
        opcion2 = input("Opcion B: ").strip()
        opcion3 = input("Opcion C: ").strip()
        opcion4 = input("Opcion D: ").strip()

        correcta = input(
            "Letra de la respuesta correcta: "
        ).strip().upper()

        while correcta not in ["A", "B", "C", "D"]:
            print("Selecciona A, B, C o D.")
            correcta = input(
                "Letra de la respuesta correcta: "
            ).strip().upper()

        test.append([
            pregunta, opcion1, opcion2,
            opcion3, opcion4, correcta
        ])

    archivo = open("test.txt", "w")

    archivo.write(nombre + "\n")
    archivo.write(str(preguntas) + "\n")

    for pregunta in test:
        for dato in pregunta:
            archivo.write(dato + "\n")

    archivo.close()

    print("\n¡Tu test se ha guardado correctamente!")


def responder_test():

    if not os.path.exists("test.txt"):
        print("\nNo existe ningun test. Primero debes crear uno.")
        return

    archivo = open("test.txt", "r")
    datos = archivo.readlines()
    archivo.close()

    if len(datos) < 2:
        print("\nEl archivo del test esta vacio o incompleto.")
        return

    try:
        preguntas = int(datos[1].strip())
    except ValueError:
        print("\nEl archivo contiene datos incorrectos.")
        return

    if preguntas <= 0 or len(datos) != 2 + preguntas * 6:
        print("\nEl archivo del test esta incompleto o tiene errores.")
        return

    nombre = datos[0].strip()
    test = []

    for numero in range(preguntas):
        posicion = 2 + numero * 6

        test.append([
            datos[posicion].strip(),
            datos[posicion + 1].strip(),
            datos[posicion + 2].strip(),
            datos[posicion + 3].strip(),
            datos[posicion + 4].strip(),
            datos[posicion + 5].strip().upper()
        ])

    participante = input("\n¿Cuál es tu nombre? ").strip().capitalize()
    correctas = 0

    print("\nTest de", nombre)

    for numero in range(preguntas):
        print("\n" + test[numero][0])
        print("A)", test[numero][1])
        print("B)", test[numero][2])
        print("C)", test[numero][3])
        print("D)", test[numero][4])

        respuesta = input("Tu respuesta: ").strip().upper()

        while respuesta not in ["A", "B", "C", "D"]:
            print("Selecciona A, B, C o D.")
            respuesta = input("Tu respuesta: ").strip().upper()

        if respuesta == test[numero][5]:
            correctas = correctas + 1

    calificacion = calcular_calificacion(preguntas, correctas)

    print("\nResultados de", participante)
    print("Respuestas correctas:", correctas, "de", preguntas)

    mostrar_resultado(calificacion)

    archivo = open("resultados.txt", "a")

    archivo.write(
        participante + " - "
        + str(round(calificacion, 2)) + "%\n"
    )

    archivo.close()

    print("\nTu resultado se ha guardado correctamente.")


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
        break

    else:
        print("\nOpción no valida. Intenta nuevamente.")
