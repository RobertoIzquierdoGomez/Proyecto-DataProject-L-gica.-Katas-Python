# Proyecto: DataProject: Lógica. Katas Python

Realizamos la descargar del fichero pdf con los enunciados y generamos archivo "Katas Python.py" en el que se va a realizar la resolución de los ejercicios.

En este README vamos a proceder a pegar también el enunciado y el código de los ejercicios.

## Enunciados y código

1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados
```python
cadena = "Hola me llamo Roberto y esto es una prueba hecha para el ejercicio de contar letras"

"""Funcion para contar letras
Args: string de texto que introducira el usuario
Returns: imprime por pantalla las letras y el numero de veces que se repiten.
Se crea un diccionario vacío. Después se recorre la cadena de texto introducida por el usuario, se pasa a minúsculas y se comprueba si es un espacio en blanco. Si es un espacio en blanco se salta a la siguiente iteración. Si la letra ya está en el diccionario se le suma 1 al valor de la clave. Si no está en el diccionario se añade con valor 1. Por último se recorre el diccionario y se imprime por pantalla la letra y el número de veces que se repite.
"""
def contarLetras(cadena):
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
```

2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
```python
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
```

3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
```python
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
```

4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
```python
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
```

5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.
```python
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
```

6. Escribe una función que calcule el factorial de un número de manera recursiva.
```python
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
```

7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
```PYTHON
listaTuplas = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

"""Funcion para convertir una lista de tuplas a una lista de strings
Args: lista de tuplas
Returns: lista de strings
Se usa la función map() para recorrer la lista de tuplas y se convierte cada tupla a un string. Se convierte el objeto map a lista y se imprime por pantalla.
"""
def convertirListaTuplas(listaTuplas):
    listaStrings = list(map(lambda x: str(x), listaTuplas))
    print(listaStrings)

convertirListaTuplas(listaTuplas)
```

8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
indicando si la división fue exitosa o no.
```PYTHON
"""Funcion para dividir dos números
Args: dos números
Returns: resultado de la división
Se pide al usuario que introduzca dos números. Se comprueba si los números introducidos son numéricos. Si no son numéricos se imprime un mensaje de error. Si son numéricos se comprueba si el segundo número es 0. Si es 0 se imprime un mensaje de error. Si no es 0 se divide el primer número entre el segundo número y se imprime por pantalla.
"""

def dividirNumeros():
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
```

9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
```PYTHON
listaMascotas = ["Perro", "Gato", "Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso", "Loro", "Pez", "Conejo"]

"""Funcion para excluir mascotas prohibidas en España
Args: lista de nombres de mascotas
Returns: lista de nombres de mascotas excluyendo las mascotas prohibidas
Se crea una lista con las mascotas prohibidas. Se usa la función filter() para recorrer la lista de mascotas y se comprueba si la mascota no está en la lista de mascotas prohibidas. Se convierte el objeto filter a lista y se imprime por pantalla.
"""

def excluirMascotasProhibidas(listaMascotas):
    mascotasProhibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    listaMascotasFiltrada = list(filter(lambda x: x not in mascotasProhibidas, listaMascotas))
    print(listaMascotasFiltrada)

excluirMascotasProhibidas(listaMascotas)
```

10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
```python
listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""Funcion para calcular el promedio de una lista de números
Args: lista de números
Returns: promedio de los números
Se comprueba si la lista de números está vacía. Si está vacía se lanza una excepción. Si no está vacía se calcula el promedio de los números y se imprime por pantalla.
"""

def calcularPromedio(listaNumeros):
    if len(listaNumeros) == 0:
        print("La lista está vacía")
    else:
        promedio = sum(listaNumeros) / len(listaNumeros)
        print(promedio)

calcularPromedio(listaNumeros)
```

11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
```python
def comprobarEdad():
    try:
        edad = int(input("Introduce tu edad: "))
    except ValueError:
        print("Debes introducir un número")
    else:
        if edad < 0 or edad > 120:
            print("La edad introducida no es válida")

comprobarEdad()
```

12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
```python
frase = "Hola me llamo Roberto y esto es una prueba hecha para el ejercicio de la longitud de palabras"

"""Funcion para calcular la longitud de cada palabra de una frase
Args: frase
Returns: lista con la longitud de cada palabra
Se separa la frase en palabras. Se usa la función map() para recorrer la lista de palabras y se calcula la longitud de cada palabra. Se convierte el objeto map a lista y se imprime por pantalla.
"""

def longitudPalabras(frase):
    palabras = frase.split()
    longitudes = list(map(len, palabras))
    print(longitudes)

longitudPalabras(frase)
```

13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()
```PYTHON
caracteres = "Hola me llamo Roberto y esto es una prueba hecha para el ejercicio de las letras"

"""Funcion para devolver una lista de tuplas con cada letra en mayúsculas y minúsculas
Args: conjunto de caracteres
Returns: lista de tuplas con cada letra en mayúsculas y minúsculas
Se crea un conjunto con los caracteres de la cadena introducida por el usuario, eliminando espacios y duplicados. 
Se usa la función map() para recorrer el conjunto y se convierte cada letra a una tupla con la letra en mayúsculas y minúsculas. 
Se convierte el objeto map a lista y se imprime por pantalla.
"""

def letrasMayusculasMinusculas(caracteres):

    caracteres = set(caracteres.replace(" ", "").lower())
    listaTuplas = list(map(lambda x: (x.upper(), x), caracteres))
    print(listaTuplas)

letrasMayusculasMinusculas(caracteres)
```

14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()
```python
listaPalabras = ["hola", "adios", "casa", "coche", "perro", "gato", "raton", "elefante", "caballo", "pajaro"]
letra = "c"

"""Funcion para devolver las palabras de una lista que comiencen con una letra en específico
Args: lista de palabras y letra
Returns: lista de palabras que comienzan con la letra en específico
Se usa la función filter() para recorrer la lista de palabras y se comprueba si la palabra comienza con la letra en específico.
Se convierte el objeto filter a lista y se imprime por pantalla.
"""

def palabrasComienzanLetra(listaPalabras, letra):
    palabras = list(filter(lambda x: x[0] == letra, listaPalabras))
    print(palabras)

palabrasComienzanLetra(listaPalabras, letra)
```

15. Crea una función lambda que sume 3 a cada número de una lista dada.
```PYTHON
listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""Funcion lambda para sumar 3 a cada número de una lista
Args: lista de números
Returns: lista con los números sumados 3
Se crea una función lambda que suma 3 a cada número de la lista. Se usa la función map() para recorrer la lista de números y se aplica la función lambda.
Se convierte el objeto map a lista y se imprime por pantalla.
"""

sumaTres = lambda x: x + 3
listaSumaTres = list(map(sumaTres, listaNumeros))
print(listaSumaTres)
```

16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()
```python
cadena = "Hola me llamo Roberto y esto es una prueba hecha para el ejercicio de la longitud de palabras"

"""Funcion que toma una cadena de texto y devuelve una lista de palabras de longitud n
Args: cadena de texto
Returns: lista con palabras de longitud n
Se crea una función para transformar la cadena en lista. Después se crea nueva variabl con la lista fitlrada utilizando el método filter. Para útilizar el método filter creamos un lambda que recorre los iterables comparando la longitud de las palabras. Finalmente imprimimos la lista filtrada.
"""
def filtarPalabras(cadena, n):
    lista = list(cadena.split())
    listaFiltrada = list(filter(lambda x: len(x)>=n, lista))
    print(listaFiltrada)

filtarPalabras(cadena, 3)
```
