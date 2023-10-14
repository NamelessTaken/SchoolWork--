sub1 = int(input("Enter marks for first Subject:: "))
sub2 = int(input("Enter marks for Second Subject:: "))
sub3 = int(input("Enter marks for Third Subject:: "))
sub4 = int(input("Enter marks for Fourth Subject:: "))
sub5 = int(input("Enter marks for Fifth Subject:: "))
avg = (sub1+sub2+sub3+sub4+sub5)/5
if avg >= 90:
    print("Grade:A")
elif avg >= 80 & avg < 90:
    print("Grade:B")
elif avg >= 70 & avg < 80:
    print("Grade:C")
elif avg >= 60 & avg < 70:
    print("Grade:D")
else:
    print("Grade:F")
