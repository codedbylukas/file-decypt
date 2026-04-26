from sys import exit

from cryptography import fernet
from src.starting import folder_or_file, encrypting_or_decrypting, check_key
from src.main_helper import if_file, store_key_encrypted, get_key_encrypted, when_its_an_folder

key = None  # Initialize key globally
input_choice: str = "None"
int_choice: int = None

def main():
    global key
    folder, file, folder_path, file_path = folder_or_file(None, None)
    encrypting, decrypting, key = encrypting_or_decrypting(None, None, key)
    check_key(key)
    if encrypting:
        store_key_encrypted(key)
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
