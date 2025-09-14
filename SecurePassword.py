import random
from string import digits #This is for the numbers in the password.
from string import punctuation #This is for the symbols in the password.
from string import ascii_letters #This is for the letters of the alphabet in the password.


symbols = ascii_letters + digits + punctuation #This is for the password to have a combination of numbers, letters, and symbols in the password.
secure_random = random.SystemRandom() #This line allows for a random selection of characters and numbers for the password.
password = "".join(secure_random.choice(symbols)for i in range(20)) #This prints the password in the range of 20 characters.


print(password) #This is the print statement line command to print the password.

