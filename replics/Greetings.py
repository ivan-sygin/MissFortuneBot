from classes.Users import User


def GreetingsKnownUser(user: User):
    return f"Здравствуйте {user.role} {user.first_name}. Чем могу помочь?"


def GreetingsUnknownUser():
    return "Я создала Вам новый аккаунт! Рада знакомству!"

