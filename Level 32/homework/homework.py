def sum_of_two_numbers(num1, num2):
    result = num1 + num2
    print("The sum of", num1, "and", num2, "is:", result)


sum_of_two_numbers(5, 3)



def reverse_string(input_string):
    return input_string[::-1]


reversed_str = reverse_string("hello")
print("Reversed string:", reversed_str)




def find_maximum(numbers):
    return max(numbers)


numbers_list = [3, 5, 7, 2, 8, 1]
maximum_value = find_maximum(numbers_list)
print("The maximum value is:", maximum_value)


# ფუნქცია არის პროგრამირების ერთ-ერთი ძირითადი კონცეფცია, რომელიც აერთიანებს კოდს, რომელიც შეიძლება შესრულდეს ერთიანი ბრძანების სახით.
# def: ეს არის სიტყვა, რომელიც Python-ში გამოიყენება ფუნქციის განსასაზღვრად.
# Function Name- ფუნქციის სახელი არის მას ობიექტის აღსანიშნავი სახელწოდება, რომლის მეშვეობითაც შეგიძლიათ მიმართოთ ფუნქციას.
# Function Parameter- ეს არის ის ცვლადი, რომელიც გამოიყენება ფუნქციაში და რომელიც შეიძლება შეიცვალოს ფუნქციის გამოძახების დროს. 
# Indentation- Python-ში ინდენტაცია არის ზღვარი, რომელიც განსაზღვრავს, რომელია კოდის ნაწილი ფუნქციის, ციკლის, ან სხვა სტრუქტურების შიგნით.
# Code Block- კოდის ბლოკი არის კოდის ნაწილი, რომელიც შედის ერთ კონკრეტულ კონტექსტში, მაგალითად, ფუნქციაში ან ციკლში.
# Function Call- ფუნქციის გამოძახება არის ის პროცესი, როდესაც პროგრამა მიუთითებს ფუნქციას მისი დასახელებით, რათა შეასრულოს იგი.
# Function Argument- არგუმენტი არის მონაცემი, რომელიც გადაეცემა ფუნქციას მისი გამოძახების დროს. ეს არის ის ცვლადი, რომელიც ემთხვევა ფუნქციის პარამეტრს.




import turtle


def draw_square_by_coordinates(coords):
    turtle.penup()
    turtle.goto(coords[0])  
    turtle.pendown()
    
    for point in coords[1:]:  
        turtle.goto(point)
    
    turtle.goto(coords[0])  


def draw_square_by_translation(start_x, start_y, size):
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()

    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)


def draw_square_by_directions(start_x, start_y, size):
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()

    moves = [(size, 0), (0, -size), (-size, 0), (0, size)]  

    for move in moves:
        turtle.goto(turtle.xcor() + move[0], turtle.ycor() + move[1])


turtle.speed(3)


square_coords = [(-300, 300), (-100, 300), (-100, 100), (-300, 100)]
draw_square_by_coordinates(square_coords)

draw_square_by_translation(100, 100, 200)


draw_square_by_directions(100, -100, 200)


square_coords_2 = [(-300, -100), (-100, -100), (-100, -300), (-300, -300)]
draw_square_by_coordinates(square_coords_2)


turtle.done()