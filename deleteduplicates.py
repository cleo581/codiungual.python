student_data={
    "id1":{"name":"sarah","class":"v","subject":"english,maths,science"},
    "id2":{"name":"sarah","class":"v","subject":"english,maths,science"},
    "id3":{"name":"jake","class":"v","subject":"english,maths,science"}


}
result={}
seen_key=[]
for student_id,details in student_data.items():
    unique_key=(details["name"],details["class"],details["subject"])
    if unique_key not in seen_key:
        seen_key.append(unique_key)
        result[student_id]=details
for k,v in result.items():
    print (k,":",v)

