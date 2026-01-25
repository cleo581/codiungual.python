#power  of a number
base=int(input("enetr base value:"))
exp=int(input("enter exponent value:"))
power=1
for i in range (1, exp+1):
  power=base*power
  print(base,"power of",exp,"=",power)