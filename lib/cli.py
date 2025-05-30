from lib.models.user import User
from lib.models.attempt import QuizAttempt
from lib.seed import get_questions
from lib.helper import find_or_create_user, save_quiz_attempt

def main():
    print("🎉 Welcome to QuizMaster! 🎉")
    name = input("Enter your name: ").strip()
    user = find_or_create_user(name)

    questions = get_questions()
    score = 0

    for q in questions:
        print(f"\n{q['question']}")
        answer = input("Your answer: ").strip()

        if answer.lower() == q['answer'].lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer was: {q['answer']}")

    print(f"\n🎯 Quiz Finished! Your score: {score}/{len(questions)}")
    save_quiz_attempt(user.id, score)

if __name__ == "__main__":
    print(" Initializing database...")
    User.create_table()
    QuizAttempt.create_table()
    main()
