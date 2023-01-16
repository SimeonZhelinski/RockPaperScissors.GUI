import math
import random
from colorama import Fore

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
another_game = ""
games_played = 0
wins = 0
draws = 0
loses = 0
win_percentage = 0
rock_count = 0
paper_count = 0
scissors_count = 0

while another_game != "n":
    player_move = input(Fore.LIGHTWHITE_EX + "Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
        rock_count += 1
    elif player_move == "p":
        player_move = paper
        paper_count += 1
    elif player_move == "s":
        player_move = scissors
        scissors_count += 1
    else:
        print("Invalid Input. Try again...")
        continue

    computer_random_number = random.randint(1, 3)
    computer_move = ""
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(Fore.CYAN + f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        wins += 1
        print(Fore.GREEN + "You win!")
    elif player_move == computer_move:
        print(Fore.YELLOW + "Draw!")
        draws += 1
    else:
        print(Fore.RED + "You lose!")
        loses += 1
    games_played += 1
    another_game = input(Fore.LIGHTBLUE_EX + "Do you want to play again: [y]es or [n]o: ")
    while True:
        if another_game == "y":
            break
        elif another_game == "n":
            break
        else:
            print("Invalid Input. Try again ...")
            another_game = input(Fore.LIGHTBLUE_EX + "Do you want to play again: [y]es or [n]o: ")

win_percentage = wins / games_played * 100
print()
print(Fore.GREEN + "Thanks for playing !")
print()
if games_played > 1:
    print(Fore.WHITE + f"You played {games_played} games.")
else:
    print(Fore.WHITE + f"You played {games_played} game.")
if wins > 1:
    print(Fore.GREEN + f"You've managed to Win {wins} times !")
else:
    print(Fore.GREEN + f"You've managed to Win {wins} time !")
if draws > 1:
    print(Fore.YELLOW + f"You Drew {draws} times")
else:
    print(Fore.YELLOW + f"You Drew {draws} time")
if loses > 1:
    print(Fore.RED + f"and you've Lost {loses} times.")
else:
    print(Fore.RED + f"and you've Lost {loses} time.")

print()
print(Fore.WHITE + f"Your win percentage is: {math.ceil(win_percentage)}% !")
print()
print("   Statistics:")
print(f"Rock played - {rock_count}")
print(f"Paper played - {paper_count}")
print(f"Scissors played - {scissors_count}")
print()
print(Fore.LIGHTGREEN_EX + "Better luck next time !")
