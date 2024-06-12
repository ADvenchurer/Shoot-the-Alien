import pgzrun
import random

WIDTH = 500
HEIGHT = 500
TITLE = "Alien Shooting Game"
message = ""
score = 0
win = False


alien = Actor("alienimg")
alien2 = Actor("alienimg2")

alien2.pos = 1000,1000

def placealien():
    alien.x = random.randint(50,450)
    alien.y = random.randint(50,450)

def removealien():
    alien.pos = 1000,1000

def placedecoy():
    alien2.pos = 250,250

placealien()

def draw():
    global message
    screen.fill(color = (128,0,0))
    alien.draw()
    alien2.draw()
    screen.draw.text(message,center = (400,10),fontsize = 30)
    screen.draw.text(str(score),center = (20,10),fontsize = 30)






def on_mouse_down(pos):
    global message,score,win
    if alien.collidepoint(pos):
        placealien()
        message = "Nice hit!"
        print(message)
        score = score+1
        print(score)

        if score >= 10:
            message = "You win!"
            placedecoy()
            removealien()
            win = True
            if win==True:
                score = 10

    else:
        if win==False:

            message = "You missed!"
            print(message)
            score = score-2
            print(score)
            if score <= -5:
                score = -5
                message = "You lose!"
                placedecoy()
                removealien()






pgzrun.go()