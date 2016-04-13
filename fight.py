from units import *
from squad import *
import queue

class Fight(object):
	unit_queue = queue.Queue()
	def __init__(self,_ally,_enemy):
		self.allies = _ally
		self.enemy = _enemy
		tmp = {}
		tmp.update(_ally.units)
		tmp.update(_enemy.units)
		t = len(tmp)
		for x in range(t):
			#for y in tmp:
			val = max(tmp.keys(), key=lambda k: tmp[k].i)
			self.unit_queue.put(val)
			del tmp[val]

	def beg(self):
		print("You aproach enemy squad consisting of:")
		self.enemy.show_members()

	def next(self):
		tmp = self.unit_queue.get()
		self.unit_queue.put(tmp)
		return tmp

	def is_end(self):
		if self.enemy.empty():
			return True
		else:
			return False