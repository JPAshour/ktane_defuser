def simple_wires():
	wires = input("Are there 3, 4, 5, or 6 wires?  ")
	if (wires=='3'):
		red = input("Are there red wires? Y/N  ")
		#print(red)
		if (red in ['Y', 'y', 'Yes', 'yes']):
			lastWhite = input("Is the last wire white? Y/N  ")
			if (lastWhite in ['Y', 'y', 'Yes', 'yes']):
				print ("Cut the last wire")
			elif(lastWhite in ['N', 'n', 'No', 'no']):
				multiBlue = input("Is there more than one blue wire? Y/N  ")
				if (multiBlue in ['Y', 'y', 'Yes', 'yes']):
					print('Cut the last blue wire')
				elif (multiBlue in ['N', 'n', 'No', 'no']):
					print('Cut the last wire')
		elif(red in ['N', 'n', 'No', 'no']):
				print ('Cut the second wire')
	elif(wires=='4'):
			red = int(input("How many red wires are there?  "))
			odd = int(input("What is the last didgit in the serial number?  "))
			if(red>1 and odd % 2 != 0):
				print('Cut the last red wire')
			elif(red<=1):
				yellow = input("Is the last wire yellow? Y/N  ")
				if(yellow in ['Y', 'y', 'Yes', 'yes'] and red == 0):
					print("Cut the first wire")
				elif(yellow in ['Y', 'y', 'Yes', 'yes'] and red != 0):
					blue = int(input("How many blue wires are there?  "))
					if(blue == 0):
						print('Cut the first wire')
					elif(blue != 0):
						yellow = int(input("How many yellow wires are there?  "))
						if(yellow>1):
							print('Cut the last wire')
						else:
							print('Cut the second wire')
					else:
						print('Invalid input')
				elif(yellow in ['N', 'n', 'No', 'no']):
					blue = int(input("How many blue wires are there?  "))
					if(blue == 1):
						print('Cut the first wire')
					elif(blue != 1):
						yellow = int(input("How many yellow wires are there?  "))
						if(yellow>1):
							print('Cut the last wire')
						else:
							print('Cut the second wire')
					else:
						print('Invalid input')
				else:
					print('Invalid input')
			else:
				print('Invalid input')
	elif(wires=='5'):
		lastBlack = input("Is the last wire black?  ")
		odd = int(input("What is the last didgit in the serial number?  "))
		if(lastBlack in ['Y', 'y', 'Yes', 'yes'] and odd % 2 != 0):
			print("Cut the 4th wire")
		elif(lastBlack in ['N', 'n', 'No', 'no']):
			black = int(input("How many black wires are there?  "))
			red = int(input('How many red wires are there?  '))
			if(black == 0 and red == 0):
				print('Cut the second wire')
			elif(black != 0 or red != 0):
				print('Cut the first wire')
			else:
				print('Invalid input')
		else:
			print('Invalid input')
	elif(wires=='6'):
		yellow = int(input("How many wires are yellow?  "))
		odd = int(input("What is the last didgit in the serial number?  "))
		white = int(input("How many wires are white?  "))
		red = int(input("How many wires are red?  "))
		if(yellow == 0 and odd % 2 != 0 ):
			print('Cut the third wire')
		elif(yellow == 1 and white >= 2):
			print('Cut the fourth wire')
		elif(red == 0):
			print("Cut the last wire")
		else:
			print("Cut the fourth wire")
	else:
		print('Something went wrong, please try again')
		print(wires, type(wires))
def buttons():
	def holdButton():
		print('Press and hold the button')
		color = input("What color is the light strip? Color or first letter of color:  ")
		if(color in ['y', 'Y', 'yellow', 'Yellow']):
			print('Release when the timer has a 5')
		elif(color in ['b', 'B', 'blue', 'Blue']):
			print('Release when the timer has a 4')
		else:
			print('Release when the timer has a 1')
	battery = int(input("How many batteries are on the bomb?  "))
	if(battery >=2):
		label = input('Does the button say "Detonate"?  Y/N  ')
		if (label in ["Y", "y", 'Yes', 'yes']):
			print('Press and immidately release the button')
		elif(label in ['N', 'n', 'No', 'no']):
			redButton = input("Is the button red with the label 'Hold'? Y/N  ")
			if(redButton in ["Y", "y", 'Yes', 'yes']):
				print('Press and immidately release the button')
			elif(redButton in ['N', 'n', 'No', 'no']):
				if (battery >= 3):
					indicatorFRK = input("Is there a lit indicator labeled 'FRK'?  Y/N  ")
					if(indicatorFRK in ["Y", "y", 'Yes', 'yes']):
						print('Press and immidately release the button')
					elif(indicatorFRK in ['N', 'n', 'No', 'no']):
						holdButton()
				else:
					holdButton()
	elif(battery <2):
		redButton = input("Is the button red with the label 'Hold'? Y/N  ")
		if(redButton in ["Y", "y", 'Yes', 'yes']):
			print('Press and immidately release the button')
		elif(redButton in ['N', 'n', 'No', 'no']):
			if (battery >= 3):
				indicatorFRK = input("Is there a lit indicator labeled 'FRK'?  Y/N  ")
				if(indicatorFRK in ["Y", "y", 'Yes', 'yes']):
					print('Press and immidately release the button')
				elif(indicatorFRK in ['N', 'n', 'No', 'no']):
					holdButton()
			else:
				holdButton()
def keypad():
	def striplist(l):
		return([x.strip() for x in l])
	print("""
		Ѽ  800, controller, omega with titlo
		æ  Ae, ae
		©  Copyright
		Ӭ  E, BW E
		Ҩ  Ha, squiggily, loop
		Ҋ  N, BW N
		ϗ  H, h, Kai
		ϰ  Z, z, Kappa, lightning
		Ԇ  R, Komi Dzje, sphinx
		Ϙ  O, Koppa, racket, head, lollypop, o, O
		Ѯ  3, Ksi, snake, three 
		ƛ  Lambda, dinosaur, wishbone
		Ω  Omega, omega
		¶  Pilcrow, paragraph, sail, flag
		ψ  Psi, trident, pitchfork, candle
		¿  ?, Query, question mark
		Ϭ  6, Shima, six
		Ͼ  C, Sigma, dot C
		Ͽ  BW C, Reversed Sigma, back C, back dot C, c, 
		★  FS, S, Dark Star, filled star
		☆  HS, s, White Star, empty star, hollow star
		҂  !=, #, Thousand, hashtag, doesn't equal
		Ѣ  TB, tb, Yat
		Ѭ  kitty, cat, monkey, spider, Big Yus 
		Ѧ  AT, at, A, a, Little Yus, pyramid, triforce
		Җ  Ks, ks, Zhe, back to back k
	        ټ  smile, smiley, Teh
		""")
	pads = input("What symbols do you have? (Use reference from above)  ")
	pads = pads.strip().split(",")
	pads = striplist(pads)
	print(pads)
	if(pads in ["AT", "at", "A", 'a', 'Little Yus', 'pyramid', 'triforce', 'Z', 'z', 'Kappa', 'lightning']):
		print("First column")
	elif(pads in ['Copyright', '800', 'controller', 'omega with titlo', 'R', 'Komi Dzje', 'sphinx']):
		print("Third column")
	elif(pads in ['C', 'Sigma', 'dot C', '3', 'Ksi', 'snake', 'three', 'FS', 'S', 'Dark Star', 'filled star']):
		print("Fifth column")
	elif(pads in ['!=', '#', 'Thousand', 'hashtag', "doesn't equal", 'Ae', 'ae', 'N', 'BW N', 'Omega', 'omega']):
		print("Sixth column")
	else:
		if(pads in ['Psi', 'trident', 'pitchfork', 'candle']):
			print("Fifth column")
		elif():
			pass
		else:
			pass

	
def defuser():
	def defuse():
		module = input("What module are you trying to defuse? Options are: Wires, Buttons, Keypad ")

		if (module in ["wires", "Wires"]):
			simple_wires()

			while True:
				repeat = input("Do you have more simple wires to defuse? Y/N  ")
				if(repeat in ['Y', 'y', 'Yes', 'yes']):
					simple_wires()
				elif(repeat in ['N', 'n', 'No', 'no']):
					break
		elif(module in ["buttons", "Buttons"]):
			buttons()

			while True:
				repeat = input("Do you have more Buttons to defuse? Y/N  ")
				if(repeat in ['Y', 'y', 'Yes', 'yes']):
					buttons()
				elif(repeat in ['N', 'n', 'No', 'no']):
					break
		elif(module in ["keypad", "Keypad"]):
			keypad()

			while True:
				repeat = input("Do you have more keypads to defuse? Y/N  ")
				if(repeat in ['Y', 'y', 'Yes', 'yes']):
					keypad()
				elif(repeat in ['N', 'n', 'No', 'no']):
					break
		else:
			print ("Invalid selection")
	defuse()
	while True:
		repeat = input("Do you have more modules to defuse? Y/N  ")
		if(repeat in ['Y', 'y', 'Yes', 'yes']):
			defuse()
		elif(repeat in ['N', 'n', 'No', 'no']):
			break

defuser()
