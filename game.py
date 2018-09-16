import assets as Data
from termcolor import colored

# This class controls the game by calling methods on the word and letter classes
class Game_controller:
    new_word = ''
    score = 0
    guessed_letters = []


    # Generate random word from words_bank
    @classmethod
    def generate_word(cls):
        import word
        import random
        random_word = random.choice(Data.Assets['words_list'])
        print('YOU GOT A NEW WORD!')
        cls.new_word = word.Word(random_word)
        # print(cls.new_word.word) # for testing only
        cls.new_word.split_letters().generate_attempts().display_word()
        cls.take_user_guess()


    # Validate that the user only enter a letter (A-Z)
    @classmethod
    def validateUserInput(cls, guess):
        if guess not in Data.Assets['valid_letters']:
            print(colored("That's not a valid guess", color='red'))
            return cls.take_user_guess()


    # Checks if all the letters the word have been guess and also the player fail attempts remaining.
    @classmethod
    def check_word_status(cls):
        while not cls.new_word.status:
            if cls.new_word.attempts <= 0:
                print(colored("G A M E O V E R !", color='red'))
                print(f'The word was {cls.new_word.word}')
                return cls.reset_game()
            return cls.take_user_guess()
        cls.score += 1
        print(f'Your score is: {cls.score}')
        cls.guessed_letters = []
        cls.generate_word()


    # Prompts the player for guesses
    @classmethod
    def take_user_guess(cls):
        user_input = input('Guess a letter ')
        guess = user_input.lower()
        cls.validateUserInput(guess)
        if guess in cls.guessed_letters:
            print(f'You have already guessed {guess}. Try again')
            print(f'Letters already guessed: ' + ','.join(cls.guessed_letters))
            return cls.take_user_guess()
        cls.guessed_letters.append(guess)
        cls.new_word.take_char(guess).track_status().display_word()
        cls.check_word_status()


    # Ask the player to continue playing or not
    @classmethod
    def reset_game(cls):
        confirm = input('WOULD YOU LIKE TO PLAY AGAIN? (y/n) ')
        response = confirm.lower()
        if response == 'y':
            cls.guessed_letters = []
            return cls.generate_word()
        return print('THANKS FOR PLAYING!')


# Start a new game
Game_controller.generate_word()
