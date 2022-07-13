from game.console import Console
from game.jumper import Jumper
from game.word_processor import Word_Processor
class Director:
    """
    A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        
    General Workflow:
    """
    def __init__(self):
        self.letter = ''
        self.keep_playing = True
        self.play_again = True
        self.jumper = Jumper()
        self.word_processor = Word_Processor()
        self.console = Console()

    def start_game(self):
        """
        Starts the game loop
        """
        self.word_processor.get_word()
        self.word_processor.set_hidden_word(self.word_processor.word_choice)
        while self.keep_playing:
            self.get_user_get_and_display()
            self.do_updates()


    def get_user_get_and_display(self):
        """
        Asks the user input
        """
        
        self.console.write('')
        self.console.write(self.word_processor.hidden_word)
        self.console.write('')
        
        self.console.write(self.jumper.displayed_chute)
        self.console.write('---------------')
        

        self.letter = self.console.read("Guess a letter [A-Z]: ")
        self.console.write('')
        

    def do_updates(self):
        """
        This will adjust data based off of user's choices
        """
        self.jumper.update_chute(self.word_processor.check_input(self.letter))
        if self.word_processor.check_complete():
            self.console.write(self.word_processor.hidden_word)
            self.console.write("You win!\nThanks for playing!")
            self.keep_playing == False
            exit()
        elif self.jumper.is_alive is False:
            self.console.write(f'Sorry the word was: {self.word_processor.word_choice}')
            self.console.google_word(self.word_processor.word_choice)
            self.console.write('Oh. He ded...')
            self.console.write(self.jumper.displayed_chute)
            self.keep_playing == False
            exit()
        