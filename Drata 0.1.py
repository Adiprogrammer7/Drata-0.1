import pygame
import random
import time


pygame.init()  #essential to initialize pygame first.

# game audio setup(wav format of audio works best in pygame)
crash_effect = pygame.mixer.Sound('crash_effect.wav')
pygame.mixer.music.load('background_music.wav') #with music you need to load it too.


# we set variables for width and height so that they can be referenced later.
dis_width = 800
dis_height = 600

# In pygame we need to define color definitions, generally using RGB method.
black = (0,0,0)
white = (255,255,255)
bluish_aqua = (51, 196, 218)
dark_blue = (12, 55, 91)
orange = (223, 136, 31)

# for hover over effect.
bright_bluish_aqua = (61, 220, 255)
bright_orange = (253, 156, 51)


game_dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Drata 0.1')
game_clk = pygame.time.Clock()

car_img = pygame.image.load('racecar.png')  #this is how we load image.
car_width = 73 #will need during boundry setup.

# game icon
#display icons in pygame are generally of 32x32 pixels, so make sure to scale icon image.
game_ico = pygame.image.load('ico_1.png')
pygame.display.set_icon(game_ico)


# function to track progress(things that dodged)
def things_dodged(count):
    font = pygame.font.SysFont('comicsansms', 22)
    text = font.render("Dodged: " +str(count), True, dark_blue)
    game_dis.blit(text, (2,2))  #somewhat top of the screeen.


def pause_opt():  #to show pause option while playing.
    font = pygame.font.SysFont('comicsansms', 22)
    text = font.render("Pause: p", True, dark_blue)
    game_dis.blit(text, (700,1))  #on the other corner of screen.


# to draw obstacles.
def things(thing_x, thing_y, thing_w, thing_h, thing_color):

    pygame.draw.rect(game_dis, thing_color, (thing_x, thing_y, thing_w, thing_h))  #to draw a rectangular object on the screen.


# defined function to set car position and blit it on screen.
def car(car_width,car_height):
    game_dis.blit(car_img, (car_width,car_height))


def text_objects(text_obj, changed_text):
    text_surface = changed_text.render(text_obj, True, black)  #it renders our text into changed text. True is for anti alising value.
    text_rectangle = text_surface.get_rect()  #.get_rect() is method of pygame for text surface which creates an rectangular thing around it.
    return text_surface, text_rectangle

# def message_display(text):
#     large_text = pygame.font.SysFont('comicsansms', 100)  #defined font.
#     text_surf, text_rect = text_objects(text, large_text)  #it will call another function and will store returned values in these variables.
#     text_rect.center = ((dis_width/2), (dis_height/2))  #x, y co-oridinates for text box.
#     game_dis.blit(text_surf, text_rect) #text_surf means actual text, text_rect means its x, y co-ordinates.
#
#     pygame.display.update()  #we need to update display otherwise we won't see message.
#
#     time.sleep(2)  #it will diplay message for 2 sec.
#     game_loop()   #after 2 sec it will again restart game loop.


# similar to game_intro().
def crash():

    # so within the crash function, we want to stop our background music and play crash effect.
    pygame.mixer.music.stop()  #stops the background music.
    pygame.mixer.Sound.play(crash_effect) #to play crash effect.

    font = pygame.font.SysFont('comicsansms', 100)
    text, text_rect = text_objects("You Crashed", font)  # called function to get modified text and rectangle around it.
    text_rect.center = ((dis_width / 2), (dis_height / 2))  # x, y co-oridinates for text box.
    game_dis.blit(text, text_rect)  # text_surf means actual text, text_rect means its x, y co-ordinates.

    crashed = True

    while crashed:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                quit()


        # drawing buttons with hover over effect.
        mouse_pos = pygame.mouse.get_pos()  # to get position of mouse in x and y format.

        mouse_click = pygame.mouse.get_pressed()  # to get which button is clicked.

        # when mouse is in position range of button. (mouse_pos[0] = mouse x, mouse_pos[1] = mouse y)
        # for first button.
        if 150 + 100 > mouse_pos[0] > 150 and 450 + 50 > mouse_pos[1] > 450:
            pygame.draw.rect(game_dis, bright_bluish_aqua, (150, 450, 100, 50))
            if mouse_click[0] == 1:  # when left-mouse click.
                game_loop() #to restart the game.


        else:
            pygame.draw.rect(game_dis, bluish_aqua, (150, 450, 100, 50))

        # for second button.
        if 550 + 100 > mouse_pos[0] > 550 and 450 + 50 > mouse_pos[1] > 450:
            pygame.draw.rect(game_dis, bright_orange, (550, 450, 100, 50))
            if mouse_click[0] == 1:  # when left-mouse click.
                pygame.quit()
                quit()

        else:
            pygame.draw.rect(game_dis, orange, (550, 450, 100, 50))

        # TEXT ON BUTTON
        # we will put text on button like we did previously in game.
        # For first button.
        small_text = pygame.font.SysFont('comicsansms', 20)
        text_surf, text_rect = text_objects('Retry', small_text)
        text_rect.center = ((150 + (100 / 2)), (450 + (50 / 2)))
        game_dis.blit(text_surf, text_rect)

        # For second button.
        small_text = pygame.font.SysFont('comicsansms', 20)
        text_surf, text_rect = text_objects('Quit', small_text)
        text_rect.center = ((550 + (100 / 2)), (450 + (50 / 2)))
        game_dis.blit(text_surf, text_rect)

        pygame.display.update()
        game_clk.tick(30)


# For Pause functionality, its gonna be so similar to game_intro().
def pause():

    #when game is paused, we want music to pause also.
    pygame.mixer.music.pause()

    # we written it out of the while loop because in while loop our text gets overwritten again and again so our big text becomes somewhat grainy.
    # game_dis.fill(white)  #we didn't filled background with white because we wanted to see the game even its paused.
    font = pygame.font.SysFont('comicsansms', 100)
    text, text_rect = text_objects("Paused", font)  # called function to get modified text and rectangle around it.
    text_rect.center = ((dis_width / 2), (dis_height / 2))  # x, y co-oridinates for text box.
    game_dis.blit(text, text_rect)  # text_surf means actual text, text_rect means its x, y co-ordinates.

    paused = True

    while paused:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN: #when p key pressed again we want to resume the game.
                if event.key == pygame.K_p:
                    paused = False

        # drawing buttons with hover over effect.
        mouse_pos = pygame.mouse.get_pos()   #to get position of mouse in x and y format.

        mouse_click = pygame.mouse.get_pressed()  #to get which button is clicked.

        # when mouse is in position range of button. (mouse_pos[0] = mouse x, mouse_pos[1] = mouse y)
        # for first button.
        if 150+100 > mouse_pos[0] > 150 and 450+50 > mouse_pos[1] > 450:
            pygame.draw.rect(game_dis, bright_bluish_aqua, (150, 450, 100, 50))
            if mouse_click[0] == 1:  #when left-mouse click.

                paused = False  #to break out of while loop and continue game.

        elif paused == False:
            pygame.mixer.music.unpause()  # to unpause the music when game is unpaused.

        else:
            pygame.draw.rect(game_dis, bluish_aqua, (150, 450, 100, 50))

        # for second button.
        if 550+100 > mouse_pos[0] > 550 and 450+50 > mouse_pos[1] > 450:
            pygame.draw.rect(game_dis, bright_orange, (550, 450, 100, 50))
            if mouse_click[0] == 1:  #when left-mouse click.
                pygame.quit()
                quit()

        else:
            pygame.draw.rect(game_dis, orange, (550, 450, 100, 50))


        #TEXT ON BUTTON
        #we will put text on button like we did previously in game.
        #For first button.
        small_text = pygame.font.SysFont('comicsansms', 20)
        text_surf, text_rect = text_objects('Resume', small_text)
        text_rect.center = ((150+(100/2)), (450+(50/2)))
        game_dis.blit(text_surf, text_rect)

        #For second button.
        small_text = pygame.font.SysFont('comicsansms', 20)
        text_surf, text_rect = text_objects('Quit', small_text)
        text_rect.center = ((550 + (100 / 2)), (450 + (50 / 2)))
        game_dis.blit(text_surf, text_rect)

        pygame.display.update()
        game_clk.tick(30)


# an intro screen.
def game_intro():

    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                quit()

        game_dis.fill(white)
        font = pygame.font.SysFont('comicsansms', 100)
        text, text_rect = text_objects("Drata 0.1", font)  #called function to get modified text and rectangle around it.
        text_rect.center = ((dis_width / 2), (dis_height / 2))  # x, y co-oridinates for text box.
        game_dis.blit(text, text_rect)  # text_surf means actual text, text_rect means its x, y co-ordinates.


        # drawing buttons with hover over effect.
        mouse_pos = pygame.mouse.get_pos()   #to get position of mouse in x and y format.

        mouse_click = pygame.mouse.get_pressed()  #to get which button is clicked.

        # when mouse is in position range of button. (mouse_pos[0] = mouse x, mouse_pos[1] = mouse y)
        # for first button.
        if 150+100 > mouse_pos[0] > 150 and 450+50 > mouse_pos[1] > 450:
            pygame.draw.rect(game_dis, bright_bluish_aqua, (150, 450, 100, 50))
            if mouse_click[0] == 1:  #when left-mouse click.
                game_loop()

        else:
            pygame.draw.rect(game_dis, bluish_aqua, (150, 450, 100, 50))

        # for second button.
        if 550+100 > mouse_pos[0] > 550 and 450+50 > mouse_pos[1] > 450:
            pygame.draw.rect(game_dis, bright_orange, (550, 450, 100, 50))
            if mouse_click[0] == 1:  #when left-mouse click.
                pygame.quit()
                quit()

        else:
            pygame.draw.rect(game_dis, orange, (550, 450, 100, 50))

        #TEXT ON BUTTON
        #we will put text on button like we did previously in game.
        #For first button.
        small_text = pygame.font.SysFont('comicsansms', 20)
        text_surf, text_rect = text_objects('Play', small_text)
        text_rect.center = ((150+(100/2)), (450+(50/2)))
        game_dis.blit(text_surf, text_rect)

        #For second button.
        small_text = pygame.font.SysFont('comicsansms', 20)
        text_surf, text_rect = text_objects('Quit', small_text)
        text_rect.center = ((550 + (100 / 2)), (450 + (50 / 2)))
        game_dis.blit(text_surf, text_rect)


        pygame.display.update()
        game_clk.tick(30)


# the main game loop function.
def game_loop():

    # In game loop we want to play the background music.
    # pygame.mixer.music.play(2) #it will play the music for 3 times(2+1)
    pygame.mixer.music.play(-1) #this will play the game indefinitely.


    # defined x, y with respect to game display for car position.
    x = (dis_width * 0.45)
    y = (dis_height * 0.8)


    # variable for position changes by keys presses.
    x_change = 0

    # initial values for obstacles(things).
    thing_width = 80
    thing_height = 80
    # (dis_width - thing_width) otherwise our thing may be some what off the screen.
    thing_startx = random.randrange(0, (dis_width - thing_width))  #x location around the width of the screen.
    thing_starty = -600   #it is little bit off the screen so that user can get some time to face obstacles at start.


    thing_speed = 7  #this value can later be added in things y value so it location on y axis will change.

    dodged_things = 0

    while True:
        for event in pygame.event.get():  #this is the 'event loop' which handles events that happens.
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:  # when key is pressed down.

                if event.key == pygame.K_LEFT: #for left arrow key.
                    x_change = -5  #left key will decrease x-axis value.

                elif event.key == pygame.K_RIGHT: #for right arrow.
                    x_change = 5  #will increase x-axis value.

                elif event.key == pygame.K_p:  # trigger for pause functionality when key p is pressed.
                    pause()

            if event.type == pygame.KEYUP: #so car doesn't move when key is released.
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x = x + x_change  #just changed out x value according to events which happens.

        # Note: filling background after image will hide the image.
        game_dis.fill(white)  #we filled background with white color that we defined earlier.


        # def things(thing_x, thing_y, thing_w, thing_h, thing_color) function to be called.
        things(thing_startx, thing_starty, thing_width, thing_height, black)  #just draws object
        thing_starty += thing_speed  #to move object along y axis.


        car(x,y)  #called the function defined above to spot out car.

        things_dodged(dodged_things)  #called function to show dodged things count on screen.
        pause_opt()  #to show pause option on screen.

        # boundary setup.
        if x > dis_width - car_width or x < 0:
            crash()    #so when car hits the boundary, we call crash function.


        # Now while loop draw thing on screen continuously, but we want some logic
        # when thing goes off the screen, we will put that same thing on screen again
        # just a little bit off the screen and we also need to change its x value
        # otherwise it will retrace the same path again and again.
        if thing_starty > dis_width:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, (dis_width - thing_width))
            dodged_things += 1

            # to manage the speed of thing over dodged things.
            if dodged_things % 4 == 0:
                thing_speed += 1

                if thing_speed == 12:
                    thing_speed = 8



        # for y axis crossover:
        if y < thing_starty + thing_height:

            if thing_starty > dis_height:  #did to remove the bug.
                pass

            # after y crossover confirmed, checking for x crossover:
            elif x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash()  #called crash function.

        pygame.display.update()
        game_clk.tick(60)

game_intro()
game_loop()
