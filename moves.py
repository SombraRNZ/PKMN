from typing import Typing

class Move:
    def__init__(self, name, typing, function):
        self.name = name
        self.typing = typing
        self.function = function

    def execute(self, a, b):
        mult = 1.0

        if self.typing in (a.typing1, a.typing2)
            mult += 0.5

        self.function(a, b mult)

    def __str__(self):
        return self.name

def tackle(a,b):
	b.curr_health -= round (40 + (a.attack / 300)) * mult

def ember(a,b):
    b.curr_health -= round (40 + (a.attack / 300)) * mult

def water_gun(a,b):
    b.curr_health -= round (40 + (a.sp_attack /300)) * mult

def vine_whip(a,b):
    b.curr_health -= round (45 + (a.sp_attack /300)) * mult

def wing_attack(a,b):
    b.curr_health -= round (60 + (a.sp_attack //300)) * mult

def double_iron_bash(a,b):
    b.curr_health -= round (60 + (a.attack //300)) * mult

move_list ={
    Move("Tackle",Typing.Normal,tackle),
    Move("Ember", Typing.Fire,ember),
    Move("Water Gun", Typing.Water, water_gun),
    Move("Vine Whip", Typing.Grass, vine_whip),
    Move("Wing Attack", Typing.Flying, wing_attack),
    Move("Double Iron Bash", Typing.Steel, double_iron_bash)
}