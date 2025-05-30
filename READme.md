# Phase-3-Project-
# QuizMaster

QuizMaster is a simple terminal-based quiz game written in Python.  
Users can take quizzes on various topics, track their scores, and see their past quiz attempts. Data is stored in an SQLite database.


## Features

- Command-line interface for playing quizzes
- User registration and lookup by name
- Tracks each quiz attempt with score
- Stores data persistently in SQLite
- Easy to extend with new questions and features


## Project Structure

QuizMaster/
│
├── Pipfile
├── Pipfile.lock
├── README.md
│
├── lib/
│ ├── models/
│ │ ├── init.py 
│ │ ├── user.py 
│ │ ├── attempt.py 
│ │
│ ├── cli.py 
│ ├── debug.py 
│ ├── seed.py 
│ ├── helper.py 

## Installation

1. Clone the repo:
   git clone https://github.com/BILLADAMS-arch/Phase-3-Project-
   cd QuizMaster

## (Optional) Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
## Currently, the project uses only Python’s standard library (sqlite3).

## Usage
Create the database tables by running:
python3 lib/debug.py
Start the quiz game:
python3 lib/cli.py
Follow the prompts to enter your name and answer quiz questions.
Your score will be saved and tracked for future sessions.

## How It Works
When you enter your name, the app checks if you already exist in the database.

-If not, a new user record is created.

-The quiz questions are loaded from lib/seed.py.

-For each question, you type your answer.

-Your score is calculated and saved in the quiz_attempts table.

## Author
Your Name – nyamweno.billadams@gmail.com
GitHub: BILLADAMS-arch

