# Şifreleme Anahtarı Oluşturma

Bu Python Kodu, Fernet şifreleme algoritması kullanarak bir şifreleme anahtarı oluşturur.

## Kullanım

1. Bu repoyu klonlayın:

 git clone https://github.com/kullanici_adi/proje_adı.git


3. Anahtar dosyası oluşturmak için şu komutu çalıştırın:

pip install -r requirements.txt


4. Anahtar dosyasını projenize dahil edin ve şifreleme işlemlerinizde kullanın.

```python
from cryptography.fernet import Fernet

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Anahtar dosyasını yükle
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

# Örnek kullanım
message = "Bu bir örnek mesajdır."
encrypted_message = encrypt_message(message, key)
print("Şifrelenmiş Mesaj:", encrypted_message)

decrypted_message = decrypt_message(encrypted_message, key)
print("Çözülmüş Mesaj:", decrypted_message)

```
## Gereksinimler
-Python 3.x
-cryptography kütüphanesi