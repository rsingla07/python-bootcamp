y=int(input("enter any year"))
if(y%400==0 and y%100==0):
    print("year is a leap year")
elif(y%4==0 and y%100!=0):
    print("year is a leap year")
else:
    print("year is not leap year")