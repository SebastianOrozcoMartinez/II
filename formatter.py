from openpyxl import load_workbook
wb = load_workbook("ii.xlsx")
data = wb['Hoja1']



class student:
    def __init__(self, name: str, uid: str, classroom: str):
        self.name = name
        self.uid = uid
        self.classroom = classroom
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
