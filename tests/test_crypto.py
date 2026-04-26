import pytest
from pathlib import Path
from cryptography import fernet
from src.crypto import encrypt_file, decrypt_file


def test_callable_encrypt_file():
    assert callable(encrypt_file)


def test_callable_decrypt_file():
    assert callable(decrypt_file)


def test_encypt_file_with_wrong_key():
    with pytest.raises(SystemExit) as excinfo:
        encrypt_file("test_files/fail.txt", "wrong_key")
    assert excinfo.value.code == 1


def test_decrypt_file_with_wrong_key():
    with pytest.raises(SystemExit) as excinfo:
        decrypt_file("test_files/fail.txt", "wrong_key")
    assert excinfo.value.code == 1


def test_test_files_dir_exists():
    assert Path("test_files").exists()
    assert Path("test_files").is_dir()

def test_test_files_contain_files():
    assert Path("test_files/fail.txt").exists()
    assert Path("test_files/test0.txt").exists()
    assert Path("test_files/test1.txt").exists()
    assert Path("test_files/test2.txt").exists()

def test_encypt_file():
    try:
        test_file = Path("test_files/test0.txt")
        with open(test_file, "w") as file:
            file.write("Hello World")
        key = fernet.Fernet.generate_key()
        encrypt_file(str(test_file), key)
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")
