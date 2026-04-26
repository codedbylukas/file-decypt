from cryptography import fernet
from sys import exit
from .usefull_for_starting import make_to_intiger, testing_exist, save_key

def folder_or_file(folder_name, file_name):
    try:
        print("""Do you want to 
        1. work with a folder 
        2. work with a single file?""")
        input_choice = input("Enter 1 or 2: ")
        int_choice = make_to_intiger(input_choice)
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
            exit(1)
        return folder, file, folder_name, file_name
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)


def encrypting_or_decrypting(encrypting, decrypting, key):
    try:
        print("""Do you want to 
        1.encrypt 
        2.decrypt 
        the files'?""")
        input_choice = input("Enter 1 or 2: ")
        int_choice = make_to_intiger(input_choice)
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
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)


def check_key(key: str):
    if key is None:  # Check if key is properly initialized
        print("Error: Key is not initialized. Exiting.")
        exit(1)
