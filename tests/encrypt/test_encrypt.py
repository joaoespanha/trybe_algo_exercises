from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("abc", "1")

    with pytest.raises(TypeError):
        encrypt_message(4, 1)

    assert encrypt_message("trybe", 5) == "ebyrt"
    assert encrypt_message("trybe", 2) == "eby_rt"
    assert encrypt_message("trybe", 3) == "yrt_eb"
