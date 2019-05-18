class Trainer:
	def __init__(self, name, money, pkmn):
		self.name = name
		self.money = money
		self.pkmn = pkmn

	def list_pkmn(self):
		print("{}'s pkmn: ".format(self.name))
		for c in self.pkmn:
			print(c.name)

	def list_money(self):
		print("{} has: ".format(self.name))
		print("PKMN$", self.money)