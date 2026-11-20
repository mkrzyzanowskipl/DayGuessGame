#!/usr/bin/env python3
import datetime
import random
import calendar
import os
import time
import sys
import re

# ANSI color codes
DARK_BG = '\033[8;2;0;0;0m'  # Dark background (black)
LIGHT_FRAME = '\033[1;36m'   # Cyan for frames

CORRECT_COLOR = '\033[92m'
INCORRECT_COLOR = '\033[91m'
RESET_COLORS = '\033[0m'

# Initialize game state
start_time = time.time()
correct_guesses = 0
total_attempts = 0

# Create a dictionary for day abbreviations
day_abbreviations = {
    'mn': 'Monday',
    'ty': 'Tuesday',
    'we': 'Wednesday',
    'tr': 'Thursday',
    'fr': 'Friday',
    'sa': 'Saturday',
    'sd': 'Sunday'
}

def get_random_date():
    year = random.randint(1000, 2500)
    month = random.randint(1, 12)
    _, num_days = calendar.monthrange(year, month)
    day = random.randint(1, num_days)
    return (year, month, day)

def print_centered(message):
    terminal_width = os.get_terminal_size().columns - 1  # Adjust by -1 column
    padding = ' ' * ((terminal_width - len(message)) // 2)
    frame = f"{LIGHT_FRAME}╔{('═' * (len(message) + 2))}╗"
    return_frame = f" {message} "
    print(f"{LIGHT_FRAME}{padding}{return_frame}{padding}{LIGHT_FRAME}\033[0m")

def update_top_bar():
    elapsed_time = int(time.time() - start_time)
    minutes, seconds = divmod(elapsed_time, 60)
    
    # Calculate percentage of correct answers
    if total_attempts > 0:
        percent_correct = (correct_guesses / total_attempts) * 100
    else:
        percent_correct = 0.0
    
    time_str = f"Time: {minutes:02d}:{seconds:02d}"
    
    # Clear previous top bar and reset terminal mode
    print('\033]8;;\a')  # Reset hyperlink escape sequence
    os.system('clear')
    
    # Print new top bar with additional stats, adjusted by -1 column
    print(f"{LIGHT_FRAME}╔═════════════════════════════════ - - - - Day Guess Game - - - - ═════════════════════════════════╗")
    print("\033[1;36m║                                                                            \033[22mby\033[97mElusiveNightSnake\033[1;36m## ║\033[0m")
    print("\033[1;36m║ ***********************                                                  *********************** ║\033[0m")
    print("\033[1;36m║                                                                                                  ║\033[0m")
    print(f"\033[?7l{LIGHT_FRAME}║ {time_str} | Correct: {correct_guesses}/{total_attempts}                                                                        ║{RESET_COLORS}\033[?7h")
    print("\033[1;36m║                                                                                    \033[22myr\033[97m1000-2500\033[1;36m## ║\033[0m")
    print("\033[1;36m║ **************                                                                   *************** ║\033[0m")
    print("\033[1;36m║                                                                                                  ║\033[0m")
    print(f"\033[?7l{LIGHT_FRAME}║ {percent_correct:.1f}%                                                                                                        ║{RESET_COLORS}\033[?7h")
    print("\033[1;36m║                                                                                           \033[22mv\033[97m3.1\033[1;36m## ║\033[0m")
    print("\033[1;36m║ ********                                                                                ******** ║\033[0m")

while True:
    update_top_bar()
    
    # Generate and display date
    year, month, day = get_random_date()
    formatted_date = f"{year}-{month:02d}-{day:02d}"
    
    try:
        date_obj = datetime.date(year, month, day)
        weekday = date_obj.strftime('%A')
    except ValueError:
        continue
    
    print("\033[1;36m║                                                                                                  ║\033[0m")
    print(f"\033[1;36m║                           What was the day of the week on {formatted_date} ??                          ║\033[0m")
    print("\033[1;36m║                                                                                                  ║\033[0m")
    print("\033[1;36m║                 Type your answer ( mn, ty, we, tr, fr, sa, sd) and press Enter ..                ║\033[0m")
    print("\033[1;36m║                                                                                                  ║\033[0m")
    print("\033[1;36m║                                                                                                  ║\033[0m")
    print("\033[1;36m╚                                                                                                  ╝\033[0m")
    print("")
    
    print("\033[1;36m        >>>>>>>    ::  \033[0m", end="")
    user_guess = input().strip()
    total_attempts += 1
    print("")
    
    # Convert abbreviation to full day name if needed
    guessed_day = day_abbreviations.get(user_guess.lower(), user_guess.capitalize())
    
    if guessed_day == weekday:
        correct_guesses += 1
        result = f"{CORRECT_COLOR}√ Correct!{RESET_COLORS}"
    else:
        result = f"{INCORRECT_COLOR}× Incorrect!{RESET_COLORS} The correct day is {weekday}.{RESET_COLORS}"
    
    print_centered(result)
    
    # Check if user wants to play again
    print("")
    play_again = input("\n\033[1;36m        >>>>>>>    ::\033[0m  Press Enter to play again... ").strip().lower()
    if play_again == 'q':
        break
    

# Reset terminal and display final message
os.system('clear')
print(f"\nThank you for playing, goodbye!  :)")
