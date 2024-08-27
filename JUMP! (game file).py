#This game was written by Sebastian Landry from May 8th 2020 to June 12th
#Game: JUMP!

import pygame, os, random, time
from pygame.locals import *

# setting up the window
WINDOWWIDTH = 800
WINDOWHEIGHT = 870

SIZE = 30   #The players size

#The level completion file
FILE = "CompletedLevels.txt"

# frame rate
FRAMERATE = 60

# ALL colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN  = (20, 255, 140)
GREY   = (210, 210 ,210)
RED    = (255, 0, 0)
PURPLE = (255, 0, 255)
BLACK  = (0,0,0)


def display_text(windowSurface, word, pos, colour, textSize):
    """ Displays text onto the screen """
    # set up fonts
    basicFont = pygame.font.SysFont('impact', textSize)

    # set up the text
    text = basicFont.render(word, True, colour)
    textRect = text.get_rect()

    # draw the text onto the surface
    windowSurface.blit(text, pos)


def start(windowSurface):
    """ draw the background onto the surface and display difficulty options """
    
    #drawing the background
    img = load_image('MainScreen.JPG')
    windowSurface.blit(img, [0,0])

    #loading the options
    word = 'Difficulties:'
    pos = (90, 80, 50 ,50)
    colour = BLACK
    textSize = 70
    display_text(windowSurface, word, pos, colour, textSize)
    
    word = '  1. Easy'
    pos = (160, 160, 50 ,50)
    colour = BLACK
    textSize = 60
    display_text(windowSurface, word, pos, colour, textSize)
    
    word = '  2. Medium'
    pos = (160, 220, 50 ,50)
    colour = BLACK
    display_text(windowSurface, word, pos, colour, textSize)
    
    word = '  3. Hard'
    pos = (160, 280, 50 ,50)
    colour = BLACK
    display_text(windowSurface, word, pos, colour, textSize)
    
    word = ' - '
    pos = (60, 185, 50 ,50)
    colour = BLACK
    textSize = 300
    display_text(windowSurface, word, pos, colour, textSize)
    word = ' Options: '
    pos = (130, 420, 50 ,50)
    textSize = 70
    colour = BLACK
    display_text(windowSurface, word, pos, colour, textSize)
    
    word = '  4. Characters'
    pos = (200, 490, 50 ,50)
    colour = BLACK
    display_text(windowSurface, word, pos, colour, textSize)

    word = '  5. How To Play'
    pos = (200, 550, 50 ,50)
    colour = BLACK
    display_text(windowSurface, word, pos, colour, textSize)
    
    #if the user has already completed a level a star will appear beside the level
    level_list = CreateList()   #list of completed levels
    img = load_image('star.png')    #loading the star image
    if 1 in level_list:
        x = 120
        y = 160
        windowSurface.blit(img, (x, y)) # displaying a star
    if 2 in level_list:
        x = 120
        y = 220
        windowSurface.blit(img, (x, y)) # displaying a star
    if 3 in level_list:
        x = 120
        y = 280
        windowSurface.blit(img, (x, y)) # displaying a star
    
    # draw the window onto the screen
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(1)
            elif event.type == KEYDOWN: 
                if event.key == ord('1'):
                    return(1)
                if event.key == ord('2'):
                    return(2)
                if event.key == ord('3'):
                    return(3)
                if event.key == ord('4'):
                    return(4)
                if event.key == ord('5'):
                    return(5)


def character_screen(windowSurface):
    """ Displays a list of characters the user can choose from """
    #drawing the background
    img = load_image('MainScreen.JPG')
    windowSurface.blit(img, [0,0])
    
    #loading the character options
    word = 'Characters:'
    pos = (90, 80, 50 ,50)
    colour = BLACK
    textSize = 70
    display_text(windowSurface, word, pos, colour, textSize)
    
    word = '1.'
    pos = (120, 150, 50 ,50)
    colour = BLACK
    textSize = 60
    display_text(windowSurface, word, pos, colour, textSize)
    
    word = '2.'
    pos = (120, 265, 50 ,50)
    colour = BLACK
    display_text(windowSurface, word, pos, colour, textSize)
    
    word = '3.'
    pos = (120, 380, 50 ,50)
    colour = BLACK
    display_text(windowSurface, word, pos, colour, textSize)
    
    #characters
    x = 160
    y = 150
    windowSurface.blit(load_image('Yellow (character).png'), (x, y)) # displaying character 1
    x = 160
    y = 265
    windowSurface.blit(load_image('Green (character).png'), (x, y)) # displaying character 2
    x = 160
    y = 380
    windowSurface.blit(load_image('Alien (character).png'), (x, y)) # displaying character 3
    # draw the window onto the screen
    pygame.display.update()
    #choosing a character
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(1)
            elif event.type == KEYDOWN: 
                if event.key == ord('1'):
                    return(1)
                if event.key == ord('2'):
                    return(2)
                if event.key == ord('3'):
                    return(3)


def info(windowSurface):
    """ Displays information on how to play the game """
    #drawing the background
    img = load_image('MainScreen.JPG')
    windowSurface.blit(img, [0,0])
    
    word = 'How To Play:'
    pos = (90, 80, 50 ,50)
    colour = BLACK
    textSize = 70
    display_text(windowSurface, word, pos, colour, textSize)
    word = "The object of the game is to reach the star all while avoiding"  
    pos = (10, 170, 50 ,50)
    colour = BLACK
    textSize = 30
    display_text(windowSurface, word, pos, colour, textSize)
    word = "enemies and falling off the map. 'JUMP!' from block to block to"
    pos = (10, 210, 50 ,50)
    colour = BLACK
    textSize = 30
    display_text(windowSurface, word, pos, colour, textSize)
    word = "get to the top of the map and obtain the star to win. You can"
    pos = (10, 250, 50 ,50)
    colour = BLACK
    textSize = 30
    display_text(windowSurface, word, pos, colour, textSize)
    word = "use the arrow keys, WASD to move and even use the space bar"
    pos = (10, 290, 50 ,50)
    colour = BLACK
    textSize = 30
    display_text(windowSurface, word, pos, colour, textSize)
    word = " to 'JUMP!'. Click backspace to go to the main screen and"
    pos = (10, 330, 50 ,50)
    colour = BLACK
    textSize = 30
    display_text(windowSurface, word, pos, colour, textSize)
    word = "remember to choose your character whenever returning to the"
    pos = (10, 370, 50 ,50)
    colour = BLACK
    textSize = 30
    display_text(windowSurface, word, pos, colour, textSize)
    word = "main screen."
    pos = (10, 410, 50 ,50)
    colour = BLACK
    textSize = 30
    display_text(windowSurface, word, pos, colour, textSize)
    word = "PS: Dont stand still for too long, you will fall!"
    pos = (10, 510, 50 ,50)
    colour = BLACK
    textSize = 30
    display_text(windowSurface, word, pos, colour, textSize)
    # draw the window onto the screen
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(1)
            elif event.type == KEYDOWN: 
                if event.key == K_BACKSPACE:
                    main()


def terminate():
    """ This function is called when the user closes the window or presses ESC """
    pygame.quit()
    os._exit(1)


def load_image(filename):
    """ Load an image from a file.  Return the image and corresponding rectangle """
    image = pygame.image.load(filename) #loads the image
    image = image.convert_alpha()   #works with transparent backgrounds
    return image


def CreateList():
    """Creates a list out of the completion files information"""
    open_file= open(FILE,"r") #opens the file
    entire_list = open_file.readlines() #a list of data in a file
    for x in range(len(entire_list)):
        entire_list[x] = int(entire_list[x].strip())
    open_file.close() #closes the file
    return entire_list



#CLASSES:
class Game():
    def __init__(self, speed, character):

        #setting up the level the player chose
        self.level = 0

        #setting up level images
        self.img1 = load_image("Easy level.jpeg")
            
        self.img2 = load_image("Medium level.png")
            
        self.img3 = load_image("Hard level.jpg")

        #setting up if the player wins or not
        self.win = False

        #Set to True when the player falls off the screen
        self.game_over = False

            
        # set up the player and blocks for the level
        self.all_sprites = pygame.sprite.Group()
        #Platform list
        self.platforms = pygame.sprite.Group()
        #Trampoline list
        self.trampolines = pygame.sprite.Group()
        #Star list
        self.stars = pygame.sprite.Group()
        #Enemy list
        self.enemies = pygame.sprite.Group()

    
        #Instantiate the player in the centre of the window
            #choosing the character
        char_img = 'Yellow (character).png'
        if character == 2:
            char_img = 'Green (character).png'
        elif character == 3:
            char_img = 'Alien (character).png'
        PlayerImage = pygame.image.load(char_img)
        PlayerStretchedImage = pygame.transform.scale(PlayerImage, (SIZE, SIZE))
        self.player = Player(PlayerImage)
        self.all_sprites.add(self.player)

        # set up sounds and music
        pygame.mixer.music.load('Game Music3.mp3')
        self.gameOverSound = pygame.mixer.Sound('gameover.wav')
        self.winSound = pygame.mixer.Sound('winSound.wav')

        # Play the background music
        pygame.mixer.music.play(-1, 0.0)
        self.musicPlaying = True

        
    def display_frame(self, windowSurface):
        """ Display everything to the screen for the game. """
        if self.level == 1:
            windowSurface.blit(self.img1, [0,0])

        elif self.level == 2:
            windowSurface.blit(self.img2, [0,0])

        elif self.level == 3:
            windowSurface.blit(self.img3, [0,-300])
        
        if self.game_over and not self.win:              #checks to see if the user died
            word = "Game Over"
            x = WINDOWWIDTH // 2 - 120
            y = WINDOWHEIGHT // 2 - 20
            pos = (x, y)
            colour = RED
            textSize = 60
            display_text(windowSurface, word, pos, colour, textSize)
            word = "(Click To Restart)"
            x = WINDOWWIDTH // 2 - 120
            y = WINDOWHEIGHT // 2 + 60
            pos = (x, y)
            colour = RED
            textSize = 40
            display_text(windowSurface, word, pos, colour, textSize)

        if self.win: #checks to see if the player won
            word = "You Won!"
            x = WINDOWWIDTH // 2 - 120
            y = WINDOWHEIGHT // 2
            pos = (x, y)
            colour = GREEN
            textSize = 60
            display_text(windowSurface, word, pos, colour, textSize)
            word = "(Click To Restart)"
            x = WINDOWWIDTH // 2 - 135
            y = WINDOWHEIGHT // 2 + 60
            pos = (x, y)
            colour = GREEN
            textSize = 40
            display_text(windowSurface, word, pos, colour, textSize)

            #adding the completed level to a file to indicate the user has already beaten that level
            add = self.level #the number the of the level that would be add to the file after level completion
            entire_list = CreateList()

            #open in write mode
            open_file= open(FILE,"w")
            #Checking where the number should be inputed
            if add < int(entire_list[0]):
                open_file.write(str(add)+"\n")
             
            for x in range(len(entire_list)):
                if add <int(entire_list[x]) and add >int(entire_list[x-1]):
                    open_file.write(str(add)+"\n")
                open_file.write(str(entire_list[x])+"\n")
            
            #if the level the user beat is greater than the last number added to the file it will be added at the end of the file
            if add > int(entire_list[len(entire_list)-1]):
                open_file.write(str(add)+"\n")
            open_file.close()
 

        else:
            # draw the player onto the surface
            self.all_sprites.draw(windowSurface)

        # draw the window onto the screen
        pygame.display.update()
            

    def process_events(self, windowSurface, speed):
        """ Process all of the keyboard and mouse events.  """

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    self.player.moveRight = False
                    self.player.moveLeft = True
                elif event.key == K_RIGHT or event.key == ord('d'):
                    self.player.moveLeft = False
                    self.player.moveRight = True
                elif event.key == K_UP or event.key == ord('w') or event.key == K_SPACE:
                    self.player.moveUp = True
                    self.jump()

                #go back to the main menu
                if event.key == K_BACKSPACE:
                    main()


            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_LEFT or event.key == ord('a'):
                    self.player.moveLeft = False
                elif event.key == K_RIGHT or event.key == ord('d'):
                    self.player.moveRight = False
                elif event.key == K_UP or event.key == ord('w') or event.key == K_SPACE:
                    self.player.moveUp = False

                
                elif event.key == ord('m'):
                   # toggles the background music
                    if self.musicPlaying:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                    self.musicPlaying = not self.musicPlaying
            

            elif event.type == pygame.MOUSEBUTTONDOWN:
                #The user clicks to restart the level when it is over
                if self.game_over or self.win:
                    #Restart the game screen
                    main()
                    
                    


    def run_logic(self, speed):
        """ This method is run each time through the frame. It
        updates positions and checks if the player falls. """
        if not self.game_over:
        
            self.player.gravity() # check gravity
           
            # update the player's position
            self.player.update(speed)

            # check if the player has intersected with any platforms and adjust them if they have
            platform_hit_list = pygame.sprite.spritecollide(self.player, self.platforms, False)
            for platform in platform_hit_list:
                if self.player.change_y > 0:
                    self.player.rect.bottom = platform.rect.top
                elif self.player.change_y < 0:
                    self.player.rect.top = platform.rect.bottom

            # check if the player collided with a trampoline and bounce the player if so
            trampoline_hit_list = pygame.sprite.spritecollide(self.player, self.trampolines, False)
            for trampoline in trampoline_hit_list:
                #if the player is going down the player will bounce
                if self.player.change_y > 0:
                    self.jump()
                #if the player is moving up the player will move to the bottom of the trampoline
                elif self.player.change_y < 0: #the player will not bounce if they are hitting the trampoline with their head
                    self.player.rect.top = trampoline.rect.bottom
                
            #check to see if the player won by colliding with a star
            star_hit_list = pygame.sprite.spritecollide(self.player, self.stars, True)
            if len(star_hit_list) > 0:
                print("won")
                self.win = True
                self.winSound.play() 

            #check to see if the player lost by colliding with an enemy
            enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemies, False)
            if len(enemy_hit_list) > 0:
                self.game_over = True

            if self.player.rect.bottom > WINDOWHEIGHT:
                print("lost")
                self.game_over = True              
                self.gameOverSound.play()



    def makePlatform(self, x, y, img):
        """ Reduces repetitive code. Makes a platform """
        platform = Platform(x, y, img) # creating level platform
        self.all_sprites.add(platform)  #adding the platform so it can be added to the screen
        self.platforms.add(platform) #adding the platform to a group of platforms


    def makeTrampoline(self, x, y):
        """ Creates a trampoline """
        trampoline = Platform(x, y, 'Trampoline.png') # creating level trampoline
        self.all_sprites.add(trampoline)  #adding the trampoline so it can be added to the screen
        self.trampolines.add(trampoline) #adding the trampoline to a group of trampolines

    def makeStar(self, x, y):
        """ Creates a star. When the player collides with this they win """
        star = Platform(x, y, 'star.png') # creating level star
        self.all_sprites.add(star)  #adding the star so it can be added to the screen
        self.stars.add(star) #adding the star to a group of stars
        
    def makeEnemy(self, x, y):
        """ Creates a enemy. If the player bumps into it they will lose """
        enemy = Platform(x, y, 'Enemy.png') # creating level star
        self.all_sprites.add(enemy)  #adding the star so it can be added to the screen
        self.enemies.add(enemy) #adding the star to a group of stars
        

    def jump(self):
        """ Controls the players jumping mechanics """
        self.player.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self.player, self.platforms, False)
        trampoline_hit_list = pygame.sprite.spritecollide(self.player, self.trampolines, False)
        self.player.rect.y -= 2

        if len(platform_hit_list) > 0:
            self.player.change_y = -7

        elif len(trampoline_hit_list) > 0:
            self.player.change_y = -12.5

            

class Player(pygame.sprite.Sprite):
    def __init__(self, PlayerImage):  
        pygame.sprite.Sprite.__init__(self)
        self.image = PlayerImage
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 800

        # set up movement variables
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

        #setting up changes in movement for gravity and jumping
        self.change_y = 0

        
    def update(self, speed):
        """ This function updates the players position """
        self.rect.y += self.change_y
        if self.moveLeft and self.rect.left > 0:
            self.rect.left -= speed
        elif self.moveRight and self.rect.right < WINDOWWIDTH:
            self.rect.right += speed


    def gravity(self):
        """ This function controls the players gravity """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
            


class Platform(pygame.sprite.Sprite):
    """ Creates a platform """
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(img)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        


#LEVELS -------------------------
def levelOne(speed, windowSurface, character):
    """ Loads the first level of the game """
    game = Game(speed, character) #setting up the game

    game.level = 1
    
    #loading platforms for level 1
    img = 'EasyPlatform.png' #platform image
    x = 0
    y = 850
    game.makePlatform(x, y, img)
    x = 300
    y = 830
    game.makePlatform(x, y, img)
    x = 500
    y = 600
    game.makePlatform(x, y, img)
    x = 320
    y = 550
    game.makePlatform(x, y, img)
    x = 225
    y = 290
    game.makePlatform(x, y, img)
    x = 500
    y = 240
    game.makePlatform(x, y, img)
    x = 600
    y = 230
    game.makePlatform(x, y, img)
    x = 700
    y = 220
    game.makePlatform(x, y, img)

    #loading trampolines for level 1
    x = 630
    y = 810
    game.makeTrampoline(x, y)
    x = 0
    y = 500
    game.makeTrampoline(x, y)

    #making a star (win if collided with)
    x = 740
    y = 150
    game.makeStar(x, y)

    return(game)


def levelTwo(speed, windowSurface, character):
    """ Loads the first level of the game """
    game = Game(speed, character) #setting up the game

    game.level = 2

    #loading platforms for level 2
    img = 'MediumPlatform.jpg' #platform image
    x = 0
    y = 850
    game.makePlatform(x, y, img)
    x = 300
    y = 800
    game.makePlatform(x, y, img)
    x = 580
    y = 600
    game.makePlatform(x, y, img)
    x = 400
    y = 350
    game.makePlatform(x, y, img)
    x = 200
    y = 500
    game.makePlatform(x, y, img)
    x = 150
    y = 175
    game.makePlatform(x, y, img)
    x = 370
    y = 125
    game.makePlatform(x, y, img)
    x = 470
    y = 125
    game.makePlatform(x, y, img)
    x = 570
    y = 125
    game.makePlatform(x, y, img)
    x = 670
    y = 125
    game.makePlatform(x, y, img)


    #loading trampolines for level 2
    x = 500
    y = 750
    game.makeTrampoline(x, y)
    x = 625
    y = 570
    game.makeTrampoline(x, y)
    x = 0
    y = 460
    game.makeTrampoline(x, y)

    #making enemies for level 2
    x = 580
    y = 570
    game.makeEnemy(x, y)
    x = 320
    y = 460
    game.makeEnemy(x, y)

    #making a star (win if collided with)
    x = 740
    y = 60
    game.makeStar(x, y)

    return(game)


def levelThree(speed, windowSurface, character):
    """ Loads the first level of the game """
    game = Game(speed-1, character) #setting up the game

    game.level = 3

    #loading platforms and trampolines for level 3
    img = 'HardPlatform.png' #platform image
    x = 0
    y = 800
    game.makePlatform(x, y, img)
    img = 'HardPlatform2.png' #platform image 2
    x = 80
    y = 600
    game.makePlatform(x, y, img)
    x = 350
    y = 530
    game.makePlatform(x, y, img)
    x = 430
    y = 800
    game.makePlatform(x, y, img)
    x = 420
    y = 200
    game.makePlatform(x, y, img)

    #loading trampolines for level 3
    x = 100
    y = 799
    game.makeTrampoline(x, y)
    x = -60
    y = 550
    game.makeTrampoline(x, y)
    x = 540
    y = 270
    game.makeTrampoline(x, y)
    x = 700
    y = 750
    game.makeTrampoline(x, y)
    x = 540
    y = 510
    game.makeTrampoline(x, y)
    x = 100
    y = 300
    game.makeTrampoline(x, y)

    #making enemies for level 3
    x = 85
    y = 565
    game.makeEnemy(x, y)
    x = 150
    y = 780
    game.makeEnemy(x, y)
    x = 320
    y = 540
    game.makeEnemy(x, y)
    x = 400
    y = 570
    game.makeEnemy(x, y)
    x = 400
    y = 780
    game.makeEnemy(x, y)
    x = 550
    y = 450
    game.makeEnemy(x, y)
    x = 20
    y = 200
    game.makeEnemy(x, y)
    x = 0
    y = 160
    game.makeEnemy(x, y)
    x = 0
    y = 120
    game.makeEnemy(x, y)
    x = 200
    y = 0
    game.makeEnemy(x, y)
    x = 235
    y = 20
    game.makeEnemy(x, y)

    #making a star (win if collided with)
    x = 0
    y = 0
    game.makeStar(x, y)

    return(game)


#----------------------------

    
def main():
    """ Mainline for the program """
    #setting up pygame
    pygame.init()

    mainClock = pygame.time.Clock()

    #Setting up the window
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('JUMP!')

    
    user_in = start(windowSurface)

    character = 1 #the default character is character 1
    #if the user chooses option 4 to pick a character
    while user_in == 4:
        character = character_screen(windowSurface)
        user_in = start(windowSurface)
        
    speed = 6
    if user_in == 1:
        game = levelOne(speed, windowSurface, character)
    elif user_in == 2:
        game = levelTwo(speed, windowSurface, character)
    elif user_in == 3:
        game = levelThree(speed, windowSurface, character)
    elif user_in == 5:
        info(windowSurface)

    while True:
        # Draw the current frame
        game.display_frame(windowSurface)
        
        # Process events (keystrokes, mouse clicks, etc)
        game.process_events(windowSurface, speed)

        # Update object positions, check for collisions
        game.run_logic(speed)

        
        mainClock.tick(FRAMERATE)

main()
