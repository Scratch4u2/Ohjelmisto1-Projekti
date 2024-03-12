import gamecredits
import gamesql
from colorama import Fore,init
init(autoreset=True)


def end_game(score,co2_used,used_time):
    print(f"\n{Fore.GREEN}-------------------------{Fore.RESET}")
    print(f"{Fore.GREEN}Game over!\n{Fore.RESET}")
    print(f"{Fore.GREEN}Your final score is: {score}\nCO2 used: {co2_used:.2f} grams.\nFlight time: {used_time / 24:.2f} days.{Fore.RESET}")
    print(f"{Fore.GREEN}-------------------------{Fore.RESET}")

    gamesql.top_players()
    while True:
        player_input = input(f"\n{Fore.GREEN}Would you like to save your score to the database? {Fore.WHITE}({Fore.CYAN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}){Fore.RESET}\n").lower()
        if player_input == "y":
            gamesql.new_score(player_name=input("Enter your name\n"),score = score)
            break
        elif player_input == "n":
            gamecredits.game_credits_query()
            print(f"{Fore.GREEN}\nThanks for playing!{Fore.RESET}")
            break
        else:
            print(f"{Fore.YELLOW}Invalid input{Fore.RESET}")
    exit()
