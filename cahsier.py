while True:
   bill=(input("enter a number"))
payed=(input("enter a number"))
due=bill-payed
if due<0:
   pass #'we are not handeling this case yet'
else:
   print("due amount is ",end)
   print(due)




