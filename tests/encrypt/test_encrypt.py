import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message('message', 0) == 'egassem'
    assert encrypt_message('message', 9999) == 'egassem'
    assert encrypt_message('message', 2) == 'egass_em'
    assert encrypt_message('message', 3) == 'sem_egas'
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message('message', '3')
    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(2, 3)
