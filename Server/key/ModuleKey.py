import base64
import uuid

class Key:
    def __init__(self):
        self.key = str(uuid.uuid4()).encode()  # Prosty klucz jako UUID

    def encrypt(self, data):
        """Proste szyfrowanie danych (base64)."""
        return base64.b64encode(data.encode())

    def decrypt(self, encrypted_data):
        """Deszyfrowanie danych (base64)."""
        return base64.b64decode(encrypted_data).decode()

if __name__ == "__main__":
    key = Key()
    encrypted = key.encrypt("Testowe dane")
    print(f"Zaszyfrowane: {encrypted}")
    decrypted = key.decrypt(encrypted)
    print(f"Odszyfrowane: {decrypted}")