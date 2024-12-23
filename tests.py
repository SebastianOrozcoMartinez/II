class student:
    def __init__(self, name: str, uid: str, classroom: str):
        self.name = name
        self.uid = uid
        self.classroom = classroom
s1 = student("juan","123","1ero A")
print(s1.name)