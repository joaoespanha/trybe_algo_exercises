from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("Hello", "1")

    with pytest.raises(TypeError):
        encrypt_message(123, 2)

    assert encrypt_message("Hello World", 15) == "dlroW olleH"

    assert encrypt_message("Hello World", 5) == "olleH_dlroW"

    assert encrypt_message("Hello World", 6) == "World_Hello"

    assert encrypt_message("Hello World", 1) == "dlroW olleH"

    assert encrypt_message("Hello World", 10) == "World_Hello"

    assert encrypt_message("", 2) == ""

    assert encrypt_message("", 1) == ""

    assert encrypt_message("", 9) == ""

    assert encrypt_message("A", 1) == "A"

    assert encrypt_message("A", 1) == "A"

    assert encrypt_message("A", 2) == "A_"
