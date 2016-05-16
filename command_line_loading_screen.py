#!/usr/bin/python

# example of a command line loading screen for learning purposes

from string import printable
from random import randrange
from time import sleep
from sys import stdout

# the loading screen can be run with the following:
# loading_screen({repetitions},{max character repetitions}).start({your text})
	
# keeping the max character repetitions low is more predictable and efficient
# e.g run screen with repetitions = 3 , maximum character repetitions = 15 and loading text = 'Loading...'

#loading_screen(3,15).start('Loading...')


class loading_screen(object):

	def __init__ (self,repetitions,max_char_repetitions):

		# create a dictionary with all printable characters
		self.char_dictionary = { index:item for index, item in enumerate(printable) }
		
		self.max_char_repetitions = max_char_repetitions
		self.repetitions = repetitions

		# check if values given are both integer
		if not isinstance(repetitions, int) or not isinstance(max_char_repetitions, int):
			print 'repetitions and max character repetitions must be integer'
			exit()

    
	def start(self,loading_text):

		# loop for the number of repetitions specified
		for x in range(0,self.repetitions):

			# create an array of each letter in the loading text, this is used to keep track of where we are in the string
			loading_text_array = [ char for char in loading_text ]	
	
			# fill stdout with blank spaces equal to the length of the loading text 
			# (clears previous text for mulitple repetitions)
			print '\r' + ' ' * len(loading_text),

			#reset our loop variables
			string=''
			char_repetitions=0
			
			while string != loading_text:
			    char_repetitions+=1

			    # pick a pseudo random character from the dictionary we generated earlier
			    # note that the last 4 characters in the dictionary are excluded (new lines \n and carriage returns \r)

			    randomchar=self.char_dictionary[randrange(len(self.char_dictionary)-4)]

			    # check to see if we reached our maximum character repetition limit 
			    # if we haven't check if the current random character matches the next letter needed in array
			    if char_repetitions == self.max_char_repetitions or randomchar == loading_text_array[0]:

				# add the next letter needed to the string
				string = string+loading_text_array[0]

				# remove that letter from the array
				loading_text_array.remove(loading_text_array[0])

				# reset our reps and print current string
				char_repetitions=0
				print '\r'+ string,
			    else:
			    	print '\r'+ string+randomchar,
			    stdout.flush()
			    sleep(0.01)
			sleep(0.25)
		#clear line before exit
		print '\r' + ' ' * len(loading_text),

#ignore this 
example_ascii_art = '''\n   __                 _                                  _      \n  / /  ___   __ _  __| |   _____  ____ _ _ __ ___  _ __ | | ___ \n / /  / _ \ / _` |/ _` |  / _ \ \/ / _` | '_ ` _ \| '_ \| |/ _ \\\n/ /__| (_) | (_| | (_| | |  __/>  < (_| | | | | | | |_) | |  __/\n\____/\___/ \__,_|\__,_|  \___/_/\_\__,_|_| |_| |_| .__/|_|\___|\n                                                  |_|    \n\n'''

# example
# the loading screen could be called with 1 repetition in between the script actually doing something

if __name__ == '__main__':
	
	print example_ascii_art

	try:	
		#loops 5 times, updating the loading screen inbetween doing something (sleeping)
		for x in range(1,6):
			loading_screen(1,15).start('Loading {}...'.format(x))
			y = x * 2 / 2
			sleep(y)
		print '\rFinished.',

	except KeyboardInterrupt:
		pass	
