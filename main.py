import json
students_file = "./data/students.json"
with open(students_file, "r") as f:
    student_list = json.load(f)

while True:
    print("Please, type a UID")
    uid = input("UID: ")
    try:
        student = student_list[uid]["name"]
        print(student)
    except KeyError:
        print("The UID isn't in the list")
        break
