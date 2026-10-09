
def calcular_calificacion(preguntas, correctas):
    calificacion = (correctas / preguntas) * 100
    return calificacion


def mostrar_resultado(calificacion):
    print("Tu calificacion es:", calificacion, "%")

    if calificacion >= 90:
        print("¡Me conoces muchisimo!")
    elif calificacion >= 70:
        print("¡Me conoces bastante!")
    elif calificacion >= 50:
        print("Me conoces mas o menos.")
    else:
        print("Tenemos que convivir mas.")


preguntas = int(input("¿Cuantas preguntas tiene el test? "))
correctas = 0

for numero in range(preguntas):
    respuesta = input("Escribe la respuesta correcta de la pregunta " + str(numero + 1) + ": ")

    respuesta_correcta = input("¿Cual era la respuesta correcta? ")

    if respuesta.lower() == respuesta_correcta.lower():
        correctas = correctas + 1

calificacion = calcular_calificacion(preguntas, correctas)
mostrar_resultado(calificacion)
correctas = int(input("¿Cuántas respuestas correctas obtuviste? "))

calificacion = calcular_calificacion(preguntas, correctas)

mostrar_resultado(calificacion)
