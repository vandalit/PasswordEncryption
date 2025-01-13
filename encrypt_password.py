import base64

def encode_password(password):
    """Encode the password in Base64."""
    return base64.b64encode(password.encode('utf-8')).decode('utf-8')

def decode_password(encoded_password):
    """Decode a Base64-encoded password."""
    return base64.b64decode(encoded_password.encode('utf-8')).decode('utf-8')

def main():
    # Choose to encode or decode
    action = input("Enter 'encode' to encode a password or 'decode' to decode a password: ").strip().lower()

    if action == 'encode':
        # Read password from a file
        try:
            with open("input_password.txt", "r") as file:
                password = file.read().strip()
        except FileNotFoundError:
            print("Error: input_password.txt file not found!")
            return

        # Encode the password
        encoded_password = encode_password(password)

        # Write the encoded password to a file
        with open("output_encoded.txt", "w") as file:
            file.write(encoded_password)

        print(f"Password encoded and saved to output_encoded.txt.\nEncoded Password: {encoded_password}")

    elif action == 'decode':
        # Read the encoded password from a file
        try:
            with open("output_encoded.txt", "r") as file:
                encoded_password = file.read().strip()
        except FileNotFoundError:
            print("Error: output_encoded.txt file not found!")
            return

        # Decode the password
        decoded_password = decode_password(encoded_password)

        # Write the decoded password to a file
        with open("output_decoded.txt", "w") as file:
            file.write(decoded_password)

        print(f"Password decoded and saved to output_decoded.txt.\nDecoded Password: {decoded_password}")

    else:
        print("Invalid action! Please enter 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
