import json
import logging

class Payload:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def generate_payload(self, type="test"):
        """Generowanie ładunku (symulacja)."""
        try:
            self.logger.info(f"Generowanie ładunku typu {type}")
            payload = {"type": type, "data": "test_payload"}
            return json.dumps(payload)
        except Exception as e:
            self.logger.error(f"Błąd generowania ładunku: {e}")
            return {"error": str(e)}

if __name__ == "__main__":
    pay = Payload()
    print(pay.generate_payload("test"))