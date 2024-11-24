import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500
TITLE = "Bee Game"

score = 0
gameover=False

bee=Actor("bee")
bee.pos = 100,100

flower=Actor("flower")
flower.pos = 300,300

def draw():
    screen.blit("hilly",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: "+str(score),color="black",topleft=(15,10))

    if gameover:
        screen.fill("pink")
        screen.draw.text("Time is up! The final score is "+str(score),center=(250,250),fontsize=40,color="purple")



def move_flower():
    flower.x=randint(50,(WIDTH-50))
    flower.y=randint(50,(HEIGHT-50))

def time_up():
    global gameover
    gameover=True

def update():
    global score
    if keyboard.right:
        bee.x = bee.x + 1
    if keyboard.left:
        bee.x = bee.x - 1
    if keyboard.up:
        bee.y = bee.y - 1
    if keyboard.down:
        bee.y = bee.y + 1
    
    if bee.colliderect(flower):
        score = score + 10
        move_flower()

clock.schedule(time_up,60.0)
    


pgzrun.go()


