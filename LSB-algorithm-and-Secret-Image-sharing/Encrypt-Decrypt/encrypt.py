from cryptography.fernet import Fernet
import sys
sys.path.append('GenerateKey')
import keyFile 
def encrypt_image(image_path, key):
    with open(image_path, 'rb') as file:
        image_data = file.read()
    
    f = Fernet(key)
    encrypted_data = f.encrypt(image_data)
    
    with open(image_path, 'wb') as file:
        file.write(encrypted_data)



def main():
    stego_image_path = "LSB\\images\\stego_image.jpg"
    key_file_path = "GenerateKey\\encryption_key.key"
    
    keyFile.generate_key_file(key_file_path)
    print("Anahtar başarıyla oluşturuldu ve '{}' dosyasına kaydedildi.".format(key_file_path))
    
    key = open(key_file_path, 'rb').read()
    encrypt_image(stego_image_path, key)
    print("Stego görüntüsü başarıyla şifrelendi.")

if __name__ == "__main__":
    main()
