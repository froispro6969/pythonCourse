# tuple = collection which is ordered and unchangeable used to group together related data

student = ("Damian", 19, "male")

print(student.count("Damian"))
print(student.index("male"))

for x in student:
    print(x)

if "Damian" in student:
    print("Damian is here")