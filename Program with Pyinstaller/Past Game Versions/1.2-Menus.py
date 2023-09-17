#new in this version:
#when standing still will have the standing still image, not wherever it was in the walk cycle
#one big while loop to encompass the new while loops, one for each menu option
#made it so that when in the air there is no running animation


import pygame,sys
clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

pygame.display.set_caption("Platformer")

screenWidth = 1920
screenHeight = 1080

win = pygame.display.set_mode((screenWidth,screenHeight))

dirt = pygame.image.load("dirtRectangle.png")
grass = pygame.image.load("grassRectangle.png")
cobble = pygame.image.load("cobbleRectangle.png")
grassCobble = pygame.image.load("grassyCobbleRectangle.png")
lavaSurface = pygame.image.load("lavaRectangleSurface.png")
lava = pygame.image.load("lavaRectangle.png")
splashScreenImg = pygame.image.load("splashScreen.png")
ladder = pygame.image.load("ladder.png")

knightRight = pygame.image.load("knightRight.png")
knightLeft = pygame.image.load("knightLeft.png")
right1 = pygame.image.load("runningRight1.png")
right2 = pygame.image.load("runningRight2.png")
right3 = pygame.image.load("runningRight3.png")
left1 = pygame.image.load("runningLeft1.png")
left2 = pygame.image.load("runningLeft2.png")
left3 = pygame.image.load("runningLeft3.png")
runningRight =[right1,right2,right3]
runningLeft =[left1,left2,left3]
playerImage = knightRight

TILE_SIZEX = 64
TILE_SIZEY = 54

walkCycle= 0

level1 =  [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],#1
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],#2
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],#3
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],#4
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],#5
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],#6
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],#7 end procedure
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],#8
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],#9
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','i',' ',' ',' ',' ',' '],#10
            [' ',' ',' ','w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','i','i','i',' ',' ',' ',' ',' ',' ',' ',' ',' ','i',' ',' ',' '],#11
            ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ','i','i','i','i','k','k',' ',' ',' ','i','i','i','i',' ',' ',' ',' ',' ',' ',' '],#12
            ['s',' ',' ',' ',' ','h','i','i','i',' ',' ',' ','k','k','k',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','i',' '],#13
            ['s','s','w','w',' ','h',' ','k','k',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','i','k',' '],#14
            [' ','s','s',' ',' ','h',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','i','k',' ',' '],#15
            [' ',' ',' ',' ',' ','h',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','i','i','i','k',' ',' ',' '],#16
            ['l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l','l'],#17
            ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],#18
            ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],#19
            ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']]#20











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

moving_right = False
moving_left = False

player_y_vel = 0
air_timer = 0
isJump = False

player_rect = pygame.Rect(50, 50, 64, 64)#starting co-ords, players width and height
test_rect = pygame.Rect(100,100,100,50)

game_map = level1
highScores = False
levelSelect = False
game = False
menu = True                                  #
options = ["play","levelSelect","highScores"]         # variables for the splash screen
choice = 0                                             # Choice holds the mode they chose, level select,play ect
selected = False
lastFacing = "Right"# so when he isnt moving i can put the correct facing standing image- right or left




run = True
while run:
##########################################################################
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
########################################################################
    while highScores:
        win.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_p:
                    highScores = False
                    menu = True
        pygame.display.update()

########################################################################        
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

########################################################################        
    while game:
        win.fill((0,0,0))
        tile_rects = []
        y =0
        for row in game_map:
            x = 0
            
            for tile in row:
                if tile == "w":
                    win.blit(grass, (x * TILE_SIZEX, y * TILE_SIZEY))
                if tile == "s":
                    win.blit(dirt, (x * TILE_SIZEX, y * TILE_SIZEY))
                if tile == "i":
                    win.blit(grassCobble, (x * TILE_SIZEX, y * TILE_SIZEY))
                if tile == "k":
                    win.blit(cobble, (x * TILE_SIZEX, y * TILE_SIZEY))
                if tile == "l":
                    win.blit(lavaSurface, (x * TILE_SIZEX, y * TILE_SIZEY))
                if tile == ".":
                    win.blit(lava, (x * TILE_SIZEX, y * TILE_SIZEY))
                if tile == "h":
                    win.blit(ladder, (x * TILE_SIZEX, y * TILE_SIZEY))                    
                if tile !=" " and tile !="h":# i dont want ladders to be on this
                    tile_rects.append(pygame.Rect(x * TILE_SIZEX, y * TILE_SIZEY, TILE_SIZEX, TILE_SIZEY))
                x += 1
            y += 1

        player_movement = [0,0]
        if moving_right :
            if walkCycle>26:
                walkCycle = 0
            walkCycle +=1
            player_movement[0]+=5
            if isJump ==False:
                playerImage = runningRight[(walkCycle)//9-1]
            else:
                playerImage = runningRight[1]
            lastfacing = "right"

        if moving_left :
            if walkCycle>26:
                walkCycle = 0
            walkCycle+=1
            player_movement[0]-=5
            if isJump == False:
                playerImage = runningLeft[(walkCycle)//9-1]
            else:
                playerImage = runningLeft[1]
            lastFacing = "left"

        if (not moving_left) and (not moving_right) :
            if lastFacing=="left":            
                playerImage = knightLeft    
            else:
                playerImage = knightRight






        player_movement[1] += player_y_vel
        player_y_vel += 0.4
        if player_y_vel > 7:
            player_y_vel = 7
       
        player_rect, collisions = move(player_rect, player_movement, tile_rects)

        if collisions["bottom"]:
            player_y_vel = 0
            air_timer = 0
            isJump = False
        else:
            air_timer += 1
      
            

        win.blit(playerImage, (player_rect.x, player_rect.y))


        for event in pygame.event.get(): # event loop
            if event.type == QUIT: # check for window quit
                pygame.quit() # stop pygame
                sys.exit() # stop script
            if event.type == KEYDOWN:
                if event.key == K_d:
                    moving_right = True
                if event.key == K_a:
                    moving_left = True
                if event.key == K_SPACE:
                    isJump = True
                    if air_timer < 6:
                        player_y_vel = -9
                    
            if event.type == KEYUP:
                if event.key == K_d:
                    moving_right = False
                if event.key == K_a:
                    moving_left = False
        
        pygame.display.update() # update display
        clock.tick(60) # maintain 60 fps
########################################################################

