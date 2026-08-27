#Ted Guerrero
#CTC389
#Lab 6

students = ["Johnny","Jaime","Joseph","Jessica","Julie"]

print("\n")
print("Welcome to the student catalog.")
print("Here is the current list:")
for i in students:
    print(i)
print("\n")
print("Option 1: ADD student to list")
print("Option 2: MODIFY student name")
print("Option 3: REMOVE student")
print("\n")

option = int(input("Make your selection:"))
index = 0+1

if (option == 1):
    add = str(input("Enter name you would like added to the list: "))
    students.append(add)
    for i in students:
        print(i)

if (option == 2):
    print(0,students[0])
    print(1,students[1])
    print(2,students[2])
    print(3,students[3])
    print(4,students[4])
    print("\n")
    mod = int(input("Which name would you like modified?: "))
    name = str(input("Enter the new name for this position: "))
    students[mod] = name
    print(0,students[0])
    print(1,students[1])
    print(2,students[2])
    print(3,students[3])
    print(4,students[4])
    print("\n")

if (option == 3 ):
    print(0,students[0])
    print(1,students[1])
    print(2,students[2])
    print(3,students[3])
    print(4,students[4])
    print("\n")
    rem = int(input("Which name would you like removed?: "))
    students.pop(rem)
    print(0,students[0])
    print(1,students[1])
    print(2,students[2])
    print(3,students[3])
    print("\n")

