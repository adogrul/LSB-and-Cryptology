from PIL import Image

def embed_image(cover_image_path, hidden_image_path, output_image_path):
    cover_image = Image.open(cover_image_path)
    hidden_image = Image.open(hidden_image_path)

    
    hidden_image = hidden_image.resize(cover_image.size)

    
    hidden_pixels = hidden_image.convert('RGB').getdata()
    binary_hidden_data = ''.join(format(pixel[i], '08b') for pixel in hidden_pixels for i in range(3))

    
    cover_pixels = list(cover_image.getdata())
    new_cover_pixels = []
    data_index = 0

    for pixel in cover_pixels:
        if data_index < len(binary_hidden_data):
            new_red = format(pixel[0], '08b')[:-1] + binary_hidden_data[data_index]
            new_green = format(pixel[1], '08b')[:-1] + binary_hidden_data[data_index+1]
            new_blue = format(pixel[2], '08b')[:-1] + binary_hidden_data[data_index+2]
            new_pixel = (int(new_red, 2), int(new_green, 2), int(new_blue, 2))
            new_cover_pixels.append(new_pixel)
            data_index += 3
        else:
            new_cover_pixels.append(pixel)

    
    stego_image = Image.new(cover_image.mode, cover_image.size)
    stego_image.putdata(new_cover_pixels)
    stego_image.save(output_image_path)


embed_image("LSB\\images\\1.jpg", "LSB\\images\\2.jpg", "LSB\\images\\stego_image.jpg")
