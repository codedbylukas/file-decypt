from pathlib import Path
import pytest
from types import FunctionType

from src.main_helper import (
    if_file,
    store_key_encrypted,
    get_key_encrypted,
    when_its_an_folder,
)


class TestBasic:
    def test_if_file_is_callable_is_callable(self):
        assert callable(if_file)

    def test_store_key_encrypted_is_callable(self):
        assert callable(store_key_encrypted)

    def test_get_key_encrypted_is_callable(self):
        assert callable(get_key_encrypted)

    def test_when_its_an_folder_is_callable(self):
        assert callable(when_its_an_folder)

    def test_if_file_is_function_type(self):
        assert isinstance(if_file, FunctionType)

    def test_store_key_encrypted_is_functiontype(self):
        assert isinstance(store_key_encrypted, FunctionType)

    def test_get_key_encrypted_is_functiontype(self):
        assert isinstance(get_key_encrypted, FunctionType)

    def test_when_its_an_folder_is_functiontype(self):
        assert isinstance(when_its_an_folder, FunctionType)


class TestKeyFunctions:
    def test_store_key_encrypted(self):
        key_file = Path("test_files/test_key_file0.txt")
        assert callable(store_key_encrypted)
        store_key_encrypted(b"test", keyfile=key_file)
        with open(key_file, "r") as f:
            assert f.read() == "test"
        key_file.unlink(missing_ok=True)

    def test_get_key_encrypted(self):
        key_file = Path("test_files/test_key_file1.txt")
        assert callable(store_key_encrypted)
        store_key_encrypted(b"test", keyfile=key_file)
        assert callable(get_key_encrypted)
        get_key_encrypted(keyfile=key_file)
        with open(key_file, "r") as f:
            assert f.read() == "test"
        key_file.unlink(missing_ok=True)
