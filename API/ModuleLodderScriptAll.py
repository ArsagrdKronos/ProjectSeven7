import os
import importlib
import importlib.util
import sys

# Dodanie folderu API do ścieżki wyszukiwania modułów
api_path = os.path.dirname(__file__)  # Ustawienie ścieżki na bieżący folder (API)
sys.path.append(api_path)

# Słownik do przechowywania załadowanych modułów
loaded_modules = {}

def load_all_modules():
    """Ładowanie wszystkich modułów z folderu API."""
    for filename in os.listdir(api_path):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]  # Usunięcie '.py' z nazwy pliku
            try:
                module = importlib.import_module(module_name)
                loaded_modules[module_name] = module
                print(f"Załadowano moduł: {module_name}")
            except Exception as e:
                print(f"Błąd ładowania modułu {module_name}: {e}")

def get_module(module_name):
    """Pobranie załadowanego modułu."""
    return loaded_modules.get(module_name)

if __name__ == "__main__":
    load_all_modules()
    # Przykład użycia załadowanych modułów
    if 'ModuleCommand' in loaded_modules:
        cmd = loaded_modules['ModuleCommand'].Command()
        print(cmd.execute('{"action": "test"}'))
    
    if 'ModuleScan' in loaded_modules:
        scan = loaded_modules['ModuleScan'].Scanner()
        print(scan.scan("localhost", 80))