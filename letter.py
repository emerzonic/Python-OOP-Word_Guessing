

class Letter:
	"""docstring for Letter"""
	def __init__(self, letter):
		# super(Letter, self).__init__()
		self.letter = letter
		self.placeholder = '_'
		self.status = False
		

	# This method checks every letter in the word and returns a letter or underscore placeholder
	def check_guess(self):
		if self.status:
			return self.letter
		return self.placeholder


	# This method takes a letter as guess and checks it against each letter of the word
	def take_guess(self, guess):
		if self.letter == guess:
			self.status = True
