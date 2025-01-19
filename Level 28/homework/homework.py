# List (სია) – ეს არის მონაცემთა სტრუქტურა, რომელიც საშუალებას იძლევა რამდენიმე ელემენტის შენახვა და მათზე მოქმედების განხორციელება ერთობლივად.
# Index (ინდექსი) – ეს არის ელემენტის მორგებული ადგილი სიაში. ინდექსები ყოველთვის იწყება ნულიდან (0), ანუ პირველ ელემენტს აქვს ინდექსი 0, მეორე ელემენტს – 1 და ასე შემდეგ.
# Indexing (ინდექსაცია) – ეს არის პროცესი, რომლის დროსაც ჩვენ მივდივართ კონკრეტულ ელემენტამდე სიაში მისი ინდექსის საშუალებით.
#  Mutable (შესაძლებელი ცვლილება) – ეს ეხება ობიექტებს, რომლებიც შეიძლება შეიცვალოს ან განახლდეს. 
# Immutable (შესაძლებელი ცვლილების გარეშე) – ეს არის ობიექტები, რომელთა ცვლილებაც შეუძლებელია, როდესაც ისინი შექმნილია.


numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[4]) 



my_list = [10, "hello", 3.14, True, [1, 2, 3], "world", 42, False, {"key": "value"}, None, 99, 3.14159, "Python", 0, 7.89, (1, 2), "apple", 15, 100, "banana"]
for i in range(len(my_list)):
    print(f"Element at index {i}: {my_list[i]}")


numbers = [10, 20, 30, 40, 50]
print("First element (using negative indexing):", numbers[-5]) 
print("Third element (using negative indexing):", numbers[-3])  
print("Last element (using negative indexing):", numbers[-1])



name = input("Please enter your name: ")
print("First symbol:", name[0]) 
print("Last symbol:", name[-1]) 
