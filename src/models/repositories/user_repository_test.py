from .user_repository import UserRepository
from unittest.mock import Mock

class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()

class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value = MockCursor())
        self.commit = Mock()

def test_registry_user():
    username = "Guilherme Jorge"
    password = "Hauck_2025!"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    repo.registry_user(username, password)

    cursor = mock_connection.cursor.return_value

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password, balance)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password, 0)

def test_edit_balance():
    user_id = 2
    new_balance = 8070.30

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    repo.edit_balance(user_id, new_balance)

    cursor = mock_connection.cursor.return_value
 
    assert "UPDATE users" in cursor.execute.call_args[0][0]
    assert "SET balance = ?" in cursor.execute.call_args[0][0]
    assert "WHERE id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (new_balance, user_id)

def test_user_by_username():
    username = "gui_hauck1998"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    repo.get_user_by_username(username)

    cursor = mock_connection.cursor.return_value

    assert "SELECT Id, username, password" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE username = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username,)