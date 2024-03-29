#-------------------------------------------------------------------------------
# ONNIN SPAGETTI KOODIA + RANEN UPEAT SOOSIT

import time
from colorama import Fore, Back, Style
#from asciiartfunc import welcome_text_to_ascii # Tuodaan asciiartfunc.py tiedostosta welcome_text_to_ascii() funktio tähän tiedostoon.

#{Fore.VÄRI} = Tekstin väri
#{Back.VÄRI} = Taustan väri
#{Style.--} = Tekstin tyyli

def starting_screen():
    """
    Funktio näyttää tervetuloa-tekstin ASCIna ja kysyy käyttäjältä, haluaako hän aloittaa pelin.
    Jos vastaus on "yes", peli alkaa.
    Jos vastaus on "no", peli loppuu.
    Jos syötä mitä tahansa muuta, while-looppia jatketaan, kunnes käyttäjä antaa jommankumman syötteen.
    """
    while True:
        intro_input = input(f"{Fore.GREEN}Do you wish to Start the game? {Fore.WHITE}({Fore.CYAN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}) \n").lower()
        
        if intro_input == "yes" or intro_input == "y":
            print(f"{Fore.GREEN}\n\nGreat! Let's get started!\n{Fore.RESET}{Style.RESET_ALL}")
            return True
        elif intro_input == "no" or intro_input == "n":
            print(f"{Fore.RED}\nGoodbye!{Fore.RESET}{Style.RESET_ALL}")
            return False
        else:
            print(f"\n{Fore.YELLOW}Invalid input, please try again:{Fore.RESET}{Style.RESET_ALL}")



def airplane_model_choice(): 
    """"
    Funktio lentokonemallin valintaan. 
    Kysyy käyttäjältä haluamansa lentokonemallin ja tulostaa valinnan. 
    Jos käyttäjä antaa väärän syötteen, loopilla pyydetään syöttämään uudelleen.
    """
    while True: 
        airplane_model_input = input(f"{Fore.GREEN}Choose your airplane model or type in {Fore.WHITE}info{Style.RESET_ALL}\n {Fore.CYAN}1{Fore.WHITE}. {Fore.CYAN}Boeing 737 \n {Fore.MAGENTA}2{Fore.WHITE}. {Fore.MAGENTA}Airbus A320 \n {Fore.RED}3{Fore.WHITE}. {Fore.RED}Saab JA 37 Viggen{Fore.RESET}{Style.RESET_ALL} \n")
        
        if airplane_model_input == "info":
            print(f"\n{Fore.GREEN}---------------------------------------------------------------------------------------------------------------------")
            print(f"{Fore.CYAN}The Boeing 737 {Fore.GREEN}is a narrow-body aircraft produced by Boeing Commercial Airplanes at its Renton Factory in Washington.")
            print(f"{Fore.MAGENTA}The Airbus A320 {Fore.GREEN}family are narrow-body airliners designed and produced by Airbus.")
            print(f"{Fore.RED}The Saab 37 Viggen {Fore.GREEN}is a retired Swedish single-seat, single-engine, short-medium range combat aircraft.")
            print(f"{Fore.GREEN}---------------------------------------------------------------------------------------------------------------------")
            print(Style.RESET_ALL + Fore.RESET + Back.RESET)   
        
        elif airplane_model_input == "1":
            print(f"{Fore.GREEN}\nYou have chosen the {Fore.CYAN}Boeing 737")
            print(Style.RESET_ALL + Fore.RESET + Back.RESET)
            return 1

        elif airplane_model_input == "2":
            print(f"{Fore.GREEN}\nYou have chosen the {Fore.MAGENTA}Airbus A320")
            print(Style.RESET_ALL + Fore.RESET + Back.RESET)
            return 2

        elif airplane_model_input == "3":
            print(f"{Fore.GREEN}\nYou have chosen the {Fore.RED}Saab JA 37 Viggen")
            print(Style.RESET_ALL + Fore.RESET + Back.RESET)
            return 3
        
        elif airplane_model_input == "Matti" or "matti":
            print(f"{Fore.GREEN}\nWow! You found {Fore.YELLOW}Matti!")
            print(Style.RESET_ALL + Fore.RESET + Back.RESET)
            return "Matti"
        
        elif airplane_model_input == "Peyman" or "peyman":
            print(f"{Fore.GREEN}\nWow! You found {Fore.YELLOW}Peyman!")
            print(Style.RESET_ALL + Fore.RESET + Back.RESET)
            return "Peyman"

        else:
            print(f"\n{Fore.YELLOW}Invalid input, please try again:{Fore.RESET}")
            print(Style.RESET_ALL + Fore.RESET + Back.RESET)


def intro(): 
    """
    Funktio joka kutsuu molemmat "intro ja airplane_model_choice" funktiot <--- siirretään myöhemmin main() funktioon.
    Tässä kohtaa testataan, että jos alussa sanotaan "no" niin peli loppuu, muussa tapauksessa kutsutaan airplane_model_choice() funktiota.
    Jos intro() palauttaa True, kutsutaan airplane_model_choice() funktiota.
    """
    pass
