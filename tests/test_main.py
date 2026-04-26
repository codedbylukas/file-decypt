from pytest import MonkeyPatch
from main import main


def test_main_is_clickable(monkeypatch: MonkeyPatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: """
    """,
    )
    assert callable(main)
