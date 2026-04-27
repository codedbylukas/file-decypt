from pathlib import Path
import pytest
from src.main_helper import (
    if_file,
    store_key_encrypted,
    get_key_encrypted,
    when_its_an_folder,
)


class TestBasic:
    def test_if_file(self):
        assert callable(if_file)

    def test_store_key_encrypted(self):
        assert callable(store_key_encrypted)

    def test_get_key_encrypted(self):
        assert callable(get_key_encrypted)

    def test_when_its_an_folder(self):
        assert callable(when_its_an_folder)


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
