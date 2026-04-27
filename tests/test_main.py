from types import NoneType
from pytest import MonkeyPatch
from main import main, key


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
