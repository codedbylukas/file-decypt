# 🔐 File Encryption and Decryption Tool (Dynamic Folder Version)

This Python script encrypts and decrypts files using the `cryptography` library and the `Fernet` encryption method.  
Unlike the basic version, this script allows you to **create and process any folder name entered by the user**.

## ✨ Features

- 🔑 Automatic key generation  
- 📁 User-defined folder selection  
- 🔒 Encrypt files  
- 🔓 Decrypt files  
- 🚫 Skips internal program files (`key_file.txt`, `main.exe`, `main.py`)

## 📦 Requirements

- Python 3.x  
- `cryptography` library  
  Install with:
```bash
  pip install cryptography
```

## 🧠 How It Works
## 1. Folder Input 📂

When the script starts, you are asked to enter the folder name that should be created and processed:
```bash
   Enter the folder name to create and process files:
```

Make sure the folder exists or create it before running the script.

## 2. Choose an Action

You then select:

```bash
    1. encrypt 🔒 
    2. decrypt 🔓
```

- 1 generates a key and encrypts all files inside the selected folder.

- 2 loads the key from key_file.txt and decrypts the files.

## 3. Key Handling 🔑

- During encryption, the script writes the generated key to:

```bash
    key_file.txt
```

- Store this key safely.
Without it, decrypting the files is impossible.

## File Collection 📁

All files inside the user-defined folder are scanned recursively.

Ignored files:

- key_file.txt
- main.exe
- main.py

## 5. Encryption / Decryption ⚙️

- Encryption uses Fernet.encrypt()
- Decryption uses Fernet.decrypt()
- Any file-level errors are displayed during processing

## ▶️ Usage

1. Create a folder with any name.
2. Run the script:

```bash
    python main.py
```
3. Enter the folder name when prompted.
4. Choose 1 (encrypt) or 2 (decrypt).
5. Keep the key file safe.

## ⚠️ Important Notes

- Do not delete or modify key_file.txt before decrypting.
- Encrypted files overwrite the originals.
- Make backups if your data matters.

## 📜 Disclaimer

Use this tool responsibly. Losing your encryption key or encrypting critical files without backups can result in irreversible data loss.
