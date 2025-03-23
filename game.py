import pgzrun
import random

WIDTH = 1200
HEIGHT = 800

startspeed = 10
currentlevel = 1
gameover = False
gamecomplete = False
finallevel = 6
animations = []

itemlist = ["battery.png", "crisps.png", "plasticbag.png", "plasticbottle.png"]
items = []

def draw():
    global itemlist, items, gamecomplete, gameover
    screen.clear()
    screen.blit("nature.png", (0, 0))
    if gameover:
        screen.draw.text("the game is over", fontsize = 60, center = (600, 400), color = "green")
    elif gamecomplete:
         screen.draw.text("the game is complete, you won!!!", fontsize = 60, center = (600, 400), color = "green")
    else:
        for i in items:
            i.draw()
#this function draws the background and items. the if makes it so the game over and game complete screens are shown.

def update():
    global items, currentlevel
    if len(items) == 0:
        items = makeitems(currentlevel)
#this function updates the level, and makes sure there are enough items in the level.
    
def makeitems(numberofextraitems):
    itemstocreate = getoptiontocreate(numberofextraitems)
    newitems = createitems(itemstocreate)
    layoutitems(newitems)
    animateitems(newitems)
    return(newitems)
#this function updates the amount of items to create, makes sure they are laid out correctly and animated to fall.

def getoptiontocreate(numberofextraitems):
    itemstocreate = ["paperbag.png"]
    for i in range(0, numberofextraitems):
        randomoption = random.choice(itemlist)
        itemstocreate.append(randomoption)
    return itemstocreate
#this sets the options of what itme to create, making sure the paper bag is in every level to ensure the possibility of winning.

def createitems(itemstocreate):
    newitems = []
    for i in itemstocreate:
        item = Actor(i)
        newitems.append(item)
    return newitems
#this adds the items to create, making sure there are enough items in each level.

def layoutitems(itemstolayout):
    numberofgaps = len(itemstolayout) + 1
    gapsize = WIDTH / numberofgaps
    random.shuffle(itemstolayout)
    for i, j in enumerate(itemstolayout):
        newx = (i + 1) * gapsize
        j.x = newx
#this makes the layout of the items even, so there is perfectly enough space between each level.

def on_mouse_down(pos):
    global items, currentlevel
    for i in items:
        if i.collidepoint(pos):
            if "paperbag" in i.image:
                handlegamecomplete()
            else:
                handlegameover()
#this tracks whether the mouse clicks on the paper bag, moving you to the next level if you do, and if not then displays the game over screen.

def handlegameover():
    global gameover
    gameover = True
#this handles the game over screen and stops the game if you click the wrong item.

def handlegamecomplete():
    global currentlevel, items, animations, gamecomplete
    stopanimations(animations)
    if currentlevel == finallevel:
        gamecomplete = True
    else:
        currentlevel += 1
        items = []
        animations = []
#this makes sure after the final level, that the game stops and displays the game won screen, and makes sure we move to the nect level if we aren't on the last on yet.

def animateitems(itemstoanimate):
    global animations
    for i in itemstoanimate:
        duration = startspeed - currentlevel
        i.anchor = ("center", "bottom")
        animation = animate(i, duration = duration, y = HEIGHT, on_finished = handlegameover)
        animations.append(animation)
#this animates items to make sure the fall and fallin the current speed and in the correct place.
    
def stopanimations(animationstostop):
    for i in animationstostop:
        if i.running:
            i.stop()
#this one stops the animations when they make it to the end of the game or when they click the paper bag.

pgzrun.go()