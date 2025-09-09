import http.client
import http.cookiejar
import logging
import os
import threading
import time
import urllib.parse
import urllib.request
import uuid
import webbrowser
import socketserver
import json

class Server:
    def __init__(self, host='localhost', port=8443):
        """Inicjalizacja serwera z hostem i portem."""
        self.host = host
        self.port = port
        self.server = None
        self.running = False
        self.logger = logging.getLogger(__name__)

    def handle_request(self, request):
        """Obsługa przychodzącego żądania (surowe dane TCP)."""
        try:
            data = request.request.recv(1024).strip().decode('utf-8', errors='ignore')  # Odbieranie danych
            session_id = str(uuid.uuid4())  # Generowanie tymczasowego ID sesji
            response = {"status": "ok", "session_id": session_id, "message": "Request received", "data": data}
            request.request.sendall(json.dumps(response).encode())
            self.logger.info(f"Obsłużono żądanie z {request.client_address}: {data}")
        except Exception as e:
            self.logger.error(f"Błąd obsługi żądania: {e}")
            request.request.sendall(json.dumps({"status": "error", "message": str(e)}).encode())

    class CustomRequestHandler(socketserver.BaseRequestHandler):
        def handle(self):
            self.server = self.server  # Poprawienie referencji
            self.server.handle_request(self)

    def start(self):
        """Uruchomienie serwera."""
        self.server = socketserver.TCPServer((self.host, self.port), self.CustomRequestHandler)
        self.server.handle_request = self.handle_request  # Przypisanie metody handle_request
        self.running = True
        self.logger.info(f"Serwer uruchomiony na {self.host}:{self.port}")
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    def stop(self):
        """Zatrzymanie serwera."""
        if self.running and self.server:
            self.server.shutdown()
            self.server.server_close()
            self.logger.info(f"Serwer na {self.host}:{self.port} zatrzymany.")
            self.running = False

if __name__ == "__main__":
    server = Server()
    server.start()
    time.sleep(10)  # Symulacja działania serwera
    server.stop()