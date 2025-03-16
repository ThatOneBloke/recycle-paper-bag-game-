import pgzrun
import random

WIDTH = 1000
HEIGHT = 800

currentlevel = 1

itemlist = ["battery.png", "crisps.png", "plasticbag.png", "plasticbottle.png"]
items = []

def draw():
    screen.clear()
    screen.blit("nature.png", (0, 0))
    for i in items:
        i.draw()

def update():
    global items
    global currentlevel
    if len(items) == 0:
        items = makeitems(currentlevel)
    
def makeitems(numberofextraitems):
    itemstocreate = getoptiontocreate(numberofextraitems)
    newitems = createitems(itemstocreate)
    layoutitems(newitems)
    #animateitems(newitems)
    return(newitems)

def getoptiontocreate(numberofextraitems):
    itemstocreate = ["paperbag.png"]
    for i in range(0, numberofextraitems):
        randomoption = random.choice(itemlist)
        itemstocreate.append(randomoption)
    return itemstocreate

def createitems(itemstocreate):
    newitems = []
    for i in itemstocreate:
        item = Actor(i)
        newitems.append(item)
    return newitems

def layoutitems(itemstolayout):
    numberofgaps = len(itemstolayout) + 1
    gapsize = WIDTH - numberofgaps
    random.shuffle(itemstolayout)
    for i, j in enumerate(itemstolayout):
        newx = (i + 1) * gapsize
        j.x = newx

def on_mouse_down(pos):
    global items, currentlevel
    for i in items:
        if i.collidepoint(pos):
            if "paperbag.png" in i.image:
                handlegamecomplete()
            else:
                gameover()
            
pgzrun.go()