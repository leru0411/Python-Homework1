#Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input("Введите число X: "))
y = int(input("Введите число Y: "))
z = int(input("Введите число Z: "))

n1 = not(x or y or z)
n2 = not x and not y and not z
print(n1 == n2)