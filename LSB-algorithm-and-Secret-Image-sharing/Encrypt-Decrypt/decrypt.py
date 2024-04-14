from cryptography.fernet import Fernet

def decrypt_image(image_path, key):
    with open(image_path, 'rb') as file:
        encrypted_data = file.read()
    
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    
    with open(image_path, 'wb') as file:
        file.write(decrypted_data)

def read_key_from_file(file_path):
    with open(file_path, "rb") as key_file:
        return key_file.read()

def main():
    stego_image_path = "LSB\\images\\stego_image.jpg"
    key_file_path = input("Lütfen anahtar dosyasının yolunu girin: ")
    key = read_key_from_file(key_file_path)
    decrypt_image(stego_image_path, key)
    print("Şifreli stego görüntüsü deşifre edildi.")

if __name__ == "__main__":
    main()
