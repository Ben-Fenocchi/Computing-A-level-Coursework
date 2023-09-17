#New in this version
#projectiles, the top of the projectiles arc will always go through where the mouse was clicked, might change this later as this is kinda an aimbot
#projectiles have a nice bomb image
#ammo counter at the top of the screen to display current ammo count for player
#In the making, ammo pickup drops
#enemy killed counter, coins collected counter
#changed the projectile motion system from earlier in this iteration, now clicking will produce a circle around the player, and when mouse released in the circle will
#draw a line representing the velocity vector for the projectile
#crytals gatehred counter
#made it so projectiles wont destroy ladders or lava or ammo crates or coins or crystals ect(projectile will be destroyed if it hits these tho(unless ladders))
import math 
import random
import pygame,sys
clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

pygame.display.set_caption("Cake Knight")

screenWidth = 1920
screenHeight = 1080

win = pygame.display.set_mode((screenWidth,screenHeight))

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
gold = (245,188,66)

font1 = 'freesansbold.ttf'
cakeEnemy = pygame.image.load("attackerEnemy.png").convert_alpha()
cakeEnemyHigh = pygame.image.load("attackerEnemyHigh.png").convert_alpha()
cakeEnemyMedium = pygame.image.load("attackerEnemyMedium.png").convert_alpha()
cakeEnemyLow = pygame.image.load("attackerEnemyLow.png").convert_alpha()
cakeAttackerImages = [cakeEnemy,cakeEnemyHigh,cakeEnemyMedium,cakeEnemyLow]
levelPreviewImageFiller =pygame.image.load("levelPreviewImageFiller.png").convert_alpha()
bombImage = pygame.image.load("bombImage.png").convert_alpha()
levelSelectBg = pygame.image.load("levelSelectBg.png").convert_alpha()  
healthbar = pygame.image.load("healthbar.png").convert_alpha()
ammoCounterImage = pygame.image.load("ammoCounter.png").convert_alpha()
timesSymbolImage = pygame.image.load("timesSymbol.png").convert_alpha()
slashSymbolImage = pygame.image.load("slashSymbol.png").convert_alpha()
image0 = pygame.image.load("image0.png").convert_alpha()
image1 = pygame.image.load("image1.png").convert_alpha()
image2 = pygame.image.load("image2.png").convert_alpha()
image3 = pygame.image.load("image3.png").convert_alpha()
image4 = pygame.image.load("image4.png").convert_alpha()
image5 = pygame.image.load("image5.png").convert_alpha()
numbers0to5 = [image0,image1,image2,image3,image4,image5]
crystalImage = pygame.image.load("crystal.png").convert_alpha()
dirt = pygame.image.load("dirtRectangle.png").convert_alpha()
grass = pygame.image.load("grassRectangle.png").convert_alpha()
cobble = pygame.image.load("cobbleRectangle.png").convert_alpha()
grassCobble = pygame.image.load("grassyCobbleRectangle.png").convert_alpha()
lavaSurface = pygame.image.load("lavaRectangleSurface.png").convert_alpha()
lava = pygame.image.load("lavaRectangle.png").convert_alpha()
ammoCrateImage = pygame.image.load("ammoCrate.png").convert_alpha()
outsideBg = pygame.image.load("outsideBg.png").convert_alpha()
splashScreenImg = pygame.image.load("splash screen v2.png").convert_alpha()
ladderImage = pygame.image.load("ladder.png").convert_alpha()
climbing1 = pygame.image.load("climbing1.png").convert_alpha()
climbing2 = pygame.image.load("climbing2.png").convert_alpha()
climbingImages = [climbing1,climbing2]
knightRight = pygame.image.load("knightRight.png").convert_alpha()
knightLeft = pygame.image.load("knightLeft.png").convert_alpha()
right1 = pygame.image.load("runningRight1.png").convert_alpha()
right2 = pygame.image.load("runningRight2.png").convert_alpha()
right3 = pygame.image.load("runningRight3.png").convert_alpha()
left1 = pygame.image.load("runningLeft1.png").convert_alpha()
left2 = pygame.image.load("runningLeft2.png").convert_alpha()
left3 = pygame.image.load("runningLeft3.png").convert_alpha()
crouchRight1 =pygame.image.load("crouchRight1.png").convert_alpha()
crouchLeft1 = pygame.image.load("crouchLeft1.png").convert_alpha()
crouchRight2 =pygame.image.load("crouchRight2.png").convert_alpha()
crouchLeft2 = pygame.image.load("crouchLeft2.png").convert_alpha()
crouchingRight =[crouchRight1,crouchRight2]
crouchingLeft =[crouchLeft1,crouchLeft2]
bigCoinImage = pygame.image.load("bigCoinImage.png").convert_alpha()
coin1 = pygame.image.load("coin1.png").convert_alpha()
coin2 = pygame.image.load("coin2.png").convert_alpha()
coinImages = [coin1,coin2]
runningRight =[right1,right2,right3]
runningLeft =[left1,left2,left3]
playerImage = knightRight
damageCounter = 0
playerHealth = 250
healthTimer = 0
playerMoney = 0
coinValue = 100
playerAmmo = 5
enemiesKilled = 0

TILE_SIZEX = 64
TILE_SIZEY = 54

crouchCycle = 0
walkCycle= 0
climbingCycle = 0
coinCounter = 0
shotsFiredCounter = 0
oneTime = True
oneTimeLevelConstructor = True
radiusAimCircle = 0
playerMaxAmmo = 5
aimDeltax = 0
aimDeltay = 0
aimLineLength = 0
aimCircleCenter = [0,0]
aimVectorDeltax = 0
aimVectorDeltay =  0
aimLineEndPoint = [0,0]


enemyCollided = ""
tileCollided = ""
isCollidedTile = False
isCollidedEnemy = False
crouching = False
moving_right = False
moving_left = False
climbing = False
canClimb = False
player_y_vel = 0
air_timer = 0
isJump = False
isPlayerAttacking = False
aiming = False
aimed = False

isPlayerHit= False
playerKnockbackCounter = 0
damagedSide = ""#so you know what side the player hits the neemy with
player_rect = pygame.Rect(50, 50, 64, 64)#starting co-ords, players width and height
test_rect = pygame.Rect(100,100,100,50)
player_movement = [0,0]
playerDealDamageCounter = 0
sword = pygame.Rect(-100,-100,50,7)
currentLevel = 1
highScores = False
levelSelect = False
game = False
menu = True                             
options = ["play","levelSelect","highScores"]         # variables for the splash screen
choice = 0                                             # Choice holds the mode they chose, level select,play ect
selected = False
lastFacing = "Right"# so when he isnt moving i can put the correct facing standing image- right or left
cantCollideList = [" ",".","l","h","c","m","e","a"]
damageBlocks = []#blocks that deal damage to the player
ladders = []
coins = []
enemies = []
projectiles = []
totalCrystals = 0
crystalsGathered = 0
crystals = []
ammoCrates = []

levelsAndNames=[
[1,"level1.txt"],
[2,"level2.txt"],
[3,"level3.txt"],
[4,"level4.txt"],
[5,"level5.txt"]
]

level1 = [" "]*20
level2 = [" "]*20
level3 = [" "]*20
level4 = [" "]*20
level5 = [" "]*20
for i in range(20):
    level1[i] = [" "]*32
for i in range(20):                 #sets up all the level arrays
    level2[i] = [" "]*32
for i in range(20):
    level3[i] = [" "]*32
for i in range(20):
    level4[i] = [" "]*32
for i in range(20):
    level5[i] = [" "]*32
levels = [level1,level2,level3,level4,level5]




def test():
    print("Test")
    
class Enemy():
    def __init__(self,x,y,width,height,health,damage,category,movementx=3,movementy=0,facing=1,counter=0):#default movement is 3 to the right
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.damage = damage
        self.category = category
        self.movementx = movementx
        self.movementy =  movementy
        self.facing = facing
        self.counter = counter
        self.totalHealth = health
    
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
    def draw(self):
        imageNumber = self.totalHealth/self.health
        remainder  = self.totalHealth % self.health
        if remainder !=0: 
            if remainder>=0.5:                               #rounds up
                imageNumber = int(round(imageNumber))
            else:                                            #rounds down
                imageNumber = int(imageNumber - remainder)
        else:
            imageNumber = int(imageNumber)
        if imageNumber >3:
            imageNumber = 4
        pygame.draw.rect(win,red,self.rect,-1)
        win.blit((cakeAttackerImages[imageNumber-1]),(self.rect[0],self.rect[1]))
    def move(self):
        self.rect, collisionsEnemy = move(self.rect, (self.movementx,self.movementy), tile_rects)#updates the enemy rect, retrieves a list of things it collides with
        if collisionsEnemy["bottom"]:
            self.movementy = 0
            self.counter = 0
        if  not (collisionsEnemy["bottom"]):  #if not standing on block after movement, undoes the movement and turns the enemy around
            self.counter +=1
            if self.counter ==3:
                self.rect[1]-= 1.2
                self.rect[0]-= self.movementx
                self.movementx = self.movementx*-1
            if self.movementx>0:
                self.facing = 1
            else:
                self.facing = -1
        if (collisionsEnemy["right"]) or (collisionsEnemy["left"]):#if hits something to the right turns around, no need to reverse movement, this for horizontals is done within move function
            self.movementx=self.movementx*-1
            self.facing = self.facing * -1
#################################################################################################################
class Projectile():
    def __init__(self,length,player_rect,damage,velx,vely,gravity=0.1,collisionTile = " ",collisionEnemy=" "):
        self.damage = damage
        self.collisionEnemy = collisionEnemy
        self.collisionTile = collisionTile
        self.length = length
        self.collided = False
        self.collidedEnemy = False
        self.collidedTile = False
        self.gravity = gravity
        self.x = player_rect[0] + (player_rect[2]//2)#sets starting co-ords of profectile to center of player
        self.y = player_rect[1] + (player_rect[3]//2)#


        self.velx = velx//25#divide by 50 otherwise too big
        self.vely = vely//25

        if abs(self.velx)<1:         #
            if self.velx>=0:         #   
                self.velx = 1        #stops the velocity from being too small
            else:                    #
                self.velx = -1       #  
        if abs(self.vely)<1:         #
            if self.vely>=0:         # 
                self.vely = 1        #  
            else:                    #
                self.vely = -1       #  
        
        
    def draw(self):
        self.rect = pygame.draw.rect(win,red,(self.x,self.y,self.length,self.length),1)
        win.blit(bombImage,(self.x,self.y))
    def move(self):
       
        self.x+= round(self.velx)
        self.y += round(self.vely)
        
        self.vely += self.gravity # the gravity on the projectile
        if self.vely>5:
            self.vely = 5
    def collisionCheck(self,tiles):
        for tile in tiles:
            if self.rect.colliderect(tile[0]):
                self.collidedTile = True
                self.collisionTile = tile
        for enemy in enemies:
            if self.rect.colliderect(enemy):
                self.collidedEnemy = True
                self.collisionEnemy = enemy
                
        return (self.collidedTile,self.collidedEnemy,self.collisionTile,self.collisionEnemy)

#################################################################################################################

def importLevel(levelNumber):
    levelToLoad = ""
    for i in range(len(levelsAndNames)):
        if levelsAndNames[i][0] == levelNumber:
            levelToLoad = levelsAndNames[i][1]
    file = open(levelToLoad,"r")
    x = 0
    for line in file:
        content = line.split(",")
        for i in range(len(content)-1):
            (levels[levelNumber-1])[x][i] = content[i]
        x +=1
    return(levels[levelNumber-1])


def canStand():
    global isCanStand
    isCanStand = True# holds boolean value representing if player can go off crouch or not
    hitList = []
    player_rect[3] = 64                #sets player to non crouch position
    player_rect[1] = player_rect[1]-14 # 
    playerTop = player_rect[1]
    playerBottom = player_rect[1]+ player_rect[3]
    tileBottom = 0# initialises the variable
    for tile in tile_rects:
        if player_rect.colliderect(tile):
            hitList.append(tile)
            
    for tile in hitList:                #if the player is touching any tile
        tileBottom = tile[1]+tile[3]
        if playerTop<=tileBottom:       # if the players head is above the bottom of the tile
            if playerBottom>tileBottom:# if the players bottom is below the bottom of the tile
                isCanStand = False   #then the player cant stand up
                
                player_rect[3]=54
                player_rect[1]= player_rect[1]+14
    return isCanStand

             


def resetValues():
    enemiesKilled = 0
    playerAmmo = playerMaxAmmo
    crystalsGathered = 0                                                    
    oneTimeLevelConstructor = True                                         
    moving_right = False                                                  
    moving_left = False                                                   
    climbing = False                                                      
    crystals=[]                                                           
    coins=[]                                                              
    totalCrystals = 0                                                     
    player_rect.x = 10                                                    
    player_rect.y = 10                                                    
    playerHealth = 250
    playerMoney = 0
    return(crystalsGathered,oneTimeLevelConstructor,moving_right,moving_left,climbing,crystals,coins,totalCrystals,player_rect.x,player_rect.y,playerHealth,playerMoney)
    
def endLevelScores(playerMoney):
    text1 = str(playerMoney)
    text = "Score is "
    text2 = text + text1
    draw_text(font1,text2,white,30,970,540)


def draw_text(font,text,text_colour,size,xcor,ycor):
    
    fonts = pygame.font.Font(font,size)
    text_surface = fonts.render(text,True,text_colour)
    text_rect = text_surface.get_rect()
    text_rect.center = (xcor,ycor)
    win.blit(text_surface,text_rect)

def displayMoneyValue():
    #draw_text(font1,"Cash:",red,40,(1500),(90))
    draw_text(font1,str(playerMoney),red,40,(1500),(150))

def drawHealthBar():
    pygame.draw.rect(win,(255,(playerHealth),0),(100,5,playerHealth,60))#health bar will go more red as player gets lower health        
    win.blit(healthbar,(50,0))
##########################################################################################################
def drawAmmoCounter(playerAmmo):
    win.blit(ammoCounterImage,(1500,0))
    win.blit(timesSymbolImage,(1560,0))
    win.blit((numbers0to5[playerAmmo]),(1620,0))

def displayMoneyCounter(playerMoney):
    win.blit(bigCoinImage,(1700,0))
    win.blit(timesSymbolImage,(1760,0))
    win.blit((numbers0to5[playerMoney//coinValue]),(1820,0))

def displayKillCounter(enemiesKilled):
    win.blit(cakeEnemy,(1300,7))
    win.blit(timesSymbolImage,(1360,0))
    win.blit((numbers0to5[enemiesKilled]),(1420,0))

def displayCrystalsGathered(totalCrystals,crystalsGathered):
    win.blit(crystalImage,(1040,0))
    win.blit(numbers0to5[totalCrystals],(1100,0))
    win.blit(slashSymbolImage,(1160,0))   
    win.blit(numbers0to5[crystalsGathered],(1220,0))
#############################################################################################################
def collision_test(rect,tiles):
    hit_list = []
    for tile in tiles:
      if rect.colliderect(tile):
         hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types


level1 = importLevel(1)
level2 = importLevel(2)
level3 = importLevel(3)
level4 = importLevel(4)
level5 = importLevel(5)

levels = [level1,level2,level3,level4,level5]
game_map = level1


run = True
while run:

    while menu:
        win.blit(splashScreenImg,(0,0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:#can press the arrow keys to move between options
                if event.key == K_DOWN:
                    if choice < len(options)-1:
                        choice +=1
                        print(options[choice])
                elif event.key ==K_UP:
                    if choice >0:
                        choice -=1
                        print(options[choice])
                elif event.key == K_RETURN: # when enter is pressed option is finalised
                    selected = True
                    menu = False 
                    print("Final choice",options[choice])
        LinePos1 =(100,(600+choice*200))
        LinePos2 =(700,(600+choice*200))
        pygame.draw.line(win,(255,215,0),(LinePos1),(LinePos2),10)#surface,colour,start,end,width

        pygame.display.update()

    if options[choice] == "play":        #
        game = True                      #
    elif options[choice]=="levelSelect": #sets the variables for each while loop
        levelSelect = True               #depending on what was picked in the
    elif options[choice] == "highScores":#splash screen menu
        highScores = True

    while highScores:
        win.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_p:
                    highScores = False
                    menu = True
        pygame.display.update()

       
    while levelSelect:
        pygame.mouse.set_visible(True)# makes the mouse visible
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)# sets cursor to a broken x
        mouse = pygame.mouse.get_pos()
        win.blit(levelSelectBg,(0,0))
        levelLocations = [[90,135],[738,135],[1398,135],[405,627],[1050,627]]#top left co-ords for each level select level
        for i in range(5):
            win.blit(levelPreviewImageFiller,(levelLocations[i]))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    levelSelect = False
                    menu = True
        if pygame.mouse.get_pressed()[0]:
            for i in range(len(levelLocations)):
                x = levelLocations[i][0]     # if you click on a certain level preview
                y = levelLocations[i][1]
                if mouse[0]>x and mouse[0]<(x + 474):
                    if mouse[1]>y and mouse[1]<(y+231):
                        game_map = levels[i]   # level is the level you clicked on
                        levelSelect = False
                        game = True             #starts the game
                        pygame.mouse.set_visible(False)
                        currentLevel = i+1
                        print(currentLevel)
        pygame.display.update()

      
    while game:
        pygame.mouse.set_visible(True)# makes the mouse visible
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)# sets cursor to a broken x
        mouse = pygame.mouse.get_pos()


        win.fill(black)
        #win.blit(outsideBg,(0,0))
        tile_rects = []                                                                                        #
        allBlocks = []
        y =0                                                                                                   #                                                                             
        for row in game_map:                                                                                   #                                        
            x = 0                                                                                              #                                                                                                                      #           
            for tile in row:                                                                                   #
                if tile == "w":                                                                                #
                    win.blit(grass, ((x-1) * TILE_SIZEX, y * TILE_SIZEY))                                      #
                if tile == "s":                                                                                #
                    win.blit(dirt, ((x-1) * TILE_SIZEX, y * TILE_SIZEY))                                       #
                if tile == "i":                                                                                #                   
                    win.blit(grassCobble, ((x-1) * TILE_SIZEX, y * TILE_SIZEY))                                #                                                              
                if tile == "k":                                                                                #                  
                    win.blit(cobble, ((x-1) * TILE_SIZEX, y * TILE_SIZEY))                                     #
                if tile == "c":
                    win.blit(crystalImage,((x-1)*TILE_SIZEX, y*TILE_SIZEY))
                    if oneTimeLevelConstructor:
                        crystals.append(pygame.Rect((x-1)*TILE_SIZEX, y*TILE_SIZEY, TILE_SIZEX, TILE_SIZEY))
                        totalCrystals +=1
                #############################################################################################################################
                if tile == "a":
                    win.blit(ammoCrateImage,((x-1)*TILE_SIZEX, y*TILE_SIZEY+4))#the plus for makes images align better
                    if oneTimeLevelConstructor:
                        ammoCrates.append(pygame.Rect((x-1)*TILE_SIZEX, y*TILE_SIZEY, TILE_SIZEX, TILE_SIZEY))
                #############################################################################################################################        
                if tile == "m" :                                                                               #
                    win.blit(coinImages[coinCounter//12-1],((x-1)*TILE_SIZEX, y*TILE_SIZEY))                   #
                    if oneTimeLevelConstructor:                                                                #
                        coins.append(pygame.Rect((x-1)*TILE_SIZEX, y*TILE_SIZEY, TILE_SIZEX, TILE_SIZEY))      #Drawing the game level                                                 
                if tile == "l":                                                                                #                  
                    win.blit(lavaSurface, ((x-1) * TILE_SIZEX, y * TILE_SIZEY))                                #
                    if oneTimeLevelConstructor:                                                                # 
                        damageBlocks.append(pygame.Rect((x-1) * TILE_SIZEX, y * TILE_SIZEY, TILE_SIZEX, TILE_SIZEY))#                                                                                                                                      #                                                       
                if tile == ".":                                                                                #                  
                    win.blit(lava, ((x-1) * TILE_SIZEX, y * TILE_SIZEY))                                       #                                
                    if oneTimeLevelConstructor:                                                                #
                        damageBlocks.append(pygame.Rect((x-1) * TILE_SIZEX, y * TILE_SIZEY, TILE_SIZEX, TILE_SIZEY))#                                   
                if tile == "h":                                                                                #                  
                    win.blit(ladderImage, ((x-1) * TILE_SIZEX, y * TILE_SIZEY))                                #
                    ladders.append(pygame.Rect((x-1) * TILE_SIZEX, y * TILE_SIZEY, TILE_SIZEX, TILE_SIZEY))    #
                if tile =="e":
                    if oneTimeLevelConstructor:
                        enemies.append(Enemy((x-1)*TILE_SIZEX, y*TILE_SIZEY,54,45,400,10,"attacker",2,0,1))
                        print(len(enemies),"enemy created")
                if tile !=" " and tile!="h":                                                                       #the list of blocks for the projectiles to be able to hit(dont want hitting air or ladders)
                    allBlocks.append([pygame.Rect((x-1) * TILE_SIZEX, y * TILE_SIZEY, TILE_SIZEX, TILE_SIZEY),tile])
                if tile not in cantCollideList :                                                               #                  
                    tile_rects.append(pygame.Rect((x-1) * TILE_SIZEX, y * TILE_SIZEY, TILE_SIZEX, TILE_SIZEY)) #                                                                                             
                x += 1
            y += 1
        oneTimeLevelConstructor = False # so it only adds certain blocks to the array once, so it doesnt have an infinitely filling up array
 
        for enemy in enemies:                                                          #
            enemy.draw()                                                               # 
            enemy.move()                                                               #
            if enemy.rect.colliderect(player_rect) and damageCounter == 0:             #  
                playerHealth -= 25                                                     #
                if player_rect[0]> enemy.rect[0]:                                      #  
                    damagedSide = 1                                                    #  
                else:                                                                  #
                    damagedSide = -1                                                   #
                isPlayerHit = True                                                     #
            enemy.movementy+=0.4                                                       #drawing and moving enemies, making enemies
            if enemy.movementy>10:                                                     #deal damage
                enemy.movementy=10                                                     #   
        damageCounter +=1                                                              #
        if damageCounter ==15:                                                         #
            damageCounter = 0                                                          #
        if playerHealth<0:                                                             #
            playerHealth = 0


        if isPlayerAttacking:                                                               #
            if lastFacing == 1:                                                             #
                sword[0] = player_rect[0]+ 64                                               #
            else:                                                                           #
                sword[0] = player_rect[0]-(32+sword[3])                                     #
            sword[1] = player_rect[1]+ 32                                                   #
                                                                                            #
            pygame.draw.rect(win,red,sword)                                                 #
        if not isPlayerAttacking:                                                           #
            sword[0] = -100                                                                 #attacking enemies, making them lose healh due to lava ect.
            sword[1] = -100                                                                 #
        for enemy in enemies:                                                               # 
            if sword.colliderect(enemy) and playerDealDamageCounter == 0:                   #
                enemy.health -= 50                                                          #
                enemy.rect[0]+=10*lastFacing                                                #
            for block in damageBlocks:                                                      #
                if block.colliderect(enemy):                                                #
                    enemy.health -=10                                                       #
            if enemy.health <=0:                                                            #
                enemies.pop(enemies.index(enemy))                                           #
                enemiesKilled += 1
        playerDealDamageCounter +=1                                                         #
        if playerDealDamageCounter >= 10:                                                   #
            playerDealDamageCounter = 0                                                     #

#########################################################################################################
        if pygame.mouse.get_pressed()[0] and playerAmmo>0:
            aiming = True
        if aiming:                                                                                                                                                    #
            aimCircleCenter = [(player_rect[0]+player_rect[2]//2),(player_rect[1]+player_rect[3]//2)]                                                                 #
            aimDeltax = mouse[0]-(player_rect[0]+player_rect[2]//2)                                                                                                   #
            aimDeltay = mouse[1]-(player_rect[1]+player_rect[3]//2)                                                                                                   #
            radiusAimCircle = ((aimDeltax)**2+(aimDeltay)**2)**0.5#radius of circle will be from center of player to mouse unless mouse is too far away               #                                                                                                                                           #
            aimLineLength = radiusAimCircle                                                                                                                           #
            if radiusAimCircle >250:                                                                                                                                  #
                radiusAimCircle = 250                                                                                                                                 #
            aimLineEndPoint = [(aimCircleCenter[0] + aimDeltax*(radiusAimCircle/aimLineLength)),(aimCircleCenter[1] + aimDeltay*(radiusAimCircle/aimLineLength))]     #
            pygame.draw.circle(win,red,(aimCircleCenter[0],aimCircleCenter[1]),radiusAimCircle,2)                                                                     # Drawing aim vectors and circle,
            pygame.draw.line(win,gold,(aimCircleCenter[0],aimCircleCenter[1]),(aimLineEndPoint[0],aimLineEndPoint[1]),3)                                              # finding values for each projectile vector
                                                                                                                                                                      #
                                                                                                                                                                      #
            pygame.draw.circle(win,gold,(aimLineEndPoint[0],aimLineEndPoint[1]),5)#next 4 shapes drawm are for aesthetics                                             # 
            pygame.draw.circle(win,green,(aimLineEndPoint[0],aimCircleCenter[1]),5)                                                                                   #
            pygame.draw.line(win,green,(aimCircleCenter[0],aimCircleCenter[1]),(aimLineEndPoint[0],aimCircleCenter[1]),3)                                             #
            pygame.draw.line(win,green,(aimLineEndPoint[0],aimCircleCenter[1]),(aimLineEndPoint[0],aimLineEndPoint[1]),3)                                             #
            if  not pygame.mouse.get_pressed()[0]:                                                                                                                    #
                aiming = False                                                                                                                                        #
                aimed = True                                                                                                                                          #
                aimVectorDeltax = aimLineEndPoint[0] - aimCircleCenter[0]                                                                                             #
                aimVectorDeltay = aimLineEndPoint[1] - aimCircleCenter[1]                                                                                             #
                    

        if  len(projectiles)<4 and shotsFiredCounter == 0 and playerAmmo>0 and aimed :                  #
            projectiles.append(Projectile(15,player_rect,99,aimVectorDeltax,aimVectorDeltay))           #
            playerAmmo-=1                                                                               #
            shotsFiredCounter += 1                                                                      # firing projecti;es
            aimed = False                                                                               #
                                                                                                        #
        shotsFiredCounter+=1                                                                            #  
        if shotsFiredCounter >7:                                                                        #
            shotsFiredCounter = 0                                                                       #  




        for projectile in projectiles:                                                                 #
            projectile.move()                                                                          #
            projectile.draw()                                                                          # making projectiles do damage
            isCollidedTile,isCollidedEnemy, tileCollided, enemyCollided = projectile.collisionCheck(allBlocks)# deleting projectiles when they hit things
            if isCollidedTile:                                                                         # making projectiles break blocks 
                if not(tileCollided[1] in cantCollideList):                                            #                     
                    game_map[(tileCollided[0][1]//TILE_SIZEY)][(tileCollided[0][0]//TILE_SIZEX +1)] = " "    # 
                                                                                                       #
            if isCollidedEnemy:                                                                        #
                enemyCollided.health -= projectile.damage                                              # 
            if isCollidedEnemy or isCollidedTile:                                                      #
                projectiles.pop(projectiles.index(projectile))                                         # must delete in the same place otherwise if bullet hits tile and enemy, will try to delete bullet twice otherwise
                                                                                                       #which is not possible  


#########################################################################################################



        if isPlayerHit:                                                                    # 
                                                                                           #
            player_y_vel = -9                                                              #
                                                                                           #  
            if playerKnockbackCounter <2:                                                  # making the player bounce back/take knockback when hit
                player_rect,collisions = move(player_rect,[(20*damagedSide),0],tile_rects) #   
                playerKnockbackCounter = 0                                                 #
                isPlayerHit = False                                                        #       
            playerKnockbackCounter +=1                                                     #

        player_movement = [0,0]

        if crouching:                                                                      #
            player_rect[3]=50                                                              #
            if lastFacing == 1:                                                            #
                playerImage = crouchRight1                                                 #
            else:                                                                          #
                playerImage = crouchLeft1                                                  #
            if crouchCycle>23:                                                             #
                crouchCycle = 0                                                            #
            crouchCycle +=1                                                                #
                                                                                           # crouching code
            if moving_right:                                                               #
                player_movement[0] = 2                                                     #
                playerImage = crouchingRight[(crouchCycle)//12-1]                          #
                lastFacing = 1                                                             #
            if moving_left:                                                                #
                player_movement[0] = -2                                                    #
                playerImage = crouchingLeft[(crouchCycle)//12-1]                           #
                lastFacing = -1                                                            #





        
        
        if moving_right and not crouching :                           #
            if walkCycle>26:                                          #
                walkCycle = 0                                         #
            walkCycle +=1                                             #
            player_movement[0]=5                                      #moving right
            if isJump ==False:                                        #
                playerImage = runningRight[(walkCycle)//9-1]          #
            else:                                                     #
                playerImage = runningRight[1]                         #
            lastFacing = 1
                                                               

        if moving_left and not crouching:                             #
            if walkCycle>26:                                          #
                walkCycle = 0                                         #
            walkCycle+=1                                              # moving left
            player_movement[0]-=5                                     #
            if isJump == False :                                      #
                playerImage = runningLeft[(walkCycle)//9-1]           #
            else:                                                     #
                playerImage = runningLeft[1]                          #    
            lastFacing = -1                                           #
            
        if climbing:                                                                                    #
            player_y_vel = 0                                                                            #
            moving_right = False                                                                        #
            moving_left = False                                                                         #
            canClimb = False                                                                            #
            for ladder in ladders:                                                                      # climbing
                    if player_rect.colliderect(ladder):#is the player touching ladders?                 #
                        canClimb = True                                                                 #
                        if oneTime:                                                                     #
                            player_rect[0]=ladder.x                                                     #
                            player_rect[1]=ladder.y#only resets the player co-ords once                 #
                            oneTime = False                                                             #
            if canClimb == False: #if player isnt next to ladders, climbing is false                    #
                climbing = False                                                                        #
                oneTime = True                                                                          #
                                                                                                        #
            else:                                                                                       #
                                                                                                        #
                if climbingCycle>23:#if the player can climb, then they climb                           #
                    climbingCycle = 0                                                                   #
                climbingCycle +=1                                                                       #
                playerImage = climbingImages[(climbingCycle)//12-1]                                     #
                player_rect[1]-=5                                                                       #
                
        if (not moving_left) and (not moving_right) and (not climbing) and (not crouching) :        #
            if lastFacing==-1:                                                                      #
                playerImage = knightLeft                                                            # standing still
            if lastFacing == 1:                                                                     #
                playerImage = knightRight                                                           #

        
        player_movement[1] += player_y_vel                                         #
        if not climbing:                                                           #
            player_y_vel += 0.4                                                    #
        if player_y_vel > 10:                                                      #
            player_y_vel = 10                                                      # collisions,falling down, and moving the player
        player_rect, collisions = move(player_rect, player_movement, tile_rects)   # also refreshing player image
        if collisions["bottom"]:                                                   #
            player_y_vel = 0                                                       #
            air_timer = 0                                                          #
            isJump = False                                                         #
        else:                                                                      #
            air_timer += 1                                                         #
        win.blit(playerImage, (player_rect.x,player_rect.y))                       #
       
        


        for event in pygame.event.get(): # event loop              #
            if event.type == QUIT: # check for window quit         #
                pygame.quit() # stop pygame                        #
                sys.exit() # stop script                           #
            if event.type == KEYDOWN:                              #
                if event.key == K_w:                               #
                    climbing = True                                # key binds
                if event.key == K_d:                               #
                    moving_right = True                            #
                if event.key == K_a:                               #
                    moving_left = True                             #
                if event.key == K_s:                               #
                    crouching = True                               #
                if event.key == K_SPACE:                           #
                    isJump = True                                  #
                    if air_timer < 6:                              #
                        player_y_vel = -9                          #
                if event.key == K_RETURN:                          #
                    isPlayerAttacking = True                       #
                if event.key == K_p:                               #
                    game = False                                   #
                                                                   #
                                                                   #
            if event.type == KEYUP:                                #
                if event.key == K_w:                               #
                    climbing = False                               #
                if event.key == K_d:                               #
                    moving_right = False                           #
                if event.key == K_a:                               #
                    moving_left = False                            #
                if event.key == K_s and canStand():                #
                    crouching = False                              #
                    isCanStand = True                              #
                    player_rect[3] = 64                            #
                if event.key == K_RETURN:                          #
                    isPlayerAttacking = False                      #



      
            for block in damageBlocks:                                    # 
                if player_rect.colliderect(block) and healthTimer == 0:   #
                    playerHealth -=10                                     #
                    healthTimer +=1                                       #Taking damage from blocks in the
                    if playerHealth<0:                                    #damage block list.
                        playerHealth = 0                                  #
            if healthTimer>0:                                             #
                healthTimer +=1                                           #
            if healthTimer>5:                                             #Health timer is so health doesnt go
                healthTimer = 0                                           #down too fast


        if coinCounter>23:                                                     # 
            coinCounter = 0                                                    #
        coinCounter+=1                                                         #
        for coin in coins:                                                     #Colliding with coins & displaying coin images
            if player_rect.colliderect(coin):                                  #               
                playerMoney += coinValue                                       #             
                coins.pop(coins.index(coin))                                   #
                game_map[(coin[1]//TILE_SIZEY)][(coin[0]//TILE_SIZEX +1)] = " "#removes coin image from the game map so wont be redrawn even if already taken by player
               


        for crystal in crystals:                                                       #
            if player_rect.colliderect(crystal):                                       #colliding with crystals
                crystalsGathered +=1                                                   #  
                crystals.pop(crystals.index(crystal))                                  #
                game_map[(crystal[1]//TILE_SIZEY)][(crystal[0]//TILE_SIZEX +1)] = " "  # removes crsytal from the map

#############################################################################################################################
        for ammoCrate in ammoCrates :                                                              #
            if player_rect.colliderect(ammoCrate) and playerAmmo<playerMaxAmmo:                    #collecting ammo from crates
                playerAmmo = playerMaxAmmo                                                         #          
                ammoCrates.pop(ammoCrates.index(ammoCrate))                                        #
                game_map[(ammoCrate[1]//TILE_SIZEY)][(ammoCrate[0]//TILE_SIZEX +1)] = " "          #


#############################################################################################################################



        drawHealthBar()
        drawAmmoCounter(playerAmmo)
        displayMoneyCounter(playerMoney)
        displayKillCounter(enemiesKilled)
        displayCrystalsGathered(crystalsGathered,totalCrystals)
        if crystalsGathered ==  totalCrystals:
            win.fill((0,0,0))                                                         #
            endLevelScores(playerMoney)                                               #
            pygame.display.update()                                                   #
            pygame.time.wait(1000)                                                    #
            win.fill((0,0,0))                                                         #
            draw_text(font1,("level"+(str(currentLevel+1))),red,40,(970),(540))       #
            pygame.display.update()                                                   #
            pygame.time.wait(1000)                                                    #
            currentLevel +=1                                                          #
            game_map = levels[currentLevel-1]                                         #
            enemies = []                                                              #
            crystalsGathered = 0                                                      #
            oneTimeLevelConstructor = True                                            #
            moving_right = False                                                      #Reseting values,dsiplaying score, moving onto next level
            moving_left = False                                                       #
            climbing = False                                                          #
            crystals=[]                                                               #
            coins=[]                                                                  #
            totalCrystals = 0                                                         #
            player_rect.x = 10                                                        #
            player_rect.y = 10                                                        #
            playerHealth = 250                                                        #
            playerMoney = 0                                                           #
            playerAmmo = playerMaxAmmo
            enemiesKilled = 0
        pygame.display.update() # update display
        clock.tick(60) # maintain 60 fps


                                                        
    crystalsGathered,oneTimeLevelConstructor,moving_right,moving_left,climbing,crystals,coins,totalCrystals,player_rect.x,player_rect.y,playerHealth,playerMoney = resetValues()
    currentLevel = 1
    enemies = []
    level1 = importLevel(1)
    level2 = importLevel(2) #resets all the levels so they can be replayed
    level3 = importLevel(3)
    level4 = importLevel(4)
    level5 = importLevel(5)
    game_map = level1
    
    menu = True
    
