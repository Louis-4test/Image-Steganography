
from PIL import Image

def _int_to_bin(rgb):
    return [format(i, '08b') for i in rgb]

def _bin_to_int(bin_rgb):
    return [int(b, 2) for b in bin_rgb]

def encode_image(image_path, text, output_path):
    image = Image.open(image_path)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    binary_text = ''.join([format(ord(char), '08b') for char in text]) + '1111111111111110'  # EOF marker
    data_index = 0
    img_data = image.getdata()
    
    new_pixels = []
    for pixel in img_data:
        r, g, b = _int_to_bin(pixel)
        if data_index < len(binary_text):
            r = r[:-1] + binary_text[data_index]
            data_index += 1
        if data_index < len(binary_text):
            g = g[:-1] + binary_text[data_index]
            data_index += 1
        if data_index < len(binary_text):
            b = b[:-1] + binary_text[data_index]
            data_index += 1
        
        new_pixels.append(tuple(_bin_to_int([r, g, b])))
        
        if data_index >= len(binary_text):
            break

    image.putdata(new_pixels)
    image.save(output_path)
    return True

def decode_image(image_path):
    image = Image.open(image_path)
    img_data = image.getdata()

    binary_data = ''
    for pixel in img_data:
        r, g, b = _int_to_bin(pixel)
        binary_data += r[-1] + g[-1] + b[-1]

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    extracted = ''
    for byte in all_bytes:
        if byte == '11111110':  # EOF marker
            break
        extracted += chr(int(byte, 2))

    return extracted