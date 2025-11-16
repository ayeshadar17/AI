import requests

def get_random_joke():
    """Fetch a random joke from the Official Joke API."""
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # handles bad HTTP codes
        joke_data = response.json()

        print(f"Full JSON Response: {joke_data}")  # debug print
        
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    
    except requests.exceptions.RequestException as e:
        return f"Failed to retrieve joke. Error: {e}"

def main():
    print("Welcome to the Random Joke Generator!")

    while True:
        user_input = input("Press Enter to get a new joke, or type 'q'/'exit' to quit: ").strip().lower()

        if user_input in ("q", "exit"):
            print("Goodbye!")
            break
        
        print(get_random_joke())

if __name__ == "__main__":
    main()

