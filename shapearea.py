from shapeareaclass import Shape,Circle,Rectangle
rad1 =float(input("Enter Radius of Circle 1: "))
fillColor1=input("Enter the Fill Color of Circle1 : ")
c1=Circle(rad1,fillColor1)

length=float(input("Enter length of Rectangle: "))
breadth=float(input("Enter the Breadth of Rectangle: "))
fillColorRect=input("Enter the Fill color of the Rectangle: ")
rect=Rectangle(length,breadth,fillColorRect)

rad2 =float(input("Enter Radius of Circle 2: "))
fillColor2=input("Enter the Fill Color of Circle 2 : ")
c2=Circle(rad2,fillColor2)

print("\nArea of Circle 1:",c1.area())
print("\nArea of Rectangle:",rect.area())
print("\nArea of Circle 2:",c2.area())

print("Cirlce 1 has a smaller area than Circle 2:",c1 < c2)