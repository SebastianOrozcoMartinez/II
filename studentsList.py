class student:
    def __init__(self, name: str, uid: str, classroom: str):
        self.name = name
        self.uid = uid
        self.classroom = classroom
studentList = {
    "23:E3:71:F7" : student("Pepito","23:E3:71:F7","2do"),
    "456" : student("Juan","456","3ro"),
    "789" : student("Luis","789","1ero A"),
    "4:C0:64:B2:5B:13:90" : student("Jaime","4:C0:64:B2:5B:13:90","1ero B"),
}
