from cryptography import fernet
from sys import exit


def encrypt_file(file_path, key):
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()

        fernet_instance = fernet.Fernet(key)
        encrypted_data = fernet_instance.encrypt(file_data)
        with open(file_path, "wb") as file:
            file.write(encrypted_data)
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
    except FileNotFoundError as e:
        print(f"File not found: {file_path}: {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred while encrypting:  {file_path}: {e}")
        exit(1)


def decrypt_file(file_path, key):
    try:
        with open(file_path, "rb") as file:
            decrypted_data = file.read()

        fernet_instance = fernet.Fernet(key)
        decrypted_data = fernet_instance.decrypt(decrypted_data)

        with open(file_path, "wb") as file:
            file.write(decrypted_data)
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
    except Exception as e:
        print(f"An error occurred during decryption: {file_path}: {e}")
        exit(1)
