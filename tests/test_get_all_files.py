from src.get_all_files import get_all_files_fnc


def test_get_all_files_fnc():
    assert callable(get_all_files_fnc)


def test_get_all_files_fnc_files_count():
    actual = set(get_all_files_fnc("test_files/get_all_files"))
    expected = {
        "test_files/get_all_files/a",
        "test_files/get_all_files/b",
    }
    assert actual == expected
    
