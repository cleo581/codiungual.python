num=int(input("enter a number"))
count=0
if num==0:
   count=1
else:
    while num!=0:
        num//=10
        count=count+1
print("total digits=",count)