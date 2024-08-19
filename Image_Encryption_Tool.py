from PIL import Image, ImageFilter
import numpy as np

def print_heading():
    """Print the tool's heading with ASCII art."""
    heading = """
  ____        _ _                 
 |  _ \\  ___ | | | ___ _ __   __ _ 
 | | | |/ _ \\| | |/ _ \\ '_ \\ / _` |
 | |_| | (_) | | |  __/ | | | (_| |
 |____/ \\___/|_|_|\\___|_| |_|\\__,_|
                                   
    """
    print(heading)
    print("------------- Image Encryption Tool --------------")

def xor_with_key(image_array, key):
    """Apply XOR operation with the key to the image array."""
    # Create an array filled with the key value, matching the shape and type of the image array
    key_array = np.full_like(image_array, key, dtype=np.uint8)
    # Apply XOR operation to each pixel
    return np.bitwise_xor(image_array, key_array)

def apply_blur(image):
    """Apply a Gaussian blur to the image."""
    return image.filter(ImageFilter.GaussianBlur(radius=5))  # Adjust radius as needed

def encrypt_image(image_path, key):
    """Encrypt the image located at image_path using the provided key and apply blur."""
    try:
        # Open the image
        original_image = Image.open(image_path)
        
        # Apply blur to the image
        blurred_image = apply_blur(original_image)
        
        # Convert image to NumPy array
        image_array = np.array(blurred_image)

        # Encrypt the image array
        encrypted_image_array = xor_with_key(image_array, key)

        # Create and save the encrypted image
        encrypted_image = Image.fromarray(encrypted_image_array)
        encrypted_image_path = "encrypted_image.png"
        encrypted_image.save(encrypted_image_path)
        
        print(f"Image encrypted successfully. Encrypted image saved at: {encrypted_image_path}")
    except FileNotFoundError:
        print("Error: Image file not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def decrypt_image(encrypted_image_path, key):
    """Decrypt the image located at encrypted_image_path using the provided key."""
    try:
        # Open the encrypted image
        encrypted_image = Image.open(encrypted_image_path)
        
        # Convert image to NumPy array
        encrypted_image_array = np.array(encrypted_image)

        # Decrypt the image array
        decrypted_image_array = xor_with_key(encrypted_image_array, key)

        # Create and save the decrypted image
        decrypted_image = Image.fromarray(decrypted_image_array)
        decrypted_image_path = "decrypted_image.png"
        decrypted_image.save(decrypted_image_path)
        
        print(f"Image decrypted successfully. Decrypted image saved at: {decrypted_image_path}")
    except FileNotFoundError:
        print("Error: Encrypted image file not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to handle user input and invoke encryption/decryption."""
    print_heading()
    
    while True:
        print("Select an option:")
        print("e - Encrypt image")
        print("d - Decrypt image")
        print("q - Quit")
        choice = input("Your choice: ").strip().lower()

        if choice == 'e':
            handle_encryption()
        elif choice == 'd':
            handle_decryption()
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")

def handle_encryption():
    """Handle the encryption process."""
    try:
        key = int(input("Enter encryption key (0-255): ").strip())
        image_location = input("Enter the location of the image: ").strip()
        encrypt_image(image_location, key)
    except ValueError:
        print("Error: Invalid key. Please enter a numeric value between 0 and 255.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def handle_decryption():
    """Handle the decryption process."""
    try:
        key = int(input("Enter decryption key (0-255): ").strip())
        encrypted_image_location = input("Enter the location of the encrypted image: ").strip()
        decrypt_image(encrypted_image_location, key)
    except ValueError:
        print("Error: Invalid key. Please enter a numeric value between 0 and 255.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

