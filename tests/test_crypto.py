import pytest
from pathlib import Path
from cryptography import fernet
from src.crypto import encrypt_file, decrypt_file
from types import FunctionType


class TestBasic:
    def test_callable_encrypt_file(self):
        assert callable(encrypt_file)

    def test_encrypted_file_fn_is_an_function_type(self):
        assert isinstance(encrypt_file, FunctionType)

    def test_callable_decrypt_file(self):
        assert callable(decrypt_file)

    def test_decrypt_file_fn_is_an_function_type(self):
        assert isinstance(decrypt_file, FunctionType)


class TestFilesExist:

    def test_test_files_dir_exists(self):
        assert Path("test_files").exists()
        assert Path("test_files").is_dir()

    def test_test_files_contain_files(self):
        assert Path("test_files/fail.txt").exists()
        assert Path("test_files/test0.txt").exists()
        assert Path("test_files/test1.txt").exists()
        assert Path("test_files/test2.txt").exists()

    def test_not_existent_file(self):
        assert Path("test_files/none_existent_file.txt").exists() == False


class TestFailCases:
    def test_encypt_file_with_wrong_key(self):
        with pytest.raises(SystemExit) as excinfo:
            encrypt_file("test_files/fail.txt", "wrong_key")
        assert excinfo.value.code == 1

    def test_decrypt_file_with_wrong_key(self):
        with pytest.raises(SystemExit) as excinfo:
            decrypt_file("test_files/fail.txt", "wrong_key")
        assert excinfo.value.code == 1

    def test_encrypt_fail(self):
        with pytest.raises(SystemExit) as excinfo:
            encrypt_file("test_files/fail.txt", "wrong_key")
        assert excinfo.value.code == 1

    def test_decrypt_file_wrong_key_and_file(self):
        key = fernet.Fernet.generate_key()
        with pytest.raises(SystemExit) as excinfo:
            decrypt_file("test_files/none_existent_file.txt", "wrong_key")
        assert excinfo.value.code == 1

    def test_encrypt_file_wrong_key(self):
        key = fernet.Fernet.generate_key()
        with pytest.raises(SystemExit) as excinfo:
            encrypt_file("test_files/none_existent_file.txt", "wrong_key")
        assert excinfo.value.code == 1

    def test_decrypt_file_not_found(self):
        key = fernet.Fernet.generate_key()
        with pytest.raises(SystemExit) as excinfo:
            decrypt_file("test_files/nonexistent.txt", key)
        assert excinfo.value.code == 1

    def test_encrypt_file_not_found(self):
        key = fernet.Fernet.generate_key()
        with pytest.raises(SystemExit) as excinfo:
            encrypt_file("test_files/nonexistent.txt", key)
        assert excinfo.value.code == 1


class TestEncryptionDecryption:
    def test_encypt_file(self):
        try:
            test_file = Path("test_files/test0.txt")
            with open(test_file, "w") as file:
                file.write("Hello World")
            key = fernet.Fernet.generate_key()
            encrypt_file(str(test_file), key)
            with open(test_file, "r") as file:
                encrypted_data = file.read()
            assert encrypted_data != "Hello World"

            with open(test_file, "w") as file:
                file.write("Hello World")
        except Exception as e:
            pytest.fail(f"An error occurred: {e}")

    def test_decrypt_file(self):
        try:
            test_file = Path("test_files/test1.txt")
            with open(test_file, "w") as file:
                file.write("Hello World")
            key = fernet.Fernet.generate_key()
            encrypt_file(str(test_file), key)
            with open(test_file, "r") as file:
                encrypted_data = file.read()
            assert encrypted_data != "Hello World"
            decrypt_file(str(test_file), key)
            with open(test_file, "r") as file:
                decrypted_data = file.read()
            assert decrypted_data == "Hello World"
            with open(test_file, "w") as file:
                file.write("Hello World")
        except Exception as e:
            pytest.fail(f"An error occurred: {e}")

    def test_encrypt_and_decrypt_file(self):
        try:
            test_file = Path("test_files/test2.txt")
            with open(test_file, "w") as file:
                file.write("Hello World")
            key = fernet.Fernet.generate_key()
            encrypt_file(str(test_file), key)
            with open(test_file, "r") as file:
                encrypted_data = file.read()
            assert encrypted_data != "Hello World"
            decrypt_file(str(test_file), key)
            with open(test_file, "r") as file:
                decrypted_data = file.read()
            assert decrypted_data == "Hello World"
            with open(test_file, "w") as file:
                file.write("Hello World")
        except Exception as e:
            pytest.fail(f"An error occurred: {e}")
