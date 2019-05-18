from typing import Typing

class Base:
	def __init__(self, index, name, attack, defense, sp_attack, sp_defense, speed, health, type1, type2 = Typing.Null):
		self.index = index
		self.name = name
		self.attack = attack
		self.defense = defense
		self.sp_attack = sp_attack
		self.sp_defense = sp_defense
		self.speed = speed
		self.health = health
		self.current_health = health
		self.type1 = type1
		self.type2 = type2

	def alive(self):
		return self.health > 0

	def status(self):
		if self.type2 != Typing.Null:
			type2_text = "\nTYPE2: " + self.type2.name
		else:
			type2_text = ""

		print("[{}]\nID: {}\nATK: {}\nDEF: {}\nSP_ATK: {}\nSP_DEF: {}\nSPD: {}\nHP: {}/{}\nTYPE1: {}{}".format(
			self.name,
			self.index,
			self.attack,
			self.defense,
			self.sp_attack,
			self.sp_defense,
			self.speed,
			self.current_health,
			self.health,
			self.type1.name,
			type2_text
		))

	def ataque(self,other):
		other.current_health -= 20

	def change(self):
		print("Em desenvolvimento")

	def item(self):
		print("Em desenvolvimento")

	def run(self):
		print("Em desenvolvimento")