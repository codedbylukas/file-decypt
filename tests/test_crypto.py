import pytest
from src.crypto import encrypt_file, decrypt_file


def test_callable_encrypt_file():
    assert callable(encrypt_file)


def test_callable_decrypt_file():
    assert callable(decrypt_file)


def test_encypt_file_with_wrong_key():
    with pytest.raises(SystemExit) as excinfo:
        encrypt_file("tests/test.txt", "wrong_key")
    assert excinfo.value.code == 1

def test_decrypt_file_with_wrong_key():
    with pytest.raises(SystemExit) as excinfo:
        decrypt_file("tests/test.txt", "wrong_key")
    assert excinfo.value.code == 1
