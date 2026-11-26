# Contexto

Este proyecto consiste en crear un test de preguntas para evaluar qué tanto conocen al usuario sus familiares, amigos y conocidos. El usuario podrá diseñar su propio test con preguntas sobre sí mismo, incluyendo temas como sus gustos, preferencias, personalidad y experiencias. Posteriormente, otras personas podrán responderlo y, al finalizar, el programa mostrará una calificación basada en la cantidad de respuestas correctas.

Cuando una persona termine de responder, el programa comparará sus respuestas con las respuestas correctas previamente establecidas por el usuario y calculará su calificación. De esta manera, cada persona podrá descubrir qué tanto conoce a quien creó el test.

### Ejecución e importación de módulos

El programa será desarrollado en Python y se ejecutará mediante su intérprete, por lo que no requiere un proceso de compilación manual. Para ejecutarlo, será necesario **abrir** el **archivo principal desde un entorno de programación o** utilizar la **terminal** con el comando `Código proyecto.py`.

Se utilizará el módulo `os`, incorporado en Python mediante la instrucción `import os`. Este módulo permitirá comprobar si existe el archivo `test.txt` antes de intentar leerlo, evitando errores cuando todavía no se ha creado un test. Además, el programa utilizará archivos de texto para almacenar las preguntas y los resultados, los cuales se abrirán y cerrarán mediante las funciones correspondientes de Python.

Considero que este proyecto es interesante porque puede utilizarse como una actividad divertida entre amigos y familiares, además de ayudar a fortalecer las relaciones interpersonales al conocer mejor los gustos y la personalidad de otras personas. Incluso, podría tener una utilidad en el ámbito laboral, ya que conocer mejor a los compañeros de trabajo puede favorecer la comunicación, la convivencia y la colaboración dentro de un equipo. Esto permitiría crear un ambiente de trabajo más agradable y facilitar la manera en que las personas se relacionan y trabajan juntas. Finalmente, considero que es un proyecto adecuado para poner en práctica mis conocimientos adquiridos de programación y desarrollar una herramienta interactiva que pueda tener diferentes aplicaciones.

# Algoritmo
1. Iniciar el programa.
2. Mostrar al usuario las opciones disponibles: crear un nuevo test o responder un test existente.
3. Si el usuario selecciona crear un nuevo test:
   1. Solicitar al usuario que ingrese su nombre.
   2. Pedir que escriba una pregunta sobre sí mismo, por ejemplo, cuál es su comida favorita.
   3. Solicitar cuatro opciones de respuesta para la pregunta.
   4. Pedir al usuario que indique cuál de las cuatro opciones es la respuesta correcta.
   5. Repetir los pasos anteriores para agregar las demás preguntas del test, incluyendo temas como gustos, preferencias, pasatiempos, películas, música o experiencias personales.
   6. Guardar las preguntas, sus cuatro opciones y las respuestas correctas.
   7. Generar un código o enlace único para identificar el test.
   8. Mostrar el enlace generado para que el usuario pueda compartirlo con sus amigos, familiares o conocidos.

4. Si el usuario selecciona responder un test existente:
   1. Solicitar el código o enlace del test que desea contestar.
   2. Buscar y recuperar las preguntas, opciones y respuestas correctas correspondientes al test.
   3. Solicitar el nombre de la persona que responderá el test.
   4. Mostrar una por una las preguntas creadas por el usuario junto con sus cuatro opciones de respuesta.
   5. Registrar la opción seleccionada por la persona que está contestando.
   6. Comparar cada respuesta seleccionada con la respuesta correcta previamente guardada.
   7. Contar el número total de respuestas correctas.
   8. Calcular la calificación del test utilizando el número de respuestas correctas y el número total de preguntas.
   9. Mostrar la calificación obtenida y un mensaje que indique qué tanto conoce la persona al creador del test.
   10. Guardar el nombre de la persona que respondió y su calificación.

5. Permitir que el creador del test consulte los resultados obtenidos por las personas que lo han contestado.
6. Mostrar los nombres de los participantes y sus respectivas calificaciones.
7. Finalizar el programa.
