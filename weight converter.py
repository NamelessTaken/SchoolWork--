weight=int(input(" Enter your Weight:"))
unit=input("(K)g or (L)bs:")
if unit.upper()=="K":
    converted = weight / 0.45454545454545
    print("weight in Lbs:"+str(converted))
else:
    converted = weight * 0.45454545454545
    print("weight in Kgs:"+str(converted))
