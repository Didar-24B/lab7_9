import pygame
import random

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SNAKE GAME")


green = (0, 255, 0)  # Background
red = (255, 0, 0)  # Snake
blue = (0, 0, 255)  # Score
yellow = (255, 255, 0)  # Food

snake_block = 10
initial_snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
level_font = pygame.font.SysFont("comicsansms", 25)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, blue)
    screen.blit(value, [0, 0])

def Your_level(level):
    value = level_font.render("Level: " + str(level), True, blue)
    screen.blit(value, [width - 150, 0])

def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(screen, red, [x[0], x[1], snake_block, snake_block])

def generate_food():
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    food_score = random.randint(1, 8)
    return food_x, food_y, food_score

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    food_x, food_y, food_score = generate_food()
    snake_speed = initial_snake_speed
    level = 1

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            screen.fill(green)
            Your_score(Length_of_snake - 1)
            Your_level(level)
            message = font_style.render("GAME OVER!", True, blue)
            screen.blit(message, [width / 6, height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(green)

        pygame.draw.rect(screen, yellow, [food_x, food_y, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        Your_level(level)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x, food_y, food_score = generate_food()
            Length_of_snake += food_score
            if Length_of_snake % 5 == 0:
                snake_speed += 1
            if Length_of_snake % 10 == 0:
                level += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()