import random
import string
import os
import sys
import datetime
import collections
import json
import re
import urllib.request
import sqlite3
import csv
import argparse
import pickle
import subprocess
import time

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def guess_the_number():
    clear_terminal()
    print("Guess the Number Game:\n"
          "I will generate a random number between 1 and 100.\n"
          "You need to guess the number and I will provide hints (higher or lower) until you guess correctly.")
    number = random.randint(1, 100)
    guess = None
    attempts = 0
    while guess != number:
        try:
            guess = int(input("Guess the number (between 1 and 100): "))
            attempts += 1
            if guess < number:
                print("Higher!")
            elif guess > number:
                print("Lower!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def math_quiz():
    clear_terminal()
    print("Math Quiz Game:\n"
          "I will generate random math questions (addition, subtraction, multiplication, etc.).\n"
          "You need to solve these questions within a time limit, and I will keep track of your score.")
    score = 0
    num_questions = 5
    for _ in range(num_questions):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*', '/'])
        question = f"What is {num1} {operator} {num2}? "
        answer = eval(str(num1) + operator + str(num2))
        try:
            user_answer = float(input(question))
            if user_answer == answer:
                score += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print(f"You scored {score} out of {num_questions}.")


def file_explorer():
    clear_terminal()
    print("File Explorer:\n"
          "You can navigate directories, list files, and perform basic file operations (copy, move, delete).")
    while True:
        path = input("Enter a directory path (or 'q' to quit): ")
        if path.lower() == 'q':
            break
        if not os.path.isdir(path):
            print("Invalid directory path.")
            continue
        clear_terminal()
        print("Contents of the directory:")
        for item in os.listdir(path):
            print(item)


def system_information():
    clear_terminal()
    print("System Information:\n"
          "I will display information about your system, such as the Python version, operating system, and command-line arguments.")
    print(f"Python Version: {sys.version}")
    print(f"Operating System: {sys.platform}")
    print(f"Command-Line Arguments: {sys.argv}")


def date_and_time_quiz():
    clear_terminal()
    print("Date and Time Quiz:\n"
          "I will generate random date and time questions.\n"
          "You need to answer questions about dates, time zones, and date arithmetic.")
    num_questions = 3
    score = 0
    for _ in range(num_questions):
        date = datetime.datetime.now() + datetime.timedelta(days=random.randint(-10, 10))
        question = f"What is the date {date.strftime('%Y-%m-%d')} {random.choice(['before', 'after'])} today? "
        user_answer = input(question)
        correct_answer = 'before' if date < datetime.datetime.now() else 'after'
        if user_answer.lower() == correct_answer:
            score += 1
    print(f"You scored {score} out of {num_questions}.")


def word_frequency_counter():
    clear_terminal()
    print("Word Frequency Counter:\n"
          "I will read a text file and count the occurrences of each word.\n"
          "Then, I will display the most common words.")
    file_path = input("Enter the path to a text file: ")
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            word_counts = collections.Counter(words)
        print("Most common words:")
        for word, count in word_counts.most_common(5):
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")


def json_data_quiz():
    clear_terminal()
    print("JSON Data Quiz:\n"
          "I will load a JSON file and ask you questions based on the data in the file.")
    file_path = input("Enter the path to a JSON file: ")
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        score = 0
        num_questions = 3
        for _ in range(num_questions):
            question = random.choice(list(data.keys()))
            correct_answer = data[question]
            user_answer = input(f"{question}: ")
            if user_answer.lower() == correct_answer.lower():
                score += 1
        print(f"You scored {score} out of {num_questions}.")
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON file.")


def regex_pattern_matcher():
    clear_terminal()
    print("Regex Pattern Matcher:\n"
          "I will challenge you to match strings to predefined regular expressions.\n"
          "I will provide feedback on whether the strings match the patterns.")
    patterns = {
        r'\d{3}-\d{3}-\d{4}': 'Phone Number (###-###-####)',
        r'\w+@\w+\.\w+': 'Email Address (example@example.com)',
        r'[A-Z][a-z]+': 'Capitalized Word',
    }
    for _ in range(3):
        pattern = random.choice(list(patterns.keys()))
        description = patterns[pattern]
        string = input(f"Enter a string that matches the pattern '{description}': ")
        if re.match(pattern, string):
            print("Match!")
        else:
            print("No match.")


def web_page_scraper():
    clear_terminal()
    print("Web Page Scraper:\n"
          "I will fetch content from a web page using the urllib module.\n"
          "You can extract specific information, such as headlines or weather data, and I will display it to you.")
    url = input("Enter the URL of a web page: ")
    try:
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        # Perform scraping or extract specific information from the content
        print(content)
    except urllib.error.URLError:
        print("Invalid URL or unable to access the web page.")


def database_query_game():
    clear_terminal()
    print("Database Query Game:\n"
          "I will create a SQLite database with a set of tables.\n"
          "You can query the database for specific information, such as retrieving records or performing calculations.")
    connection = sqlite3.connect('game_database.db')
    cursor = connection.cursor()
    while True:
        query = input("Enter a SQL query (or 'q' to quit): ")
        if query.lower() == 'q':
            break
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    connection.close()


def csv_data_analyzer():
    clear_terminal()
    print("CSV Data Analyzer:\n"
          "I will load a CSV file and allow you to perform operations on the data.\n"
          "You can sort, filter, or generate statistics based on the data.")
    file_path = input("Enter the path to a CSV file: ")
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        # Perform operations on the data, such as sorting, filtering, or generating statistics
        print(data)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")


def command_line_adventure():
    clear_terminal()
    print("Command-Line Adventure:\n"
          "I will build a text-based adventure game that uses the argparse module to accept player commands.\n"
          "You can navigate through the story and interact with the game using command-line commands.")
    parser = argparse.ArgumentParser(description="Text-Based Adventure Game")
    parser.add_argument("action", choices=['go', 'look', 'take'], help="Action to perform")
    parser.add_argument("target", help="Target of the action")
    args = parser.parse_args()
    # Implement the game logic based on the player's commands


def serialization_challenge():
    clear_terminal()
    print("Serialization Challenge:\n"
          "I will demonstrate how to use the json module to serialize and deserialize Python objects.\n"
          "You can save and load game states using JSON.")
    game_state = {
        'score': 100,
        'level': 5,
        'inventory': ['sword', 'shield', 'potion'],
    }
    # Save game state to a JSON file and load it back


def object_serialization_puzzle():
    clear_terminal()
    print("Object Serialization Puzzle:\n"
          "I will create a game where you must serialize and deserialize complex Python objects using the pickle module.\n"
          "You need to solve puzzles by correctly serializing and deserializing objects.")

    class PuzzleObject:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return f"PuzzleObject({self.name})"

    puzzle_objects = [PuzzleObject('Object 1'), PuzzleObject('Object 2'), PuzzleObject('Object 3')]
    # Serialize the puzzle_objects using pickle and create a puzzle for the player to solve


def process_management_simulator():
    clear_terminal()
    print("Process Management Simulator:\n"
          "I will simulate a process management game where you can spawn, terminate, and communicate with virtual processes.\n"
          "You can perform various actions on the processes using the subprocess module.")
    processes = []
    while True:
        command = input("Enter a command (spawn, terminate, communicate, list, q): ")
        if command.lower() == 'q':
            break
        if command.lower() == 'spawn':
            process_name = input("Enter the name of the process: ")
            process = subprocess.Popen(['python', '-c', 'print("Hello from", input())'], stdin=subprocess.PIPE)
            processes.append((process_name, process))
        elif command.lower() == 'terminate':
            process_name = input("Enter the name of the process to terminate: ")
            for name, process in processes:
                if name == process_name:
                    process.terminate()
                    processes.remove((name, process))
        elif command.lower() == 'communicate':
            process_name = input("Enter the name of the process to communicate with: ")
            input_message = input("Enter the input message: ")
            for name, process in processes:
                if name == process_name:
                    process.stdin.write(input_message.encode())
                    process.stdin.flush()
        elif command.lower() == 'list':
            print("Running processes:")
            for name, process in processes:
                print(name)


def hangman():
    clear_terminal()
    print("Hangman Game:")
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    word = random.choice(words)
    guessed_letters = []
    max_attempts = 6
    attempts = 0
    while attempts < max_attempts:
        display_word = "".join([letter if letter in guessed_letters else '_' for letter in word])
        print(f"Word: {display_word}")
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print("Correct!")
        else:
            attempts += 1
            print(f"Wrong guess. Attempts remaining: {max_attempts - attempts}")
        if "_" not in display_word:
            print(f"Congratulations! You guessed the word: {word}")
            break
    if attempts == max_attempts:
        print(f"Out of attempts. The word was: {word}")


def tic_tac_toe():
    clear_terminal()
    print("Tic-Tac-Toe Game:")
    board = [" " for _ in range(9)]
    current_player = "X"
    game_over = False

    def print_board(board):
        for i in range(0, 9, 3):
            print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
            if i < 6:
                print("-" * 9)

    def check_winner(board):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            a, b, c = condition
            if board[a] == board[b] == board[c] != " ":
                return True
        return False

    while not game_over:
        clear_terminal()
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")
        if not move.isdigit() or not (1 <= int(move) <= 9) or board[int(move) - 1] != " ":
            print("Invalid move. Please try again.")
            continue
        board[int(move) - 1] = current_player
        if check_winner(board):
            clear_terminal()
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif " " not in board:
            clear_terminal()
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"


def snake_game():
    clear_terminal()
    print("Snake Game:")
    print("Use WASD keys to control the snake.")
    print("Eat the food ('@') to grow the snake.")
    print("Avoid running into the walls or yourself.")
    print("Press 'q' to quit the game.")

    # Define the game board size
    width = 20
    height = 10

    # Initialize snake position and direction
    snake_x = width // 2
    snake_y = height // 2
    snake_direction = 'RIGHT'

    # Initialize snake body
    snake_body = [{'x': snake_x, 'y': snake_y}]

    # Initialize food position
    food = {'x': random.randint(1, width - 2), 'y': random.randint(1, height - 2)}

    # Initialize the score
    score = 0

    # Game loop
    while True:
        clear_terminal()

        # Display the game board
        for y in range(height):
            for x in range(width):
                if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                    print('#', end=' ')
                elif {'x': x, 'y': y} == snake_body[0]:
                    print('O', end=' ')
                elif {'x': x, 'y': y} in snake_body[1:]:
                    print('o', end=' ')
                elif x == food['x'] and y == food['y']:
                    print('@', end=' ')
                else:
                    print(' ', end=' ')
            print()

        # Get user input
        key = input()

        # Handle user input
        if key == 'q':
            break
        elif key == 'a' and snake_direction != 'RIGHT':
            snake_direction = 'LEFT'
        elif key == 'd' and snake_direction != 'LEFT':
            snake_direction = 'RIGHT'
        elif key == 'w' and snake_direction != 'DOWN':
            snake_direction = 'UP'
        elif key == 's' and snake_direction != 'UP':
            snake_direction = 'DOWN'

        # Update snake position
        if snake_direction == 'LEFT':
            snake_x -= 1
        elif snake_direction == 'RIGHT':
            snake_x += 1
        elif snake_direction == 'UP':
            snake_y -= 1
        elif snake_direction == 'DOWN':
            snake_y += 1

        # Check for collision with food
        if snake_x == food['x'] and snake_y == food['y']:
            # Increase the score and generate new food
            score += 1
            food = {'x': random.randint(1, width - 2), 'y': random.randint(1, height - 2)}

            # Extend the snake's body
            new_head = {'x': snake_x, 'y': snake_y}
            snake_body.insert(0, new_head)

        # Check for collision with walls or itself
        if (
            snake_x == 0
            or snake_x == width - 1
            or snake_y == 0
            or snake_y == height - 1
            or {'x': snake_x, 'y': snake_y} in snake_body[1:]
        ):
            print(f"Game Over! Your score: {score}")
            input("Press Enter to continue...")
            break

        # Move the snake
        new_head = {'x': snake_x, 'y': snake_y}
        snake_body.insert(0, new_head)

        # Remove the tail segment if not eating food
        if len(snake_body) > score + 1:
            del snake_body[-1]

def random_password(length, letters=True, numbers=True, symbols=True):
    characters = ''
    if letters:
        characters += string.ascii_letters
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def bubble_sort_visualizer():
    clear_terminal()
    print("Bubble Sort Visualizer")
    num_bars = 20  # You can change this to the number of bars you want to sort
    bars = [random.randint(1, 22) for _ in range(num_bars)]

    # Increment all bars by 1
    bars = [bar + 1 for bar in bars]

    def print_bars(bars):
        max_height = max(bars)
        for height in reversed(range(1, max_height + 1)):
            bar_line = ""
            for bar_height in bars:
                if bar_height >= height:
                    bar_line += "█ "
                else:
                    bar_line += "  "
            print(bar_line)

    while True:
        clear_terminal()
        print("Bubble Sort Visualizer")
        print_bars(bars)
        swapped = False
        for i in range(len(bars) - 1):
            if bars[i] > bars[i + 1]:
                bars[i], bars[i + 1] = bars[i + 1], bars[i]
                swapped = True
                time.sleep(0.06)  # Add a slight delay for visualization
                clear_terminal()
                print("Bubble Sort Visualizer")
                print_bars(bars)
        if not swapped:
            clear_terminal()
            break

    clear_terminal()
    print_bars(bars)  # Display the sorted bars
    input("Press Enter to continue...")

def main():
    while True:
        clear_terminal()
        print("Mini-Game Menu:")
        print("1. Guess the Number")
        print("2. Math Quiz")
        print("3. File Explorer")
        print("4. System Information")
        print("5. Date and Time Quiz")
        print("6. Word Frequency Counter")
        print("7. JSON Data Quiz")
        print("8. Regex Pattern Matcher")
        print("9. Web Page Scraper")
        print("10. Database Query Game")
        print("11. CSV Data Analyzer")
        print("12. Command-Line Adventure")
        print("13. Serialization Challenge")
        print("14. Object Serialization Puzzle")
        print("15. Process Management Simulator")
        print("16. Hangman")
        print("17. Tic-Tac-Toe")
        print("18. Snake Game")
        print("19. Random Password Maker")
        print("20. Bubble Sort Visualizer")
        print("21. Exit")
        
        choice = input("Enter the number of the mini-game you want to play (or '21' to exit): ")
        try:
            choice = int(choice)
            if choice == 1:
                guess_the_number()
            elif choice == 2:
                math_quiz()
            elif choice == 3:
                file_explorer()
            elif choice == 4:
                system_information()
            elif choice == 5:
                date_and_time_quiz()
            elif choice == 6:
                word_frequency_counter()
            elif choice == 7:
                json_data_quiz()
            elif choice == 8:
                regex_pattern_matcher()
            elif choice == 9:
                web_page_scraper()
            elif choice == 10:
                database_query_game()
            elif choice == 11:
                csv_data_analyzer()
            elif choice == 12:
                command_line_adventure()
            elif choice == 13:
                serialization_challenge()
            elif choice == 14:
                object_serialization_puzzle()
            elif choice == 15:
                process_management_simulator()
            elif choice == 16:
                hangman()
            elif choice == 17:
                tic_tac_toe()
            elif choice == 18:
                snake_game()
            elif choice == 19:
                length = int(input("Enter the length of the password: "))
                letters = input("Include letters? (y/n): ").lower() == 'y'
                numbers = input("Include numbers? (y/n): ").lower() == 'y'
                symbols = input("Include symbols? (y/n): ").lower() == 'y'
                password = random_password(length, letters, numbers, symbols)
                print(f"Generated password: {password}")
            elif choice == 20:  # Add the choice for the bubble sort visualizer
                bubble_sort_visualizer()
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
if __name__ == '__main__':
    main()
