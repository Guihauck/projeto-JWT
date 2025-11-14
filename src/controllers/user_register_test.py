from src.controllers.user_register import UserRegister

class MockUserRegister:
    def __init__(self) -> None:
        self.registry_user_attributes = {}

    def registry_user(self, username, password) -> None:
        self.registry_user_attributes["username"] = username
        self.registry_user_attributes["password"] = password

def test_registry():
    repository = MockUserRegister()
    controller = UserRegister(repository)

    username = 'guihauck98'
    password = 'haucks2s3'

    response = controller.registry(username, password)

    assert response["type"] == "User"
    assert response["username"] == username
    
    assert repository.registry_user_attributes["username"] == username
    assert repository.registry_user_attributes["password"] is not None
    assert repository.registry_user_attributes["password"] != password
