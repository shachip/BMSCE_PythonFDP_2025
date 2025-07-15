name = input("Enter your name: ")
age = int(input("Enter your age: "))
empID = int(input("Enter your EmpID: "))

#without formatted string
print("Your name is " +name+ " and your age is " +str(age)+ " and your empID is: ", empID) #can use comma only at the end and only one variable

#Formatted strings do not require explicit type-casting
#use 'f'
print(f"Your name is {name} and your age is {age} and your empID is {empID}")#{} is placeholder
