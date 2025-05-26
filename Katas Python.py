
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

sumaTres = lambda x: x + 3
"""
Funcion lambda para sumar 3 a cada número de una lista

Args:
    lista de números
Returns:
    lista con los números sumados

Se crea una función lambda que suma 3 a cada número de la lista. Se usa la función map() para recorrer la lista de números y se aplica la función lambda.
Se convierte el objeto map a lista y se imprime por pantalla.
"""

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
        una lista de enteros

    Returns:
        devuelve un numero entero concatenado de los dígitos de la lista
    
    Crea una función que recibe una lista de números enteros. La lista recorre cada elemento y lo transforma a string concatenandolo con el siguiente número tras transformarlo en string. 
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
        diccionario de un estudiante que contiene su nombre, edad y calificacion.

    Returns:
        devuelve verdadero si la calficación del estudiante es mayor de 90 o falso de lo contrario.

    Crea una función que recibe una lista de diccionarios y comprueba si su calificación es mayor que 90 y devolviendo un valor booleano.    
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
        recogerá un elemento de un array

    Returns:
        devuelve verdadero si el elemento es un integer

    Función que recibe un parámetro y comprueba si es del tipo integer y devuelve un valor booleano.
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
    """
    Función para multiplicar dos números dados por el usuario.

    Args:
        primer numero de la función
        segundo numero de la función

    Returns:
        Devuelve la multiplicación entre ambos números

    Función que recibe como parámetro dos números y los multiplica entre ellos.
    """
    return num1 * num2

producto_total_lista = reduce(producto_total, lista)
print(producto_total_lista)

#23. Concatena una lista de palabras. Usa la función reduce().

lista_palabras = ["super", "cali", "fragi","listi","co","espia","lidoso"]

def concatenar_palabras(palabra1, palabra2):
    """
    Función para concatenar dos palabras

    Args:
        palabra1 (string): una palabra
        palabra2 (string): palabra de 

    Returns:
        devuelve la concatenación de dos palabras.
    
    Función que recibe dos palabras y las concatena entre ellas.
    """
    return palabra1 + palabra2

palabra_concatenada = reduce(concatenar_palabras, lista_palabras)
print(palabra_concatenada)

#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

lista_numeros = [20,8,6,4]

def resta_lista(lista):
    """
    Función para calcular la diferencia total en los valores de una lista.

    Args:
        Lista de números

    Returns:
        Imprime el resultado de restar todos los números de la lista

    Función que recoge una lista y va restando cada elemento. Devuelve el resultado de restar todos los números.
    """
    resultado = reduce(lambda x,y: x-y, lista)
    return print(resultado)

resta_lista(lista_numeros)

#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

cadena = "Hola me llamo Roberto y esto es una prueba hecha para el ejercicio de contar caracteres"

def longitud_texto(text):
    """
    Función que devuelve el número de caracteres de una cadena de texto

    Args:
        cadena de texto

    Returns:
        devuelve la longitud de la cadena de texto
    
    Funcion que toma como dato una cadena de texto y devuelve su longitud.
    """
    return len(text)

print(longitud_texto(cadena))

#26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda x,y: x%y

#27. Crea una función que calcule el promedio de una lista de números.

lista_numeros = [9,8,9,7,9,5]

def promedio_numeros(lista):
    """
    Función para calcular el promedio de una lista de numeros

    Args:
        lista de números

    Returns:
        devuelve la media de una lista de números

    Se almacena en una variable la suma de todos los números de la lista.
    Se utiliza la función reduce() junto con una función lambda para recorrer la lista recibida en el parametro y calcular su suma.
    Devolvemos la media realizando la división de la variable suma y la longitud de la lista.
    """
    suma = reduce(lambda x,y: x + y, lista)
    return suma / len(lista)

promedio_numeros(lista_numeros)

#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

lista_numeros = [1,2,3,4,4,5,6,6,7]

def devuelve_primer_duplicado(lista):
    """
    Funcion para encontrar primer duplicado de una lista

    Args:
        lista de un conjunto de datos

    Returns:
        devuelve el primer duplicado de la lista

    Establecemeos un conjunto de datos vacío.
    Establecemos un for que recorre los elementos de la lista proporcionada.
    Comprueba si el elemento de la lista está en el conjunto de datos. 
    En caso de que sí, devuelve el valor. En caso contrario, lo almacena en el conjunto y sigue iterando en el for.
    """
    set_numeros = set()
    for elemento in lista:
        if elemento in set_numeros:
            return print(elemento)
        else:
            set_numeros.add(elemento)

devuelve_primer_duplicado(lista_numeros)

#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el carácter '#', excepto los últimos cuatro.

variable = 47032604

def transformar_variable(var):
    """
    Esta función recibe una variable (entero, texto, etc.), la convierte en una cadena de texto y enmascara todos sus caracteres con el símbolo '#' excepto los últimos cuatro.

    Args:
        La variable a enmascarar. Se convertirá a string automáticamente.

    Returns:
        Una nueva cadena con todos los caracteres enmascarados con '#' excepto los últimos cuatro.
    
    Tranformamos la variable a texto y establecemos una nueva varieble de texto vacía
    Recorremos todos los caracteres del texto.
    Utilizamos un condicional para comprobar sino son los ultimos 4 carácteres. En tal caso, agregamos '#' a la nueva cadena.
    Si son los últimos 4 caracteres agregamos el carácter original a la nueva cadena de texto.
    """
    texto = str(var)
    nueva_cadena = ""

    for i in range(len(texto)):
        if i < len(texto) - 4:
            nueva_cadena += "#"
        else:
            nueva_cadena += texto[i]

    return nueva_cadena

print(transformar_variable(variable))

#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

palabra1 = "perro"
palabra2 = "roper"

def es_anagrama(pal1, pal2):
    """
    Esta función recibe dos palabras (cadenas de texto) y determina si son anagramas, es decir, si están formadas por las mismas letras con la misma cantidad, aunque estén en distinto orden.

    Args:
        pal1: Primera palabra a comparar.
        pal2: Segunda palabra a comparar.

    Returns:
        True si ambas palabras son anagramas (mismas letras y cantidades), False en caso contrario.
    
    Comprobamos si las palabras tienen distinta longitud. Si es así, no pueden ser anagramas.
    Creamos dos conjuntos con las letras únicas de cada palabra.
    Inicializamos dos diccionarios para contar cuántas veces aparece cada letra en cada palabra.
    Recorremos cada palabra y aumentamos el contador correspondiente para cada letra.
    Finalmente, comparamos ambos diccionarios. Si son iguales, las palabras son anagramas.
    """
    if len(pal1) != len(pal2):
        return False
    set_palabras1 = set(pal1)
    set_palabras2 = set(pal2)
    diccionario1 = dict()
    diccionario2 = dict()

    for a in set_palabras1:
        diccionario1[a] = 0
    for a in set_palabras2:
        diccionario2[a] = 0
    
    for a in pal1:
        diccionario1[a] += 1
    for a in pal2:
        diccionario2[a] += 1
    return diccionario1 == diccionario2

es_anagrama(palabra1, palabra2)

#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

tamaño_lista = int(input("Indica cuántos nombres vas a añadir"))

def encontrar_nombre(size):
    """
    Esta función solicita al usuario una cantidad determinada de nombres, los guarda en una lista y luego le pide ingresar un nombre para buscar. Si el nombre está en la lista, imprime un mensaje; si no está, lanza una excepción indicando que no fue encontrado.

    Args:
        size: Un número entero que indica cuántos nombres se van a ingresar.

    Returns:
        No retorna un valor directamente. Imprime un mensaje si encuentra el nombre
        o lanza una excepción si no lo encuentra.

    Se define una lista vacía para almacenar los nombres.
    Se recorre un bucle que pide al usuario que ingrese un nombre en cada iteración.
    Luego, se solicita un nombre adicional para buscarlo dentro de la lista.
    Si el nombre se encuentra, se imprime un mensaje indicando éxito.
    Si el nombre no está en la lista, se lanza una excepción con un mensaje de error.
    """
    lista = list()
    for i in range(size):
        lista.append(input(f"Ingresa el nombre #{i+1}: "))
    nombre = input("Ingresa un nombre a buscar")
    if nombre in lista:
        print("Nombre encontrado")
    else:
        raise Exception("Nombre no encontrado")

encontrar_nombre(tamaño_lista)

#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

lista_empleados = {
    "Javier Perez": "Analista",
    "Roberto Izquierdo": "Gerente",
    "Antonio Garcia": "Analista",
    "Laura Fernández": "Contadora",
    "Maria Lopez": "Recursos Humanos",
    "Luis Ortega": "Desarrollador",
    "Paula Martinez": "Diseñadora",
    "Fernando Ruiz": "Soporte Técnico",
    "Natalia Gomez": "Marketing",
    "Sergio Ramirez": "Gerente de Proyecto",
    "Isabel Castro": "Administrativa",
    "Andres Molina": "Auditor",
    "Patricia Romero": "Analista de Datos",
    "Carlos Vazquez": "Ventas",
    "Elena Sanchez": "Product Manager"
}

def encontrar_puesto(lista):
    """
    Esta función solicita al usuario ingresar el nombre completo de un empleado, busca ese nombre dentro de un diccionario de empleados y devuelve su puesto si se encuentra. Si el nombre no está en el diccionario, se muestra un mensaje indicando que la persona no trabaja en la empresa.

    Args:
        lista: Un diccionario donde las claves son nombres completos de empleados y los valores son los puestos que ocupan.

    Returns:
        No retorna un valor directamente. Imprime el puesto si el empleado existe, o un mensaje de que no trabaja en la empresa si no se encuentra.

    Se solicita al usuario que introduzca el nombre del empleado a buscar.
    El nombre ingresado se normaliza con el método .title() para igualar el formato del diccionario.
    Se verifica si el nombre existe como clave en el diccionario proporcionado.
    Si el nombre está, se imprime el puesto correspondiente.
    Si no está, se imprime un mensaje indicando que la persona no trabaja aquí.
    """
    nombre_buscado = input("Introduce el nombre del empleado a buscar: ").title()
    if nombre_buscado in lista:
        print(f'El puesto de {nombre_buscado} es {lista[nombre_buscado]}')
    else:
        print("La persona no trabaja aquí")

encontrar_puesto(lista_empleados)

#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

lista1 = [1,2,3,4]
lista2 = [4,3,2,1]

nueva_lista = lambda list1, list2: [elemento1 + elemento2 for elemento1, elemento2 in zip(list1, list2)]
"""
Esta función recibe dos listas de números y devuelve una nueva lista donde cada elemento es la suma de los elementos correspondientes en las dos listas originales.

Args:
    list1: Primera lista de números.
    list2: Segunda lista de números.

Returns:
    Una lista con la suma de los elementos emparejados de list1 y list2.

Se utiliza la función zip() para recorrer ambas listas a la vez, elemento por elemento.
Por cada par de elementos (uno de cada lista), se suman y se agregan a la nueva lista.
El resultado final es una lista con las sumas posición por posición.
"""

print(nueva_lista(lista1, lista2))

#34. Crea la clase  Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco ,  nueva_rama ,  crecer_ramas ,  quitar_rama  e  info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.<br>
#Código a seguir:
#- Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#- Implementar el método  crecer_tronco  para aumentar la longitud del tronco en una unidad.
#- Implementar el método  nueva_rama  para agregar una nueva rama de longitud 1 a la lista de ramas.
#- Implementar el método  crecer_ramas  para aumentar en una unidad la longitud de todas las ramas existentes.
#- Implementar el método  quitar_rama  para eliminar una rama en una posición específica.
#- Implementar el método info_arbol  para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
#Caso de uso:
#- Crear un árbol.
#- Hacer crecer el tronco del árbol una unidad.
#- Añadir una nueva rama al árbol.
#- Hacer crecer todas las ramas del árbol una unidad.
#- Retirar la rama situada en la posición 2.
#- Obtener información sobre el árbol.

class Arbol:
    """
    Esta clase representa un árbol con un tronco y una serie de ramas.
    Permite manipular la estructura del árbol mediante distintos métodos como hacer crecer el tronco, añadir nuevas ramas, hacer crecer las ramas, eliminar ramas y mostrar información del estado actual del árbol.

    Atributos:
        tronco (int): Longitud del tronco del árbol. Se inicializa en 1.
        rama (list): Lista que contiene la longitud de cada rama del árbol. Se inicializa como lista vacía.
    """

    def __init__(self):
        """
        Inicializa un objeto de tipo Arbol con un tronco de longitud 1 y una lista vacía de ramas.
        """
        self.tronco = 1
        self.rama = []

    def crecer_tronco(self):
        """
        Incrementa la longitud del tronco en una unidad.
        """
        self.tronco += 1

    def nueva_rama(self):
        """
        Agrega una nueva rama al árbol con una longitud inicial de 1.
        """
        self.rama.append(1)
    
    def crecer_ramas(self):
        """
        Aumenta en una unidad la longitud de todas las ramas existentes.
        """
        for i in range(len(self.rama)):
            self.rama[i] += 1
    
    def quitar_rama(self, posicion):
        """
        Elimina una rama del árbol en la posición indicada.

        Args:
            posicion (int): Índice de la rama a eliminar (comienza desde 0).
        """
        self.rama.pop(posicion)
    
    def info_arbol(self):
        """
        Imprime por pantalla información detallada del árbol:
        - Longitud del tronco
        - Número de ramas
        - Longitud de cada rama
        """
        print(f"La longitud del tronco es de: {self.tronco}")
        print(f"El número de ramas es de: {len(self.rama)}")
        for indice, elemento in enumerate(self.rama):
            print(f"La rama numero {indice + 1} es de longitud: {elemento}")

# Caso de uso
arbol = Arbol()              # Se crea un árbol
arbol.crecer_tronco()        # Se hace crecer el tronco una unidad
arbol.nueva_rama()           # Se añade una nueva rama
arbol.nueva_rama()           # Se añade otra rama
arbol.nueva_rama()           # Se añade una tercera rama
arbol.crecer_ramas()         # Todas las ramas crecen una unidad
arbol.info_arbol()           # Se muestra la información actual del árbol
arbol.quitar_rama(2)         # Se elimina la tercera rama (índice 2)
arbol.info_arbol()           # Se muestra nuevamente la información del árbol

#36. Crea la clase `UsuarioBanco`,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.<br>
# Código a seguir:
#    - Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante `True` y `False`.
#    - Implementar el método  `retirar_dinero`  para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
#    - Implementar el método `transferir_dinero` para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
#    - Implementar el método `agregar_dinero` para agregar dinero al saldo del usuario.<br><br>
# Caso de uso:
#    - Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#    - Agregar 20 unidades de saldo de "Bob".
#    - Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
#    - Retirar 50 unidades de saldo a "Alicia"

class UsuarioBanco:
    """
    Esta clase representa a un usuario de un banco, con su nombre, saldo y si tiene o no una cuenta corriente. Permite realizar operaciones como retirar dinero, transferir dinero a otro usuario y agregar dinero al saldo.

    Atributos:
        nombre (str): Nombre del usuario.
        saldo (float/int): Saldo actual en la cuenta del usuario.
        cuenta_corriente (bool): Indica si el usuario tiene cuenta corriente (True o False).
    """

    def __init__(self, nombre, saldo, cuentaCorriente):
        """
        Inicializa una nueva instancia de UsuarioBanco con nombre, saldo y estado de cuenta corriente.

        Args:
            nombre (str): El nombre del usuario.
            saldo (float/int): El saldo inicial del usuario.
            cuentaCorriente (bool): Si tiene cuenta corriente (True o False).
        """
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuentaCorriente

    def retirar_dinero(self, cantidad):
        """
        Retira una cantidad del saldo del usuario si tiene suficiente dinero.

        Args:
            cantidad (float/int): Monto a retirar.

        Comprobamos si el saldo actual es suficiente. Si lo es, se descuenta del saldo.
        Si no, se muestra un mensaje de error indicando saldo insuficiente.
        """
        if self.saldo - cantidad < 0:
            print("ERROR: saldo insuficiente")
        else:
            self.saldo -= cantidad

    def transferir_dinero(self, usuarioDestino, cantidad):
        """
        Transfiere una cantidad de dinero desde este usuario hacia otro.

        Args:
            usuarioDestino (UsuarioBanco): La instancia de usuario que recibirá el dinero.
            cantidad (float/int): Monto a transferir.

        Se verifica si el saldo actual es suficiente. Si lo es, se descuenta del saldo
        del usuario actual y se suma al saldo del usuario destino.
        Si no hay saldo suficiente, se muestra un mensaje de error.
        """
        if cantidad > self.saldo:
            print("ERROR: saldo insuficiente")
        else:
            self.saldo -= cantidad
            usuarioDestino.saldo += cantidad

    def agregar_dinero(self, cantidad):
        """
        Agrega una cantidad de dinero al saldo del usuario.

        Args:
            cantidad (float/int): Monto a agregar.

        Se suma el valor al saldo actual del usuario.
        """
        self.saldo += cantidad


# Caso de uso
alicia = UsuarioBanco("Alicia", 100, True)   # Se crea el usuario Alicia con saldo 100
bob = UsuarioBanco("Bob", 50, True)          # Se crea el usuario Bob con saldo 50

bob.agregar_dinero(20)                       # Bob recibe 20 → saldo ahora 70
bob.transferir_dinero(alicia, 80)            # Da "error" indicando que no hay saldo suficiente.
alicia.retirar_dinero(50)                    # Alicia retira 50 → nuevo saldo: 130


#37. Crea una función llamada `procesar_texto` que procesa un texto según la opción especificada: `contar_palabras`, `reemplazar_palabras`, `eliminar_palabra`. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función  procesar_texto .<br>
#    Código a seguir:
#    - Crear una función `contar_palabras` para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
#    - Crear una función `reemplazar_palabras` para remplazar una `palabra_original` del texto por una `palabra_nueva`. Tiene que devolver el texto con el remplazo de palabras.
#    - Crear una función `eliminar_palabra` para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
#    - Crear la función `procesar_texto` que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.<br><br>
#    Caso de uso:
#    - Comprueba el funcionamiento completo de la función `procesar_texto`.


texto = "El perro ladra y el gato maulla, pero el perro no deja de ladrar."

def contar_palabras(text):
    """
    Esta función recibe un texto en forma de cadena y devuelve un diccionario que contiene cada palabra del texto como clave y la cantidad de veces que aparece como valor.

    Args:
        text (str): Texto a analizar. Puede contener mayúsculas y palabras repetidas.

    Returns:
        dict: Un diccionario donde las claves son las palabras en minúsculas y los valores son las veces que cada palabra aparece en el texto.

    El texto se convierte todo a minúsculas para unificar la comparación de palabras.
    Luego se divide en palabras usando el espacio como separador.
    Se recorre la lista de palabras, y por cada palabra se incrementa su conteo en el diccionario. Si la palabra no existía previamente, se añade con valor 1.
    """
    texto = text.replace(",", "").replace(".", "")  # Eliminamos puntuación básica
    palabras = texto.lower().split()
    resultado = dict()
    for palabra in palabras:
        if palabra in resultado:
            resultado[palabra] += 1
        else:
            resultado[palabra] = 1

    return resultado


def reemplazar_palabras(text, palabraVieja, palabraNueva):
    """
    Esta función reemplaza todas las apariciones de una palabra específica en un texto por otra palabra nueva, y devuelve el texto modificado.

    Args:
        text (str): El texto original donde se realizará el reemplazo.
        palabraVieja (str): La palabra que se desea reemplazar.
        palabraNueva (str): La palabra que se desea usar como reemplazo.

    Returns:
        str: El texto resultante después de realizar el reemplazo de palabras.

    Se utiliza el método .replace() para sustituir todas las ocurrencias de 'palabraVieja' por 'palabraNueva' en el texto original.
    """
    nuevo_texto = text.replace(palabraVieja, palabraNueva)
    return nuevo_texto


def eliminar_palabra(text, palabra):
    """
    Esta función elimina todas las apariciones de una palabra específica en un texto y devuelve el texto modificado sin esa palabra.

    Args:
        text (str): El texto original del cual se desea eliminar una palabra.
        palabra (str): La palabra que se desea eliminar del texto.

    Returns:
        str: El texto resultante después de eliminar todas las apariciones de la palabra.

    Se utiliza el método .replace() para reemplazar todas las ocurrencias de la palabra por una cadena vacía, eliminándola del texto.
    """
    nuevo_texto = text.replace(palabra, "")
    return nuevo_texto



def procesar_texto(text, opcion, *args):
    """
    Esta función recibe un texto, una opción de procesamiento y un número variable de argumentos según la operación elegida. Dependiendo de la opción, llama a una función específica para contar palabras, reemplazar una palabra o eliminar una palabra del texto.

    Args:
        text (str): El texto original a procesar.
        opcion (str): Puede ser "contar", "reemplazar" o "eliminar".
        *args: Argumentos adicionales según la opción:
            - Para "contar": no se requieren argumentos adicionales.
            - Para "reemplazar": args[0] es la palabra a reemplazar, args[1] es la palabra nueva.
            - Para "eliminar": args[0] es la palabra a eliminar.

    Returns:
        None. Imprime directamente el resultado por pantalla.

    Se evalúa el valor de 'opcion'. Según el caso, se llama a la función correspondiente.
    El resultado de la operación se muestra usando print().
    """
    if opcion.lower() == "contar":
        print(contar_palabras(text))
    elif opcion.lower() == "reemplazar":
        print(reemplazar_palabras(text, args[0], args[1]))
    else:
        print(eliminar_palabra(text, args[0]))

# Caso de uso
procesar_texto(texto, "contar") # {'el': 3, 'perro': 2, 'ladra': 1, 'y': 1, 'gato': 1, 'maulla,': 1, 'pero': 1, 'no': 1, 'deja': 1, 'de': 1, 'ladrar.': 1}
procesar_texto(texto, "reemplazar", "perro", "mono") # El mono ladra y el gato maulla, pero el mono no deja de ladrar.
procesar_texto(texto, "eliminar", "perro") # El  ladra y el gato maulla, pero el  no deja de ladrar.

#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def momento_del_dia(hora):
    """
    Esta función recibe una hora del día (en formato entero o cadena convertible a entero)
    y devuelve una cadena que indica el momento del día correspondiente: "noche", "día" o "tarde".

    Args:
        hora (int o str): La hora del día, expresada en formato de 24 horas (0 a 23).

    Returns:
        str: Una cadena indicando el momento del día:
            - "noche" si la hora está entre las 0 y 5 o entre las 21 y 23
            - "día" si la hora está entre las 6 y 11
            - "tarde" si la hora está entre las 12 y 20

    La hora se convierte primero a entero usando int(hora) para asegurar compatibilidad con entradas tipo string. Luego se evalúa en qué rango de horas cae para determinar y devolver el momento del día correspondiente.
    """
    if (0 <= int(hora) < 6) or (21 <= int(hora) <= 23):
        return "noche"
    elif 6 <= int(hora) < 12:
        return "día"
    else:
        return "tarde"

print(momento_del_dia(input("Ingresa una hora")))

#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:
#    - 0-69: insuficiente
#    - 70-79: bien
#    - 80-89: muy bien
#    - 90-100: excelente

def calificacion(puntuacion):
    """
    Esta función recibe una puntuación numérica y muestra por pantalla una calificación cualitativa según el rango en el que se encuentre.

    Args:
        puntuacion (int o float): Valor numérico que representa la puntuación obtenida.

    Returns:
        None. La función imprime directamente una calificación textual según la puntuación:
            - "Insuficiente" si la puntuación está entre 0 y 69 (inclusive)
            - "Bien" si está entre 70 y 79 (inclusive)
            - "Muy bien" si está entre 80 y 89 (inclusive)
            - "Excelente" si es 90 o superior

    La función evalúa la puntuación mediante condicionales encadenadas (if-elif-else) y determina la calificación correspondiente a cada rango. El resultado se muestra usando la función print().
    """
    if puntuacion >= 0 and puntuacion <= 69:
        print("Insuficiente")
    elif puntuacion >= 70 and puntuacion <= 79:
        print("Bien")
    elif puntuacion >= 80 and puntuacion <= 89:
        print("Muy bien")
    else:
        print("Excelente")

#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

#Rectangulo Area=base×altura
#Circulo Area=π×r
#Triangulo (base x altura)/2

parametros = (2,3)

def calcular_area(figura, datos):
    """
    Esta función calcula y muestra por pantalla el área de una figura geométrica
    según el tipo de figura indicado y los datos proporcionados.

    Args:
        figura (str): El nombre de la figura. Puede ser "rectangulo", "circulo" o cualquier otro valor, que será interpretado como "triángulo".
        datos (tuple): Una tupla de valores numéricos necesarios para calcular el área:
            - Para "rectangulo": se esperan dos valores (base y altura).
            - Para "circulo": se espera un valor (radio).
            - Para "triángulo": se esperan dos valores (base y altura).

    Returns:
        None. La función imprime directamente el resultado del área correspondiente.

    La función convierte el nombre de la figura a minúsculas para facilitar la comparación.
    Luego evalúa el tipo de figura mediante condicionales:
        - Si es "rectangulo", calcula base * altura.
        - Si es "circulo", calcula π * radio², utilizando 3.14 como valor de π.
        - En cualquier otro caso, se calcula como triángulo: (base * altura) / 2.
    """
    if figura.lower() == "rectangulo":
        print(f"El área del rectángulo es {datos[0] * datos[1]}")
    elif figura.lower() == "circulo":
        print(f"El área del círculo es {3.14 * (datos[0]**2)}")
    else:
        print(f"El área del triángulo es {(datos[0] * datos[1]) / 2}")

calcular_area("triangulo", parametros)

#41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:<br><br>
#    - Solicita al usuario que ingrese el precio original de un artículo.
#    - Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#    - Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#    - Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€. 
#    - Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
#    - Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

"""
Este programa solicita al usuario el precio de un artículo y pregunta si dispone de un cupón de descuento. Si el usuario tiene un cupón, se le pide que introduzca el valor del descuento. El programa valida que el descuento sea mayor que cero y no superior al precio del artículo. Luego muestra el precio final con el descuento aplicado.

Entradas:
    - El precio original del artículo (como número entero).
    - Una respuesta de sí/no indicando si el usuario tiene un cupón de descuento.
    - En caso afirmativo, el valor del cupón de descuento (como número entero).

Lógica:
    - Si el usuario tiene un cupón, se verifica que el valor sea mayor que cero y no mayor que el precio del artículo.
    - Si el descuento es válido, se aplica restando al precio original.
    - Si no hay descuento o es inválido, se muestra el precio completo o un mensaje de error.

Salidas:
    - Se imprime por pantalla el precio final del artículo, con o sin descuento aplicado.
    - Si el descuento no es válido, se imprime un mensaje de error.
"""

precioArticulo = int(input("Ingresa el precio del artículo: "))

if input("¿Tienes un cupón de descuento? Responde con sí o no").lower() == "si":
    descuento = int(input("Ingresa el valor del cupón de descuento: "))
    if descuento <= precioArticulo and descuento > 0:
        print(f"El precio total a pagar es de {precioArticulo - descuento}")
    else:
        print("ERROR descuento no válido")
else:
    print(f"El precio a pagar es {precioArticulo} al no tener descuento")