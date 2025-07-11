import re, random
from colorama import Fore, init

init(autoreset=True)

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
        print(Fore.CYAN + "TravelBot: do you like it? (yes/No)")
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
        print(Fore.RED + "TravelBot: sorry, I dpont have that type of destination.")
    show_help()

def packing_tips():
    print(Fore.GREEN + "TravelBot: Packing tips for{days} days in {location}:")
    print(Fore.GREEN + "-Pack versatile clothes.")
    print(Fore.GREEN + "-Bring chargers/adapters.")
    print(Fore.GREEN + "-Check the weather forcast.")

def tell_joke():
    print(Fore.YELLOW + f"TraveBot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "-Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "-offer packing tips (say 'packing')")
    print(Fore.GREEN + "-Tell a joke  (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n" )

def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input("Fore.YELLOW + your name?")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}:")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "funny" in user_input:
            recommend()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")

if __name__ == " __ main__":
        chat()                                          
    


