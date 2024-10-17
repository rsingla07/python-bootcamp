x=int(input("enter any number"))
if(x%3==0 and x%5!=0):
    print("divisible by 3")
elif(x%5==0 and x%3!=0):
    print("divisible by 5")
elif(x%3==0 and x%5==0):
    print("divisible by both 3 and 5")
else:
    print("not divible by 3 or 5")