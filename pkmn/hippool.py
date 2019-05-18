from .base import Base
from typing import Typing

class Hippool(Base):
	def __init__(self):
		super().__init__(
			index=8,
			name="Hippool",
			type1=Typing.Water,
			type2=Typing.Ground,
			health=79,
			speed=83,
			attack=100,
			sp_attack=85,
			defense=105,
			sp_defense=78
		)