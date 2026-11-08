import pygame
import random

GRID_SIZE = 10
DIRECTIONS = {
    "R":(1,0),
    "L":(-1,0),
    "U":(0,-1),
    "D":(0,1)
    
}
OPPOSITE = {
    "R":"L",
    "L":"R",
    "U":"D",
    "D":"U"
}
def display_game():
    pygame.init()

    CELL_SIZE = 50
    MARGIN = 20
    HEADER = 60
    WIDTH = GRID_SIZE * CELL_SIZE + 2 * MARGIN
    HEIGHT = GRID_SIZE * CELL_SIZE + HEADER + 2 * MARGIN

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 30)

    snake = [(5, 5)]
    direction = "R"
    score = 0
    fixed_foods = [(7, 5), (0, 0)]
    food = generate_food(snake, fixed_foods)
    running = True
    game_over = False
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                

            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                else:
                    keys = {
                        pygame.K_RIGHT: "R",
                        pygame.K_LEFT: "L",
                        pygame.K_UP: "U",
                        pygame.K_DOWN: "D"
                    }

                    if event.key in keys:
                        new_direction = keys[event.key]

                        if new_direction != OPPOSITE[direction]:
                            direction = new_direction

        # Move the snake at a controlled speed
        if not paused and not game_over:
            dx, dy = DIRECTIONS[direction]
            head_x, head_y = snake[0]
            new_head = (head_x + dx, head_y + dy)
            x, y = new_head

            if not (0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE):
                game_over = True
            else:
                eating = new_head == food
                body_to_check = snake if eating else snake[:-1]

                if new_head in body_to_check:
                    game_over = True
                else:
                    snake.insert(0, new_head)

                    if eating:
                        score += 10
                        food = generate_food(snake, fixed_foods)
                    else:
                        snake.pop()

        screen.fill((20, 20, 30))

        score_text = font.render(
            f"Score: {score}", True, (255, 255, 255)
        )
        screen.blit(score_text, (MARGIN, 15))
        
        if paused:
            pause_text = font.render("PAUSED",True, (255,255,0))
            screen.blit(pause_text, (150,200))

        # Draw the grid
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                rect = pygame.Rect(
                    MARGIN + x * CELL_SIZE,
                    HEADER + MARGIN + y * CELL_SIZE,
                    CELL_SIZE, CELL_SIZE
                )
                pygame.draw.rect(screen, (65, 65, 75), rect, 1)

        # Draw food
        if food is not None:
            pygame.draw.circle(
                screen, (255, 60, 60),
                (
                    MARGIN + food[0] * CELL_SIZE + CELL_SIZE // 2,
                    HEADER + MARGIN + food[1] * CELL_SIZE + CELL_SIZE // 2
                ),
                CELL_SIZE // 3
            )

        # Draw snake
        for index, (x, y) in enumerate(snake):
            rect = pygame.Rect(
                MARGIN + x * CELL_SIZE + 3,
                HEADER + MARGIN + y * CELL_SIZE + 3,
                CELL_SIZE - 6, CELL_SIZE - 6
            )
            color = (80, 255, 100) if index == 0 else (30, 180, 80)
            pygame.draw.rect(screen, color, rect, border_radius=8)

        if game_over:
            message = font.render(
                "GAME OVER! Close the window.",
                True, (255, 80, 80)
            )
            screen.blit(message, (MARGIN, HEIGHT - 30))

        pygame.display.flip()
        clock.tick(2)  

    pygame.quit()
        
        
    
def generate_food(snake, fixed_foods):
    if fixed_foods:
        position = fixed_foods.pop(0)
        if position not in snake:
             return position
    available = [
        (x,y)
        for x in range(GRID_SIZE)
        for y in range(GRID_SIZE)
        if(x,y) not in snake
    ]
    return random.choice(available) if available else None
def play_snake(moves):
    snake = [(5,5)]
    direction = "R"
    score = 0
    game_over = False
    
    fixed_foods = [(7,5),(0,0)]
    food =generate_food(snake,fixed_foods)
    
    for key in moves:
        key = key.strip().upper()
        if key not in DIRECTIONS:
            print("Invalid key. Use R,L,,U or D.")
            continue
        if key==OPPOSITE[direction]:
            print(
                f"Reverse move not allowed."
                f"Snake continues {direction}."
            )
        else:
            direction = key
        
        dx,dy = DIRECTIONS[direction]
        head_x, head_y = snake[0]
        new_head = (head_x +dx,head_y+dy)    
        
        x,y = new_head
        
        if  not(0<= x< GRID_SIZE and 0 <= y < GRID_SIZE):
            print(f"GAME OVER! Wall hit at {new_head}.")
            game_over = True
            break
        eating = new_head == food
        body_to_check = snake if eating else snake[:-1]
        
        if new_head in body_to_check:
            print(f"GAME OVER! Snake eat itself at {new_head}.")
            game_over = True
            break
        
        snake.insert(0,new_head)
        
        if eating:
            score+=10
            print(f"Food eaten at {food}! Score: {score}")
            food = generate_food(snake, fixed_foods)
            
        else:
            snake.pop()
            print(f"Head:{snake[0]}")
    
    
    display_game(snake,food,score)
    print(f"Length: {len(snake)}| Head:{snake[0]}")
    print(f"Final score: {score}")
    
if __name__ == "__main__":
    
    display_game()