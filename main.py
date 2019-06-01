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

def tackle(a,b):
	b.curr_health -= round (40 + (a.attack / 225))
grey.pkmn[3].do_move(grey.pkmn[4]), tackle)
grey.pkmn[3].status()
grey.pkmn[4].status()