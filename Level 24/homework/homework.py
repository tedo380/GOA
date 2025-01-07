x = 5
x += 3  # x = x + 3
print(x)  # 8

y = 10
y += 2  # y = y + 2
print(y)  # 12

a = 0
a += 10  # a = a + 10
print(a)  # 10

b = -5
b += 4  # b = b + 4
print(b)  # -1

c = 15
c += 7  # c = c + 7
print(c)  # 22

d = -10
d += -2  # d = d + (-2)
print(d)  # -12

e = 8
e += 0  # e = e + 0
print(e)  # 8

f = 2
f += -3  # f = f + (-3)
print(f)  # -1

g = 5
g += 100  # g = g + 100
print(g)  # 105

h = 50
h += -25  # h = h + (-25)
print(h)  # 25





x = 10
x -= 3  # x = x - 3
print(x)  # 7

y = 20
y -= 5  # y = y - 5
print(y)  # 15

a = 5
a -= 5  # a = a - 5
print(a)  # 0

b = -3
b -= -2  # b = b - (-2)
print(b)  # -1

c = 8
c -= 3  # c = c - 3
print(c)  # 5

d = 50
d -= 25  # d = d - 25
print(d)  # 25

e = 100
e -= 50  # e = e - 50
print(e)  # 50

f = 0
f -= 1  # f = f - 1
print(f)  # -1

g = -10
g -= 10  # g = g - 10
print(g)  # -20

h = 30
h -= 15  # h = h - 15
print(h)  # 15






x = 2
x *= 3  # x = x * 3
print(x)  # 6

y = 5
y *= 4  # y = y * 4
print(y)  # 20

a = 10
a *= 0  # a = a * 0
print(a)  # 0

b = -3
b *= 2  # b = b * 2
print(b)  # -6

c = 7
c *= 5  # c = c * 5
print(c)  # 35

d = -4
d *= -2  # d = d * (-2)
print(d)  # 8

e = 6
e *= 1  # e = e * 1
print(e)  # 6

f = 3
f *= -3  # f = f * (-3)
print(f)  # -9

g = 10
g *= 10  # g = g * 10
print(g)  # 100

h = 12
h *= -1  # h = h * (-1)
print(h)  # -12






x = 20
x /= 4  # x = x / 4
print(x)  # 5.0

y = 18
y /= 3  # y = y / 3
print(y)  # 6.0

a = 10
a /= 2  # a = a / 2
print(a)  # 5.0

b = 9
b /= 3  # b = b / 3
print(b)  # 3.0

c = 25
c /= 5  # c = c / 5
print(c)  # 5.0

d = 6
d /= 2  # d = d / 2
print(d)  # 3.0

e = 7
e /= 7  # e = e / 7
print(e)  # 1.0

f = 100
f /= 10  # f = f / 10
print(f)  # 10.0

g = 50
g /= 5  # g = g / 5
print(g)  # 10.0

h = 0
h /= 1  # h = h / 1
print(h)  # 0.0






# >= (მეტია ან ტოლია): ეს ოპერატორი ამოწმებს, თუ მარცხენა Operand-ის მნიშვნელობა მეტია ან ტოლია მარჯვენა Operand-ს.

# <= (ნაკლებია ან ტოლია): ეს ოპერატორი ამოწმებს, თუ მარცხენა Operand-ის მნიშვნელობა ნაკლებია ან ტოლია მარჯვენა Operand-ს.


#პირობითი განცხადებები ამოწმებენ რაიმე პირობას და კონკრეტულ მოქმედებებს
#ასრულებენ იმის მიხედვით, თუ იქნება ეს პირობა ჭეშმარიტი თუ მცდარი. ძირითადი
#პირობითი განცხადებები არის if, elif (else if), და else.


# შემოიტანეთ რიცხვი
number = float(input("შეიტანეთ რიცხვი: "))

# პირობითი განცხადება დადებითი თუ უარყოფითი რიცხვის შესამოწმებლად
if number > 0:
    print("დადებითი რიცხვი")
elif number < 0:
    print("უარყოფითი რიცხვი")
else:
    print("რიცხვი არის 0")





# შემოიტანეთ მთელი რიცხვი
number = int(input("შეიტანეთ რიცხვი: "))

# პირობითი განცხადება 100-ზე დიდობის გასაგებად
if number > 100:
    print("big number")
else:
    print("small number")