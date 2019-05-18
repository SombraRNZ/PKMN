from .base import Base
from typing import Typing

class Wolfly(Base):
	def __init__(self):
		super().__init__(
			index=99,
			name="Wolfly",
			type1=Typing.Flying,
			health=100,
			speed=100,
			attack=90,
			sp_attack=150,
			defense=140,
			sp_defense=90
		)