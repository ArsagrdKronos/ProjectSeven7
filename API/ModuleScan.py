import json
import logging
import socket

class Scanner:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def scan(self, target, port):
        """Skanowanie portów (symulacja)."""
        try:
            self.logger.info(f"Skanowanie {target}:{port}")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target, port))
            sock.close()
            return {"target": target, "port": port, "open": result == 0}
        except Exception as e:
            self.logger.error(f"Błąd skanowania: {e}")
            return {"target": target, "error": str(e)}

if __name__ == "__main__":
    scan = Scanner()
    print(scan.scan("localhost", 80))