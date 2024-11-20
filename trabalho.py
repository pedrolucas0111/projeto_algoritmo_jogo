import pygame
import random
pygame.init()

# Configurações de janela e cores
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CONFETTI_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 7

# Alterando as fontes para Arial
SCORE_FONT = pygame.font.SysFont("Arial", 50)
NAME_FONT = pygame.font.SysFont("Arial", 30)
WINNING_SCORE = 10

# Classes
class Paddle:
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        self.y += -self.VEL if up else self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y


class Ball:
    MAX_VEL = 5
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def increase_speed(self):
        self.x_vel *= 1.1
        self.y_vel *= 1.1

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel = self.MAX_VEL if self.x_vel < 0 else -self.MAX_VEL


def draw(win, paddles, ball, left_score, right_score, left_name, right_name):
    win.fill((34, 139, 34))  # Fundo verde claro

    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    win.blit(left_score_text, (WIDTH // 4 - left_score_text.get_width() // 2, 20))
    win.blit(right_score_text, (WIDTH * (3 / 4) - right_score_text.get_width() // 2, 20))

    left_name_text = NAME_FONT.render(left_name, 1, WHITE)
    right_name_text = NAME_FONT.render(right_name, 1, WHITE)
    win.blit(left_name_text, (10, 10))
    win.blit(right_name_text, (WIDTH - right_name_text.get_width() - 10, 10))

    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, HEIGHT, HEIGHT // 20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, BLACK, (WIDTH // 2 - 5, i, 10, HEIGHT // 20))  # Linha preta

    ball.draw(win)
    pygame.display.update()


def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= HEIGHT or ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:  # Indo para a esquerda
        if left_paddle.y <= ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1
                adjust_ball_velocity(ball, left_paddle)
    else:  # Indo para a direita
        if right_paddle.y <= ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1
                adjust_ball_velocity(ball, right_paddle)


def adjust_ball_velocity(ball, paddle):
    middle_y = paddle.y + paddle.height / 2
    difference_in_y = middle_y - ball.y
    reduction_factor = (paddle.height / 2) / ball.MAX_VEL
    y_vel = difference_in_y / reduction_factor
    ball.y_vel = -y_vel
    ball.increase_speed()


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)


def display_winner(win, text):
    confetti_count = 100
    confetti_positions = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(confetti_count)]

    for _ in range(50):  # Dura 50 frames
        win.fill(BLACK)
        
        # Confetes atrás da frase
        for pos in confetti_positions:
            pygame.draw.circle(win, random.choice(CONFETTI_COLORS), pos, 5)
        
        # Desenha a frase
        winner_text = SCORE_FONT.render(text, 1, WHITE)
        win.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - winner_text.get_height() // 2))

        pygame.display.update()
        pygame.time.delay(100)


def main():
    run = True
    clock = pygame.time.Clock()

    # Inicializando nomes
    left_name = ""
    right_name = ""

    while run:
        # Tela inicial para obter nomes apenas se necessário
        if not left_name or not right_name:
            left_name = input("Nome do Jogador da Esquerda: ")
            right_name = input("Nome do Jogador da Direita: ")

        left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

        left_score, right_score = 0, 0

        game_running = True
        while game_running:
            clock.tick(FPS)
            draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score, left_name, right_name)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    game_running = False

            keys = pygame.key.get_pressed()
            handle_paddle_movement(keys, left_paddle, right_paddle)

            ball.move()
            handle_collision(ball, left_paddle, right_paddle)

            if ball.x < 0:
                right_score += 1
                ball.reset()
            elif ball.x > WIDTH:
                left_score += 1
                ball.reset()

            if left_score >= WINNING_SCORE:
                display_winner(WIN, f"Vitória de {left_name}!")
                game_running = False
            elif right_score >= WINNING_SCORE:
                display_winner(WIN, f"Vitória de {right_name}!")
                game_running = False

        # Menu de fim de jogo
        menu_running = True
        while menu_running:
            WIN.fill(BLACK)
            restart_text = SCORE_FONT.render("Pressione R para Recomeçar", 1, WHITE)
            quit_text = SCORE_FONT.render("Pressione Q para Voltar", 1, WHITE)
            WIN.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 3))
            WIN.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    menu_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Jogar novamente
                        menu_running = False
                    elif event.key == pygame.K_q:  # Voltar ao início
                        menu_running = False
                        left_name = ""
                        right_name = ""
                        break


    pygame.quit()

if __name__ == '__main__':
    main()
