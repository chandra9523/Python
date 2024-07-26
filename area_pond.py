'''
There is a circular pond in a village. 
This pond has a radius of 84 meters. 
Can you find the area of the pond? 
(Bonus: If there is exactly 1.4 liter of water in a square meter, what is the total amount of water in the pond?)
'''

def area_pond(radius):
    area = (22/7)*radius**2
    total_amount_water = 1.4*area
    
    print(f"Area of pond = {area}")
    print(f"Total amount of water in Pond  = {total_amount_water}")

radius = float(input("Enter Radius of Pond = "))

area_pond(radius)



