number = int(input("შეიტანეთ მთელი რიცხვი: "))
if number > 10:
    print("bigger than 10")
else:
    print("smaller than 10")




    
response = input("Are you a student? (yes/no): ")
if response == "yes" or response == "Yes":
    is_student = True
else:
    is_student = False
    print("is_student =", is_student)