from typing import Typing

class Base:
	def __init__(self, index, name, attack, defense, sp_attack, sp_defense, speed, health, type1, type2 = Typing.Null):
		self.index = index
		self.name = name
		self.attack = attack
		self.buff_attack = 0
		self.defense = defense
		self.buff_defense = 0
		self.sp_attack = sp_attack
		self.buff_sp_attack = 0
		self.sp_defense = sp_defense
		self.buff_sp_defense = 0
		self.speed = speed
		self.buff_speed = 0
		self.health = health
		self.curr_health = health
		self.type1 = type1
		self.type2 = type2


	def alive(self):
		return self.health > 0

	def status(self):
		if self.type2 != Typing.Null:
			type2_text = "\nTYPE2: " + self.type2.name
		else:
			type2_text = ""

		print("[{}]\nID: {}\nATK: : {}/{}\nDEF: {}/{}\nSP_ATK: {}/{}\nSP_DEF: {}/{}\nSPD: {}/{}\nHP: {}/{}\nTYPE1: {}{}".format(
			self.name,
			self.index,
			self.attack,
			self.buff_attack,
			self.defense,
			self.buff_defense,
			self.sp_attack,
			self.buff_sp_attack,
			self.sp_defense,
			self.buff_sp_defense,
			self.speed,
			self.buff_speed,
			self.curr_health,
			self.health,
			self.type1.name,
			type2_text
		))

	def do_move(self,other,move):
		move(self,other)

	def change(self):
		print("Em desenvolvimento")

	def item(self):
		print("Em desenvolvimento")

	def run(self):
		print("Em desenvolvimento")