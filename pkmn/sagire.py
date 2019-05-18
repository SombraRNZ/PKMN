from .base import Base
from typing import Typing

class Sagire(Base):
	def __init__(self):
		super().__init__(
			index=6,
			name="Sagire",
			type1=Typing.Fire,
			type2=Typing.Steel,
			health=58,
			speed=64,
			attack=58,
			sp_attack=80,
			defense=65,
			sp_defense=80
		)