def tackle(a,b,Typing.Normal):
	b.curr_health -= round (40 + (a.attack / 300))

def ember(a,b,Typing.Fire):
    b.curr_health -= round (40 + (a.attack / 300))

def water_gun(a,b,Typing.Water):
    b.curr_health -= round (40 + (a.sp_attack /300))

def vine_whip(a,b,Typing.Grass):
    b.curr_health -= round (45 + (a.sp_attack /300))

def wing_attack(a,b,Typing.Flying):
    b.curr_health -= round (60 + (a.sp_attack //300))

def double_iron_bash(a,b,Typing.Iron):
    b.curr_health -= round (60 + (a.attack //300))