import pygame
import time
import asyncio

# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([600, 600])

# Initializing surface
  
# Initialing Color
color = (0,0,0)
colorW = (255,255,255)

mainColor = (50,50,50)

color1 = (50,50,50)
color2 = (50,50,50)

color3 = (50,50,50)
color4 = (50,50,50)
color5 = (50,50,50)

color6 = (50,50,50)
color7 = (50,50,50)
color8 = (50,50,50)
color9 = (50,50,50)

index = 0
delay = 0.5

carImg = pygame.image.load('Assets/Cross.png')
carImg = pygame.transform.scale(carImg, (150, 150))

carImg2 = pygame.image.load('Assets/Ring.png')
carImg2 = pygame.transform.scale(carImg2, (150, 150))

ico = pygame.image.load('Assets/Tic-Tac-Toe-Game.Png')
pygame.display.set_icon(ico)

pygame.display.set_caption('Tick Tack Toe')

b1 = False
b2 = False
b3 = False

b4 = False
b5 = False
b6 = False

b7 = False
b8 = False
b9 = False


soundObj = pygame.mixer.Sound('Assets/Super Mario Bros. Music - Level Complete.wav')
soundObj2 = pygame.mixer.Sound('Assets/Super Mario Bros. - Game Over Sound Effect.wav')


f1 = False
f2 = False
f3 = False

f4 = False
f5 = False 
f6 = False

f7 = False
f8 = False
f9 = False


Used1 = False
Used2 = False
Used3 = False

Used4 = False
Used5 = False
Used6 = False

Used7 = False
Used8 = False
Used9 = False

playS = True
playS2 = True

def Restart():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global f1,f2,f3,f4,f5,f6,f7,f8,f9
    global Used1,Used2,Used3,Used4,Used5,Used6,Used7,Used8,Used9
    global running2
    global color1 , color2, color3, color4, color5, color6,color7,color8,color9
    global colorW, color
    global playS, playS2
    
    playS = True
    playS2 = True
    
    running2 = True
    
    f1 = False
    f2 = False
    f3 = False
    
    f4 = False
    f5 = False
    f6 = False
    
    f7 = False
    f8 = False
    f9 = False
    
    
    b1 = False
    b2 = False
    b3 = False
    
    b4 = False
    b5 = False
    b6 = False
    
    b7 = False
    b8 = False
    b9 = False
    
    Used1 = False
    Used2 = False
    Used3 = False
    
    Used4 = False
    Used5 = False
    Used6 = False
    
    Used7 = False
    Used8 = False
    Used9 = False

    color1 = mainColor
    color2 = mainColor
    color3 = mainColor
    
    color4 = mainColor
    color5 = mainColor
    color6 = mainColor
    
    color7 = mainColor
    color8 = mainColor
    color9 = mainColor
def playSound():
    soundObj.play()

def playSound2():
    soundObj2.play()


def is_over(rect, pos):
    # function takes a tuple of (x, y) coords and a pygame.Rect object
    # returns True if the given rect overlaps the given coords
    # else it returns False
    return True if rect.collidepoint(pos[0], pos[1]) else False


async def ai():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global f1,f2,f3,f4,f5,f6,f7,f8,f9
    global Used1,Used2,Used3,Used4,Used5,Used6,Used7,Used8,Used9
    global running2
    global color1 , color2, color3, color4, color5, color6,color7,color8,color9
    global colorW, color
    global playS, playS2
    if f1 == f2 and f2 == f3 and f1 == True:
        color1 = colorW
        color2 = colorW
        color3 = colorW
        running2 = False
        if playS2 == True:
            playSound2()
            playS2 = False

    elif f4 == f5 and f5 == f6 and f4 == True:
        color4 = colorW
        color5 = colorW
        color6 = colorW
        running2 = False
        if playS2 == True:
            playSound2()
            playS2 = False

    elif f7 == f8 and f8 == f9 and f7 == True:
        color7 = colorW
        color8 = colorW
        color9 = colorW
        running2 = False
        if playS2 == True:
            playSound2()
            playS2 = False

    elif f1 == f4 and f4 == f7 and f1 == True:
        color1 = colorW
        color4 = colorW
        color7 = colorW
        running2 = False
        if playS2 == True:
            playSound2()
            playS2 = False

    elif f2 == f5 and f5 == f8 and f2 == True:
        color2 = colorW
        color5 = colorW
        color8 = colorW
        running2 = False
        if playS2 == True:
            playSound2()
            playS2 = False

    elif f3 == f6 and f6 == f9 and f3 == True:
        color3 = colorW
        color6 = colorW
        color9 = colorW
        running2 = False
        if playS2 == True:
            playSound2()
            playS2 = False
    elif f1 == f5 and f5 == f9 and f1 == True:
        color1 = colorW
        color5 = colorW
        color9 = colorW
        running2 = False
        if playS2 == True:
            playSound2()
            playS2 = False
    elif f3 == f5 and f5 == f7 and f3 == True:
        color3 = colorW
        color5 = colorW
        color7 = colorW
        running2 = False
        if playS2 == True:
            playSound2()
            playS2 = False
    
    
    if b1 == b2 and b2 == b3 and b1 == True:
        color1 = color
        color2 = color
        color3 = color
        running2 = False
        if playS == True:
            playSound()
            playS = False
    elif b4 == b5 and b5 == b6 and b4 == True:
        color4 = color
        color5 = color
        color6 = color
        running2 = False
        if playS == True:
            playSound()
            playS = False
    elif b7 == b8 and b8 == b9 and b7 == True:
        color7 = color
        color8 = color
        color9 = color
        running2 = False
        if playS == True:
            playSound()
            playS = False
    elif b1 == b4 and b4 == b7 and b1 == True:
        color1 = color
        color4 = color
        color7 = color
        running2 = False
        if playS == True:
            playSound()
            playS = False
    elif b2 == b5 and b5 == b8 and b2 == True:
        color2 = color
        color5 = color
        color8 = color
        running2 = False
        if playS == True:
            playSound()
            playS = False
    elif b3 == b6 and b6 == b9 and b3 == True:
        color3 = color
        color6 = color
        color9 = color
        running2 = False
        if playS == True:
            playSound()
            playS = False
    elif b1 == b5 and b5 == b9 and b1 == True:
        color1 = color
        color5 = color
        color9 = color
        running2 = False
        if playS == True:
            playSound()
            playS = False
    elif b3 == b5 and b5 == b7 and b3 == True:
        color3 = color
        color5 = color
        color7 = color
        running2 = False
        if playS == True:
            playSound()
            playS = False
            
            
            
            
    if running2 == True:
        if f1 == True and f4 == True and Used7 != True:
            f7 = True
        elif f2 == True and f5 == True and Used8 != True:
            f8 = True
        elif f3 == True and f6 == True and Used9 != True:
            f9 = True
            
        elif f3 == True and f2 == True and Used1 != True:
            f1 = True
        elif f6 == True and f5 == True and Used4 != True:
            f4 = True
        elif f9 == True and f8 == True and Used7 != True:
            f7 = True
        
        elif f9 == True and f6 == True and Used3 != True:
            f3 = True
        elif f8 == True and f5 == True and Used2 != True:
            f2 = True
        elif f7 == True and f4 == True and Used1 != True:
            f1 = True
            
        elif f7 == True and f8 == True and Used9 != True:
            f9 = True
        elif f4 == True and f5 == True and Used6 != True:
            f6 = True
        elif f1 == True and f2 == True and Used3 != True:
            f3 = True
            
        elif f1 == True and f7 == True and Used4 != True:
            f4 = True
        elif f2 == True and f8 == True and Used5 != True:
            f5 = True
        elif f3 == True and f9 == True and Used6 != True:
            f6 = True
            
        elif f1 == True and f3 == True and Used2 != True:
            f2 = True
        elif f4 == True and f6 == True and Used5 != True:
            f5 = True
        elif f7 == True and f9 == True and Used8 != True:
            f8 = True
            
            
            
            
            
        elif b1 == True and b4 == True and Used7 != True: 
            f7 = True
            Used7 = True
        elif b2 == True and b5 == True and Used8 != True: 
            f8 = True
            Used8 == True
        elif b3 == True and b6 == True and Used9 != True: 
            f9 = True
            Used9 == True
        
        elif b3 == True and b2 == True and Used1 != True: 
            f1 = True
            Used1 == True
        elif b5 == True and b6 == True and Used4 != True: 
            f4 = True
            Used4 == True
        elif b8 == True and b9 == True and Used7 != True: 
            f7 = True
            Used7 == True
        
        elif b9 == True and b6 == True and Used3 != True: 
            f3 = True
            Used3 == True
        elif b8 == True and b5 == True and Used2 != True: 
            f2 = True
            Used2 == True
        elif b7 == True and b4 == True and Used1 != True: 
            f1 = True
            Used1 == True

        elif b7 == True and b8 == True and Used9 != True: 
            f9 = True
            Used9 == True
        elif b4 == True and b5 == True and Used6 != True: 
            f6 = True
            Used6 == True
        elif b1 == True and b2 == True and Used3 != True: 
            f3 = True
            Used3 == True
        
        
        
        elif b1 == True and b3 == True and Used2 != True: 
            f2 = True
            Used2 == True
        elif b4 == True and b6 == True and Used5 != True: 
            f5 = True
            Used5 == True
        elif b7 == True and b9 == True and Used8 != True: 
            f8 = True
            Used8 == True

        elif b1 == True and b7 == True and Used4 != True: 
            f4 = True
            Used4 == True
        elif b2 == True and b8 == True and Used5 != True: 
            f5 = True
            Used5 == True
        elif b3 == True and b9 == True and Used6 != True: 
            f6 = True
            Used6 == True
        
        #Diagonal
        elif b1 == True and b9 == True and Used5 != True: 
            f5 = True
            Used5 == True
        elif b3 == True and b7 == True and Used5 != True: 
            f5 = True
            Used5 == True
        
        
        elif b1 == True and b5 == True and Used9 != True: 
            f9 = True
            Used9 == True
        elif b9 == True and b5 == True and Used1 != True: 
            f1 = True
            Used1 == True
        
        elif b3 == True and b5 == True and Used7 != True: 
            f7 = True
            Used7 == True
        elif b7 == True and b5 == True and Used3 != True: 
            f3 = True
            Used3 == True
        else:
            if Used5 == False:
                f5 = True
            
            elif Used1 == False:
                f1 = True
                Used1 == True
            elif Used2 == False:
                f2 = True
                Used2 == True
            elif Used3 == False:
                f3 = True
                Used3 == True
            elif Used4 == False:
                f4 = True
                Used4 == True
            elif Used5 == False:
                f5 = True
                Used5 == True
            elif Used6 == False:
                f6 = True
                Used6 == True
            elif Used7 == False:
                f7 = True
                Used7 == True
            elif Used8 == False:
                f8 = True
                Used8 == True
            elif Used9 == False:
                f9 = True
                Used9 == True
        
    


# Run until the user asks to quit
running2 = True;
running = True
while running:
        
        
    # Did the user click the window close button?
    for event in pygame.event.get():
        if b1 == b2 and b2 == b3 and b1 == True:
            color1 = color
            color2 = color
            color3 = color
            running2 = False
            if playS == True:
                playSound()
                playS = False

        elif b4 == b5 and b5 == b6 and b4 == True:
            color4 = color
            color5 = color
            color6 = color
            running2 = False
            if playS == True:
                playSound()
                playS = False
        elif b7 == b8 and b8 == b9 and b7 == True:
            color7 = color
            color8 = color
            color9 = color
            running2 = False
            if playS == True:
                playSound()
                playS = False
        elif b1 == b4 and b4 == b7 and b1 == True:
            color1 = color
            color4 = color
            color7 = color
            running2 = False
            if playS == True:
                playSound()
                playS = False

        elif b2 == b5 and b5 == b8 and b2 == True:
            color2 = color
            color5 = color
            color8 = color
            running2 = False
            if playS == True:
                playSound()
                playS = False

        elif b3 == b6 and b6 == b9 and b3 == True:
            color3 = color
            color6 = color
            color9 = color
            running2 = False
            if playS == True:
                playSound()
                playS = False
    
        elif b1 == b5 and b5 == b9 and b1 == True:
            color1 = color
            color5 = color
            color9 = color
            running2 = False
            if playS == True:
                playSound()
                playS = False

        elif b3 == b5 and b5 == b7 and b3 == True:
            color3 = color
            color5 = color
            color7 = color
            running2 = False
            if playS == True:
                playSound()
                playS = False

            
            
            
            
            
        
        if f1 == f2 and f2 == f3 and f1 == True:
            color1 = colorW
            color2 = colorW
            color3 = colorW
            running2 = False
            if playS2 == True:
                playSound2()
                playS2 = False

        elif f4 == f5 and f5 == f6 and f4 == True:
            color4 = colorW
            color5 = colorW
            color6 = colorW
            running2 = False
            if playS2 == True:
                playSound2()
                playS2 = False

        elif f7 == f8 and f8 == f9 and f7 == True:
            color7 = colorW
            color8 = colorW
            color9 = colorW
            running2 = False
            if playS2 == True:
                playSound2()
                playS2 = False

        elif f1 == f4 and f4 == f7 and f1 == True:
            color1 = colorW
            color4 = colorW
            color7 = colorW
            running2 = False
            if playS2 == True:
                playSound2()
                playS2 = False

        elif f2 == f5 and f5 == f8 and f2 == True:
            color2 = colorW
            color5 = colorW
            color8 = colorW
            running2 = False
            if playS2 == True:
                playSound2()
                playS2 = False

        elif f3 == f6 and f6 == f9 and f3 == True:
            color3 = colorW
            color6 = colorW
            color9 = colorW
            running2 = False
            if playS2 == True:
                playSound2()
                playS2 = False
        elif f1 == f5 and f5 == f9 and f1 == True:
            color1 = colorW
            color5 = colorW
            color9 = colorW
            running2 = False
            if playS2 == True:
                playSound2()
                playS2 = False
        elif f3 == f5 and f5 == f7 and f3 == True:
            color3 = colorW
            color5 = colorW
            color7 = colorW
            running2 = False
            if playS2 == True:
                playSound2()
                playS2 = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and running2 == True:
            if event.button == 1 and Used1 == False and index == 1:
                b1=True
                Used1 = True
                asyncio.run(ai())

            if event.button == 1 and Used2 == False and index == 2:
                b2=True
                Used2 = True
                asyncio.run(ai())

            if event.button == 1 and Used3 == False and index == 3:
                b3=True
                Used3 = True
                asyncio.run(ai())

                
            if event.button == 1 and Used4 == False and index == 4:
                b4=True
                Used4 = True
                asyncio.run(ai())

            if event.button == 1 and Used5 == False and index == 5:
                b5=True
                Used5 = True
                asyncio.run(ai())

            if event.button == 1 and Used6 == False and index == 6:
                b6=True
                Used6 = True
                asyncio.run(ai())

                
            if event.button == 1 and Used7 == False and index == 7:
                b7=True
                Used7 = True
                asyncio.run(ai())

            if event.button == 1 and Used8 == False and index == 8:
                b8=True
                Used8 = True
                asyncio.run(ai())

            if event.button == 1 and Used9 == False and index == 9:
                b9=True
                Used9 = True
                asyncio.run(ai())

                
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print("Restart")
                Restart()
        
        if event.type == pygame.KEYDOWN and running2 == True:
            
                
            if event.key == pygame.K_1 and Used1 == False:
                b1=True
                Used1 = True
                asyncio.run(ai())

            if event.key == pygame.K_2 and Used2 == False:
                b2=True
                Used2 = True
                asyncio.run(ai())

            if event.key == pygame.K_3 and Used3 == False:
                b3=True
                Used3 = True
                asyncio.run(ai())

                
            if event.key == pygame.K_4 and Used4 == False:
                b4=True
                Used4 = True
                asyncio.run(ai())

            if event.key == pygame.K_5 and Used5 == False:
                b5=True
                Used5 = True
                asyncio.run(ai())

            if event.key == pygame.K_6 and Used6 == False:
                b6=True
                Used6 = True
                asyncio.run(ai())

                
            if event.key == pygame.K_7 and Used7 == False:
                b7=True
                Used7 = True
                asyncio.run(ai())

            if event.key == pygame.K_8 and Used8 == False:
                b8=True
                Used8 = True
                asyncio.run(ai())

            if event.key == pygame.K_9 and Used9 == False:
                b9=True
                Used9 = True
                asyncio.run(ai())

        
        
        if event.type == pygame.QUIT:           
            running = False

    
        
    
    
    if b1 == True or f1 == True:
        Used1 = True
        
    if b2 == True or f2 == True:
        Used2 = True
    if b3 == True or f3 == True:
        Used3 = True
        
    if b4 == True or f4 == True:
        Used4 = True
    if b5 == True or f5 == True:
        Used5 = True
    if b6 == True or f6 == True:
        Used6 = True
        
    if b7 == True or f7 == True:
        Used7 = True
    if b8 == True or f8 == True:
        Used8 = True
    if b9 == True or f9 == True:
        Used9 = True

    # Fill the background with white
    screen.fill((100, 100, 100))

    # Draw a solid blue circle in the center
    r1 = pygame.draw.rect(screen, color1, pygame.Rect(50, 50,150, 150))
    r2 = pygame.draw.rect(screen, color2, pygame.Rect(225, 50,150, 150))
    r3 = pygame.draw.rect(screen, color3, pygame.Rect(400, 50,150, 150))
    
    r4 = pygame.draw.rect(screen, color4, pygame.Rect(50, 225,150, 150))
    r5 = pygame.draw.rect(screen, color5, pygame.Rect(225, 225,150, 150))
    r6 = pygame.draw.rect(screen, color6, pygame.Rect(400, 225,150, 150))
    
    r7 = pygame.draw.rect(screen, color7, pygame.Rect(50, 400,150, 150))
    r8 = pygame.draw.rect(screen, color8, pygame.Rect(225, 400,150, 150))
    r9 = pygame.draw.rect(screen, color9, pygame.Rect(400, 400,150, 150))
    
    
    pos = pygame.mouse.get_pos() # gets the current mouse coords
    if is_over(r1, pos): # pass in the pygame.Rect and the mouse coords
        index = 1
    elif is_over(r2, pos): # pass in the pygame.Rect and the mouse coords
        index = 2
    elif is_over(r3, pos): # pass in the pygame.Rect and the mouse coords
        index = 3
        
    elif is_over(r4, pos): # pass in the pygame.Rect and the mouse coords
        index = 4
    elif is_over(r5, pos): # pass in the pygame.Rect and the mouse coords
        index = 5
    elif is_over(r6, pos): # pass in the pygame.Rect and the mouse coords
        index = 6
    
    elif is_over(r7, pos): # pass in the pygame.Rect and the mouse coords
        index = 7
    elif is_over(r8, pos): # pass in the pygame.Rect and the mouse coords
        index = 8
    elif is_over(r9, pos): # pass in the pygame.Rect and the mouse coords
        index = 9
    else:
        index = 0
        

    
    #crosses
    if b1 == True: screen.blit(carImg, (50,50))
    if b2 == True: screen.blit(carImg, (225,50))
    if b3 == True: screen.blit(carImg, (400,50))

    if b4 == True: screen.blit(carImg, (50,225))
    if b5 == True: screen.blit(carImg, (225,225))
    if b6 == True: screen.blit(carImg, (400,225))

    if b7 == True: screen.blit(carImg, (50,400))
    if b8 == True: screen.blit(carImg, (225,400))
    if b9 == True: screen.blit(carImg, (400,400))
    
    
    
    #Circles
    if f1 == True: screen.blit(carImg2, (50,50))
    if f2 == True: screen.blit(carImg2, (225,50))
    if f3 == True: screen.blit(carImg2, (400,50))

    if f4 == True: screen.blit(carImg2, (50,225))
    if f5 == True: screen.blit(carImg2, (225,225))
    if f6 == True: screen.blit(carImg2, (400,225))

    if f7 == True: screen.blit(carImg2, (50,400))

    if f8 == True: screen.blit(carImg2, (225,400))
    if f9 == True: screen.blit(carImg2, (400,400))



    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()