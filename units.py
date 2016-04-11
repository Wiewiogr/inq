from random import randint
from weapon import *

def dice():
	return randint(1,6)


class Unit(object):
	rank = ""
	name = ""
	t = 4
	weapons = []
	bs = 4
	w = 1
	save = 4
	"""
	def __init__(self,_name,  _bs, _save, _w, _weapons):
		name = _name
		bs = bs
		save = save
		w = _w
		weapons = list(weapons)
	"""
	def shoot(self,target,weapon):
		num = 0
		for i in range(self.weapons[weapon].num):
			res = dice()
			print(self.name,"rolled",res,"for hit, succes on",self.bs,"+")
			if res>=self.bs :
				res = dice()
				print(self.name,"rolled",res,"for wound, succes on",target.t,"+")
				if res>= target.t:   ##szajs!!!!
					num += 1
		target.take_damage(num,self.weapons[weapon].ap)		
	
	def take_damage(self, amount, ap):
		if amount == 0 :
			return
		if ap <= self.save :
			self.w -= amount
			print("No saves allowed,",self.name," takes ",amount, "wounds!")
			if self.w <= 0 :
				self.die()
		else:
			for i in range(amount):
				res = dice()
				if res >= self.save:
					print(self.name,"'s save succesful, rolled",res)
				else:
					print(self.name,"'s save unsuccesful, rolled",res,"and is wounded!")
					self.w -= 1
					if self.w <= 0 :
						self.die()	
						return			

	def die(self):
		print(self.name,"died!")


class Acolyte(Unit):
	t = 3
	weapons = [cr_lasgun()]
	bs = 3
	w = 1
	save = 5
	rank = "Acolyte"
	def __init__(self, _name):
		self.name =_name





print("SADFSADF")