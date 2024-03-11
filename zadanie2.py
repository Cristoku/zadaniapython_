age= int(input("what's your age? "))
wallet= int(input("how much money do you have? "))
year = int(2024)
missingmoney = int(20-wallet)
ageneed= int(18-age)

if (age>=18 and wallet>=20):
    print("you can buy alkohol, hell yea")
elif age>=18 and wallet<20 :
    print("you are a man but you need at least ", missingmoney, "bucks, to buy alkohol" )
elif age<18 and wallet>=20 :
    print("you are kid but at least you have money, you need ", ageneed ,"more years to but alkohol")
elif age<18 and wallet<20 :
    print("you are kid and dont have money, you need ", missingmoney ,"more years to buy alkohol and ", ageneed ,"moere bucks to buy it")
    
   