import argparse
import os
from crypto_utils import generate_key, load_key, encrypt_message, decrypt_message

def check_directories():
    os.makedirs("keys", exist_ok=True)
    os.makedirs("messages", exist_ok=True)

def main():
    parser = argparse.ArgumentParser(description="SecureChatCLI: Encrypt & Decrypt Messages")
    parser.add_argument("mode", choices=["generate", "encrypt", "decrypt"], help="Mode of operation")
    parser.add_argument("--message", type=str, help="Message to encrypt")
    args = parser.parse_args()
    
    check_directories()
    
    if args.mode == "generate":
        generate_key()
        print("Key generated and saved to 'keys/key.key'")
    elif args.mode == "encrypt":
        if not args.message:
            print("Error: --message argument needs a message to encrypt")
            return
        key = load_key()
        encrypt_message(args.message, key)
        print("Message encrypted and saved to 'messages/ciphertext.bin' and 'messages/iv.bin'")
    elif args.mode == "decrypt":
        key = load_key()
        decrypted_message = decrypt_message(key)
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()