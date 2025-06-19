from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_key(route="keys/key.key"):
    key = get_random_bytes(32)
    with open(route, "wb") as key_file:
        key_file.write(key)
    return key

def load_key(route="keys/key.key"):
    with open(route, "rb") as key_file:
        return key_file.read()
    
def encrypt_message(message, key, iv_path="messages/iv.bin", message_path="messages/ciphertext.bin"):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    
    with open(iv_path, "wb") as f_iv, open(message_path, "wb") as f_message:
        f_iv.write(iv)
        f_message.write(ciphertext)
        
def decrypt_message(key, iv_path="messages/iv.bin", message_path="messages/ciphertext.bin"):
    with open(iv_path, "rb") as f_iv, open(message_path, "rb") as f_message:
        iv = f_iv.read()
        ciphertext = f_message.read()
    
    descipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(descipher.decrypt(ciphertext), AES.block_size)
    
    return plaintext.decode()