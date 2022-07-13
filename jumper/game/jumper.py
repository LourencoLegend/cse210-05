class Jumper():
    """Class that holds information regarding the jumper.
    Stereotype:
        Information Holder
    Attributes:
        self.num_guesses (int): counts the number of times the user has guessed a letter.
        self.is_alive (boolean): determines if the jumpe is still alive or not, based on how much chute is left.
        self.chute (): holds the string to display the jumpers parachute.
    """

    def __init__(self):
        """
        """
        self.num_guesses = 0
        self.is_alive = True
        self.head = 'O'
        self.chute = ['    ___\n',
                      '  /     \ \n',
                      ' /_______\ \n',
                      ' \       / \n',
                      '  \     /  \n',
                      '   \   /\n',
                      f'     {self.head}    \n',
                      '    /|\   \n',
                      '    / \   ']
        self.displayed_chute = ''.join(self.chute)

    def update_chute(self, result):
        """
        Updates the parachute each turn.
        Updates the jumper head based self.is_alive boolean.
        Args:
            result (boolean): tells the update_chute whether or not the chute needs to be reduced. 
                              If False, the chute is reduced by one line.
                              If True, the chute is not changed
        
        Returns:
            chute (list): each line of the chute
        """
        
        
        

        # If result is True, the chute doesn't change. If result is Fale, the chute is reduced by one line.
        if result == False:
            self.chute.pop(0)
            self.num_guesses += 1

        # If the number of guesses excedes 6, the jumper dies
        if self.num_guesses > 6:
            self.is_alive = False

        # If is_alive is True, self.head = 'O', otherwise, self.head = 'X'
        if self.is_alive == False:
            self.head = 'x'
            self.chute.insert(0,f'     {self.head}    \n')

        # This is being used right now just to test the chute display
        # for line in self.chute:
        #     print(line)
        self.displayed_chute = ''.join(self.chute)

        return self.chute



# # Test
# jumper = Jumper()
# jumper.update_chute(True)

# for line in jumper.chute:
#     print(line)