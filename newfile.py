import time # Add this at the top with 'import random'
import os

# --- Inside run_redcode(line) ---

    # --- INPUT COMMAND ---
    elif command == "INPUT":
        # Usage: INPUT name What is your name?
        if len(tokens) < 3:
            print("Error: INPUT needs a variable and a prompt.")
        else:
            var_name = tokens[1]
            prompt = " ".join(tokens[2:])
            variables[var_name] = input(f"{prompt} ")

    # --- SLEEP COMMAND ---
    elif command == "SLEEP":
        # Usage: SLEEP 2 (pauses for 2 seconds)
        try:
            time.sleep(float(tokens[1]))
        except:
            print("Error: SLEEP needs a number of seconds.")

    # --- CLEAR COMMAND ---
    elif command == "CLEAR":
        # Clears the Pydroid terminal screen
        print("\033[H\033[J", end="") 

import random  # Required for the RANDOM command

variables = {}

# ANSI Color Codes for the terminal
COLORS = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "BLUE": "\033[34m",
    "YELLOW": "\033[33m",
    "RESET": "\033[0m"
}

def run_redcode(line):
    tokens = line.split()
    if not tokens: return

    command = tokens[0].upper()

    # --- RANDOM COMMAND ---
    # Usage: RANDOM var_name min max
    if command == "RANDOM":
        if len(tokens) < 4:
            print("Error: RANDOM needs a name, min, and max! (Example: RANDOM d6 1 6)")
        else:
            var_name = tokens[1]
            try:
                val = random.randint(int(tokens[2]), int(tokens[3]))
                variables[var_name] = val
                print(f"Randomized {var_name}: {val}")
            except ValueError:
                print("Error: Min and Max must be numbers.")

    # --- COLOR COMMAND ---
    # Usage: COLOR RED
    elif command == "COLOR":
        color_name = tokens[1].upper() if len(tokens) > 1 else "RESET"
        if color_name in COLORS:
            print(COLORS[color_name], end="")
        else:
            print(f"Unknown color. Use: {', '.join(COLORS.keys())}")

    # --- REPEAT COMMAND ---
    elif command == "REPEAT":
        if len(tokens) >= 3:
            try:
                for _ in range(int(tokens[1])):
                    run_redcode(" ".join(tokens[2:]))
            except: print("Error in REPEAT")

    # --- SET COMMAND ---
    elif command == "SET":
        if len(tokens) >= 3:
            variables[tokens[1]] = tokens[2]

    # --- PRINT COMMAND ---
    elif command == "PRINT":
        content = tokens[1:]
        output = [str(variables.get(word, word)) for word in content]
        print(" ".join(output))

    else:
        print(f"Unknown: {command}")

# Main Shell
print("RedCode v2.3 Ready! Commands: RANDOM, COLOR, REPEAT, SET, PRINT")
while True:
    try:
        user_input = input("RedCode > ")
        if user_input.upper() == "EXIT": break
        run_redcode(user_input)
    except Exception as e:
        print(f"Error: {e}")
