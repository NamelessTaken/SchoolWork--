cost = float(input(" Please Enter the Actual Product Price: "))
sale = float(input(" Please Enter the Sales Amount: "))
if(cost > sale):
   amount = cost - sale
   print("Total Loss Amount = {0}".format(amount))
elif(sale > cost):
   amount = sale - cost
   print("Total Profit = {0}".format(amount))
else:
   print("No Profit No Loss!!!")