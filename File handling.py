file = open("sample_students.txt", "w")
file.write("John Doe\n")
file.write("Jane Smith\n")
file.write("Alice Johnson\n")
file.close()


file = open("sample_students.txt", "r")
print(file.read())
file.close()

