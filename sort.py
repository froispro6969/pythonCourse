students = ["Squidward", "Sandy", "Patrick", "Spongebob","Mr.Krabs"]
studentsTuple = ["Squidward", "Sandy", "Patrick", "Spongebob","Mr.Krabs"]

students.sort()
#students.sort(reverse=True)

sorted_students = sorted(studentsTuple)

#for i in sorted_students:
    #print(i)

studentss = [("Squidward","F", 60),
             ("Sandy","A",33),
             ("Patrick","D",36),
             ("Spongebob","B",20),
             ("Mr.Krabs","C",78)]

grade = lambda grades: grades[1]

studentss.sort(key=grade)

for i in studentss:
    print(i)


