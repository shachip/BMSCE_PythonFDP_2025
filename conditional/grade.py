s1 = int(input("Enter subject1: "))
s2 = int(input("Enter subject2: "))
s3 = int(input("Enter subject3: "))
s4 = int(input("Enter subject4: "))
s5 = int(input("Enter subject5: "))
perc = (s1+s2+s3+s4+s5)/5
if perc>=75:
    print("A")
elif perc>=50 and perc<75:
    print("B")
elif perc>=30 and perc<50:
    print("C")
else:
    print("FAIL")
