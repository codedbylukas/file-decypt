from src.get_all_files import get_all_files_fnc


def test_get_all_files_fnc():
    assert callable(get_all_files_fnc)


def test_get_all_files_fnc_files_count():
    assert get_all_files_fnc("test_files/get_all_files") == [
        "test_files/get_all_files/a",
        "test_files/get_all_files/b",
    ]
