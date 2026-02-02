print("we have to check how many times a character is repeated in a word")
word=input("enter a username")
char=input("enter a charchter to search")
i=0
count=0
while i<len(word):
    if word[i]==char:
        count=count+1
    i=i+1
print("the total number of your charcter is ",count)

        
