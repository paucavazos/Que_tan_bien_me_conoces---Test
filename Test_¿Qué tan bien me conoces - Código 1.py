
def calcular_calificacion(preguntas, correctas):
    calificacion = (correctas / preguntas) * 100
    return calificacion


def mostrar_resultado(calificacion):
    print("Tu calificación es:", calificacion, "%")

    if calificacion >= 90:
        print("¡Me conoces muchísimo!")
    elif calificacion >= 70:
        print("¡Me conoces bien!")
    elif calificacion >= 50:
        print("Me conoces más o menos.")
    else:
        print("Tenemos que convivir mas.")


preguntas = int(input("¿Cuántas preguntas tiene el test? "))
test = []

for numero in range(preguntas):
    pregunta = input(
        "Escribe la pregunta " + str(numero + 1) + ": "
    )

    opcion1 = input("Opcion A: ")
    opcion2 = input("Opcion B: ")
    opcion3 = input("Opcion C: ")
    opcion4 = input("Opcion D: ")

    correcta = input("Escribe la letra de la respuesta correcta: ")

    test.append([
        pregunta,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        correcta
    ])

correctas = 0

for numero in range(preguntas):
    print("\n" + test[numero][0])
    print("A)", test[numero][1])
    print("B)", test[numero][2])
    print("C)", test[numero][3])
    print("D)", test[numero][4])

    respuesta = input("Tu respuesta: ").upper()

    if respuesta == test[numero][5].upper():
        correctas = correctas + 1

calificacion = calcular_calificacion(preguntas, correctas)
mostrar_resultado(calificacion)
