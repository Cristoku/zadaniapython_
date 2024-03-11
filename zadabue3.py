incometype= input("Whats type of income you will provide? \t Type M for monthly \t Type Y for yearly")

if incometype.lower()=="m":
    incomeM= int(input("Whats your monthly income?"))
    incomeY=incomeM*12

elif incometype.lower()=="y":
    incomeY= int(input("Whats your yearly income?"))   

else:
    print("wrong value, try again")
    exit()
    
if incomeY<= 120000:
    podatek=incomeY*0.12

else:
    incomeY >120000
    podatek=(120000*0.12)+((incomeY-120000)*0.32)

print("Your income tax is: ",podatek)