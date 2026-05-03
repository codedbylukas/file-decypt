from src.get_all_files import get_all_files_fnc
import os
from types import FunctionType


class BasicTest:
    def test_get_all_files_fnc_callable():
        assert callable(get_all_files_fnc)

    def test_get_all_files_fnc_right_type():
        assert isinstance(get_all_files_fnc, FunctionType)


class AtherTests:
    def test_get_all_files_fnc_files_count():
        actual = {
            os.path.normpath(p) for p in get_all_files_fnc("test_files/get_all_files")
        }
        expected = {
            os.path.normpath("test_files/get_all_files/a"),
            os.path.normpath("test_files/get_all_files/b"),
        }
        assert actual == expected
