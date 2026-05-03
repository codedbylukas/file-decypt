import pytest
from pathlib import Path
import os
from src.usefull_for_starting import make_to_intiger, testing_exist as check_exist, save_key
from types import FunctionType


@pytest.fixture
def key_file_cleanup():
    """Cleanup key_file.txt after each test that uses it"""
    yield
    key_path = Path("key_file.txt")
    if key_path.exists():
        key_path.unlink()


class TestBasic:
    def test_callable_make_to_intiger(self):
        assert callable(make_to_intiger)

    def test_make_to_intiger_fn_is_a_function_type(self):
        assert isinstance(make_to_intiger, FunctionType)

    def test_callable_testing_exist(self):
        assert callable(check_exist)

    def test_testing_exist_fn_is_a_function_type(self):
        assert isinstance(check_exist, FunctionType)

    def test_callable_save_key(self):
        assert callable(save_key)

    def test_save_key_fn_is_a_function_type(self):
        assert isinstance(save_key, FunctionType)


class TestMakeToIntiger:
    def test_make_to_intiger_valid_positive_number(self):
        result = make_to_intiger("42")
        assert result == 42
        assert isinstance(result, int)

    def test_make_to_intiger_valid_negative_number(self):
        result = make_to_intiger("-10")
        assert result == -10
        assert isinstance(result, int)

    def test_make_to_intiger_zero(self):
        result = make_to_intiger("0")
        assert result == 0
        assert isinstance(result, int)

    def test_make_to_intiger_large_number(self):
        result = make_to_intiger("9999999999")
        assert result == 9999999999
        assert isinstance(result, int)

    def test_make_to_intiger_invalid_string(self):
        with pytest.raises(SystemExit) as excinfo:
            make_to_intiger("not_a_number")
        assert excinfo.value.code == 1

    def test_make_to_intiger_float_string(self):
        with pytest.raises(SystemExit) as excinfo:
            make_to_intiger("3.14")
        assert excinfo.value.code == 1

    def test_make_to_intiger_empty_string(self):
        with pytest.raises(SystemExit) as excinfo:
            make_to_intiger("")
        assert excinfo.value.code == 1

    def test_make_to_intiger_with_spaces(self):
        # Python's int() strips leading/trailing spaces
        result = make_to_intiger("  123  ")
        assert result == 123
        assert isinstance(result, int)


class TestTestingExist:
    def test_testing_exist_file_exists(self, capsys):
        test_file = Path("test_files/test0.txt")
        with open(test_file, "w") as f:
            f.write("test content")

        check_exist(str(test_file))
        captured = capsys.readouterr()
        assert str(test_file) in captured.out

    def test_testing_exist_file_not_found(self):
        with pytest.raises(SystemExit) as excinfo:
            check_exist("test_files/nonexistent_file_xyz.txt")
        assert excinfo.value.code == 1

    def test_testing_exist_directory_exists(self, capsys):
        test_dir = "test_files"
        check_exist(test_dir)
        captured = capsys.readouterr()
        assert test_dir in captured.out

    def test_testing_exist_with_relative_path(self, capsys):
        test_file = Path("test_files/test0.txt")
        with open(test_file, "w") as f:
            f.write("test content")

        check_exist(str(test_file))
        captured = capsys.readouterr()
        assert str(test_file) in captured.out


class TestSaveKey:
    def teardown_method(self):
        """Cleanup key_file.txt after each test"""
        key_path = Path("key_file.txt")
        if key_path.exists():
            key_path.unlink()

    def setup_method(self):
        """Cleanup key_file.txt before each test"""
        key_path = Path("key_file.txt")
        if key_path.exists():
            key_path.unlink()

    def test_save_key_file_exists(self):
        key_path = Path("key_file.txt")
        test_key = b"test_key_content"

        with open(key_path, "wb") as f:
            f.write(test_key)

        result = save_key()
        assert result == test_key

    def test_save_key_file_not_found(self):
        key_path = Path("key_file.txt")

        # Remove key file if it exists
        if key_path.exists():
            key_path.unlink()

        with pytest.raises(SystemExit) as excinfo:
            save_key()
        assert excinfo.value.code == 1

    def test_save_key_returns_bytes(self):
        key_path = Path("key_file.txt")
        test_key = b"another_test_key"

        with open(key_path, "wb") as f:
            f.write(test_key)

        result = save_key()
        assert isinstance(result, bytes)

    def test_save_key_with_empty_file(self):
        key_path = Path("key_file.txt")

        with open(key_path, "wb") as f:
            f.write(b"")

        result = save_key()
        assert result == b""

    def test_save_key_with_multiline_content(self):
        key_path = Path("key_file.txt")
        test_key = b"line1\nline2\nline3"

        with open(key_path, "wb") as f:
            f.write(test_key)

        result = save_key()
        assert result == test_key


class TestIntegration:
    def teardown_method(self):
        """Cleanup key_file.txt after each test"""
        key_path = Path("key_file.txt")
        if key_path.exists():
            key_path.unlink()

    def test_make_to_intiger_and_testing_exist_integration(self, capsys):
        test_file = Path("test_files/test0.txt")
        with open(test_file, "w") as f:
            f.write("test content")

        choice = make_to_intiger("1")
        assert choice == 1

        check_exist(str(test_file))
        captured = capsys.readouterr()
        assert str(test_file) in captured.out

    def test_save_key_and_make_to_intiger_integration(self):
        key_path = Path("key_file.txt")
        test_key = b"integration_test_key"

        with open(key_path, "wb") as f:
            f.write(test_key)

        key = save_key()
        assert key == test_key

        choice = make_to_intiger("42")
        assert choice == 42
