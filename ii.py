'''
II V0.3
Este código está hecho para poder identificar distintas personas
a traves de codigos de identificación y para registrarlos en una
base de datos en forma de lista de asistencia
'''
##### Modificables #####
# Hola :)
######### Inicio

from openpyxl import load_workbook
import time, regex
# Variables a inicializar
wb = load_workbook("ii.xlsx") # Indica con que archivo se esta trabajando
data = wb['Hoja1']
config = wb['Ajustes']

# Funciones creadas
def getKey(diccionario: dict, valor_buscado: str): #GPT
    # Encuentra todas las claves correspondientes al valor
    claves_encontradas = []
    for clave, valor in diccionario.items():
        if valor == valor_buscado:
            claves_encontradas.append(clave)
    return ''.join(claves_encontradas)
def interdicc(dicc1: dict,dicc2: dict,column,searched: str):
    x = dicc1.get(searched)
    if x == None:
        return 'None'
    num = regex.findall('\d',x)
    if dicc2.get(num[0]) != 'None':
        y = getKey(dicc2,f'{column}{num[0]}')
    else:
        y = 'Nop'
    return y
def numToWord(num):
# Esta función sirve para transformar numeros a columnas de excel
# Ejemplo: 1 = A, 4 = D
    dicc = {
        # Listado de las letras
        1 : 'A', 2 : 'B', 3 : 'C',
        4 : 'D', 5 : 'E', 6 : 'F',
        7 : 'G', 8 : 'H', 9 : 'I',
        10 : 'J', 11 : 'K', 22 : 'L',
        13 : 'M', 14 : 'N', 15 : 'O',
        16 : 'P', 17 : 'Q', 18 : 'R',
        19 : 'S', 20 : 'T', 21 : 'U',
        22 : 'V', 23 : 'W', 24 : 'X',
        25 : 'Y', 26 : 'Z'
    }
    x = []
    while num > 0:
        letter = dicc.get(num)
        x.append(letter)
        num = num - 26
    return x
def readCols(col,hoja):
    # Esta funcion ayuda en guardar en un diccionario de esta manera
    #  Dato1:Celda, Dato2:Celda, Dato3:Celda
    lista = []
    lista2 = []
    for i in range (2,1000):
        contador = (f"{col}{i}")
        celda = hoja[contador].value
        lista2.append(contador)
        lista.append(str(celda))
    return dict(zip(lista, lista2))
def readRows(row,hoja):
# Sigue en desarrollo, es lo mismo que readcols() pero para filas.
    list = []
    for i in []:
        contador = (f"{i}{row}")
        celda = hoja[contador].value
        list.append(str(celda))
    return list

# Guarda en diccionarios la siguiente información:
UIDs = readCols('B',data)    # UID
Alumnos = readCols('A',data) # Alumno
Grados = readCols('C',data)   # Grados
entrada = int(config['B1'].value) # Busca la hora de entrada
######### Other code

while 1: # Bucle infinito
    
    # Se solicita el UID y se comprueba su existencia en la lista
    print('Introduce el UID')    
    alumno = interdicc(UIDs,Alumnos,'A',input())
    if alumno == 'None':
        print('No se encontro el UID ⚠️')
        continue
    # Se comprueba el grado del alumno para guardar su asistencia
    grado = interdicc(Alumnos, Grados, 'C', alumno)
    if grado == '1A':
        grado = '1ero A'
        sheet = wb['1ero A']
    elif grado == '1B':
        grado = '1ero B'
        sheet = wb['1ero B']
    elif grado == '2':
        grado = '2do'
        sheet = wb['2do']
    elif grado == '3':
        grado = '3er'
        sheet = wb['3ero']
    # Se comprueba la hora actual y se compara con la de llegada.
    asistencia = False
    tiempoActual = time.localtime()
    hora = tiempoActual.tm_hour
    if hora >= entrada:
        print(f'El alumno {alumno} de {grado} llegó tarde')
        asistencia = False
    else:
        print(f'El alumno {alumno} de {grado} llegó temprano')
        asistencia = True

    # Se anota la asistencia
    Alumnos_por_grado = readCols('A',sheet)
    row = Alumnos_por_grado.get(alumno)
    print(row)
    contador = 1
    for i in row:
        if i != 'None':
            contador = contador + 1
    word = numToWord(contador)[0]
    if asistencia == True:
        sheet[f'{word}{row}'] = 'O'
    else:
        sheet[f'{word}{row}'] = 'X'

    #Se guarda la asistencia
    wb.save('ii.xlsx')
    print('Se ha registrado la asistencia')
# Hola marte :)