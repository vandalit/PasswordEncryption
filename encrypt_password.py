import base64
import pyperclip  # To copy results to the clipboard (optional)

def encode_password(password):
    """Encode the password in Base64."""
    return base64.b64encode(password.encode('utf-8')).decode('utf-8')

def decode_password(encoded_password):
    """Decode a Base64-encoded password."""
    return base64.b64decode(encoded_password.encode('utf-8')).decode('utf-8')

def main():
    # Choose the action: Encode or Decode
    action = input("Enter 'encode' to encode a password or 'decode' to decode a password: ").strip().lower()

    if action == 'encode':
        # Get password input from the user
        password = input("Enter the password to encode: ").strip()
        encoded_password = encode_password(password)
        print(f"Encoded Password: {encoded_password}")
        
        # Copy to clipboard (optional)
        pyperclip.copy(encoded_password)
        print("Encoded password copied to clipboard!")

    elif action == 'decode':
        # Get encoded password input from the user
        encoded_password = input("Enter the Base64-encoded password to decode: ").strip()
        try:
            decoded_password = decode_password(encoded_password)
            print(f"Decoded Password: {decoded_password}")

            # Copy to clipboard (optional)
            pyperclip.copy(decoded_password)
            print("Decoded password copied to clipboard!")
        except Exception as e:
            print(f"Error: Unable to decode the password. {e}")

    else:
        print("Invalid action! Please enter 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
