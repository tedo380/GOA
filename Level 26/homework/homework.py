#elif არის Python-ში კლავიშის ერთ-ერთი ნაწილაკი, რომელიც გამოიყენება იმისთვის, რომ შეამოწმოთ სხვადასხვა პირობები ერთდროულად, როდესაც რაიმე პირობა არ სრულდება.
#"elif" გულისხმობს "else if"-ს, რაც ნიშნავს "თუ წინასწარი პირობები არ შესრულდა, მაშინ შეამოწმეთ სხვა პირობა".

#მაშინ გამოიყენებთ elif, როდესაც გსურთ რამდენიმე პირობის გადამოწმება ერთდროულად, მაგრამ არც ერთ მათგანს არ შეასრულებს if.
#else ყოველთვის ბოლო ვარიანტია, რომელიც გამოიყენება ყველა სხვა ვერაგებული მდგომარეობისთვის.


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")



correct_password = "Goa best"
incorrect_attempts = 0

while True:
     password = input("Enter password: ")
if password == correct_password:
        print("Correct password! Access granted.")
else:
        incorrect_attempts += 1
        print("Incorrect password. Try again.")
        print(f"Incorrect attempts: {incorrect_attempts}")









num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"




