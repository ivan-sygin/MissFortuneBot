from modules.connectors.ConnectorDB import DataBaseConnector
import os
from classes.Users import User


class BotHandlerDB:
    dbname = os.environ["NAME_DB"]
    username = os.environ["USERNAME_DB"]
    password = os.environ["PASSWORD_DB"]

    def __init__(self):
        self.UsersDB = DataBaseConnector(self.dbname, self.username, self.password, 'localhost', '5432')

    def getUsers(self):
        data = self.UsersDB.fetchData(
            "SELECT * FROM public.users ORDER BY chat_id ASC"
        )
        response = []
        for row in data:
            response.append(User(*row))
        return response

    def findUser(self, chat_id):
        data = self.UsersDB.fetchData(
            f"SELECT * FROM public.users WHERE users.chat_id = '{chat_id}' ORDER BY chat_id ASC "
        )
        if data:
            return User(*data[0])
        else:
            return None

    def createUser(self, chat_id, first_name=None, last_name=None, role="Пользователь", stage="start"):
        self.UsersDB.sqlRequest(
            f"""INSERT INTO public.users (chat_id, first_name, last_name, role, stage) 
            VALUES ('{chat_id}', '{first_name}', '{last_name}', '{role}', '{stage}');"""
        )
        return User(chat_id, first_name, last_name, role, stage)

    def getStage(self, chat_id: int):
        data = self.UsersDB.fetchData(
            f"SELECT stage FROM public.users WHERE chat_id = '{chat_id}'"
        )
        if data:
            return data[0][0]
        else:
            return None

    def getRole(self, chat_id: int):
        data = self.UsersDB.fetchData(
            f"SELECT role FROM public.users WHERE chat_id = '{chat_id}'"
        )
        if data:
            return data[0][0]
        else:
            return None

    def setStageUser(self, chat_id, stage):
        self.UsersDB.sqlRequest(
            f"UPDATE public.users SET stage = '{stage}' WHERE users.chat_id = '{chat_id}';"
        )

    def setRoleUser(self, chat_id, role):
        self.UsersDB.sqlRequest(
            f"UPDATE public.users SET role = '{role}' WHERE users.chat_id = '{chat_id}';"
        )

    def getTask(self):
        pass


bot_connector = BotHandlerDB()


