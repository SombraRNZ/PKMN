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

grey.pkmn[3].do_move(grey.pkmn[4], tackle)
grey.pkmn[3].status()
grey.pkmn[4].status()