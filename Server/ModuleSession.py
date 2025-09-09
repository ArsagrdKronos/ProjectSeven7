import time
import ssl
import socket

class Session:
    def __init__(self, client):
        """Inicjalizacja sesji z obiektem klienta."""
        self.client = client
        self.active = False
        self.start_time = None
        self.timeout = 300  # Limit czasu sesji w sekundach (5 minut)

    def start(self):
        """Rozpoczęcie sesji."""
        if not self.active:
            self.active = True
            self.start_time = time.time()
            print(f"Sesja rozpoczęta o {time.ctime(self.start_time)}")
            self._establish_connection()
        else:
            print("Sesja już jest aktywna.")

    def _establish_connection(self):
        """Symulacja ustanowienia połączenia (można rozszerzyć o SSL/sockety)."""
        try:
            # Przykładowe użycie klienta do nawiązania połączenia
            self.client.connect()
            print("Połączenie z klientem ustanowione.")
        except Exception as e:
            print(f"Błąd podczas nawiązywania połączenia: {e}")
            self.active = False

    def is_active(self):
        """Sprawdzenie, czy sesja jest nadal aktywna."""
        if not self.active:
            return False
        elapsed = time.time() - self.start_time
        return elapsed < self.timeout

    def close(self):
        """Zamknięcie sesji."""
        if self.active:
            self.active = False
            self.client.disconnect()
            print("Sesja została zamknięta.")
        else:
            print("Sesja nie jest aktywna, nie ma czego zamykać.")

    def get_session_duration(self):
        """Zwrócenie czasu trwania sesji (w sekundach)."""
        if self.start_time:
            return time.time() - self.start_time
        return 0

# Przykładowa integracja z klientem (jeśli nie zdefiniowano w ModuleClient)
if __name__ == "__main__":
    class DummyClient:
        def connect(self):
            print("DummyClient: Połączenie udane.")
        
        def disconnect(self):
            print("DummyClient: Rozłączenie udane.")

    # Test klasy Session
    dummy_client = DummyClient()
    session = Session(dummy_client)
    session.start()
    time.sleep(2)
    print(f"Czas trwania sesji: {session.get_session_duration()} sekund")
    session.close()