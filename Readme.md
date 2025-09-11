# Seven7 - Etyczny Skaner Emaili

Witaj w projekcie **Seven7**, zaawansowanym narzędziu open-source napisanym w Pythonie, zaprojektowanym do etycznego skanowania i analizy systemów pocztowych oraz zarządzania sesjami sieciowymi. Seven7 wspiera użytkowników w testowaniu bezpieczeństwa emaili, oferując funkcje takie jak skanowanie serwerów SMTP, wysyłanie zaszyfrowanych testowych emaili, generowanie logów oraz zarządzanie sesjami klient-serwer.

## Opis Projektu

Seven7 to wielomodułowa aplikacja, która łączy w sobie narzędzia do:
- **Skanowania serwerów SMTP** – Sprawdzanie dostępności i funkcji serwerów pocztowych.
- **Wysyłania testowych emaili** – Możliwość wysyłania zaszyfrowanych wiadomości z logowaniem działań.
- **Zarządzania sesjami** – Rozpoczynanie, resetowanie i zamykanie sesji sieciowych.
- **Logowania** – Zapis działań do plików lokalnych oraz opcjonalne wysyłanie logów na email.
- **Etycznych testów exploitów** – Bezpieczne testowanie potencjalnych luk w systemach pocztowych.

Projekt jest rozwijany z myślą o edukacyjnym i etycznym wykorzystaniu, a jego kod jest otwarty na sugestie i modyfikacje ze strony społeczności.

## Wymagania

- **Środowisko**: Python 3.13 lub nowszy.
- **Biblioteki**:
  - `colorama` – Do kolorowego wyjścia w terminalu.
  - `pyreadline3` – Opcjonalnie, dla funkcjonalności readline na Windowsie.
  - `smtplib` i `email` – Wbudowane w Python.
  - `urllib.request` – Wbudowane w Python.
  - Inne moduły mogą być wymagane w zależności od rozszerzeń (np. dla szyfrowania).

### Instalacja Zależności

## Struktura Projektu

- `Seven7.py` – Główny skrypt aplikacji.
- `Server/` – Moduły związane z serwerem i sesjami:
- `ModuleClient.py` – Moduł klienta.
- `ModuleServer.py` – Moduł serwera.
- `ModuleSession.py` – Moduł sesji.
- `session_manager.py` – Zarządzanie sesjami.
- `key/` – Podfolder z modułami kluczy:
 - `ModuleKey.py` – Obsługa kluczy szyfrowania.
 - `GenKeyMaster.py` – Generowanie kluczy master.
- `API/` – Moduły API:
- `ModuleCommand.py` – Wykonywanie komend.
- `ModuleExploit.py` – Testy exploitów.
- `ModuleMaping.py` – Mapowanie sieci.
- `ModulePayload.py` – Generowanie payloadów.
- `ModuleMenu.py` – Interfejs menu.
- `ModuleScan.py` – Skanowanie.
- `ModuleLodderScriptAll.py` – Ładowanie wszystkich modułów.
- `log/` – Folder na pliki logów (automatycznie tworzony).
- `Email/` – Folder na logi email (automatycznie tworzony).
- `README.md` – Ten plik z dokumentacją.
## Licencja

Projekt jest udostępniony na zasadach [licencji MIT](LICENSE) (jeśli nie określono inaczej). Upewnij się, że używasz go zgodnie z obowiązującymi przepisami prawa i zasadami etyki.

---

