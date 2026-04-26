from cryptography import fernet
from sys import exit
import os


def testing_exist(name):
    try:
        if os.path.exists(name):
            print(name)
        else:
            print("File not found. Exiting.")
            exit(1)
    except FileNotFoundError:
        print("File not found. Exiting.")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to exit...")
        exit()


def save_key():
    try:
        with open("key_file.txt", "r") as key_file:
            key = key_file.read().encode()  # Read key for decryption
    except FileNotFoundError:
        print("Key file not found. Cannot decrypt.")
        exit(1)
    return key


def folder_or_file(folder_name, file_name):
    print("""Do you want to 
    1. work with a folder 
    2. work with a single file?""")
    input_choice = input("Enter 1 or 2: ")
    int_choice = int(input_choice)
    if int_choice == 1:
        folder = True
        file = False
        folder_name = input("Enter the folder path: ").strip()
        testing_exist(folder_name)
    elif int_choice == 2:
        folder = False
        file = True
        file_name = input("Enter the file path: ").strip()
        testing_exist(file_name)
    else:
        print("Invalid choice. Exiting.")
        exit()
    return folder, file, folder_name, file_name


def encrypting_or_decrypting(encrypting, decrypting, key):
    print("""Do you want to 
    1.encrypt 
    2.decrypt 
    the files'?""")
    input_choice = input("Enter 1 or 2: ")
    int_choice = int(input_choice)
    if int_choice == 1:
        encrypting = True
        decrypting = False
        key = fernet.Fernet.generate_key()  # Generate key for encryption
    elif int_choice == 2:
        encrypting = False
        decrypting = True
        key = save_key()
    else:
        print("Invalid choice. Exiting.")
        exit(1)
    return encrypting, decrypting, key


def check_key(key: str):
    if key is None:  # Check if key is properly initialized
        print("Error: Key is not initialized. Exiting.")
        exit(1)
