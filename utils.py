def get_valid_guess():
    """Ensures the user enters a single valid letter."""
    while True:
        user_input = input("Guess a letter: ").strip().lower()
        if len(user_input) != 1 or not user_input.isalpha():
            print("❌ Invalid input! Please enter a single letter.")
        else:
            return user_input

