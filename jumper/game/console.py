import webbrowser as w

class Console:
    """A code template for a computer console. The responsibility of this
    class of objects is to get text or numerical input and display text output.
    Stereotype:
        Service Provider, Interfacer
    Attributes:
        prompt (string): The prompt to display on each line.
    """

    def read(self, prompt):
        """Gets text input from the user through the screen.
        Args:
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.
        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the user through the screen.
        Args:
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.
        Returns:
            float: The user's input as a float.
        """
        return float(input(prompt))

    def write(self, text):
        """Displays the given text on the screen.
        Args:
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text)

    def google_word(self, word):
        choice = input(f'Did you want to google {word}?\nIt could save a life next time!\n(Y)/(N):')
        if choice.lower() == 'y':
            w.open(f'https://www.google.com/search?q={word}', new=2)