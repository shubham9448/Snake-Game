import pygame
import random
import os

pygame.mixer.init()
pygame.init()

bimg=pygame.image.load("snake1.webp")
bimg=pygame.transform.scale(bimg,(900,500))

#color used RGB
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

food_size=20
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    screen_text= font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])


def plot_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size]) #to draw rectangle


#game window
gamewindow = pygame.display.set_mode((900,500))
pygame.display.set_caption("Snakes Game")

def welcome():
    pygame.mixer.music.load("back.mp3")
    pygame.mixer.music.play()
    exit_game=False
    while not exit_game:
        gamewindow.fill((250,120,170))
        text_screen("WELCOME TO SNAKES",(113,1,200),250,190)
        text_screen("Press Space To Play",(221,210,5),275,250)
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                exit_game = True
            
            if even.type == pygame.KEYDOWN:
                if even.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)
 

#Game loop
def gameloop():
    exit_game=False
    game_over=False
    snake_x=450
    snake_y=250
    snake_size=20
    velocity_x=0
    velocity_y=0
    fps=60
    init_velocity=3
    score =0
    snk_list=[]
    snk_length = 1
    food_x=random.randint(20,850)
    food_y=random.randint(20,450)
    
    if(not os.path.exists("high_score.txt")):
        with open("high_score.txt","w") as f:
            f.write("0")

    with open("high_score.txt","r") as f:
        High_score=f.read()

    while not exit_game:

        if game_over:
            with open("high_score.txt","w") as f: #upload highest score in txt file
                f.write(str(High_score))
                
            gamewindow.fill(white)
            text_screen("Game Over! Press Enter",red,250,240)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT: #to exit the game
                    exit_game = True
                
                else:
                    event.type==pygame.KEYDOWN
                    if event.key==pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT: #to exit the game
                    exit_game = True

                if event.type==pygame.KEYDOWN: #to sense the keys on the keyboard
                    if event.key==pygame.K_RIGHT: #to sense the right key
                        velocity_x=init_velocity
                        velocity_y=0
                    elif event.key==pygame.K_LEFT: #to sense the left key
                        velocity_x=-init_velocity
                        velocity_y=0
                    elif event.key==pygame.K_UP: #to sense the up key 
                        velocity_x=0
                        velocity_y=-init_velocity
                    elif event.key==pygame.K_DOWN: #to sense the down key
                        velocity_x=0
                        velocity_y=init_velocity
            snake_x+=velocity_x
            snake_y+=velocity_y


            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score+=10
                food_x=random.randint(100,800)
                food_y=random.randint(100,400)
                snk_length+=10

                if score>int(High_score):
                    High_score=score

            gamewindow.fill((233,220,229)) #to create white screen
            

            gamewindow.blit(bimg,(0,0))
            text_screen("Score : "+str(score),(255,255,255),15,5)
            text_screen("Highest : "+str(High_score),(255,255,255),665,5)
            
            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if snake_x<0 or snake_x>900 or snake_y<0 or snake_y>500:
                game_over=True
                pygame.mixer.music.load("beep-02.mp3")
                pygame.mixer.music.play()
            if head in snk_list[:-1]:
                game_over= True


            pygame.draw.rect(gamewindow,black,[food_x,food_y,food_size,food_size]) #rectangle for food
            plot_snake(gamewindow,(11,66,255),snk_list,snake_size)
           
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
