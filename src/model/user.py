class User:
    def __init__(self, username, password, user_id=None):
        self.user_id = user_id
        self.username = username
        self.password = password

    def __str__(self):
        return f"id: {self.user_id}, username: {self.username}, password: {self.password}"

