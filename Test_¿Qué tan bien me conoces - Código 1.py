preguntas = int(input("¿Cuántas preguntas tiene el test? "))
correctas = int(input("¿Cuántas respuestas correctas obtuviste? "))

calificacion = (correctas / preguntas) * 100

print("Tu calificación es:", calificacion, "%")

