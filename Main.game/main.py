import gameintro
import quizv2
import gamesql
import gamecredits

from colorama import Fore,init
#import quiz <<- pitää kutsua tyyppisesti from quiz import quiz_asker tms. -onni

# testataan main funktion toimintaa

score = 0
distance = 0
used_time = 0
co2_used = 0
current_airport = gamesql.random_fly()
game_going = True

if gameintro.starting_screen(): # aloitetaanko peli vai ei

    airplane_model = gameintro.airplane_model_choice() # kysyy ja tallentaa lentokoneen

    while game_going:

        # pelaajan komento functiot

        print(f"{Fore.GREEN}Your current location is: {current_airport[0]}{Fore.RESET}")
        gamesql.travel_co2(current_airport, airplane_model)
        print(f"{Fore.GREEN}CO2 used: {co2_used}g, Distance traveled: {distance}km, Time used: {used_time}h{Fore.RESET}")
    if gameintro.starting_screen():
        if quizv2.question_query_from_database():
            score += 1     # lisää pisteen oikein vastatusta kysymyksestä
            travel_info = gamesql.travel_co2(current_airport, airplane_model) # lentoon liittyvät tiedot
            distance += travel_info[0]
            co2_used += travel_info[1]
            used_time += travel_info[2]
            current_airport = travel_info[3]

            continue_game = input(f"{Fore.GREEN}Do you want to continue? (y/n):\n{Fore.RESET}").lower()
            if continue_game == "y":
                game_going = True
            elif continue_game == "n":
                game_going = False
            else:
                print(f"{Fore.YELLOW}Invalid input entered")

        else:
            print(f"{Fore.GREEN}Your final score is: {score}{Fore.RESET}")
            print(f"Your final co2 and how long your flighttime is: \n {co2_used:.2f}gramms and {used_time % 24:.2f}days")
            gamecredits.print_game_credits()
            gamesql.top_players()
            game_going = False # lopettaa pelin puuttuu pelin loppuun kuuluvat funktiot

#