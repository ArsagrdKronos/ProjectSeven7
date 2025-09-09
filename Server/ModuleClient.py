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

class Client:
    def __init__(self, host='localhost', port=8443):
        """Inicjalizacja klienta z hostem i portem."""
        self.host = host
        self.port = port
        self.connection = None
        self.cookie_jar = http.cookiejar.CookieJar()
        self.session_id = str(uuid.uuid4())
        self.logger = logging.getLogger(__name__)

    def connect(self):
        """Nawiązanie połączenia z serwerem."""
        try:
            self.connection = http.client.HTTPSConnection(self.host, self.port)
            self.connection.connect()
            self.logger.info(f"Połączenie z {self.host}:{self.port} ustanowione. ID sesji: {self.session_id}")
            return True
        except Exception as e:
            self.logger.error(f"Błąd połączenia: {e}")
            return False

    def disconnect(self):
        """Zamknięcie połączenia z serwerem."""
        if self.connection:
            self.connection.close()
            self.logger.info(f"Połączenie z {self.host}:{self.port} zamknięte.")
            self.connection = None

    def send_request(self, path="/", method="GET", body=None):
        """Wysłanie żądania HTTP do serwera."""
        if not self.connection:
            if not self.connect():
                return None
        headers = {"Session-ID": self.session_id}
        try:
            self.connection.request(method, path, body, headers)
            response = self.connection.getresponse()
            data = response.read().decode()
            self.logger.info(f"Odebrano odpowiedź: {data}")
            return json.loads(data) if data else {}
        except Exception as e:
            self.logger.error(f"Błąd żądania: {e}")
            return None

    def open_in_browser(self, url):
        """Otwarcie URL w przeglądarce."""
        webbrowser.open(f"https://{self.host}:{self.port}{url}")

if __name__ == "__main__":
    client = Client()
    client.connect()
    client.send_request("/test")
    client.disconnect()