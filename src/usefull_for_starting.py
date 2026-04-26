from cryptography import fernet
from sys import exit
import os


def make_to_intiger(input_choice: str):
    try:
        int_choice = int(input_choice)
    except ValueError:
        print("Invalid choice. Exiting.")
        exit(1)
    return int_choice


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
