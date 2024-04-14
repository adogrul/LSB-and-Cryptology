# Steganography ve LSB Algoritması

Bu projede steganografi ve Least Significant Bit (LSB) algoritması hakkında bilgi verilecek ve basit bir örnek uygulama sunulacaktır.

## Steganografi Nedir?

Steganografi, gizli mesajların başka bir veri içerisine gizlenmesi yöntemidir. Bu teknik, gizli mesajın varlığını tespit etmeyi zorlaştırır, çünkü görünür veri normal görünür.

## Least Significant Bit (LSB) Algoritması Nedir?

LSB algoritması, steganografi için sıkça kullanılan bir yöntemdir. Bu algoritma, bir resim dosyasının piksellerinin en az anlamlı bitlerini değiştirerek gizli mesajı saklar.

## Projede Kullanılan Modüller

1. `implementsLSB.py`: Bu modül, steganografi işlemlerini gerçekleştirmek için kullanılır.
2. `keyFile.py`: Verimizi şifrelemek için anahtar üretir.
3. `encrypt.py`: Gizli verinin şifrelenmesi ve şifreli verinin gizlenmesi için kullanılır.
4. `decrypt.py`: Şifrelenen verinin deşifre edilmesi için kullanılır
5. `psnr.py`: Steganography işleminin doğru yapılıp yapılmadığını anlamak için iki resim arasında benzerlik hesabı yaparız.

## Gereksinimler

Bu projeyi çalıştırmak için Python 3 ve aşağıdaki ek paketlere ihtiyacınız vardır:
- numpy
- cv2
- PIL
- cryptography 

## Nasıl Kullanılır?

1. Projeyi bilgisayarınıza klonlayın.
2. Gereksinimleri yüklemek için terminalde `pip install -r requirements.txt` komutunu çalıştırın.
3. Örnek uygulamayı çalıştırmak için:
1. `implementsLSB.py` dosyasını çalıştırın.
2. `keyFile.py` dosyasını çalıştırarak bir anahtar üretin.
3. `encrypt.py` dosyasını çalıştırarak Steganography uygulanmış resminizi şifreleyin.
4. `decrypt.py` dosyasını çalıştırarak şifrelenmiş resminizi deşifreleyin.


## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasını kontrol edin.
