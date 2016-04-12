from random import randint
from weapon import * 
from units import *
from squad import *
from options import *

me = cr_acolyte("Andrzej")
enemy = cr_acolyte("Jurek")
henchmans = Squad()
henchmans.units = [cr_acolyte("Andrzej"),cr_acolyte("Seba"),cr_acolyte("Janusz")]
henchmans.show_members()

me.shoot(enemy,0)
me.show_info()


#while True:

	






