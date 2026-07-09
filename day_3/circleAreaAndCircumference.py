#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius = float(input("Radius of the circle : "))
print("Area of the circle :", 3.14 * radius ** 2)
print("Circumference of the circle :", 2 * 3.14 * radius)