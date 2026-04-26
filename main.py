from sys import exit

from cryptography import fernet
from crypto import encrypt_file, decrypt_file
from get_all_files import file_paths, get_all_files_fnc
from starting import folder_or_file, encrypting_or_decrypting, check_key

key = None  # Initialize key globally
input_choice: str = "None"
int_choice: int = None


def if_file(encrypting: bool, decrypting: bool, file_path: str, key: bytes):
    if encrypting:
        encrypt_file(file_path, key)
    elif decrypting:
        decrypt_file(file_path, key)


def store_key_encrypted():
    print("You chose to encrypt the files.")
    print("Schlüssel: ", key.decode())
    with open("key_file.txt", "w") as key_file:
        key_file.write(key.decode())
    print("Please keep the key safe, otherwise this can never be decrypted again.")


def get_key_encrypted():
    print("You chose to decrypt the files.")
    with open("key_file.txt", "r") as key_file:
        key_input = key_file.read()
        key = key_input.encode()


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


def main():
    global key
    folder, file, folder_path, file_path = folder_or_file(None, None)
    encrypting, decrypting, key = encrypting_or_decrypting(None, None, key)
    check_key(key)
    if encrypting:
        store_key_encrypted()
    elif decrypting:
        get_key_encrypted()
    if folder:
        when_its_an_folder(folder_path, key, encrypting, decrypting)
    elif file:
        if_file(encrypting, decrypting, file_path, key)
    print("Process completed.")


if __name__ == "__main__":
    while True:
        main()
        do_exit = input("Do you want to exit? (y/n): ")
        if do_exit.lower() == "y":
            exit(0)
        if do_exit.lower() == "n":
            continue
        if do_exit.lower() != "n" and do_exit.lower() != "y":
            print("Invalid choice. Continuing.")
            continue
