print("exam eligibilty check")
medical_cause=(input("is there any medical cause?yes/no"))
attendance=int(input("enter attendance percentage"))
if medical_cause=="yes":
    print("eligable for exam")
else:
    if attendance>=75:
        print("eligable for exam")
    else:
        print("not eligable for exam")