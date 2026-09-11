def calcular_calificacion(preguntas, correctas):
    calificacion = (correctas / preguntas) * 100
    return calificacion


def mostrar_resultado(calificacion):
    print("Tu calificación es:", calificacion, "%")


preguntas = int(input("¿Cuántas preguntas tiene el test? "))
correctas = int(input("¿Cuántas respuestas correctas obtuviste? "))

calificacion = calcular_calificacion(preguntas, correctas)

mostrar_resultado(calificacion)
