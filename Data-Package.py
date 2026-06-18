net = int(input("Enter your net: "))
if (net <=2):
    gb = net * 19
elif (net <=3):
     gb = net * 39
elif (net >3  and net <=5):
     gb = net * 59
elif (net > 5 and net <=10):
     gb = net * 119
elif (net > 10):
     print("Thambi thappu ")
    # print("10 gb ku mela use panni Yaru Poola oomba poraaah")
else:
    print ("Rupees ",gb)
