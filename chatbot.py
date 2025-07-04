import re, random
from colorama import Fore, init

init(autoreser=True)

destination = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swis Alps", "Rocky Mountains", "Himalayas"],
    "cities":["Tokyo", "Paris", "Newyork"]
}
jokes = [
    "why don't programmers like nature? Too many bugs!",
    "why did the computer go to the doctor? Because of all their hot spots",
    "why do travelers always feel warm? Beacuse of all their hotspots"
]
def normalize_input(text):
    return re.sub(r"\s+" " ", text.strip().lower())

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destination:
        suggestion = random.choice(destination[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: do you like it? (yes\No)")
        answer = input(Fore.YELLOW + "you: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Lets try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: i,ll suggest again.")
            recommend()

    else:
        print(Fore.RED + "TravelBot: sorry, I dpont have that type of destination")
    show_help()
          
    


