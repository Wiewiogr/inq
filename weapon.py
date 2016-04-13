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

class CCWeapon(object):
	def __init__(self, name, s,i, ap, num,desc):
		self.name = name
		self.ap = ap
		self.s = s
		self.i = i
		self.num = num
		self.desc = desc
	def show_info(self):
		print("	"+self.name)
		print("	AP :",self.ap)
		print(""+self.desc)



def cr_base_ccw():
	return CCWeapon("CCW",lambda x : x,lambda x : x,7,0,"Base ccw weapon")


def cr_bolter():
	return Weapon("Bolter",4,5,2)

def cr_lasgun():
	return Weapon("Lasgun",3,6,2)
		
