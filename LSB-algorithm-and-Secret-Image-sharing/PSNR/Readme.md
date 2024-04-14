# PSNR Hesaplama

Bu  Python kodu, iki görüntü arasındaki Piksel Sıradan Kare Hatası (PSNR) değerini hesaplamak için kullanılır. PSNR, orijinal görüntü ile sıkıştırılmış veya değiştirilmiş bir görüntü arasındaki kalite kaybını ölçmek için kullanılan bir metriktir.

## Nasıl Çalışır?

1. **OpenCV ve NumPy Kütüphaneleri:** Kod, görüntü işleme işlemleri için OpenCV kütüphanesini ve matematiksel işlemler için NumPy kütüphanesini kullanır.

2. **psnr Fonksiyonu:** `psnr` fonksiyonu, iki görüntü arasındaki PSNR değerini hesaplar. PSNR hesaplaması, ortalama kare hata (MSE) kullanılarak gerçekleştirilir. Eğer MSE 0 ise, PSNR sonsuz olarak kabul edilir. Aksi takdirde, PSNR hesaplanır ve döndürülür.

3. **Giriş Görüntüleri:** Kod, iki farklı görüntü alır: `image1` ve `image2`. `image1` genellikle orijinal görüntüyü, `image2` ise orijinal görüntü üzerine uygulanmış bir işlemi (örneğin, sıkıştırma veya gizli veri gömülme) temsil eder.

4. **PSNR Değerinin Kullanımı:** PSNR değeri, iki görüntü arasındaki benzerliği veya farkı nicel olarak ifade eder. Daha yüksek bir PSNR değeri, iki görüntü arasındaki benzerliğin daha yüksek olduğunu gösterirken, daha düşük bir PSNR değeri daha fazla kayıp olduğunu gösterir.

## Nasıl Kullanılır?

1. Kodu İndir: Kodu bilgisayarınıza indirin veya kopyalayın.

2. Görüntüleri Tanımlayın: Kodu kullanmadan önce, karşılaştırmak istediğiniz iki görüntüyü belirtin. Bunları `image1` ve `image2` değişkenlerine atayın.

3. Kodu Çalıştırın: Kodu çalıştırarak PSNR değerini hesaplayın.

## Örnek Kullanım

```python
import cv2
import numpy as np

def psnr(image1, image2):
    # PSNR hesaplama fonksiyonu
    # Kodunuz buraya gelecek

image1 = cv2.imread('LSB\\images\\1.jpg')
image2 = cv2.imread('LSB\\images\\stego_image.jpg')

psnr_value = psnr(image1, image2)
print("PSNR değeri:", psnr_value)
