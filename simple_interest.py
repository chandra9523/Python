#Store the principal amount, rate of interest, and time in different variables
#and then calculate the Simple Interest for 3 years**.*

def simple_interest(principal,rate,time):
    si = principal*rate*time/100
    print(f"Simple Interest for {time} years at {rate}% is {si}")
    
principal = float(input("enter pricipal amount = "))
rate = float(input("enter the rate of intrest = "))
time = int(input("Enter Time = "))

simple_interest(principal,rate,time)


    

