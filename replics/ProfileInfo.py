from classes.Users import User


def ProfileInfo(user: User):
    return (
f"""
👤 Ваш профиль:
ФИО: {user.first_name}
Роль: {user.role}
"""
    )

def ProfileWantUpdate(user: User, status: str):
    return (
        f"""
👤 Пользователь:
ФИО: {user.first_name}
Роль: {user.role}
Запрашивает разрешение получить статус {status}
    """
    )





