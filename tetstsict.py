#define test dictionary
test_dict={"codinlingual":3, "is":2, "best":2,"for":2,"for":2,"coding":1}
#print the test_dict so user can see it
print ("TEST DICTIONARY:",test_dict)
# tell user to put user input to check it
#we wrap in it in a interger()becuase the values are in this example  are intergers
val=int(input("enter the values you  want to check the frequency of:"))
#count the ocuurences of that value
#.value[] gives us  [3,2,2,2,2,1]
frequency=list(test_dict.values().count(val))
#print the result of this
print(f"the frequency of vali{val} is {frequency}")