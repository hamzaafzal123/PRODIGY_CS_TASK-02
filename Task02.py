from PIL import Image
import numpy as np


def encrypt_image(image_path, key):
  
    img = Image.open(image_path)
    img_array = np.array(img)

    
    encrypted_array = (img_array + key) % 256

    
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))

    
    encrypted_img.save('encrypted_image.png')
    print("Image encrypted and saved as 'encrypted_image.png'.")

def decrypt_image(encrypted_image_path, key):
   
    img = Image.open(encrypted_image_path)
    img_array = np.array(img)

    
    decrypted_array = (img_array - key) % 256

    
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))

  
    decrypted_img.save('decrypted_image.png')
    print("Image decrypted and saved as 'decrypted_image.png'.")


if __name__ == "__main__":
    
    image_path = 'your_image.png'  # Replace with your image path
    key = 50

   
    encrypt_image(image_path, key)

    
    decrypt_image('encrypted_image.png', key)
