income=int(input("Enter your income: "))
if income<=250000:
    tax=0
elif income>=250000 and income<=500000:
    tax=income*0.05
elif income>=500000 and income<=1000000:
    tax=income*0.10
elif income>=1000000:
    tax =income*0.20
print("tax = ",tax)
