'''
There is a circular pond in a village. 
This pond has a radius of 84 meters. 
Can you find the area of the pond? 
(Bonus: If there is exactly 1.4 liter of water in a square meter, what is the total amount of water in the pond?)
'''

def area_pond(radius):
    area = (22/7)*radius**2
    
    print(f"Area of pond = {area}")

radius = float(input("Enter Radius of Pond = "))

area_pond(radius)



