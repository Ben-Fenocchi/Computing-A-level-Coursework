#New in this version
#convert alpha after images to make it run smoother
#crytals to collect as a level objective
#end level screen-to be improved upon later 
import random
import pygame,sys
clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

pygame.display.set_caption("Platformer")

screenWidth = 1920
screenHeight = 1080

win = pygame.display.set_mode((screenWidth,screenHeight))

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

font1 = 'freesansbold.ttf'
healthbar = pygame.image.load("healthbar.png").convert_alpha()
crystalImage = pygame.image.load("crystal.png").convert_alpha()
dirt = pygame.image.load("dirtRectangle.png").convert_alpha()
grass = pygame.image.load("grassRectangle.png").convert_alpha()
cobble = pygame.image.load("cobbleRectangle.png").convert_alpha()
grassCobble = pygame.image.load("grassyCobbleRectangle.png").convert_alpha()
lavaSurface = pygame.image.load("lavaRectangleSurface.png").convert_alpha()
lava = pygame.image.load("lavaRectangle.png").convert_alpha()
splashScreenImg = pygame.image.load("splashScreen.png").convert_alpha()
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
coin1 = pygame.image.load("coin1.png").convert_alpha()
coin2 = pygame.image.load("coin2.png").convert_alpha()
coinImages = [coin1,coin2]
runningRight =[right1,right2,right3]
runningLeft =[left1,left2,left3]
playerImage = knightRight
playerHealth = 250
healthTimer = 0
playerMoney = 0
coinValue = 100

TILE_SIZEX = 64
TILE_SIZEY = 54

walkCycle= 0
climbingCycle = 0
coinCounter = 0
oneTime = True
oneTimeLevelConstructor = True


moving_right = False
moving_left = False
climbing = False
canClimb = False
player_y_vel = 0
air_timer = 0
isJump = False

player_rect = pygame.Rect(50, 50, 64, 64)#starting co-ords, players width and height
test_rect = pygame.Rect(100,100,100,50)
player_movement = [0,0]


highScores = False
levelSelect = False
game = False
menu = True                             
options = ["play","levelSelect","highScores"]         # variables for the splash screen
choice = 0                                             # Choice holds the mode they chose, level select,play ect
selected = False
lastFacing = "Right"# so when he isnt moving i can put the correct facing standing image- right or left
cantCollideList = [" ",".","l","h","c","m"]
damageBlocks = []#blocks that deal damage to the player
ladders = []
coins = []
totalCrystals = 0
crystalsGathered = 0
crystals = []

def endLevelScores(playerMoney):
    text1 = str(playerMoney)
    text = "Score is "
    text2 = text + text1
    draw_text(font1,text2,white,30,500,500)


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
    pygame.draw.rect(win,(255,(playerHealth),0),(100,55,playerHealth,60))#health bar will go more red as player gets lower health        
    win.blit(healthbar,(50,50))


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


level1 =  [ ['k',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','k'],#1
            ['k',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','k'],#2
            ['k',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','k'],#3
            ['k',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','k'],#4
            ['k',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','k'],#5
            ['k',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','m',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','k'],#6
            ['k',' ',' ',' ',' ',' ','h',' ','m',' ',' ','i','i',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','k'],#7 end procedure
            ['k',' ',' ',' ',' ',' ','h','i','i',' ',' ',' ','k',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','k'],#8
            ['k',' ',' ',' ',' ',' ','h',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','k'],#9
            ['k',' ',' ',' ','c',' ','h',' ',' ',' ',' ',' ',' ',' ',' ',' ','m',' ',' ',' ',' ',' ',' ',' ',' ','i',' ',' ',' ',' ',' ','k'],#10
            ['k',' ',' ',' ','w',' ','h',' ',' ',' ',' ','c','c',' ',' ','i','i','i',' ',' ',' ',' ',' ',' ',' ',' ',' ','i',' ',' ',' ','k'],#11
            ['k','w','w','w',' ',' ','h','i',' ',' ',' ','i','i','i','i','k','k',' ',' ',' ','i','i','i','i',' ',' ',' ',' ',' ',' ',' ','k'],#12
            ['k','s',' ',' ',' ','i','h','k','i','i',' ',' ',' ','k','k','k',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','i','i','k'],#13
            ['k','s','s','w','w',' ','h',' ','k','k',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','i','k',' ','k'],#14
            ['k',' ','s','s',' ',' ','h',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','i','k',' ',' ','k'],#15
            ['k',' ',' ',' ',' ',' ','h',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','i','i','i','k',' ',' ',' ','k'],#16
            ['k','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','k'],#17
            ['k','.','.','.','.','k','.','.','.','k','.','.','.','.','.','k','.','.','.','.','k','.','.','.','.','.','.','k','.','.','.','k'],#18
            ['k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','.','.','.','k','k','k','k','k','k','k','k','k','k','k','k','k'],#19
            ['k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k','k']]#20
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
        levels = [level1,level2,level3]
        win.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_p:
                    highScores = False
                    menu = True
                if choice < len(levels)-1:
                        choice +=1
                        print(choice)
                elif event.key ==K_UP:
                    if choice >0:
                        choice -=1
                        print(choice)
                elif event.key == K_RETURN: # when enter is pressed option is finalised
                    selected = True
                    menu = False 
                    print("Final level choice",choice)
                    game_map = levels[choice]
        pygame.display.update()

      
    while game:
        win.fill((0,0,0))
        tile_rects = []                                                                                        #                                   
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
                    ladders.append(pygame.Rect((x-1) * TILE_SIZEX, y * TILE_SIZEY, TILE_SIZEX, TILE_SIZEY))    #                                                                                                                               # 
                if tile not in cantCollideList :                                                               #                  
                    tile_rects.append(pygame.Rect((x-1) * TILE_SIZEX, y * TILE_SIZEY, TILE_SIZEX, TILE_SIZEY)) #                                                                                             
                x += 1
            y += 1
        oneTimeLevelConstructor = False # so it only adds certain blocks to the array once, so it doesnt have an infinitely filling up array

        player_movement = [0,0]
        if moving_right :                                             #
            if walkCycle>26:                                          #
                walkCycle = 0                                         #
            walkCycle +=1                                             #
            player_movement[0]=5                                      #moving right
            if isJump ==False:                                        #
                playerImage = runningRight[(walkCycle)//9-1]          #
            else:                                                     #
                playerImage = runningRight[1]                         #
            lastFacing = "right"
                                                               

        if moving_left :                                              #
            if walkCycle>26:                                          #
                walkCycle = 0                                         #
            walkCycle+=1                                              # moving left
            player_movement[0]-=5                                     #
            if isJump == False :                                      #
                playerImage = runningLeft[(walkCycle)//9-1]           #
            else:                                                     #
                playerImage = runningLeft[1]                          #    
            lastFacing = "left"                                       #
            
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
                
        if (not moving_left) and (not moving_right) and (not climbing) :        #
            if lastFacing=="left":                                              #
                playerImage = knightLeft                                        # standing still
            if lastFacing == "right":                                           #
                playerImage = knightRight                                       #

        
        player_movement[1] += player_y_vel                                         #
        if not climbing:                                                           #
            player_y_vel += 0.4                                                    #
        if player_y_vel > 10:                                                       #
            player_y_vel = 10                                                       # collisions,falling down, and moving the player
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
                if event.key == K_SPACE:                           #
                    isJump = True                                  #
                    if air_timer < 6:                              #
                        player_y_vel = -9                          #
                                                                   #
            if event.type == KEYUP:                                #
                if event.key == K_w:                               #
                    climbing = False                               #
                if event.key == K_d:                               #
                    moving_right = False                           #
                if event.key == K_a:                               #
                    moving_left = False                            #



      
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
               


        for crystal in crystals:                                                    #
            if player_rect.colliderect(crystal):                                    #colliding wiht crystals
                crystalsGathered +=1                                                #  
                crystals.pop(crystals.index(crystal))                               #
                game_map[(crystal[1]//TILE_SIZEY)][(crystal[0]//TILE_SIZEX +1)] = " "  # removes crsytal from the map


        drawHealthBar()
        if crystalsGathered ==  totalCrystals:
            game = False
            
        
        pygame.display.update() # update display
        clock.tick(60) # maintain 60 fps
    win.fill((0,0,0))    
    endLevelScores(playerMoney)
    pygame.display.update()
    pygame.time.wait(5000)
    menu = True
