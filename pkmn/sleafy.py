from .base import Base
from typing import Typing

class Sleafy(Base):
	def __init__(self):
		super().__init__(
			index=1,
			name="Sleafy",
			type1=Typing.Grass,
			health=45,
			speed=49,
			attack=49,
			sp_attack=65,
			defense=65,
			sp_defense=45
		)