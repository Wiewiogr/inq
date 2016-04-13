from units import *
from weapon import *

class Squad(object):
	units = {}
	def show_members(self):
		for i in self.units:
			print(i,"-",self.units[i].rank)

