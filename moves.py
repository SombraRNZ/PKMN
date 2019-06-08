def tackle(a,b):
	b.curr_health -= round (40 + (a.attack / 225))

def ember(a,b):
    b.curr_health -= round (40 + (a.attack / 225))

def water_gun(a,b):
    b.curr_health -= round (40 + (a.sp_attack /225))

def vine_whip(a,b):
    b.curr_health -= round (45 + (a.sp_attack /225))

def wing_attack(a,b):
    b.curr_health -= round (60 + (a.sp_attack //225))