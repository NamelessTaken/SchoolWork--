def area_square(a):
    area1=float(a*a);
    print("Area of square is:",area1)
def area_circle(r):
    area2=float(3.14*r*r);
    print("Area of circle is:",area2)
def area_rectangle(a,b):
    area3=float(a*b);
    print("Area of rectangle is:",area3)
def area_triangle(x,y):
    area4=float((x*y)/2);
    print("Area of triangle is:",area4)
def peri_square(a):
    peri1=float(4*a);
    print("Perimeter of square is:",peri1)
def peri_circle(r):
    peri2=float(2*3.14*r);
    print("Perimter of circle is:",peri2)
def peri_triangle(a,b):
    hypotenuse=float(a*a+b*b)
    peri3=float(a+b+hypotenuse)
    print("Perimter of right angled triangle is:",peri3)
def peri_rectangle(a,b):
    peri4=float(2*(a+b))
    print("Perimter of rectangle is:",peri4)
side=float(input("enter the side of square:"))
area_square(side)
print()
peri_square(side)
radius=float(input("enter the radius of circle:"))
area_circle(radius)
peri_circle(radius)
length=float(input("enter the length of rectangle:"))
breadth=float(input("enter the breadth of rectangle:"))
area_rectangle(length,breadth)
peri_rectangle(length,breadth)
base=float(input("enter the base of right angled triangle:"))
height=float(input("enter the height of right angled triangle:"))
area_triangle(base,height)
peri_triangle(base,height)
