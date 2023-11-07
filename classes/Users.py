

class User:
    chat_id: str
    first_name: str
    last_name: str
    role: str
    stage: str

    def __init__(self, chat_id, first_name, last_name, role, stage):
        self.chat_id = chat_id
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.stage = stage

    def __str__(self):
        return f'{self.chat_id}:{self.first_name}:{self.last_name}:{self.role}'

    def __repr__(self):
        return f'{self.chat_id}:{self.first_name}:{self.last_name}:{self.role}'


