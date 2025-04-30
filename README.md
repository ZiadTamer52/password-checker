# 🔐 Password Strength Checker

![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Python Version](https://img.shields.io/badge/python-3.x-blue)

A terminal-based password strength checker built with Python. It analyzes the strength of a password, provides improvement tips, and estimates how long it would take to crack it using brute-force attacks.

---

## 🧰 Features

- Hidden password input using `getpass`
- Strength classification: **Weak**, **Moderate**, or **Strong**
- Suggestions to improve weak or moderate passwords
- Estimated time to crack based on brute-force attack speed
- Color-coded output for better readability (via `colorama`)

---

## 🚀 Getting Started

### 1. Clone the repository or download the file

```bash
git clone https://github.com/YourUsername/password-checker.git
cd password-checker
```
### 2. Install the required library
This project uses colorama for terminal colors. You can install it via pip:
```bash
pip install colorama
```
### 3. Run the script
```bash
python password_checker.py
```
### How would it look like:
```bash
🔐 Password Strength Checker 🔐
Enter your password:
✅ Password Strength: Strong

Suggestions to improve:
- Add special characters (e.g., !, @, #, etc.).

🧠 Estimated time to crack: 1,234.56 years
```
## 🧠 How It Works

This Password Strength Checker evaluates your password on multiple criteria and estimates how long it would take to crack it using brute-force techniques. Here's how it works:

#### 1. **Password Strength Analysis**
The tool checks your password based on the following criteria:

- **Minimum Length**: The password should be at least 8 characters long.
- **Uppercase Letters**: At least one uppercase letter (A-Z).
- **Lowercase Letters**: At least one lowercase letter (a-z).
- **Numbers**: At least one digit (0-9).
- **Special Characters**: At least one special character (e.g., !, @, #, $, etc.).

For each of these criteria, the tool will assign a score. The more criteria your password meets, the stronger it is!

#### 2. **Strength Classification**
Based on the password evaluation, the tool classifies your password into one of three categories:

- **Strong**: Meets all 5 criteria.
- **Moderate**: Meets 3 or 4 criteria.
- **Weak**: Meets 2 or fewer criteria.

This classification is displayed with color-coded feedback to make it easier to understand at a glance.

#### 3. **Improvement Suggestions**
If your password is rated as **Moderate** or **Weak**, the tool will provide a list of suggestions to help you improve its strength. These tips are personalized based on which criteria your password is lacking.

#### 4. **Time to Crack Estimation**
The tool calculates how long it would take to crack your password using brute-force techniques. It assumes an attacker can attempt **100 billion guesses per second**.

The time to crack is estimated based on:
- **Password Length**: The longer the password, the more combinations an attacker has to try.
- **Character Set**: The more diverse your password is (e.g., using uppercase, lowercase, numbers, and special characters), the more possible combinations there are.

The result is displayed in a human-readable format (e.g., years, days, or minutes) to give you a sense of how safe your password really is.
---
## 🔒 Disclaimer

This tool is for educational and testing purposes only. It does **not** store or transmit any passwords.

## 👨‍💻 Author

- **Shadow** (aka Ziad)
- GitHub: [ZiadTamer52](https://github.com/ZiadTamer52)

## 📜 License

  This project is open-source and free to use under the [MIT License](LICENSE).








