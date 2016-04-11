from units import *
from weapon import *

class Squad(object):
	units = []
	def show_members(self):
		for i in range(len(self.units)):
			print(i,self.units[i].rank,"-",self.units[i].name)
