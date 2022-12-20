class InvalidUsernameException(Exception):
    def __init__(self, msg="Invalid username"):
        super().__init__(msg)


class InvalidPasswordException(Exception):
    def __init__(self, msg="Invalid password"):
        super().__init__(msg)


class UserNotExistException(Exception):
    def __init__(self, msg="User does not exist"):
        super().__init__(msg)


class BlankPasswordException(Exception):
    def __init__(self, msg="Blank password"):
        super().__init__(msg)


class BlankUsernameException(Exception):
    def __init__(self, msg="Blank username"):
        super().__init__(msg)


class UserAlreadyExistsException(Exception):
    def __init__(self, msg="User already exists"):
        super().__init__(msg)


class NotInitializedException(Exception):
    def __init__(self, msg="Not initialized"):
        super().__init__(msg)


class NotFoundException(Exception):
    def __init__(self, msg="Not found"):
        super().__init__(msg)
