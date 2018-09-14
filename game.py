import word
import words_bank
import random

class Game_controller:
    new_word = ''

    # generate randon word from words_bank
    @classmethod
    def generate_word(cls):
        random_word = random.choice(words_bank.words_list)
        cls.new_word = word.Word(random_word)
        print(cls.new_word.word)
        cls.new_word.split_letters()
        cls.new_word.display_word()
        cls.take_user_guess()

    # Checks the word's status, prompts and takes the user guess and validate
    @classmethod
    def take_user_guess(cls):
        while not cls.new_word.status:
            guess = input('Guess a letter ')
            cls.new_word.take_char(guess)
            cls.new_word.track_status()
            cls.new_word.display_word()
        cls.reset_game()
           

    @classmethod
    def reset_game(cls):
        confirm = input('WOULD YOU LIKE TO PLAY AGAIN? (y/n) ')
        if confirm == 'y':
            cls.generate_word()
        return print('THANKS FOR PLAYING!')





Game_controller.generate_word()
       