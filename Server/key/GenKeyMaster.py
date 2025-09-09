import uuid
import json

class GenKeyMaster:
    def __init__(self):
        self.master_key = None

    def generate_master_key(self):
        """Generowanie master key."""
        self.master_key = str(uuid.uuid4())
        print(f"Master key wygenerowany: {self.master_key}")
        return self.master_key

    def save_master_key(self, file_path='master_key.json'):
        """Zapisywanie master key do pliku."""
        if self.master_key:
            with open(file_path, 'w') as f:
                json.dump({"master_key": self.master_key}, f)
            print(f"Master key zapisany w {file_path}")

if __name__ == "__main__":
    gen = GenKeyMaster()
    gen.generate_master_key()
    gen.save_master_key()