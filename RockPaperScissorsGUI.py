import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

LIGHT_GRAY = (199, 203, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
SHADOW_COLOR = (50, 50, 50)
BORDER_COLOR = (0, 0, 0)
DARK_GREEN = (0, 150, 0)
LIGHT_GREEN = (0, 200, 0)
DARK_RED = (180, 30, 30)
LIGHT_RED = (200, 0, 0)
color_message = ()
smaller_font = pygame.font.Font(None, 30)

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

yes_button = pygame.Rect(200, 320, 100, 50)
no_button = pygame.Rect(320, 320, 100, 50)
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
    draw_text(f"Thanks for playing!", font, BLUE, 180, 20)
    
    smaller_font.set_underline(True)
    draw_text(f"Statistics:", smaller_font, BLACK, 250, 70)
    smaller_font.set_underline(False)
    draw_text(f"You played {games_played} game{'s' if games_played > 1 else ''}.", smaller_font, BLACK, 50, 100)
    draw_text(f"Wins: {wins}", smaller_font, DARK_GREEN, 50, 140)
    draw_text(f"Draws: {draws}", smaller_font, BLUE, 160, 140) 
    draw_text(f"Losses: {loses}", smaller_font, DARK_RED, 270, 140)
    draw_text(f"Your win percentage is: {win_percentage}%", smaller_font, BLACK, 50, 180)
    draw_text(f"Rock played - {rock_count}", smaller_font, BLACK, 50, 220)
    draw_text(f"Paper played - {paper_count}", smaller_font, BLACK, 50, 260)
    draw_text(f"Scissors played - {scissors_count}", smaller_font, BLACK, 50, 300)
    draw_text("Better luck next time!", font, BLUE, 180, 350)
    
    pygame.draw.rect(screen, SHADOW_COLOR, (exit_button.x + 5, exit_button.y + 5, exit_button.width, exit_button.height))
    pygame.draw.rect(screen, BORDER_COLOR, (exit_button.x - 2, exit_button.y - 2, exit_button.width + 4, exit_button.height + 4))
    pygame.draw.rect(screen, LIGHT_RED, exit_button)
    
    draw_text("Exit", font, BLACK, exit_button.x + 25, exit_button.y + 15)
    
    pygame.display.flip()

playing = True
ask_play_again = False

while playing:
    screen.fill(LIGHT_GRAY)
    if show_statistics:
        display_statistics()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    playing = False  
                    
    elif not ask_play_again:
    
        screen.blit(rock_image, rock_button)
        screen.blit(paper_image, paper_button)
        screen.blit(scissors_image, scissors_button)
        
        draw_text("Rock", font, BLACK, rock_button.x + 25, rock_button.y + button_height + 10)
        draw_text("Paper", font, BLACK, paper_button.x + 25, paper_button.y + button_height + 10)
        draw_text("Scissors", font, BLACK, scissors_button.x + 10, scissors_button.y + button_height + 10)
        
        draw_text(f"Choose ROCK, PAPER or SCISSORS:", font, DARK_RED, 80, 80)   
        draw_text(f"Games played: {games_played}", font, BLACK, 200, 20)   
       
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
                    color_message = DARK_GREEN
                elif player_move == computer_move:
                    draws += 1
                    result_message = "It's a draw!"
                    color_message = BLUE
                else:
                    loses += 1
                    result_message = "You lose!"
                    color_message = DARK_RED
                
                games_played += 1
                ask_play_again = True
    
    elif ask_play_again:
        draw_text("Do you want to play again?", font, BLACK, 150, 200)

        draw_text(result_message, font, color_message, 250, 50)
        draw_text(f"You chose: {player_move}", font, BLACK, 200, 90)
        draw_text(f"Computer chose: {computer_move}", font, BLACK, 150, 130)
        draw_text(f"Games played: {games_played}", font, BLACK, 210, 250)
        
        pygame.draw.rect(screen, SHADOW_COLOR, (yes_button.x + 5, yes_button.y + 5, yes_button.width, yes_button.height))
        pygame.draw.rect(screen, BORDER_COLOR, (yes_button.x - 2, yes_button.y - 2, yes_button.width + 4, yes_button.height + 4))
        pygame.draw.rect(screen, LIGHT_GREEN, yes_button)
        
        pygame.draw.rect(screen, SHADOW_COLOR, (no_button.x + 5, no_button.y + 5, no_button.width, no_button.height))
        pygame.draw.rect(screen, BORDER_COLOR, (no_button.x - 2, no_button.y - 2, no_button.width + 4, no_button.height + 4))
        pygame.draw.rect(screen, LIGHT_RED, no_button)
        
        draw_text("Yes", font, BLACK, yes_button.x + 30, yes_button.y + 15)
        draw_text("No", font, BLACK, no_button.x + 35, no_button.y + 15)
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