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

## Jak Uruchomić

1. Pobierz projekt do wybranego katalogu (np. `C:\Users\ARPdevil\Desktop\Seven7`).
2. Zainstaluj zależności, jak opisano powyżej.
3. Uruchom główny skrypt:


4. Postępuj zgodnie z instrukcjami wyświetlanymi w menu (np. wybierz opcję 5, aby uruchomić sesję, lub 9 dla pomocy).

## Twórca: ArsagrdKronos

ArsagrdKronos to pseudonim twórcy projektu Seven7, pasjonata technologii i cyberbezpieczeństwa. Inspiracją dla ArsagrdKronosa jest głęboka fascynacja programowaniem oraz etycznym hackowaniem, co znajduje odzwierciedlenie w funkcjonalnościach Seven7. Twórca, pochodzący z kręgu entuzjastów open-source, dąży do tworzenia narzędzi edukacyjnych, które wspierają naukę bezpieczeństwa IT w sposób odpowiedzialny. ArsagrdKronos aktywnie eksperymentuje z nowymi technologiami, co czyni Seven7 projektem dynamicznie rozwijanym. Jego motto brzmi: "Bezpieczeństwo przez wiedzę, etyka ponad wszystko."

## Licencja

Projekt jest udostępniony na zasadach [licencji MIT](LICENSE) (jeśli nie określono inaczej). Upewnij się, że używasz go zgodnie z obowiązującymi przepisami prawa i zasadami etyki.

## Kontakt

Jeśli masz pytania, sugestie lub chcesz zgłosić błąd, skontaktuj się z ArsagrdKronosem:
- Email: [wstaw email, jeśli dostępny] (opcjonalne).
- Platforma: [wstaw link, jeśli projekt jest hostowany, np. GitHub].

## Wkład

Zapraszamy do współpracy! Jeśli chcesz dodać nowe funkcje, poprawić kod lub zgłosić problem, otwórz issue lub wyślij pull request na platformie hostingowej projektu.

## Historia Zmian

- **09.09.2025, 23:46 CEST**: Utworzono i opublikowano pierwszą wersję `README.md`. Dodano opis projektu, wymagania, strukturę i informacje o twórcy.

---
