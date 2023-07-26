from challenges.challenge_encrypt_message import encrypt_message
import pytest


invalid_message = 2938457
invalid_key = "invalid"

valid_out_of_range_key = 10
valid_message = "flamengo"

valid_even_key = 4
valid_odd_key = 5


def test_encrypt_message():
    # testar se os valores de param sao validos senao gerar value error
    with pytest.raises(TypeError):
        encrypt_message(invalid_message, invalid_key)

    # testar se a key é um valor negativo se sim retornar a message invertida
    assert encrypt_message(valid_message, valid_out_of_range_key) == "".join(
        reversed(valid_message)
    )
    # testar se a key é par
    assert encrypt_message(valid_message, valid_even_key) == "".join(
        reversed(valid_message[valid_even_key:])
    ) + "_" + "".join(reversed(valid_message[:valid_even_key]))

    # testar se a key é impar
    assert encrypt_message(valid_message, valid_odd_key) == "".join(
        reversed(valid_message[:valid_odd_key])
    ) + "_" + "".join(reversed(valid_message[valid_odd_key:]))
