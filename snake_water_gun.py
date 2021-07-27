#snake water and gun project -1 
import random
def gamewin(comp, user):
    if comp == user:
        return None
    elif comp == 's':       #WHEN COMPUTER CHOOSES 
        if user == 'g':
            return True
        elif user == 'w':
            return False
    elif comp == '   w':       #WHEN COMPUTER CHOOSES WATER  
        if user == 's':
            return True
        elif user == 'g':
            return False
    elif comp == 'g':       #WHEN COMPUTER CHOOSES GUN
        if user == 'w':
            return True
        elif user == 's':
            return False

print("****YOU ARE PLAYING WITH THE COMPUTER!!....")
print("****CHOOSE SNAKE with (s),WATER with (w),GUN with (g) when your turn comes...")
width = 50 
print(" LET'S START THR GAME!! ".center(width,"*"))
print("Computer's turn: CHOOSE SNAKE(s), WATER(w), GUN(g)?: " )
randomNo = random.randint(1,3)
if randomNo == 1:
    comp = 's'
elif randomNo == 2:
    comp = 'w'
if randomNo == 3:
    comp = 'g'
user = input("Your's turn:CHOOSE SNAKE(s), WATER(w), GUN(g)?: ")
print(f"COMPUTER chooses:{comp}")
print(f"YOU chooses:{user}")
w = "🎉🎉"
f = "😥😥"
t = "🙌"
result = gamewin(comp, user)
if result == None:
    print ("RESULTS: THERE IS A TIE!!" + t)
elif result == True:
    print ("RESULTS: YOU WON!!"+ w)
if result == False:
    print ("RESULTS: YOU LOSE!!"+ f)
