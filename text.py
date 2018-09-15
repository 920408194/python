from random import randint

ran = randint(1,100)
guess = -1

while guess != ran:
	guess = input("now you can rnter the num you guess!\n")
	guess = int(guess)
	if guess > ran:
		print("It's too big")
	if guess < ran:
		print("It's too small")

if guess == ran:
	print("success!")
