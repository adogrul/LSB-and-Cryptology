from cryptography.fernet import Fernet

def generate_key_file(file_path):
    key = Fernet.generate_key()
    with open(file_path, "wb") as key_file:
        key_file.write(key)

def main():
    key_file_path = "GenerateKey\\encryption_key.key"
    generate_key_file(key_file_path)
    print(f"Anahtar dosyası {key_file_path} olarak oluşturuldu.")

if __name__ == "__main__":
    main()
