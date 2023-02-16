x=1
marks=59
grades=89
mileage=8900
#if statement
if(x>0):
    print("The number is positive")
    print(4+10)
#if..else statement
if marks>=60:
    print("you have passed")
else:
    print("You have failed")

#if..elif..else
if grades<=29 and grades>=0:
    print("You have failed")
elif grades<=49 and grades>=30:
    print("You have passed")
elif grades<=79 and grades >=50:
    print("You have credit")
elif grades<=100 and grades>=80:
    print("You have distinction")
else:
    print("Wrong input")


if mileage<=500 and mileage>=0:
    print("Brand new")
elif mileage<=10000 and mileage>=501:
    print("Slightly used")
elif mileage>=10001:
    print("Used")
else:
    print("Wrong input")






