def calcular_calificacion(preguntas, correctas):
    calificacion = (correctas / preguntas) * 100
    return calificacion


def mostrar_resultado(calificacion):
    print("Tu calificación es:", calificacion, "%")

    if calificacion >= 90:
        print("¡Me conoces muchísimo!")
    elif calificacion >= 70:
        print("¡Me conoces bastante!")
    elif calificacion >= 50:
        print("Me conoces más o menos.")
    else:
        print("Tenemos que convivir más. 😭")


preguntas = int(input("¿Cuántas preguntas tiene el test? "))
correctas = int(input("¿Cuántas respuestas correctas obtuviste? "))

calificacion = calcular_calificacion(preguntas, correctas)

mostrar_resultado(calificacion)
