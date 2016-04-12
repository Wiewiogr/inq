from random import randint


class Weapon(object):
	def __init__(self, name, s, ap, num):
		self.name = name
		self.ap = ap
		self.s = s
		self.num = num
	def show_info(self):
		print("	"+self.name)
		print("	S :",self.s)
		print("	AP :",self.ap)
		print("	Shoots :",self.num)


def cr_bolter():
	return Weapon("Bolter",4,5,2)

def cr_lasgun():
	return Weapon("Lasgun",3,6,2)
		
