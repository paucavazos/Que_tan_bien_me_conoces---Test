
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
        print("Tenemos que convivir más.")


nombre = input("¿Como te llamas? ").strip().capitalize()

print("\nBienvenido al test de", nombre)
print("¡Vamos a descubrir que tanto te conocen!")

preguntas = int(input("\n¿Cuantas preguntas tendra el test? "))
test = []

for numero in range(preguntas):
    pregunta = input(
        "\nEscribe la pregunta " + str(numero + 1) + ": "
    ).strip()

    opcion1 = input("Opcion A: ").strip()
    opcion2 = input("Opcion B: ").strip()
    opcion3 = input("Opcion C: ").strip()
    opcion4 = input("Opcion D: ").strip()

    correcta = input("Letra de la respuesta correcta: ").strip().upper()

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

    respuesta = input("Tu respuesta: ").strip().upper()

    if respuesta == test[numero][5]:
        correctas = correctas + 1

calificacion = calcular_calificacion(preguntas, correctas)

print("\nResultados de", nombre)
print("Respuestas correctas:", str(correctas) + " de " + str(preguntas))

mostrar_resultado(calificacion)

