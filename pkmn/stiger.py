from .base import Base
from typing import Typing

class Stiger(Base):
	def __init__(self):
		super().__init__(
			index=100,
			name="Stiger",
			type1=Typing.Steel,
			type2=Typing.Dragon,
			health=100,
			speed=150,
			attack=140,
			sp_attack=100,
			defense=90,
			sp_defense=90
		)