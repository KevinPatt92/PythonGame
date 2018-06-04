# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:00:11 2017

@author: Kevin Patterson
"""

import pygame
import time
import csv

#Setting up variable for the window size of the game
windowWidth = 800
windowHeight = 650
frameRate = 10

#Set up some basic colours used in the game
white = (255, 255, 255)
black = (0, 0, 0)
green = (68, 244, 78)
blue = (0, 153, 255)
blueDark = (37, 84, 142)
red = (255, 0, 0)
brown = (104, 78, 56)
grey = (106, 118, 137)

years = []
provinces = []
scores = []

pygame.init()
gameDisplay = pygame.display.set_caption('Inter-provincial Curling Challenge Version 1.0')
gameDisplay = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None,35)

#Load csv file into the game's memory
def fileLoader():
    with open('00010014-eng.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            year = row[0]
            province = row[1]
            score = row[5]
    
            years.append(year)
            provinces.append(province)
            scores.append(score)
            
        print (scores[10])
        print (provinces[10])
        print (years[10])

#create a way to display text to the user
def userMessage(msg,colour, Xline, Yline):
    screen_text = font.render(msg, True, colour)
    # (what to display, [where to display it x, y])
    gameDisplay.blit(screen_text, (Xline, Yline))

def highScore():
    hScore = True
    
    while hScore:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    hScore = False
                    
                elif event.key ==pygame.K_q:
                    pygame.quit()
                    quit()
                    
        gameDisplay.fill(white)
        userMessage("Welcome to highscore Screen", black, 400, 50)
        userMessage("Press c to continue", black, 400, 100)
        userMessage("Press q to quit", black, 400, 150)
        userMessage("HighScores", black, 300, 200)
        userMessage("Score* *Region* *Year*", black, 20, 250)
        userMessage(scores[10]+"* *"+provinces[10]+"* *"+years[10], red, 20, 300)
        userMessage(scores[455]+"* *"+provinces[455]+"* *"+years[455], blue, 20, 400)
        userMessage(scores[1000]+"* *"+provinces[1000]+"* *"+years[1000], green, 20, 350)
        #userMessage(scores[10], black, 20, 300)
        
        pygame.display.update()
        clock.tick(5)
        
def info():
    infoScreen = True
    
    while infoScreen:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    infoScreen = False
                    
                elif event.key ==pygame.K_q:
                    pygame.quit()
                    quit()
                    
        gameDisplay.fill(white)
        userMessage("Welcome to Inter-provincial Curling Challenge", black, 50, 50)
        userMessage("Use the space bar to make a shot", black, 50, 100)
        userMessage("Use the 'tab' button to reset the board", black, 50, 150)
        userMessage("Left and Right arrow keys will align your shot", black, 50, 200)
        userMessage("Up and Down arrow keys will set the stones initial power", black, 50, 250)
        userMessage("Pressing 'i' will change the curling orientation of the stone", black, 50, 300)
        userMessage("(marked by a white circle at the bottom of the screen)", black, 50, 350)
        userMessage("Note: The horizontal movement of a stone (the curl)", black, 50, 400)
        userMessage("will become more pronounced as a stone slows down!", black, 50, 450)
        userMessage("Press c to continue", black, 400, 550)
        userMessage("Press q to quit", black, 400, 600)
        
        pygame.display.update()
        clock.tick(5)
        
def gameCycle():
    #varialbe tracking wheather use has x'ed out of window
    gameExit = False
    throwStone = False
    playAgain = False
    reset = False
    infoScreen = False
    hScore = False
    inTurn = False
    #game will run until this condition is met
    #create some variable for the position of the curling stone
    stoneX = 400
    stoneY = 600
    stoneDeltaY = 27
    while not gameExit:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            #Player sets up early game parameters
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and stoneX >= 320:
               stoneX -= 10
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and stoneX <= 480:
               stoneX += 10
               
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and stoneDeltaY > 25:
               stoneDeltaY -= 1
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and stoneDeltaY < 35:
               stoneDeltaY += 1   
               
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                if inTurn == True:
                    inTurn = False
                else:
                    inTurn = True
                  
            #Pausing game to view highscore stats
            if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
               highScore()
               
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
               info()
            
            #create an event where the player shoots the curling stone
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                #print("oh hello")
                #Initiate throwing of stone
                throwStone = True
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            #print("oh hello")
            #Initiate throwing of stone
                reset = True
        
        if  throwStone == True:
            stoneY -= stoneDeltaY
            stoneDeltaY -= 1
            if inTurn == True:
                if stoneDeltaY<6:
                    stoneX += (3 + stoneDeltaY)
                else:
                    stoneX += 3
                    
            if inTurn == False:
                if stoneDeltaY<6:
                    stoneX -= (3 + stoneDeltaY)
                else:
                    stoneX -= 3
            
        if stoneDeltaY <= 0:
                throwStone = False
                playAgain = True
        
        #allows player to reset game after a shot is thrown
        if reset == True:
            stoneX = 400
            stoneY = 600
            stoneDeltaY = 27
            throwStone = False
            playAgain = False
            reset = False
                    
        gameDisplay.fill(blueDark)
        #This area is used to render all objects to game window
        #list [location x, location y, width, height]
            
        pygame.draw.rect(gameDisplay, white, [windowWidth/4, 0, windowWidth/2, windowHeight])
        #make cirle with (surface, colour, pos, radius)
        pygame.draw.circle(gameDisplay, red, [400, 150], 125)
        pygame.draw.circle(gameDisplay, blue, [400, 150], 75)
        pygame.draw.circle(gameDisplay, white, [400, 150], 25)
        #Draw a curling stone, should not be hardcoded so it can move
        
        pygame.draw.circle(gameDisplay, brown, [stoneX, stoneY], 20)
        
        #Power marker
        pygame.draw.circle(gameDisplay, red, [75, 600], 10)
        
        if stoneDeltaY >26:
            pygame.draw.circle(gameDisplay, red, [75, 550], 12)
        if stoneDeltaY >31:    
            pygame.draw.circle(gameDisplay, red, [75, 500], 15)
        if stoneDeltaY == 35:
            pygame.draw.circle(gameDisplay, red, [75, 450], 17)
        
        #Handle marker
        if inTurn == True:
            pygame.draw.circle(gameDisplay, white, [75, 600], 10)
        if inTurn == False:
            pygame.draw.circle(gameDisplay, white, [700, 600], 10)
        
        #Welcome player to the game
        userMessage("Welcome to", grey, 10, 50)
        userMessage("Inter-provincial", grey, 10, 100)
        userMessage("Curling Challenge", grey, 10, 150)
        userMessage("Practice Mode", grey, 10, 200)
        #pause screen options
        userMessage("Pause Screen", red, 10, 400)
        userMessage("F - Info", red, 10, 450)
        userMessage("H- HighScore", red, 10, 500)
        
        
        #Give player instruction
        if throwStone == False and playAgain == True:
            #Print out 'nice shot'
            userMessage("Nice Shot", green, 400, 200)
            userMessage("Hit Tab to shoot again", green, 400, 250)
        userMessage("Press Space", green, 625, 50)
        userMessage("To Take a", green, 625, 100)
        userMessage("Practice Shot", green, 625, 150)
        
        
            
        pygame.display.update()
        
        #Set how many times a sec the screen is updated
        clock.tick(frameRate)
        
    pygame.quit()
    quit()

fileLoader()
gameCycle()