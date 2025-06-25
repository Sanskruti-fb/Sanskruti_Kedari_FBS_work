subject1 = int(input("Enter marks obtained in sub1: "))
subject2 = int(input("Enter marks obtained in sub2: "))
subject3 = int(input("Enter marks obtained in sub3: "))
subject4 = int(input("Enter marks obtained in sub4: "))
subject5 = int(input("Enter marks obtained in sub5: "))

total1 = int(input("Enter total marks of sub1: "))
total2 = int(input("Enter total marks 0f sub2: "))
total3 = int(input("Enter total marks of sub3: "))
total4 = int(input("Enter total marks of sub4: "))
total5 = int(input("Enter total marks of sub5: "))

totalmarksobtained = (subject1+subject2+subject3+subject4+subject5)

print("total marks obtained in all 5 sub: ",totalmarksobtained )


totalmaximummarks = (total1+total2+total3+total4+total5)

print("total maximum marks of all 5 sub: ",totalmaximummarks )


percentage = totalmarksobtained/totalmaximummarks*100

print("Percentage of students based on marks obtained in 5 subjects: ",percentage)