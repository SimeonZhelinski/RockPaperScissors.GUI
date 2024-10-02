import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

font = pygame.font.Font(None, 36)

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
games_played = 0
wins = 0
draws = 0
loses = 0
rock_count = 0
paper_count = 0
scissors_count = 0
player_move = ""
computer_move = ""

button_width = 100
button_height = 150
rock_button = pygame.Rect(80, 180, button_width, button_height)
paper_button = pygame.Rect(255, 180, button_width, button_height)
scissors_button = pygame.Rect(430, 180, button_width, button_height)

rock_image = pygame.image.load("rock.png")
paper_image = pygame.image.load("paper.png")
scissors_image = pygame.image.load("scissors.png")

rock_image = pygame.transform.scale(rock_image, (button_width, button_height))
paper_image = pygame.transform.scale(paper_image, (button_width, button_height))
scissors_image = pygame.transform.scale(scissors_image, (button_width, button_height))


def draw_text(text, font, color, x, y):
    text_obj = font.render(text, True, color)
    screen.blit(text_obj, (x, y))

def get_computer_move():
    moves = [rock, paper, scissors]
    return random.choice(moves)

running = True
while running:
    screen.fill(WHITE)
    
    screen.blit(rock_image, rock_button)
    screen.blit(paper_image, paper_button)
    screen.blit(scissors_image, scissors_button)
    
    draw_text(f"Games played: {games_played}", font, BLACK, 20, 20)
    draw_text(f"Wins: {wins}, Draws: {draws}, Losses: {loses}", font, BLACK, 20, 60)
    
    if player_move and computer_move:
        draw_text(f"Player: {player_move} vs Computer: {computer_move}", font, BLACK, 20, 100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rock_button.collidepoint(event.pos):
                player_move = rock
                rock_count += 1
            elif paper_button.collidepoint(event.pos):
                player_move = paper
                paper_count += 1
            elif scissors_button.collidepoint(event.pos):
                player_move = scissors
                scissors_count += 1
            else:
                continue
            
            computer_move = get_computer_move()
            
            if (player_move == rock and computer_move == scissors) or \
               (player_move == paper and computer_move == rock) or \
               (player_move == scissors and computer_move == paper):
                wins += 1
            elif player_move == computer_move:
                draws += 1
            else:
                loses += 1
            
            games_played += 1
    
    pygame.display.flip()

pygame.quit()
