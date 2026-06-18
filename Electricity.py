units = int(input("Units: "))
if units <= 100:
    total = units * 5
elif units <= 250:
    total = (100*5)+((units-100)*7)
elif units <= 300:
    total = (100*5)+(150*7)+((units-250)*9)
else:
    total = (100*5)+(150*7)+(50*9)+((units-300)*13)
print("Rupees", total)
