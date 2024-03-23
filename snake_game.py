import random
import pygame
import os
pygame.init()

pygame.mixer.init()

#window variables
screen_width = 900
screen_height = 400

#window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SnakesWithRohan")

#Background Image
bgimg = pygame.image.load("C:\\Users\\rohan\\VS_code\\rohan\\python\\ursina assets\\green_neon_grid.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

#game specific variables

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)

#colors
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

#game functions
def text_on_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,45,210))
        text_on_screen("Welcome to Snakes", black, 260, 140)
        text_on_screen("Press spacebar to play", black, 230, 190)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("C:\\Users\\rohan\\VS_code\\rohan\\python\\ursina assets\\neon-gaming-128925.mp3")
                    pygame.mixer.music.play()
                    gameloop()


#main loop
def gameloop():
    exit_game = False
    game_over = False
    food_x = random.randint(20, int(screen_width/2))
    food_y = random.randint(20, int(screen_height/2))
    score = 0
    snake_x = 45
    snake_y = 55
    snake_size = 30
    velocity_x = 0
    velocity_y = 0
    init_velocity = 10
    fps = 30
    snk_list = []
    snk_length = 1

    #Check if hiscore.txt exists
    if not os.path.exists("C:\\Users\\rohan\\VS_code\\rohan\\python\\pygame\\snakeGame\\hiscore.txt"):
        with open("C:\\Users\\rohan\\VS_code\\rohan\\python\\pygame\\snakeGame\\hiscore.txt", "w") as f:
            f.write("0")

    with open("C:\\Users\\rohan\\VS_code\\rohan\\python\\pygame\\snakeGame\\hiscore.txt", "r") as f:
            hiscore = f.read()

    while not exit_game:
        if game_over:
            with open("C:\\Users\\rohan\\VS_code\\rohan\\python\\pygame\\snakeGame\\hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_on_screen(f"Score: {score}", red, 5, 5)
            text_on_screen("Game Over! Press Enter to Continue", red, 100, 150)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

                if event.type == pygame.QUIT:
                    exit_game = True

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if velocity_x != -init_velocity:
                            velocity_x = init_velocity
                            velocity_y = 0

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if velocity_x != init_velocity:
                            velocity_x = -init_velocity
                            velocity_y = 0
                
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if velocity_y != -init_velocity:
                            velocity_y = init_velocity
                            velocity_x = 0
                    
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if velocity_y != init_velocity:
                            velocity_y = -init_velocity
                            velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 5

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 1
                # print(f"Score: {score}")
                food_x = random.randint(20, int(screen_width/2))
                food_y = random.randint(20, int(screen_height/2))
                snk_length += 5
                if score>int(hiscore):
                    hiscore = score

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                pygame.mixer.music.load("C:\\Users\\rohan\\VS_code\\rohan\\python\\explosion.mp3")
                pygame.mixer.music.play()
                game_over = True

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:            
                game_over = True
                pygame.mixer.music.load("C:\\Users\\rohan\\VS_code\\rohan\\python\\explosion.mp3")
                pygame.mixer.music.play()

            gameWindow.fill((100,100,100))
            gameWindow.blit(bgimg, (0,0))
            text_on_screen(f"Score: {score}, Hiscore: {hiscore}", red, 5, 5)
            
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            plot(gameWindow, blue, snk_list, snake_size)
            snake_x += velocity_x
            snake_y += velocity_y

        pygame.display.update()
        clock.tick(fps)
        
    #game quit
    pygame.quit()
    quit()

# gameloop()
welcome()