from random import randint

#Function to take users choice and generate a random choice for computer and decides a win.
#while also updating the wins,loses and draws of the user.

def com_select(x,w,l,d):
    y = randint(1,3)
    if x==y:
        d+=1
        return [("Draw"),(w,l,d)]
    elif x==1:
        if y==2:
            w+=1
            return [("You win"),(w,l,d)]
        else:
            l+=1
            return [("Com win"),(w,l,d)]
    elif x==2:
        if y==3:
            w+=1
            return [("You win"),(w,l,d)]
        else:
            l+=1
            return [("Com win"),(w,l,d)]
    elif x==3:
        if y==1:
            w+=1
            return [("You win"),(w,l,d)]
        else:
            l+=1
            return [("Com win"),(w,l,d)]

#initialising the values for wins,loses,draws before starting infinite while loop
w = 0
l = 0
d = 0

#Infinite loop to let user play for as long as he wants until he wishes to break the loop
while True:
    #Menu of choices for users
    print("Choose a number from menu")
    print("1.Rock")
    print("2.Scissor")
    print("3.Paper")
    print("4.Quit Game")
    x = int(input("Your choice: "))
    if x==4:
        print("Wins: %d"%(w))
        print("Loses: %d"%(l))
        print("Draws: %d"%(d))
        break
    elif x in [1,2,3]:
        #function returns a list of a string and a tuple, the string is the result to be printed while
        #tuple updates the values of w,l,d. ["String",(w,l,d)]
        result = com_select(x,w,l,d)
        w = result[1][0]
        l = result[1][1]
        d = result[1][2]
        print("*************")
        print(result[0])
        print("*************")
    else:
        print("Please Enter Correct Choice !!")
