import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

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
result_message = ""
show_statistics = False

button_width = 100
button_height = 150
rock_button = pygame.Rect(80, 180, button_width, button_height)
paper_button = pygame.Rect(255, 180, button_width, button_height)
scissors_button = pygame.Rect(430, 180, button_width, button_height)

yes_button = pygame.Rect(200, 250, 100, 50)
no_button = pygame.Rect(320, 250, 100, 50)
exit_button = pygame.Rect(250, 400, 100, 50)

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

def display_statistics():
    win_percentage = math.ceil((wins / games_played) * 100) if games_played > 0 else 0
    screen.fill(WHITE)
    draw_text(f"Thanks for playing!", font, GREEN, 200, 50)
    
    draw_text(f"You played {games_played} game{'s' if games_played > 1 else ''}.", font, BLACK, 50, 100)
    draw_text(f"Wins: {wins}, Draws: {draws}, Losses: {loses}", font, BLACK, 50, 140)
    draw_text(f"Your win percentage is: {win_percentage}%", font, BLACK, 50, 180)
    draw_text(f"Rock played - {rock_count}", font, BLACK, 50, 220)
    draw_text(f"Paper played - {paper_count}", font, BLACK, 50, 260)
    draw_text(f"Scissors played - {scissors_count}", font, BLACK, 50, 300)
    draw_text("Better luck next time!", font, GREEN, 200, 340)
    
    pygame.draw.rect(screen, RED, exit_button)
    draw_text("Exit", font, WHITE, exit_button.x + 25, exit_button.y + 10)
    
    pygame.display.flip()

playing = True
ask_play_again = False

while playing:
    if show_statistics:
        display_statistics()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    playing = False  
                    
    elif not ask_play_again:
        screen.fill(WHITE)
    
        screen.blit(rock_image, rock_button)
        screen.blit(paper_image, paper_button)
        screen.blit(scissors_image, scissors_button)
        
        draw_text("Rock", font, BLACK, rock_button.x + 25, rock_button.y + button_height + 10)
        draw_text("Paper", font, BLACK, paper_button.x + 25, paper_button.y + button_height + 10)
        draw_text("Scissors", font, BLACK, scissors_button.x + 10, scissors_button.y + button_height + 10)
        
        draw_text(f"Games played: {games_played}", font, BLACK, 20, 20)   
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            
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
                    result_message = "You win!"
                elif player_move == computer_move:
                    draws += 1
                    result_message = "It's a draw!"
                else:
                    loses += 1
                    result_message = "You lose!"
                
                games_played += 1
                ask_play_again = True
    
    elif ask_play_again:
        screen.fill(WHITE)
        draw_text("Do you want to play again?", font, BLACK, 180, 150)

        draw_text(result_message, font, BLACK, 180, 50)
        draw_text(f"You chose: {player_move}", font, BLACK, 180, 90)
        draw_text(f"Computer chose: {computer_move}", font, BLACK, 180, 130)
        draw_text(f"Games played: {games_played}", font, BLACK, 180, 170)

        pygame.draw.rect(screen, GREEN, yes_button)
        pygame.draw.rect(screen, RED, no_button)
        draw_text("Yes", font, BLACK, yes_button.x + 25, yes_button.y + 10)
        draw_text("No", font, BLACK, no_button.x + 35, no_button.y + 10)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_button.collidepoint(event.pos):
                    ask_play_again = False 
                elif no_button.collidepoint(event.pos):
                    show_statistics = True
    
    pygame.display.flip()

pygame.quit()