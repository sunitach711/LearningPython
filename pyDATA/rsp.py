import random

l = ["rock", "scissor", "paper"]
'''
rock.vs.paper->.paper.wins
rock.vs.scissor->.rock.wins
paper.vs.scissor->.scissor.wins

'''

while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
Game start.....
1 Yes 
2 No | Exit     
    '''))
    if uc == 1:
        for a in range(1, 6):
            userInput = int(input('''
1.Rock
2.Scissor
3.Paper            
            
            '''))
            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "scissor"
            elif userInput == 3:
                uchoice = "paper"
            Cchoice = random.choice(l)
            if Cchoice == uchoice:
                print("Computer Value", Cchoice)
                print("User Value", uchoice)
                print("Game Draw")
                ucount = ucount + 1
                ccount = ccount + 1
            elif (uchoice == "rock" and Cchoice == "scissor") or (uchoice == "paper" and Cchoice == "rock") or (
                    uchoice == "scissor" and Cchoice == "paper"):
                print("Computer Value", Cchoice)
                print("User Value", uchoice)
                print("You Win")
                ucount=ucount+1
            else:
                print("Computer Value", Cchoice)
                print("User Value", uchoice)
                print("Computer Win")
                ccount = ccount + 1

        if ucount==ccount:
                print("Final Game Draw....")
                print("User score",ucount)
                print("Computer Score",ccount)
        elif ucount>ccount:
                print("Final You Win The Game....")
                print("User score", ucount)
                print("Computer Score", ccount)
        else:
                print("Final Computer Win The Game....")
                print("User score", ucount)
                print("Computer Score", ccount)

    else:
         break







