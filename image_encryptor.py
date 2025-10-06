from PIL import Image

def encrypt_image(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (255 - r, 255 - g, 255 - b)  # simple invert

    img.save("encrypted_" + image_path)
    print(f"Encrypted image saved as encrypted_{image_path}")

def decrypt_image(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (255 - r, 255 - g, 255 - b)  # same logic to revert

    img.save("decrypted_" + image_path)
    print(f"Decrypted image saved as decrypted_{image_path}")

if __name__ == "__main__":
    image_file = input("Enter image filename: ")
    action = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    if action == 'e':
        encrypt_image(image_file)
    elif action == 'd':
        decrypt_image(image_file)
    else:
        print("Invalid choice.")
