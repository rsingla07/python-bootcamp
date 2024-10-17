x=int(input("enter any number"))
y=int(input("enter any number"))
z=int(input("enter any number"))
if(x+y>z or x+z>y or y+z>x):
    print("valid triangle")
else:
    print("not valid triangle")