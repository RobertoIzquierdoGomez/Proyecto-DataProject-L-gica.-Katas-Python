#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados

"""Funcion para contar letras
Args: string de texto que introducira el usuario
Returns: imprime por pantalla las letras y el numero de veces que se repiten.
Se crea un diccionario vacío. Después se recorre la cadena de texto introducida por el usuario, se pasa a minúsculas y se comprueba si es un espacio en blanco. Si es un espacio en blanco se salta a la siguiente iteración. Si la letra ya está en el diccionario se le suma 1 al valor de la clave. Si no está en el diccionario se añade con valor 1. Por último se recorre el diccionario y se imprime por pantalla la letra y el número de veces que se repite.
"""
def contarLetras(cadena=input("Introduce una cadena de texto: ")):
    diccionarioLetras = {}
    for letra in cadena:
        letra = letra.lower()
        if letra == " ":
            continue
        if letra in diccionarioLetras:
            diccionarioLetras[letra] += 1
        else:
            diccionarioLetras[letra] = 1

    for letra in diccionarioLetras:
        print(f"La letra {letra} se repite {diccionarioLetras[letra]} veces")

contarLetras()

#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""Funcion para doblar los valores de una lista
Args: lista de números
Returns: lista con los valores doblados
Se usa la función map() para recorrer la lista de números y se multiplica por 2 cada valor. Se convierte el objeto map a lista y se imprime por pantalla.
"""
def doblarValores(listaNumeros):
    listaDoblada = list(map(lambda x: x * 2, listaNumeros))
    print(listaDoblada)
doblarValores(listaNumeros)

#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
listaPalabras = ["hola", "adios", "casa", "coche", "perro", "gato", "raton", "elefante", "caballo", "pajaro"]
palabraObjetivo = "coche"

"""Funcion para buscar palabras que contengan una palabra objetivo
Args: lista de palabras y letra objetivo
Returns: lista con las palabras que contienen la palabra objetivo
Se crea una lista vacía. Se recorre la lista de palabras y se comprueba si la palabra objetivo está en la lista. Si está se añade a la lista. Se imprime por pantalla la lista.
"""
def buscarPalabras(listaPalabras, palabraObjetivo):
    listaPalabrasObjetivo = []
    for palabra in listaPalabras:
        if palabraObjetivo in palabra:
            listaPalabrasObjetivo.append(palabra)
    print(listaPalabrasObjetivo)

buscarPalabras(listaPalabras, palabraObjetivo)

#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
"""Funcion para calcular la diferencia entre los valores de dos listas
Args: dos listas de números
Returns: lista con la diferencia entre los valores de las dos listas
Se usa la función map() para recorrer las dos listas y se resta el valor de la primera lista con el valor de la segunda lista. Se convierte el objeto map a lista y se imprime por pantalla.
"""
def diferenciaListas(lista1, lista2):
    diferencia = list(map(lambda x, y: x - y, lista1, lista2))
    print(diferencia)

lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 4, 3, 2, 1]
diferenciaListas(lista1, lista2)

#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.
listaNotas = [4, 5, 6, 7, 8, 9, 10]
notaAprobado = 5

"""Funcion para calcular la media de una lista de números y determinar si está aprobado o suspendido
Args: lista de números y nota de aprobado
Returns: lista con la media y el estado
Se calcula la media de la lista de números y se comprueba si es mayor o igual que la nota de aprobado. Se devuelve una lista con la media y el estado.
"""
def calcularMedia(listaNotas, notaAprobado=5):
    media = sum(listaNotas) / len(listaNotas)
    if media >= notaAprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    return media, estado

print(calcularMedia(listaNotas, notaAprobado))

#6. Escribe una función que calcule el factorial de un número de manera recursiva.
numero = 5

"""Funcion para calcular el factorial de un número de manera recursiva
Args: número
Returns: factorial del número
Se comprueba si el número es 0 o 1. Si es 0 se devuelve 1. Si es 1 se devuelve 1. Si no es 0 ni 1 se devuelve el número multiplicado por la función recursiva con el número - 1.
"""
def factorialRecursivo(numero):
    if numero == 0:
        return 1
    elif numero == 1:
        return 1
    else:
        return numero * factorialRecursivo(numero - 1)
    
print(factorialRecursivo(numero))