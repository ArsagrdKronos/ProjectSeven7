# Special modules to handle Server, Client, Key and Generate Key Master
import Server.ModuleClient as ModuleClient
import Server.ModuleServer as ModuleServer
import Server.key.ModuleKey as ModuleKey
import Server.key.GenKeyMaster as GenKeyMaster
# Dodane importy
import Server.session_manager as session_manager
# API to Seven7.py
import API.ModuleCommand as ModuleCommand
import API.ModuleExploit as ModuleExploit
import API.ModuleMaping as ModuleMaping
import API.ModulePayload as ModulePayload
import API.ModuleMenu as ModuleMenu
import Server.ModuleSession as ModuleSession
import API.ModuleScan as ModuleScan
import API.ModuleLodderScriptAll as ModuleLodderScriptAll
# LIB
import socketserver
import ssl
import struct
import venv
import zipfile
import shutil
import subprocess
import platform
import sysconfig
import json
import html
import enum
import smtplib
import mimetypes
import email
import email.policy
import email.mime.application
import email.mime.multipart
import email.mime.text
import email.mime.base
import email.mime.image
import email.mime.audio
import email.encoders
import getpass
import inspect
import pathlib
import re
import time
import urllib.request  # Do pobrania IP
import os  # Do obsługi plików i folderów logów
import datetime  # Do timestampów w logach
from colorama import init, Fore, Style
init()

# Ścieżki do folderów i plików logów
LOG_FOLDER = "log"
EMAIL_FOLDER = "Email"
REBOOT_LOG = os.path.join(LOG_FOLDER, "Reboot.txt")
RELOAD_LOG = os.path.join(LOG_FOLDER, "Reload.txt")
RESET_LOG = os.path.join(LOG_FOLDER, "Reset.txt")
EMAIL_LOG = os.path.join(EMAIL_FOLDER, "Email.txt")

# Tworzenie folderów jeśli nie istnieją
os.makedirs(LOG_FOLDER, exist_ok=True)
os.makedirs(EMAIL_FOLDER, exist_ok=True)

class Seven7Main:
    def __init__(self):
        """Inicjalizacja głównego programu Seven7."""
        self.menu = ModuleMenu.Menu()
        self.session_manager = session_manager.EtycznyMenadzerSesji()
        self.key_gen = GenKeyMaster.GenKeyMaster()
        self.key = ModuleKey.Key()
        self.master_key = self.key_gen.generate_master_key()  # Generowanie master key
        self.session = None
        self.scanner = ModuleScan.Scanner()
        self.command = ModuleCommand.Command()
        self.exploit = ModuleExploit.Exploit()
        self.mapping = ModuleMaping.Mapping()
        self.payload = ModulePayload.Payload()
        # Ładowanie wszystkich modułów z API
        ModuleLodderScriptAll.load_all_modules()
        print(Fore.GREEN + "Seven7: Etyczny skaner emaili załadowany. Master key: " + self.master_key + Style.RESET_ALL)
        self.log_action("Inicjalizacja programu")

    def log_action(self, message, log_file=EMAIL_LOG, send_to_email=False, email_to=None, smtp_host=None, smtp_port=None, from_email=None, password=None):
        """Logowanie akcji do pliku i opcjonalnie wysyłanie na email."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
        print(Fore.YELLOW + f"Log dodany do {log_file}: {message}" + Style.RESET_ALL)
        
        if send_to_email and email_to and smtp_host and smtp_port and from_email and password:
            encrypted_log = self.key.encrypt(log_entry)
            decrypted_log = self.key.decrypt(encrypted_log)  # Dla weryfikacji
            self.send_test_email(smtp_host, smtp_port, from_email, email_to, password, "Log Seven7", decrypted_log)

    def start_session(self):
        """Rozpoczęcie sesji z użyciem session_manager."""
        try:
            self.session_manager.startuj_serwer()
            self.session_manager.polacz_klienta()
            self.session = self.session_manager
            self.log_action("Sesja rozpoczęta", log_file=RESET_LOG, send_to_email=True, 
                            email_to=input("Email do logu (opcjonalnie): ") or None,
                            smtp_host=input("SMTP Host: ") or 'smtp.gmail.com',
                            smtp_port=int(input("Port: ") or 587),
                            from_email=input("From: ") or '',
                            password=getpass.getpass("Password: ") if input("Wyślij log na email? (t/n): ") == 't' else None)
            print(Fore.GREEN + "Sesja rozpoczęta z master key." + Style.RESET_ALL)
        except Exception as e:
            self.log_action(f"Błąd startu sesji: {e}", log_file=RESET_LOG)
            print(Fore.RED + f"Błąd sesji: {e}" + Style.RESET_ALL)

    def close_session(self):
        """Zamknięcie sesji."""
        try:
            self.session_manager.zamknij_sesje()
            self.log_action("Sesja zamknięta", log_file=RESET_LOG)
            print(Fore.GREEN + "Sesja zamknięta." + Style.RESET_ALL)
        except Exception as e:
            self.log_action(f"Błąd zamknięcia sesji: {e}", log_file=RESET_LOG)
            print(Fore.RED + f"Błąd zamknięcia sesji: {e}" + Style.RESET_ALL)

    def reset_session(self):
        """Reset sesji: Zamknięcie i ponowne otwarcie."""
        self.log_action("Reset sesji rozpoczęty", log_file=RESET_LOG)
        self.close_session()
        time.sleep(2)
        self.start_session()
        self.log_action("Reset sesji zakończony", log_file=RESET_LOG, send_to_email=True, 
                        email_to=input("Email do logu resetu: ") or None,
                        smtp_host='smtp.gmail.com', smtp_port=587,
                        from_email=input("From: ") or '', password=getpass.getpass("Password: "))

    def reboot_program(self):
        """Symulacja reboot: Zapisz logi i wyjście z programu."""
        self.log_action("Reboot programu", log_file=REBOOT_LOG, send_to_email=True, 
                        email_to=input("Email do logu reboot: ") or None,
                        smtp_host='smtp.gmail.com', smtp_port=587,
                        from_email=input("From: ") or '', password=getpass.getpass("Password: "))
        print(Fore.RED + "Symulacja reboot: Program zostanie zamknięty." + Style.RESET_ALL)
        exit(0)

    def reload_modules(self):
        """Przeładowanie modułów z API."""
        self.log_action("Reload modułów rozpoczęty", log_file=RELOAD_LOG)
        ModuleLodderScriptAll.load_all_modules()
        self.log_action("Reload modułów zakończony", log_file=RELOAD_LOG, send_to_email=True, 
                        email_to=input("Email do logu reload: ") or None,
                        smtp_host='smtp.gmail.com', smtp_port=587,
                        from_email=input("From: ") or '', password=getpass.getpass("Password: "))
        print(Fore.GREEN + "Moduły przeładowane." + Style.RESET_ALL)

    def get_public_ip(self):
        """Pobranie publicznego IP użytkownika."""
        try:
            ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
            return ip
        except Exception as e:
            print(Fore.RED + f"Błąd pobierania IP: {e}" + Style.RESET_ALL)
            return "Nieznane IP"

    def scan_and_send_user_data(self):
        """Scanowanie: Podaj dane i wyślij email z nimi."""
        email = input("Podaj swój adres email: ")
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        data_zalozenia = input("Podaj datę założenia konta (np. YYYY-MM-DD): ")
        ip = self.get_public_ip()
        dane = f"Imię: {imie}\nNazwisko: {nazwisko}\nData założenia: {data_zalozenia}\nIP: {ip}"
        # "Szyfrowanie" danych kluczem (demonstracja)
        encrypted_dane = self.key.encrypt(dane)
        print(Fore.YELLOW + f"Zaszyfrowane dane: {encrypted_dane}" + Style.RESET_ALL)
        decrypted_dane = self.key.decrypt(encrypted_dane)
        # Wysyłanie emaila
        smtp_host = input("SMTP Host (np. smtp.gmail.com): ")
        smtp_port = int(input("Port (np. 587): "))
        from_email = input("Email nadawcy: ")
        password = getpass.getpass("Hasło nadawcy: ")
        self.send_test_email(smtp_host, smtp_port, from_email, email, password, "Skan Seven7", decrypted_dane)
        self.log_action(f"Skan użytkownika: {dane}", log_file=EMAIL_LOG, send_to_email=True, 
                        email_to=email, smtp_host=smtp_host, smtp_port=smtp_port, from_email=from_email, password=password)

    def show_help(self):
        """Wyświetlenie pomocy."""
        print(Fore.CYAN + "Pomoc Seven7:" + Style.RESET_ALL)
        print("- 1: Skanuj serwer SMTP")
        print("- 2: Wyślij testowy email")
        print("- 3: Skanuj plik email")
        print("- 4: Etyczny test exploitów")
        print("- 5: Uruchom sesję klient-serwer")
        print("- 6: Mapuj sieć")
        print("- 7: Wykonaj komendę")
        print("- 8: Scanowanie użytkownika (wyślij email z danymi)")
        print("- 9: Help (ta komenda)")
        print("- 10: Reset sesji")
        print("- 11: Reboot programu")
        print("- 12: Reload modułów")
        print("- 13: Wyjście")
        self.log_action("Wyświetlono pomoc", log_file=EMAIL_LOG)

    def scan_smtp_server(self, host='localhost', port=587):
        """Skanowanie serwera SMTP (ulepszone z logowaniem)."""
        try:
            print(Fore.YELLOW + f"Skanowanie SMTP {host}:{port}..." + Style.RESET_ALL)
            server = smtplib.SMTP(host, port, timeout=10)
            # Opcjonalne wyłączenie TLS dla testów (usuń, jeśli niepotrzebne)
            use_tls = input("Użyć TLS? (t/n): ") == 't'
            if use_tls:
                server.starttls()
            server.ehlo()
            capabilities = server.esmtp_features
            server.quit()
            result = {"status": "success", "capabilities": capabilities}
            print(Fore.GREEN + f"Sukces: Serwer SMTP dostępny. Funkcje: {json.dumps(capabilities, indent=2)}" + Style.RESET_ALL)
            self.log_action(f"Skan SMTP {host}:{port} - Wynik: {result}", log_file=EMAIL_LOG, send_to_email=True, 
                            email_to=input("Email do logu: ") or None,
                            smtp_host='smtp.gmail.com', smtp_port=587,
                            from_email=input("From: ") or '', password=getpass.getpass("Password: "))
            return result
        except Exception as e:
            print(Fore.RED + f"Błąd skanowania SMTP: {e}" + Style.RESET_ALL)
            self.log_action(f"Błąd skanowania SMTP {host}:{port}: {e}", log_file=EMAIL_LOG)
            return {"status": "error", "message": str(e)}

    def send_test_email(self, smtp_host, smtp_port, from_email, to_email, password, subject, message):
        """Wysłanie testowego emaila (ulepszone z logowaniem)."""
        try:
            msg = email.mime.text.MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = from_email
            msg['To'] = to_email

            server = smtplib.SMTP(smtp_host, smtp_port)
            use_tls = input("Użyć TLS? (t/n): ") == 't'
            if use_tls:
                server.starttls()
            server.login(from_email, password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            server.quit()
            print(Fore.GREEN + "Testowy email wysłany pomyślnie." + Style.RESET_ALL)
            self.log_action(f"Wysłano email do {to_email}: {subject}", log_file=EMAIL_LOG)
            return {"status": "success"}
        except Exception as e:
            print(Fore.RED + f"Błąd wysyłania emaila: {e}" + Style.RESET_ALL)
            self.log_action(f"Błąd wysyłania emaila: {e}", log_file=EMAIL_LOG)
            return {"status": "error", "message": str(e)}

    def scan_email_file(self, file_path):
        """Skanowanie pliku email (ulepszone z logowaniem)."""
        try:
            print(Fore.YELLOW + f"Skanowanie pliku email: {file_path}" + Style.RESET_ALL)
            with open(file_path, 'r', encoding='utf-8') as f:
                msg = email.message_from_file(f, policy=email.policy.default)
            
            results = {
                "subject": msg.get('Subject', 'Brak'),
                "from": msg.get('From', 'Brak'),
                "links": re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', msg.as_string()),
                "attachments": [part.get_filename() for part in msg.walk() if part.get_filename()],
                "suspicious": len(re.findall(r'http', msg.as_string())) > 5
            }
            print(Fore.GREEN + f"Wyniki skanowania: {json.dumps(results, indent=2, ensure_ascii=False)}" + Style.RESET_ALL)
            self.log_action(f"Skan pliku {file_path} - Wynik: {results}", log_file=EMAIL_LOG, send_to_email=True, 
                            email_to=input("Email do logu: ") or None,
                            smtp_host='smtp.gmail.com', smtp_port=587,
                            from_email=input("From: ") or '', password=getpass.getpass("Password: "))
            return results
        except Exception as e:
            print(Fore.RED + f"Błąd skanowania pliku: {e}" + Style.RESET_ALL)
            self.log_action(f"Błąd skanowania pliku {file_path}: {e}", log_file=EMAIL_LOG)
            return {"status": "error", "message": str(e)}

    def ethical_exploit_test(self, smtp_host):
        """Etyczny test exploitów (ulepszone z logowaniem)."""
        result = self.exploit.test_vulnerability(smtp_host)
        payload = self.payload.generate_payload("smtp_test")
        print(Fore.CYAN + f"Test exploitów: {json.dumps(result)}" + Style.RESET_ALL)
        print(Fore.CYAN + f"Testowy payload: {payload}" + Style.RESET_ALL)
        self.log_action(f"Test exploitów na {smtp_host} - Wynik: {result}, Payload: {payload}", log_file=EMAIL_LOG, send_to_email=True, 
                        email_to=input("Email do logu: ") or None,
                        smtp_host='smtp.gmail.com', smtp_port=587,
                        from_email=input("From: ") or '', password=getpass.getpass("Password: "))
        return result

    def run_menu(self):
        """Główne menu programu (rozszerzone o nowe opcje)."""
        options = {
            "1": ("Skanuj serwer SMTP", lambda: self.scan_smtp_server(input("Host: ") or 'localhost', int(input("Port: ") or 587))),
            "2": ("Wyślij testowy email", lambda: self.send_test_email(
                input("SMTP Host: "), int(input("Port: ")), 
                input("From: "), input("To: "), getpass.getpass("Password: "), 
                input("Temat: "), input("Wiadomość: "))),
            "3": ("Skanuj plik email (EML/MBOX)", lambda: self.scan_email_file(input("Ścieżka do pliku: "))),
            "4": ("Etyczny test exploitów na mailu", lambda: self.ethical_exploit_test(input("SMTP Host: "))),
            "5": ("Uruchom sesję klient-serwer", lambda: self.start_session()),
            "6": ("Mapuj sieć mailową", lambda: self.mapping.map_network(input("Target: "))),
            "7": ("Wykonaj komendę", lambda: print(self.command.execute(input("Komenda (JSON): ")))),
            "8": ("Scanowanie użytkownika (wyślij email z danymi)", self.scan_and_send_user_data),
            "9": ("Help", self.show_help),
            "10": ("Reset sesji", self.reset_session),
            "11": ("Reboot programu", self.reboot_program),
            "12": ("Reload modułów", self.reload_modules),
            "13": ("Wyjście", exit)
        }
        while True:
            self.menu.display(options)
            choice = input("Wybierz: ")
            if choice in options:
                options[choice][1]()
            else:
                print("Nieprawidłowy wybór.")
            self.log_action(f"Wybrano opcję menu: {choice}", log_file=EMAIL_LOG)

if __name__ == "__main__":
    app = Seven7Main()
    app.start_session()  # Rozpoczęcie sesji na starcie
    try:
        app.run_menu()
    finally:
        app.close_session()
        app.log_action("Program zakończony", log_file=REBOOT_LOG)