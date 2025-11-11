import random
import pygame
import sys

# ---------- SNAKE GAME WITH RESTART & HIGH SCORE ----------
def snake_game():
    pygame.init()
    width, height = 500, 400
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("🐍 Snake Game - Professional Look")

    font = pygame.font.SysFont("consolas", 22, bold=True)
    clock = pygame.time.Clock()

    def draw_text(text, color, x, y):
        label = font.render(text, True, color)
        win.blit(label, (x, y))

    def draw_grid():
        for x in range(0, width, 10):
            pygame.draw.line(win, (40, 40, 40), (x, 0), (x, height))
        for y in range(0, height, 10):
            pygame.draw.line(win, (40, 40, 40), (0, y), (width, y))

    def run_game():
        x, y = 60, 60
        vel = 10
        snake = [[x, y]]
        food = [random.randrange(0, width-10, 10), random.randrange(0, height-10, 10)]
        direction = 'RIGHT'
        score = 0

        if hasattr(snake_game, "high_score"):
            high_score = snake_game.high_score
        else:
            snake_game.high_score = 0
            high_score = 0

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return  # <-- return instead of exit

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and direction != 'RIGHT': direction = 'LEFT'
            if keys[pygame.K_RIGHT] and direction != 'LEFT': direction = 'RIGHT'
            if keys[pygame.K_UP] and direction != 'DOWN': direction = 'UP'
            if keys[pygame.K_DOWN] and direction != 'UP': direction = 'DOWN'

            if direction == 'LEFT': x -= vel
            elif direction == 'RIGHT': x += vel
            elif direction == 'UP': y -= vel
            elif direction == 'DOWN': y += vel

            # WALL HIT
            if x < 0 or y < 0 or x >= width or y >= height:
                return score

            snake.append([x, y])

            # FOOD HIT
            if [x, y] == food:
                score += 1
                food = [random.randrange(0, width-10, 10), random.randrange(0, height-10, 10)]
            else:
                del snake[0]

            # SELF HIT
            if [x, y] in snake[:-1]:
                return score

            win.fill((15, 15, 15))
            draw_grid()

            for part in snake:
                pygame.draw.rect(win, (0, 255, 130), (part[0], part[1], 10, 10))

            pygame.draw.rect(win, (255, 80, 80), (food[0], food[1], 10, 10))

            draw_text(f"Score: {score}", (200, 200, 200), 10, 10)
            draw_text(f"High Score: {snake_game.high_score}", (200, 200, 0), width - 180, 10)

            pygame.display.update()
            clock.tick(10) 

    while True:
        score = run_game()
        if score is None:
            return

        if score > getattr(snake_game, "high_score", 0):
            snake_game.high_score = score

        win.fill((20, 20, 20))
        draw_text("GAME OVER", (255, 60, 60), width//2 - 80, height//2 - 40)
        draw_text(f"Your Score: {score}", (255, 255, 255), width//2 - 80, height//2)
        draw_text(f"High Score: {snake_game.high_score}", (255, 255, 0), width//2 - 95, height//2 + 30)
        draw_text("Press R = Restart   |   Q = Quit", (180, 180, 180), width//2 - 150, height//2 + 70)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        break
                    if event.key == pygame.K_q:
                        return
            else:
                continue
            break

# ---------- ROCK PAPER SCISSORS ----------
def rock_paper_scissors():
    print("\nRock Paper Scissors Game")
    choices = ["rock", "paper", "scissors"]
    while True:
        user = input("Enter rock, paper or scissors (or q to quit): ").lower()
        if user == 'q':
            break
        if user not in choices:
            print("Invalid input! Try again.")
            continue
        comp = random.choice(choices)
        print("Computer chose:", comp)
        if user == comp:
            print("It's a tie!")
        elif (user == "rock" and comp == "scissors") or \
             (user == "paper" and comp == "rock") or \
             (user == "scissors" and comp == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

# ---------- QUIZ GAME ----------
def quiz_game():
    print("\nCoding Quiz Game (Choose A/B/C/D)")
    questions = [
        {"q": "1. Output of print(2*3*2)?", "options": ["A. 64", "B. 12", "C. 8", "D. 16"], "ans": "B"},
        {"q": "2. Which keyword defines a function?", "options": ["A. func", "B. define", "C. def", "D. lambda"], "ans": "C"},
        {"q": "3. Type of 3/2 ?", "options": ["A. int", "B. float", "C. double", "D. complex"], "ans": "B"},
        {"q": "4. Mutable type?", "options": ["A. tuple", "B. list", "C. string", "D. int"], "ans": "B"},
        {"q": "5. break does?", "options": ["A. Restarts loop", "B. Ends loop", "C. Skips iteration", "D. Exit program"], "ans": "B"}
    ]
    score = 0
    for item in questions:
        print("\n" + item["q"])
        for opt in item["options"]:
            print(opt)
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        if ans == item["ans"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!", "Correct:", item["ans"])
    print("\nYour final score:", score, "/", len(questions))

# ---------- MAIN ----------
def main():
    while True:
        print("\n--- 🎮 GAME ZONE ---")
        print("1. Snake Game")
        print("2. Rock Paper Scissors")
        print("3. Quiz Game")
        print("4. Exit")
        ch = input("Enter choice: ")
        if ch == '1': snake_game()
        elif ch == '2': rock_paper_scissors()
        elif ch == '3': quiz_game()
        elif ch == '4':
            print("Bye 👋"); sys.exit()
        else:
            print("Invalid!")

main()