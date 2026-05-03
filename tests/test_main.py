from types import NoneType, FunctionType
from pytest import MonkeyPatch
from main import main, key, input_choice, int_choice


class TestBasic:
    def test_main_is_clickable(self, monkeypatch: MonkeyPatch):
        monkeypatch.setattr(
            "builtins.input",
            lambda _: """
        """,
        )
        assert callable(main)

    def test_key_is_setted(self):
        assert isinstance(key, NoneType)

    def test_input_choice_is_setted(self):
        assert isinstance(input_choice, str)

    def test_int_choice_is_setted(self):
        assert isinstance(int_choice, NoneType)

    def test_main_is_Functiontype(self, monkeypatch: MonkeyPatch):
        monkeypatch.setattr(
            "builtins.input",
            lambda _: """
        """,
        )
        assert isinstance(main, FunctionType)
