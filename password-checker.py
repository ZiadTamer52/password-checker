'''
# Password Checker #
## Aouther: Ziad Tamer #
## Date: 2025-5-1 ##
## Description: This script checks the strength of a password and estimates the time it would take to crack it using brute force. It provides feedback on the password's strength and suggestions for improvement. The script uses regular expressions to check for various character types and calculates the number of possible combinations based on the length and character set used. ##
'''
import re
import getpass
import math
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# --- Password strength checker ---
def check_password_strength(password):
    suggestions = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Make it at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters (e.g., !, @, #, etc.).")

    if score == 5:
        return "Strong", suggestions
    elif score >= 3:
        return "Moderate", suggestions
    else:
        return "Weak", suggestions

# --- Time to crack estimation ---
def estimate_crack_time(password):
    guesses_per_sec = 1e11  # 100 billion guesses/sec
    length = len(password)

    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"\d", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    if charset == 0 or length == 0:
        return "Instantly (empty or invalid password)"

    combinations = math.pow(charset, length)
    time_seconds = combinations / guesses_per_sec

    return format_time(time_seconds)

def format_time(seconds):
    units = [("years", 60 * 60 * 24 * 365),
             ("days", 60 * 60 * 24),
             ("hours", 60 * 60),
             ("minutes", 60),
             ("seconds", 1)]
    
    for unit_name, unit_seconds in units:
        if seconds >= unit_seconds:
            value = seconds / unit_seconds
            return f"{value:,.2f} {unit_name}"
    return "less than a second"

# --- Main ---
if __name__ == "__main__":
    print("🔐 Password Strength Checker 🔐")
    password = getpass.getpass("Enter your password: ")
    strength, tips = check_password_strength(password)

    if strength == "Strong":
        print(Fore.GREEN + "✅ Password Strength: Strong")
    elif strength == "Moderate":
        print(Fore.YELLOW + "⚠️  Password Strength: Moderate")
    else:
        print(Fore.RED + "❌ Password Strength: Weak")

    if tips:
        print("\nSuggestions to improve:")
        for tip in tips:
            print(Fore.CYAN + f"- {tip}")

    crack_time = estimate_crack_time(password)
    print(f"\n🧠 Estimated time to crack: {Fore.MAGENTA}{crack_time}")
