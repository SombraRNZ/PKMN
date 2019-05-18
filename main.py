import pkmn
from trainer import Trainer
print()

grey =Trainer("Grey",7,[
	pkmn.Sleafy(),
	pkmn.Sagire(),
	pkmn.Hippool(),
	pkmn.Stiger(),
	pkmn.Wolfly()
]) 

print()
grey.pkmn[0].status()
print()
grey.pkmn[1].status()
print()
grey.list_pkmn()
print()
grey.list_money()
grey.pkmn[0].ataque(grey.pkmn[1])
grey.pkmn[1].status()