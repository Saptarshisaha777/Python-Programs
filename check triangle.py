print("In Triangle ABC")
a=input("Input side a: ")
b=input("Input side b: ")
c=input("Input side c: ")
if (a==b==c):
    print("It is an Equilateral Triangle")
elif (a!=b and b!=c and c!=a):
    print("It is a Scalene Triangle")
else:
    print("It is an isosceles Triangle")
