from types import NoneType, FunctionType
import pytest
from src.starting import folder_or_file, encrypting_or_decrypting, check_key

class TestBasic:
    def test_folder_or_file(self):
        assert callable(folder_or_file)
    def test_encrypting_or_decrypting(self):
        assert callable(encrypting_or_decrypting)
    def test_check_key(self):
        assert callable(check_key)
    def test_folder_or_file_is_setted(self):
        assert isinstance(folder_or_file, FunctionType)
    def test_encrypting_or_decrypting_is_setted(self):
        assert isinstance(encrypting_or_decrypting, FunctionType)
    def test_check_key_is_setted(self):
        assert isinstance(check_key, FunctionType)