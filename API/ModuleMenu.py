import os
import time
from colorama import init, Fore, Back, Style
init()

class Menu:
    def __init__(self):
        self.options = {}

    def display(self, options):
        """Wyświetlanie menu z kolorowym banerem ASCII."""
        self.options = options
        # Baner ASCII w kolorach tęczy
        banner = """
            ███████╗███████╗██╗   ██╗███████╗███╗   ██╗███████╗
            ██╔════╝██╔════╝██║   ██║██╔════╝████╗  ██║╚════██║
            ███████╗█████╗  ██║   ██║█████╗  ██╔██╗ ██║    ██╔╝
            ╚════██║██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██╔╝ 
            ███████║███████╗ ╚████╔╝ ███████╗██║ ╚████║   ██║  
            ╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝                
         Created by arsagrdkronos
        """
        colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
        for i, line in enumerate(banner.split('\n')):
            if line.strip():
                color = colors[i % len(colors)]
                print(color + line + Style.RESET_ALL)
        print("\nWybierz opcję:")
        for key, (desc, _) in options.items():
            print(f"{key}: {desc}")

    def get_choice(self):
        """Pobranie wyboru użytkownika."""
        while True:
            choice = input("Wybierz: ")
            if choice in self.options:
                return choice
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    menu = Menu()
    menu.display({"1": ("Test", lambda: print("Test")), "2": ("Wyjście", exit)})
    choice = menu.get_choice()
    menu.options[choice][1]()