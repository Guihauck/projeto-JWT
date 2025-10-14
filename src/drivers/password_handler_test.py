from .password_handler import PasswordHandler

def test_encrypt():
    my_password = "guilherme.hauck@1998!"
    password_handler = PasswordHandler()

    hashed_password = password_handler.encrypt_password(my_password)
    password_checked = password_handler.check_password(my_password, hashed_password)

    assert password_checked