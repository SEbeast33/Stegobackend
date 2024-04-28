from stegano import lsb
import hashlib
import cloudinary.uploader
# import cloudinary.downloader
import requests
import os
from django.conf import settings

# Function to encrypt message with secret key

cloudinary.config(
  cloud_name = "dkzbn6s7o",
  api_key = "469164442535396",
  api_secret = "gCw9wEEb42-nBMmGdPJ9vGlOu10"
)

# Function to decrypt message with secret key
def decrypt_message(encrypted_message, key):
    # Take the first four integers of the key and concatenate them
    key_str = ''.join(map(str, key[:4]))
    # Use hashlib to hash the concatenated key
    hashed_key = hashlib.sha256(key_str.encode()).hexdigest()
    # Check if the hashed key matches the first characters of the encrypted message
    if encrypted_message.startswith(hashed_key):
        # If it matches, return the decrypted message
        return encrypted_message[len(hashed_key):]
    else:
        # If it doesn't match, return None
        return None
def encrypt_message(message, key):
    key_str = ''.join(map(str, key[:4]))
    hashed_key = hashlib.sha256(key_str.encode()).hexdigest()
    encrypted_message = hashed_key + message
    return encrypted_message

# Function to hide message in image and save to Cloudinary
def hide_message_in_image(image_path, message, key):
    base_dir_path = settings.BASE_DIR
    # print(base_dir_path)
    # print(path)
    image_path = os.path.join(base_dir_path,*image_path.split('/'))
	

	
	
    encrypted_message = encrypt_message(message, key)
    secret = lsb.hide(image_path, encrypted_message)
    secret_image_path = 'hidden_image.png'
    secret.save(secret_image_path)
    # Save the image with the hidden message to Cloudinary
 
    result = cloudinary.uploader.upload(secret_image_path, public_id="hidden_image", overwrite=True)
    print("Message hidden successfully.")
    # Return the URL of the saved image
    return result['secure_url']

# Function to extract message from image


def extract_message_from_image(image_url, key):
    # Temporary folder path
    temp_folder = 'temp'

    # Create the temporary folder if it doesn't exist
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    # Extract the image filename from the URL
    image_filename = image_url.split('/')[-1]

    # File path to save the image in the temporary folder
    image_path = os.path.join(temp_folder, image_filename)

    # Download the image from Cloudinary
    response = requests.get(image_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the image to the temporary folder
        with open(image_path, 'wb') as f:
            f.write(response.content)

        print("Image downloaded successfully to:", image_path)

        # Extract the hidden message from the image
        encrypted_message = lsb.reveal(image_path)
        print(encrypt_message)

        # Decrypt the message with the secret key
        decrypted_message = decrypt_message(encrypted_message, key)
        if decrypted_message:
            print("Decrypted message:", decrypted_message)
        else:
            return("Invalid key or no message found.")

        return decrypted_message
    else:
        return("Failed to download the image from the specified URL.")



# Example usage

# key = [123, 456, 789, 1011]

# Hide message in image and save to Cloudinary

