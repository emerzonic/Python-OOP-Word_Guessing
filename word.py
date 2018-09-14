import letter

class Word:
	"""docstring for Word"""
	def __init__(self, word):
		# super(Word, self).__init__()
		self.word = word
		self.splitted_letters = []
		self.status = False
		self.feed_back = 0

	# This method takes a word and splits the letters into objects 
	def split_letters(self):
		for l in self.word:
			letter_obj = letter.Letter(l)
			self.splitted_letters.append(letter_obj)
		


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
			print('INCORRECT!')
		print(f'You have {int(len(self.word) - tracker)} more remaining')
		


	# This method takes each letter object and calls the Letter check_guess method and returns a word and status of user guesses left.
	def display_word(self):
		display_word = ''
		for obj in self.splitted_letters:
			display_word += " " + obj.check_guess()
		print(display_word)
		if '_' not in display_word:
			self.status = True
			print('You guessed it right!')
		

	# This method takes the user's guess(letter) and calls the Letter take_guess method on it.
	def take_char(self, guess):
		for l in self.splitted_letters:
			l.take_guess(guess)
		