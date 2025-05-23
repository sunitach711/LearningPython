import randon0
Cnumber=random.randrange(1,101)
userInput=int(input("Enter your number:---"))
if userInput>Cnumber:
    print("Computer Number",Cnumber)
    print("Your guess number is too high")
elif Cnumber>userInput:
    print("Computer Number", Cnumber)
    print("Your guess number is too low")
else:
    print("Computer Number", Cnumber)
    print("Your guess number is equal")

#Enter your number:---45
#Computer Number 82
#Your guess number is too low

#Enter your number:---90
#Computer Number 45
#Your guess number is too high


