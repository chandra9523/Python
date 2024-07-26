#Python program to find Area of Traingle

def area_triangle(base,height):
    area = (1/2)*base*height
    print(f"Area of Traingle = {area}")


base = float(input("Enter Base of Traingle = "))

height = float(input("Enter Height of Traingle = "))

area_triangle(base,height)

