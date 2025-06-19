# SecureChatCLI

Aplicación de línea de comando CLI en Python que:

- Genera y guarda claves secretas
- Crifra un mensaje con AES en modo CBC
- Envia el mensaje cifrado
- Descifra con la misma clave y IV
- Gestiona claves desde archivos

## Ejemplo de uso
```bash
python main.py generate
python main.py encrypt --message "[Message to encrypt]"
python main.py decrypt
```

## Outputs

- Key -> `keys/key.key`
- Ciphertext -> `messages/ciphertext.bin`
- IV -> `messages/iv.bin`