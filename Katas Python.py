
# Importamos reduce para los ejercicios que se necesitan.
from functools import reduce

#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados
cadena = "Hola me llamo Roberto y esto es una prueba hecha para el ejercicio de contar letras"


def contarLetras(cadena):
    """
    Funcion para contar letras
    Args: 
        string de texto que introducira el usuario
    Returns: 
        imprime por pantalla las letras y el numero de veces que se repiten.
    
    Se crea un diccionario vacío. Después se recorre la cadena de texto introducida por el usuario, se pasa a minúsculas y se comprueba si es un espacio en blanco. Si es un espacio en blanco se salta a la siguiente iteración. Si la letra ya está en el diccionario se le suma 1 al valor de la clave. Si no está en el diccionario se añade con valor 1. Por último se recorre el diccionario y se imprime por pantalla la letra y el número de veces que se repite.
    """
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

contarLetras(cadena)

#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def doblarValores(listaNumeros):
    """
    Funcion para doblar los valores de una lista

    Args:
        lista de números
    Returns:
        lista con los valores doblados

    Se usa la función map() para recorrer la lista de números y se multiplica por 2 cada valor. Se convierte el objeto map a lista y se imprime por pantalla.
    """
    listaDoblada = list(map(lambda x: x * 2, listaNumeros))
    print(listaDoblada)
doblarValores(listaNumeros)

#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
listaPalabras = ["hola", "adios", "casa", "coche", "perro", "gato", "raton", "elefante", "caballo", "pajaro"]
palabraObjetivo = "coche"

def buscarPalabras(listaPalabras, palabraObjetivo):
    """
    Funcion para buscar palabras que contengan una palabra objetivo

    Args:
        lista de palabras y letra objetivo
    Returns:
        lista con las palabras que contienen la palabra objetivo

    Se crea una lista vacía. Se recorre la lista de palabras y se comprueba si la palabra objetivo está en la lista. Si está se añade a la lista. Se imprime por pantalla la lista.
    """
    listaPalabrasObjetivo = []
    for palabra in listaPalabras:
        if palabraObjetivo in palabra:
            listaPalabrasObjetivo.append(palabra)
    print(listaPalabrasObjetivo)

buscarPalabras(listaPalabras, palabraObjetivo)

#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferenciaListas(lista1, lista2):
    """
    Funcion para calcular la diferencia entre los valores de dos listas

    Args:
        dos listas de números
    Returns:
        lista con la diferencia entre los valores de las dos listas
    
    Se usa la función map() para recorrer las dos listas y se resta el valor de la primera lista con el valor de la segunda lista. Se convierte el objeto map a lista y se imprime por pantalla.
    """
    diferencia = list(map(lambda x, y: x - y, lista1, lista2))
    print(diferencia)

lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 4, 3, 2, 1]
diferenciaListas(lista1, lista2)

#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.
listaNotas = [4, 5, 6, 7, 8, 9, 10]
notaAprobado = 5

def calcularMedia(listaNotas, notaAprobado=5):
    """
    Funcion para calcular la media de una lista de números y determinar si está aprobado o suspendido
    
    Args:
        lista de números y nota de aprobado
    Returns:
        lista con la media y el estado
    
    Se calcula la media de la lista de números y se comprueba si es mayor o igual que la nota de aprobado. Se devuelve una lista con la media y el estado.
    """
    media = sum(listaNotas) / len(listaNotas)
    if media >= notaAprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    return media, estado

print(calcularMedia(listaNotas, notaAprobado))

#6. Escribe una función que calcule el factorial de un número de manera recursiva.
numero = 5

def factorialRecursivo(numero):
    
    """
    Funcion para calcular el factorial de un número de manera recursiva

    Args:
        número
    Returns:
        factorial del número
        
    Se comprueba si el número es 0 o 1. Si es 0 se devuelve 1. Si es 1 se devuelve 1. Si no es 0 ni 1 se devuelve el número multiplicado por la función recursiva con el número - 1.
    """
    if numero == 0:
        return 1
    elif numero == 1:
        return 1
    else:
        return numero * factorialRecursivo(numero - 1)
    
print(factorialRecursivo(numero))

#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

listaTuplas = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

def convertirListaTuplas(listaTuplas):
    """
    Funcion para convertir una lista de tuplas a una lista de strings

    Args:
        lista de tuplas
    Returns:
        lista de strings

    Se usa la función map() para recorrer la lista de tuplas y se convierte cada tupla a un string. Se convierte el objeto map a lista y se imprime por pantalla.
    """
    listaStrings = list(map(lambda x: str(x), listaTuplas))
    print(listaStrings)

convertirListaTuplas(listaTuplas)

#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

def dividirNumeros():
    """
    Funcion para dividir dos números

    Args:
        dos números
    Returns:
        resultado de la división
    
    Se pide al usuario que introduzca dos números. Se comprueba si los números introducidos son numéricos. Si no son numéricos se imprime un mensaje de error. Si son numéricos se comprueba si el segundo número es 0. Si es 0 se imprime un mensaje de error. Si no es 0 se divide el primer número entre el segundo número y se imprime por pantalla.
    """
    try:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
    except ValueError:
        print("Debes introducir un número")
    else:
        try:
            resultado = numero1 / numero2
        except ZeroDivisionError:
            print("No se puede dividir por 0")
        else:
            print(f"El resultado de la división es {resultado}")

dividirNumeros()

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

listaMascotas = ["Perro", "Gato", "Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso", "Loro", "Pez", "Conejo"]

def excluirMascotasProhibidas(listaMascotas):
    """
    Funcion para excluir mascotas prohibidas en España
    
    Args:
        lista de nombres de mascotas
    Returns:
        lista de nombres de mascotas excluyendo las mascotas prohibidas
    
    Se crea una lista con las mascotas prohibidas. Se usa la función filter() para recorrer la lista de mascotas y se comprueba si la mascota no está en la lista de mascotas prohibidas. Se convierte el objeto filter a lista y se imprime por pantalla.
    """
    mascotasProhibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    listaMascotasFiltrada = list(filter(lambda x: x not in mascotasProhibidas, listaMascotas))
    print(listaMascotasFiltrada)

excluirMascotasProhibidas(listaMascotas)

#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def calcularPromedio(listaNumeros):
    """
    Funcion para calcular el promedio de una lista de números

    Args:
        lista de números
    Returns:
        promedio de los números

    Se comprueba si la lista de números está vacía. Si está vacía se lanza una excepción. Si no está vacía se calcula el promedio de los números y se imprime por pantalla.
    """
    if len(listaNumeros) == 0:
        print("La lista está vacía")
    else:
        promedio = sum(listaNumeros) / len(listaNumeros)
        print(promedio)

calcularPromedio(listaNumeros)

#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def comprobarEdad():
    """
    Funcion para comprobar la edad introducida por el usuario

    Args:
        edad introducida por el usuario
    Returns:
        mensaje de error si la edad no es válida

    Se pide al usuario que introduzca su edad. Se comprueba si la edad introducida es un número. Si no es un número se imprime un mensaje de error. Si es un número se comprueba si la edad está en el rango de 0 a 120. Si no está en ese rango se imprime un mensaje de error.
    """
    try:
        edad = int(input("Introduce tu edad: "))
    except ValueError:
        print("Debes introducir un número")
    else:
        if edad < 0 or edad > 120:
            print("La edad introducida no es válida")

comprobarEdad()

#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

frase = "Hola me llamo Roberto y esto es una prueba hecha para el ejercicio de la longitud de palabras"

def longitudPalabras(frase):
    """
    Funcion para calcular la longitud de cada palabra de una frase
    
    Args:
        frase
    Returns:
        lista con la longitud de cada palabra

    Se separa la frase en palabras. Se usa la función map() para recorrer la lista de palabras y se calcula la longitud de cada palabra. Se convierte el objeto map a lista y se imprime por pantalla.
    """
    palabras = frase.split()
    longitudes = list(map(len, palabras))
    print(longitudes)

longitudPalabras(frase)

#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()

caracteres = "Hola me llamo Roberto y esto es una prueba hecha para el ejercicio de las letras"

def letrasMayusculasMinusculas(caracteres):
    """
    Funcion para devolver una lista de tuplas con cada letra en mayúsculas y minúsculas
    
    Args:
        conjunto de caracteres
    Returns:
        lista de tuplas con cada letra en mayúsculas y minúsculas
    
    Se crea un conjunto con los caracteres de la cadena introducida por el usuario, eliminando espacios y duplicados. 

    Se usa la función map() para recorrer el conjunto y se convierte cada letra a una tupla con la letra en mayúsculas y minúsculas.

    Se convierte el objeto map a lista y se imprime por pantalla.
    """
    caracteres = set(caracteres.replace(" ", "").lower())
    listaTuplas = list(map(lambda x: (x.upper(), x), caracteres))
    print(listaTuplas)

letrasMayusculasMinusculas(caracteres)

#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

listaPalabras = ["hola", "adios", "casa", "coche", "perro", "gato", "raton", "elefante", "caballo", "pajaro"]
letra = "c"

def palabrasComienzanLetra(listaPalabras, letra):
    """
    Funcion para devolver las palabras de una lista que comiencen con una letra en específico
    
    Args:
        lista de palabras y letra
    Returns:
        lista de palabras que comienzan con la letra en específico
    
    Se usa la función filter() para recorrer la lista de palabras y se comprueba si la palabra comienza con la letra en específico.
    
    Se convierte el objeto filter a lista y se imprime por pantalla.
    """
    palabras = list(filter(lambda x: x[0] == letra, listaPalabras))
    print(palabras)

palabrasComienzanLetra(listaPalabras, letra)

#15. Crea una función lambda que sume 3 a cada número de una lista dada.

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
Funcion lambda para sumar 3 a cada número de una lista

Args:
    lista de números
Returns:
    lista con los números sumados 3

Se crea una función lambda que suma 3 a cada número de la lista. Se usa la función map() para recorrer la lista de números y se aplica la función lambda.

Se convierte el objeto map a lista y se imprime por pantalla.
"""

sumaTres = lambda x: x + 3
listaSumaTres = list(map(sumaTres, listaNumeros))
print(listaSumaTres)

#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

cadena = "Hola me llamo Roberto y esto es una prueba hecha para el ejercicio de la longitud de palabras"

def filtarPalabras(cadena, n):
    """
    Funcion que toma una cadena de texto y devuelve una lista de palabras de longitud n
    
    Args:
        cadena de texto
    Returns:
        lista con palabras de longitud n
        
    Se crea una función para transformar la cadena en lista. Después se crea nueva variabl con la lista fitlrada utilizando el método filter. Para útilizar el método filter creamos un lambda que recorre los iterables comparando la longitud de las palabras. Finalmente imprimimos la lista filtrada.
    """
    lista = list(cadena.split())
    listaFiltrada = list(filter(lambda x: len(x)>=n, lista))
    print(listaFiltrada)

filtarPalabras(cadena, 3)

#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función  reduce()

numeros = [5,7,2]

def concatenar_numeros(lista):
    """
    Función que toma una lista de dígitos para devolver el número "concatenado"

    Args:
        num1 (lista): una lista de enteros

    Returns:
        numero entero: devuelve un numero entero concatenado de los dígitos de la lista
    """
    resultado = reduce(lambda x,y: str(x) + str(y),lista)
    return resultado

print(concatenar_numeros(numeros))

#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función  filter()

estudiantes = [ #Creamos lista de diccionarios con los estudiantes
    {"nombre": "Roberto", "edad": 32, "calificacion": 95},
    {"nombre": "Francisco", "edad": 35, "calificacion": 20},
    {"nombre": "Debora", "edad": 20, "calificacion": 90},
    {"nombre": "Dario", "edad": 24, "calificacion": 80},
    {"nombre": "Ivan", "edad": 20, "calificacion": 91},
    {"nombre": "Nicolás", "edad": 26, "calificacion": 80}
]

def calificacion_mayor_90(estudiante):
    """
    Función para filtrar estudiantes con una calificación de más de 90.

    Args:
        estudiante (diccionario): diccionario de un estudiante que contiene su nombre, edad y calificacion.

    Returns:
        booleano: devuelve verdadero si la calficación del estudiante es mayor de 90 o falso de lo contrario.
    """ 
    return estudiante["calificacion"] > 90

# Filtramos los estudiantes y los almacenamos en una nueva lista
estudiantes_calificados = list(filter(calificacion_mayor_90,estudiantes))

# Imprimimos la lista de los estudiantes pero solo mostrando el nombre
print(f'Los estudiantes aprobados son {[e["nombre"] for e in estudiantes_calificados]}')

#19. Crea una función  lambda  que filtre los números impares de una lista dada.

lista_numeros = [1,2,3,4,5,6,7,8,9]

#Establecemos función lambda para filtrar los numeros impares de otra lista
impares = lambda lista: [numero for numero in lista if numero % 2 == 1]

print(impares(lista_numeros))

#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

lista_variada = [1,"2",3,"4",5]

def prueba(elemento):
    """
    Función para comprobar si un elemento es del tipo integer

    Args:
        elemento (integer o string): recogerá un elemento de un array

    Returns:
        boolean: devuelve verdadero si el elemento es un integer
    """
    elemento
    return type(elemento) == int

print(list(filter(prueba,lista_variada)))

#21. Crea una función que calcule el cubo de un número dado mediante una función lambda

cubo = lambda x: x**3
print(cubo(2))

#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().

lista = [1,2,3,4,5,6]

def producto_total(num1, num2):
    return num1 * num2

resultado = reduce(producto_total, lista)

print(resultado)