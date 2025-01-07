# შემოტანეთ მთელი რიცხვი
number = int(input("შეიტანეთ მთელი რიცხვი: "))

# პირობითი განცხადება
if number > 0:
    print("Bigger than 0")
elif number == 0:
    print("0")
else:
    print("Smaller than 0")



# მომხმარებლისგან ორი რიცხვის მიღება
first_number = int(input("შეიტანეთ პირველი რიცხვი: "))
second_number = int(input("შეიტანეთ მეორე რიცხვი: "))

# პირობითი განცხადება და დიაპაზონის შექმნა
if first_number > second_number:
    # თუ პირველი რიცხვი მეტია მეორეზე
    number_range = range(second_number, first_number + 1)
elif second_number > first_number:
    # თუ მეორე რიცხვი მეტია პირველზე
    number_range = range(first_number, second_number + 1)
else:
    # როდესაც რიცხვები ტოლია
    print("numbers are equal")

# დიაპაზონშიiterating for ციკლით
for number in number_range:
    print(number)



score = float(input("Enter the score (0-100): "))
if score < 0 or score > 100:
    print("Invalid score! Please enter a score between 0 and 100.")
if score >= 90:
        grade = 'A'
elif score >= 80:
        grade = 'B'
elif score >= 70:
        grade = 'C'
elif score >= 60:
        grade = 'D'
else:
        grade = 'F'    
print("The grade is: {grade}")
    