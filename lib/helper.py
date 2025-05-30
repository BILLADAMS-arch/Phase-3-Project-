from lib.models.user import User
from lib.models.attempt import QuizAttempt

def find_or_create_user(name):
    user = User.find_by_name(name)
    if user:
        return user
    user = User(name)
    user.save()
    return user

def save_quiz_attempt(user_id, score):
    attempt = QuizAttempt(user_id=user_id, score=score)
    attempt.save()
