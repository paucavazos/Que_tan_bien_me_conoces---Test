
def calcular_calificacion(preguntas, correctas):
    calificacion = (correctas / preguntas) * 100
    return calificacion


def mostrar_resultado(calificacion):
    print("\nTu calificacion es:", round(calificacion, 2), "%")

    if calificacion >= 90:
        print("¡Me conoces muchísimo!")
    elif calificacion >= 70:
        print("¡Me conoces bien!")
    elif calificacion >= 50:
        print("Me conoces más o menos.")
    else:
        print("Tenemos que convivir más.")


def crear_test():
    nombre = input("¿Cómo te llamas? ").strip().capitalize()

    preguntas = int(input("¿Cuántas preguntas tendrá el test? "))
    test = []

    for numero in range(preguntas):
        print("\nPregunta", numero + 1)

        pregunta = input("Escribe la pregunta: ").strip()
        opcion1 = input("Opcion A: ").strip()
        opcion2 = input("Opcion B: ").strip()
        opcion3 = input("Opcion C: ").strip()
        opcion4 = input("Opcion D: ").strip()
        correcta = input("Letra de la respuesta correcta: ").strip().upper()

        test.append([
            pregunta, opcion1, opcion2,
            opcion3, opcion4, correcta
        ])

    with open("test.txt", "w") as archivo:
        archivo.write(nombre + "\n")
        archivo.write(str(preguntas) + "\n")

        for pregunta in test:
            for dato in pregunta:
                archivo.write(dato + "\n")

    print("\n¡Tu test se ha guardado correctamente!")


def responder_test():
    with open("test.txt", "w") as archivo:
        datos = archivo.readlines()

    nombre = datos[0].strip()
    preguntas = int(datos[1].strip())
    test = []

    for numero in range(preguntas):
        posicion = 2 + numero * 6

        test.append([
            datos[posicion].strip(),
            datos[posicion + 1].strip(),
            datos[posicion + 2].strip(),
            datos[posicion + 3].strip(),
            datos[posicion + 4].strip(),
            datos[posicion + 5].strip()
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

        if respuesta == test[numero][5]:
            correctas = correctas + 1

    calificacion = calcular_calificacion(preguntas, correctas)

    print("\nResultados de", participante)
    print("Respuestas correctas:", correctas, "de", preguntas)

    mostrar_resultado(calificacion)

    with open("resultados.txt", "w") as archivo:
        archivo.write(participante + " - " + str(round(calificacion, 2)) + "%\n")

    print("\nTu resultado se ha guardado correctamente.")


print("¿QUÉ TANTO ME CONOCES?")
print("\n1. Crear un test")
print("2. Responder un test")

opcion = input("\nSelecciona una opción: ")

if opcion == "1":
    crear_test()
elif opcion == "2":
    responder_test()
else:
    print("Opción no válida.")
