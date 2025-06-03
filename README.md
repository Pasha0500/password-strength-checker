# 🔐 Cybersecurity Password Strength Checker

This is a simple CLI and Flask web application to evaluate the strength of user passwords. It scores passwords based on various criteria and provides suggestions for improving weak passwords.

## Features
- Password scoring system (0-5)
- Checks for:
  - Length
  - Uppercase & lowercase letters
  - Numbers
  - Special characters
  - Common password blacklist
- CLI & Web interface (Flask)
- Feedback and recommendations

## Installation
```bash
git clone https://github.com/Pasha0500/password-strength-checker.git
cd password-strength-checker
pip install -r requirements.txt
```

## Usage

### CLI
```bash
python main.py
```

### Web App
```bash
cd web
python app.py
```

## License
MIT
