print ("Welcome to Thomas.T.'s Pizza Parlour")
Diameter = int(input("please tell me how large would you like your pizza to be in inches: "))
Labour_cost = 0.75
Rent = 1
Materials = 0.5 
HST = 0.13
Subtotal = Labour_cost + Rent + Materials * Diameter
Tax = Subtotal * HST 
Total = Subtotal + Tax 
print ("your total comes out to ${:0.2f}." . format(Total))