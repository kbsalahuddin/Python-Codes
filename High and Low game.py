import random
guesses=0
card=random.randint(1,13)

print("This is dealer's first card:",card)

inp=input(str("Guess the next card number high/low! "))
while guesses<=4:
    
    if guesses==4:
        print("Congratulations!!YOU'VE WON")
        break
    else:
        nxtNum=random.randint(1,13)
        print('Dealer served you ', nxtNum)

        if inp=='h' and nxtNum <= card:
            print('Wrong Guess, You have lost the game')
            break
        elif inp=='l' and nxtNum >= card:
            print('Wrong Guess, You have lost the game')
            break
        else:
            inp=input('the card was ' + str(nxtNum)+'.Is the next number higher or lower?')
            
        guesses+=1
        money=250*guesses
        print('Total money you have won:$',money)
        card=nxtNum
