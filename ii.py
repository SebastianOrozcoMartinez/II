'''
II V0.3
Este código está hecho para poder identificar distintas personas
a traves de codigos de identificación y para registrarlos en una
base de datos en forma de lista de asistencia
'''

# initialize variables and import libraries
from openpyxl import load_workbook
from adafruit_pn532.i2c import PN532_I2C
import time, regex, board, busio
wb = load_workbook("ii.xlsx")
data = wb['Hoja1']
config = wb['Ajustes']
# Start I2C
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c)  # No se necesita especificar la dirección


def getKey(diccionario: dict, valor_buscado: str): #GPT
    # Finds all the keys
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
def numToCol(num):
# This function turns any number to a excel column
# Example: Input: 1 Output: A, Input: 4 Output: D
    Alphabet = {
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
        letter = Alphabet.get(num)
        x.append(letter)
        num = num - 26
    return x
def readCols(col,hoja):
    # This function format the data in a dictionary with his cell
    #  Data1:Cell, Data2:Cell, Data3:Cell
    lista = []
    lista2 = []
    for i in range (2,1000):
        contador = (f"{col}{i}")
        celda = hoja[contador].value
        lista2.append(contador)
        lista.append(str(celda))
    return dict(zip(lista, lista2))
def readRows(row,hoja):
# Its in development, its readCols() but for rows
    list = []
    for i in []:
        contador = (f"{i}{row}")
        celda = hoja[contador].value
        list.append(str(celda))
    return list

# Saves student data:
UIDs = readCols('B',data)    # UID
students = readCols('A',data) # Student
classroom = readCols('C',data)   # Classroom
entrada = int(config['B1'].value) # Searches for the check-in time
######### Other code

while 1: # Infinite loop
    # Searches for a PICC
    uid = pn532.read_passive_target()
    if uid is not None:
        print("Tarjeta detectada con UID:", [hex(i) for i in uid])
        time.sleep(1)
    
    # Takes the UID and then checks if its on the list
    print('Introduce el UID')    
    student = interdicc(UIDs,students,'A',input())
    if student == 'None':
        print('No se encontro el UID ⚠️')
        continue
    # Search for the classroom of the student
    grado = interdicc(students, classroom, 'C', student)
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
    # Checks and compares the actual time with the check-in time 
    asistencia = False
    tiempoActual = time.localtime()
    localTime = tiempoActual.tm_hour
    if localTime >= entrada:
        print(f'El student {student} de {grado} llegó tarde')
        asistencia = False
    else:
        print(f'El student {student} de {grado} llegó temprano')
        asistencia = True

    # Assistance is recorded
    students_por_grado = readCols('A',sheet)
    row = students_por_grado.get(student)
    print(row)
    contador = 1
    for i in row:
        if i != 'None':
            contador = contador + 1
    word = numToCol(contador)[0]
    if asistencia == True:
        sheet[f'{word}{row}'] = 'O'
    else:
        sheet[f'{word}{row}'] = 'X'

    #Save changes
    wb.save('ii.xlsx')
    print('Se ha registrado la asistencia')