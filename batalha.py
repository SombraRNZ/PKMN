def battle(a,b):
	while a.alive() and b.alive():
		a.status()
		b.status()

		choice(a,b)
		if b.alive():
			choice(b,a)

	if a.alive():
		print(a.name,"wins")
	elif b.alive():
		print(b.name,"wins")
	else:
		print("Draw")

def choice(a,b):
	print(a.name,"'s turn")

	while True:
		try:
			print(" 1: Attack\n 2: PKMN\n 3: Item\n 4: Run")
			c = int(input())
			if c < 1 or c > 4:
				raise ValueError
			break
		except ValueError:
			print("Por favor coloque um número entre 1 e 4")

	if c == 1:
		a.attack(b)
	elif c == 2:
		a.change()
	elif c == 3:
		a.item()
	else:
		a.run()