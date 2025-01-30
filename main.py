'''
II V0.3
This code helps identifing difrent people using UIDs (Unique Identificator Device)
and saving his assistant in a Excel file
'''

# initialize variables and import libraries
from openpyxl import load_workbook
# from adafruit_pn532.i2c import PN532_I2C
import time, re, config#, board, busio
wb = load_workbook("ii.xlsx")
data = wb['Hoja1']
config_sheet = wb['Ajustes']
# Start I2C
# i2c = busio.I2C(board.SCL, board.SDA)
# pn532 = PN532_I2C(i2c)


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
######### Other code
while 1: # Infinite loop
    # Searches for a PICC
    print("Aproxima una tarjeta")
    uid = "4:C0:64:B2:5B:13:90" #Debugging
    '''
    while uid is None:
        uid = pn532.read_passive_target()
        if uid is not None:
            uid = "".join([hex(i) for i in uid])
            uid = regex.sub(r'0x', ':', uid).replace(":","",1).upper()
            print(uid)
            time.sleep(0.5)
    '''
    # Takes the UID and then checks if its on the list
    student = config.studentList.get(uid).name
    if student == 'None':
        print('No se encontro el UID ⚠️')
        continue
    # Search for the classroom of the student
    grado = config.studentList.get(uid).classroom
    sheet = wb[grado]
    # Checks and compares the actual time with the check-in time 
    asistencia = False
    tiempoActual = time.localtime()
    localTime = tiempoActual.tm_hour
    if localTime >= config.entrada:
        print(f'El alumno {student} de {grado} llegó tarde')
        asistencia = False
    else:
        print(f'El alumno {student} de {grado} llegó temprano')
        asistencia = True
    ### WARNDING: ❗ THE NEXT CODE DOESNT WORK ALREADY ❗ ###
    # Assistance is recorded
    students_por_grado = readCols('A',sheet)
    row = students_por_grado.get(student)
    print(row)
    word = ''.join(numToCol(2))
    print(students_por_grado)
    
    # Write if the student is present or not
    if asistencia == True:
        sheet[f'{word}{row}'] = 'O'
        print(f'{word}{row}')
    else:
        sheet[f'{word}{row}'] = 'X'
        print(f'{word}{row}')

    # Save changes
    wb.save('ii.xlsx')
    print('Se ha registrado la asistencia')
    break