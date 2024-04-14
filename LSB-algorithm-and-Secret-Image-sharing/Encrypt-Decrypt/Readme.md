# Görüntü Şifreleme Kılavuzu

Bu program, bir görüntü dosyasını şifrelemek için kullanılır. Şifreleme işlemi, kullanıcı tarafından sağlanan bir anahtarla yapılmaktadır.

## Şifreleme Nedir?

Şifreleme, bir bilgi parçasını anlamsız hale getirerek, sadece yetkilendirilmiş kişilerin erişebileceği hale getirme işlemidir. Bu işlem, gizlilik ve güvenlik sağlamak için kullanılır.

## Kullanılan Algoritma

Bu programda, şifreleme için Fernet algoritması kullanılmıştır. Fernet, modern şifreleme için güçlü bir simetrik anahtar algoritmasıdır. Anahtarlar, AES algoritması ile oluşturulur ve verileri güvenli bir şekilde şifreler.

## Neden Şifreleme Gereklidir?

Şifreleme, hassas verilerin korunmasında kritik bir rol oynar. İnternet üzerinden iletilen veya saklanan verilerin gizliliğini sağlamak için şifreleme kullanmak önemlidir. Bu, bilgi hırsızlığını ve veri sızıntılarını önlemeye yardımcı olur.

## Kullanım Kılavuzu

1. Anahtar Oluşturma: Öncelikle, bir anahtar dosyası oluşturulmalıdır. Bu anahtar, şifreleme ve şifre çözme işlemlerinde kullanılacaktır.

2. Görüntü Şifreleme: Anahtar dosyası oluşturulduktan sonra, şifrelenecek görüntü dosyası ve anahtar dosyası belirtilmelidir. Program, görüntüyü şifreleyecek ve orijinal dosyanın üzerine yazacaktır.

## Örnek Kullanım

```python
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

```
# Görüntü Deşifreleme Kılavuzu

Bu program, şifrelenmiş bir görüntü dosyasını deşifrelemek için kullanılır. Deşifreleme işlemi, kullanıcı tarafından sağlanan bir anahtarla gerçekleştirilir.

## Deşifreleme Nedir?

Deşifreleme, şifrelenmiş bir bilgi parçasını orijinal haline döndürme işlemidir. Bu işlem, doğru anahtar kullanılarak gerçekleştirilir ve şifrelenmiş verinin orijinal veriye dönüştürülmesini sağlar.

## Kullanılan Algoritma

Bu programda, deşifreleme için Fernet algoritması kullanılmıştır. Fernet, modern şifreleme için güçlü bir simetrik anahtar algoritmasıdır. Anahtarlar, AES algoritması ile oluşturulur ve verileri güvenli bir şekilde şifreler.

## Kullanım Kılavuzu

1. Anahtarın Alınması: Öncelikle, şifreleme sırasında kullanılan anahtarı sağlayan bir dosyanın yolunu belirtin.

2. Görüntü Deşifreleme: Anahtar dosyası belirlendikten sonra, deşifre edilecek şifreli görüntü dosyasının yolunu belirtin. Program, görüntüyü deşifreleyecek ve orijinal dosyanın üzerine yazacaktır.

## Örnek Kullanım

```python
stego_image_path = "LSB\\images\\stego_image.jpg"
    key_file_path = input("Lütfen anahtar dosyasının yolunu girin: ")
    key = read_key_from_file(key_file_path)
    decrypt_image(stego_image_path, key)
    print("Şifreli stego görüntüsü deşifre edildi.")

if __name__ == "__main__":
    main()

```



