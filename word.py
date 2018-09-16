import letter


class Word:
    """docstring for Word"""

    def __init__(self, word):
        # super(Word, self).__init__()
        self.word = word
        self.splitted_letters = []
        self.status = False
        self.feed_back = 0
        self.attempts = 0

    # This method takes a word and splits the letters into objects
    def split_letters(self):
        for l in self.word:
            letter_obj = letter.Letter(l)
            self.splitted_letters.append(letter_obj)
        return self

    # This method generates the number of attempts base on the length of the random word
    def generate_attempts(self):
        self.attempts = len(self.word)
        print(f'You have {self.attempts} fail attempts to make on this word.')
        return self

    # This method takes each letter object and calls the Letter check_guess method and returns a word and status of user guesses left.
    def display_word(self):
        display_word = ''
        for obj in self.splitted_letters:
            display_word += " " + obj.check_guess()
        print(display_word)
        if '_' not in display_word:
            self.status = True
            print('You guessed it right!')
        return self

    # This method takes the user's guess(letter) and calls the Letter take_guess method on it.
    def take_char(self, guess):
        for l in self.splitted_letters:
            l.take_guess(guess)
        return self

    # This method tracks the status of the guesses remaining and updates if guess is wrong or correct
    def track_status(self):
        tracker = 0
        for obj in self.splitted_letters:
            if obj.check_guess() != '_':
                tracker += 1
        if self.feed_back != tracker:
            print('CORRECT!')
            self.feed_back = tracker
        else:
            self.attempts -= 1
            print('INCORRECT!')
            attempts = 'attempts' if self.attempts >= 2 else 'attempt'
            print(f'You have {self.attempts} {attempts} remaining.')
        remaining_num = int(len(self.word) - tracker)
        letters = 'letters' if remaining_num >= 2 else 'letter'
        print(f'...{remaining_num} more {letters} remaining to guess it right')
        return self
