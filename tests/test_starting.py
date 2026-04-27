from types import NoneType, FunctionType
import pytest
from pytest import MonkeyPatch
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


class TestFolderOrFileWorks:
    def test_folder_or_file_folder_choice(self, monkeypatch: MonkeyPatch):
        """test working with folder"""
        folder_path = "./test_files"
        inputs = iter(["1", folder_path])
        monkeypatch.setattr(
            "builtins.input",
            lambda _: next(inputs),
        )
        folder, file, folder_name, file_name = folder_or_file(
            folder_name="", file_name=""
        )
        assert folder == True
        assert file == False
        assert folder_name == folder_path

    def test_folder_or_file_file_choice(self, monkeypatch: MonkeyPatch):
        """test working with single file"""
        file_path = "./test_files/does_exists.txt"
        inputs = iter(["2", file_path])
        monkeypatch.setattr(
            "builtins.input",
            lambda _: next(inputs),
        )
        folder, file, folder_name, file_name = folder_or_file(
            folder_name="", file_name=""
        )
        assert folder == False
        assert file == True
        assert file_name == file_path


class TestFolderOrFileNotWorks:
    def test_folder_or_file_folder_choice_does_not_exists(
        self, monkeypatch: MonkeyPatch
    ):
        """test working with folder"""
        folder_path = "non_existing_dir_for_sure"
        inputs = iter(["1", folder_path])
        monkeypatch.setattr(
            "builtins.input",
            lambda _: next(inputs),
        )
        with pytest.raises(SystemExit):
            folder, file, folder_name, file_name = folder_or_file(
                folder_name="", file_name=""
            )

    def test_folder_or_file_file_choice_does_not_exists(self, monkeypatch: MonkeyPatch):
        """test working with single file"""
        file_path = "./test_files/does_not_exists.txt"
        inputs = iter(["2", file_path])
        monkeypatch.setattr(
            "builtins.input",
            lambda _: next(inputs),
        )
        with pytest.raises(SystemExit):
            folder, file, folder_name, file_name = folder_or_file(
                folder_name="", file_name=""
            )
