from sys import exit
from src.crypto import encrypt_file, decrypt_file
from src.get_all_files import file_paths, get_all_files_fnc


def if_file(encrypting: bool, decrypting: bool, file_path: str, key: bytes):
    if encrypting:
        encrypt_file(file_path, key)
    elif decrypting:
        decrypt_file(file_path, key)


def store_key_encrypted(key: bytes, keyfile: str = "key_file.txt"):
    print("You chose to encrypt the files.")
    print("Schlüssel: ", key.decode())
    with open(keyfile, "w") as key_file:
        key_file.write(key.decode())
    print("Please keep the key safe, otherwise this can never be decrypted again.")


def get_key_encrypted(keyfile: str = "key_file.txt") -> bytes:
    print("You chose to decrypt the files.")
    with open(keyfile, "r") as key_file:
        key_input = key_file.read()
        key = key_input.encode()
    return key


def when_its_an_folder(
    folder_path: str, key: bytes, encrypting: bool, decrypting: bool
):
    if not folder_path:
        print("Error: Folder path is not set. Exiting.")
        exit(1)
    get_all_files_fnc(folder_path)
    for file in file_paths:
        if encrypting:
            encrypt_file(file, key)
        elif decrypting:
            decrypt_file(file, key)
