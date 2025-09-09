import Server.ModuleClient as ModuleClient
import Server.ModuleServer as ModuleServer
import Server.ModuleSession as ModuleSession
import socketserver
import ssl

class EtycznyMenadzerSesji:
    def __init__(self, host='localhost', port=8443):
        self.host = host
        self.port = port
        self.sesja = None

    def startuj_serwer(self):
        # Symulacja uruchomienia serwera do zarządzania sesją
        serwer = ModuleServer.Server(self.host, self.port)
        serwer.start()
        print(f"Serwer uruchomiony na {self.host}:{self.port}")
        return serwer

    def polacz_klienta(self):
        # Etyczne połączenie klienta do przetestowania sesji
        klient = ModuleClient.Client(self.host, self.port)
        self.sesja = ModuleSession.Session(klient)
        self.sesja.start()
        print("Sesja klienta została ustanowiona.")
        return klient

    def zamknij_sesje(self):
        if self.sesja:
            self.sesja.close()
            print("Sesja została etycznie zamknięta.")

if __name__ == "__main__":
    menadzer = EtycznyMenadzerSesji()
    serwer = menadzer.startuj_serwer()
    klient = menadzer.polacz_klienta()
    # Symulacja aktywności sesji (np. testowanie limitu czasu)
    import time
    time.sleep(5)
    menadzer.zamknij_sesje()