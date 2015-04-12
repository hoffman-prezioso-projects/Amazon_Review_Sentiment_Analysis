class SpellChecker:
	dictionary = {}

	def __init__(self):
		self.dictionary = {}
		word_list = open("../res/en_dictionary.txt")

		for word in word_list:
			self.dictionary[word.strip()] = True

	def check(self, word):
		try:
			self.dictionary[word] # throws KeyError if word is not found

			# word in dictionary
			return True

		except: # word not in dictionary
			return False