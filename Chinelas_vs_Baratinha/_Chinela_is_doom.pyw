import pygame
import time
import random
 
pygame.init()
 
display_width = 800
display_height = 600
pygame.mixer.music.load('loopsong.mp3') # Loyalty Freak Music: It feels good to be alive too
#Free, encontrado em http://freemusicarchive.org/genre/Electro-punk/
black = (0,0,0)
white = (255,255,255)
red = (150,0,0)
green = (0,150,0)
bright_green = (0,255,0)
bright_red = (255,0,0)
block_color = (255,255,255)
quitgame = pygame.QUIT
baratinha_width = 25
fundoImg = pygame.image.load('piso.jpg')
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Chinela's is doom")
clock = pygame.time.Clock()
chinela = pygame.image.load('chinelo.png') 
baratinhaImg = pygame.image.load('baratinha.png')
rect = None
 
def chinelos_dodged(count):
    font = pygame.font.SysFont(None, 45)
    text = font.render("Esquivou: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))
 
def chinelos(chinelox, chineloy, chinelow, chineloh, color):
    s = pygame.Surface((1000,750))  # the size of your rect
    s.set_alpha(50)                # alpha level
    s.fill((0,0,0))           # this fills the entire surface
    gameDisplay.blit(s, (0,0))
    pygame.draw.rect(s, color, [chinelox, chineloy, chinelow, chineloh])
    rect = chinela.get_rect()
    rect = rect.move((chinelox, chineloy))
    gameDisplay.blit(chinela, rect)
 
def baratinha(x,y):
    gameDisplay.blit(baratinhaImg,(x,y))
 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def message_display(text):
    largeText = pygame.font.SysFont('chiller',200)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 
    game_loop()
        
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("freesansbold",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
def crash():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('crash.mp3') #Punch or Whack Sound - Public Domain
    #Free, encontrado em http://soundbible.com/1952-Punch-Or-Whack.html
    pygame.mixer.music.play()
    s = pygame.Surface((1000,750))  # the size of your rect
    s.set_alpha(10)                # alpha level
    s.fill((0,0,0))           # this fills the entire surface
    gameDisplay.blit(s, (0,0))
    message_display('You died')
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("chiller",120)
        TextSurf, TextRect = text_objects("Chinela's doom", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Jogar!",150,450,100,50,green,bright_green,game_loop)
        button("Sair.",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('loopsong.mp3') # Loyalty Freak Music: It feels good to be alive too
    #Free, encontrado em http://freemusicarchive.org/genre/Electro-punk/
    pygame.mixer.music.play(-1)
    x = (display_width * 0.45)
    y = (display_height * 0.8)
 
    x_change = 0
 
    chinelo_inix = random.randrange(0, display_width)
    chinelo_iniy = -650
    chinelo_speed = 4
    chinelo_width = 150
    chinelo_height = 50
 
    dodged = 0
 
    gameExit = False
 
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    pygame.transform.rotate(baratinhaImg, 90)
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
 
        x += x_change
        gameDisplay.fill(white)
        gameDisplay.blit(fundoImg,(0,0))
        
        chinelos(chinelo_inix, chinelo_iniy, chinelo_width, chinelo_height, block_color)
        chinelo_iniy += chinelo_speed
        baratinha(x,y)
        chinelos_dodged(dodged)
 
        if x > display_width - baratinha_width or x < 0:
            gameExit = True
            crash()
            
            
        if chinelo_iniy > display_height:
            chinelo_iniy = 0 - chinelo_height
            chinelo_inix = random.randrange(0,display_width)
            dodged += 1
            chinelo_speed += 2
            chinelo_width += (dodged * 1.2)
 
        if y < chinelo_iniy+chinelo_height:
            if x > chinelo_inix and x < chinelo_inix + chinelo_width or x+baratinha_width > chinelo_inix and x + baratinha_width < chinelo_inix+chinelo_width:
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
