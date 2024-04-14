# En Az Anlamlı Bit (LSB) Kullanarak Steganografi

Steganografi, mesajları veya bilgileri diğer gizli olmayan verilerin içine gizleme pratiğidir. Dijital görüntülerde steganografinin yaygın bir yöntemi, En Az Anlamlı Bit (LSB) tekniğidir.

## LSB Steganografi Nasıl Çalışır

LSB steganografisinde, bir görüntünün her pikselinin en az anlamlı biti, gizli mesajın bir kısmıyla değiştirilir. Çoğunlukla LSB'ler genellikle renk bilgilerinin en az fark edilen kısmını temsil ettiğinden, bunları değiştirmek genellikle görüntünün insan gözü için görünümünü önemli ölçüde etkilemez.

## Uygulama

Sağlanan Python kodu, PIL (Python Imaging Library) kullanarak LSB steganografisinin basit bir uygulamasını göstermektedir. Adımların açıklaması şu şekildedir:

1. **Görüntülerin Açılması**: Veri gizlenecek kapak görüntüsü ve gizli görüntü (gizli mesaj) PIL kullanılarak açılır.
   
2. **Yeniden Boyutlandırma**: Gizli görüntü, uyumluluğu sağlamak için kapak görüntüsünün boyutlarına uyacak şekilde yeniden boyutlandırılır.

3. **İkiliye Dönüştürme**: Gizli görüntünün RGB piksel değerleri ikili formata dönüştürülür.

4. **Verinin Gömülmesi**: Her kapak görüntüsünün pikseli, LSB'leri gizli görüntüden gelen bitlerle değiştirilerek işlenir.

5. **Stego Görüntüsünün Kaydedilmesi**: Gömülü verilerle sonuçlanan görüntü, çıktı görüntüsü olarak kaydedilir.

## Nasıl Kullanılır

Bu kodu kullanmak için şu adımları izleyebilirsiniz:

1. Kapak görüntüsünü (`cover_image_path`) ve gizlemek istediğiniz görüntüyü (`hidden_image_path`) hazırlayın.
   
2. Bu yolları, istenen çıktı yolunu (`output_image_path`) ile birlikte `embed_image` işlevine çağırın.

3. İşlev, gizli görüntüyü kapak görüntüsüne gömecek ve sonuçta oluşan stego görüntüsünü kaydedecektir.

## Örnek

```python
embed_image("LSB\\images\\1.jpg", "LSB\\images\\2.jpg", "LSB\\images\\stego_image.jpg")
