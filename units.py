from random import randint
from weapon import *
from charts import *

def dice():
	return randint(1,6)


class Unit(object):
	"""
	rank = ""
	name = ""
	t = 4
	weapons = []
	bs = 4
	w = 1
	save = 4
	ws = 4
	i = 4
	a = 1
	inv_save = 7
	"""

	def __init__(self,_name, _rank,  _bs,_ws,_s, _t,_w,_i,_a,_save,_inv_save, _weapons, _cc_weapons):
		self.bs = _bs
		self.ws = _ws
		self.s = _s
		self.t = _t
		self.w = _w
		self.i = _i
		self.a = _a
		self.save  = _save
		self.inv_save = _inv_save
		self.weapons = list(_weapons)
		self.cc_weapons = list(_cc_weapons)
		self.name = _name
		self.rank = _rank
		self.cur_w = _w ##current wounds

	def shoot(self,target,weapon):
		num = 0
		for i in range(self.weapons[weapon].num):
			res = dice()
			print(self.name,"rolled",res,"for hit, succes on",to_hit_ranged[self.bs-1],"+")
			if res>=to_hit_ranged[self.bs-1] :
				res = dice()
				print(self.name,"rolled",res,"for wound, succes on",to_wound[self.weapons[weapon].s][target.t],"+")
				if res>= to_wound[self.weapons[weapon].s][target.t]:   ##szajs!!!!
					num += 1
		target.take_damage(num,self.weapons[weapon].ap)		
	
	def attack(self,target,weapon):
		num = 0
		for i in range(self.cc_weapons[weapon].num + self.a):
			res = dice()
			print(self.name,"rolled",res,"for hit in cc with",target.name,", succes on",to_hit_cc[self.ws-1][target.ws-1],"+")
			if res>=to_hit_cc[self.ws-1][target.ws-1] :
				res = dice()
				print(self.name,"rolled",res,"for wound, succes on",to_wound[self.cc_weapons[weapon].s(self.s)][target.t],"+")
				if res>= to_wound[self.cc_weapons[weapon].s(self.s)][target.t]:
					num += 1
		target.take_damage(num,self.cc_weapons[weapon].ap)		
	
	def take_damage(self, amount, ap):
		if amount == 0 :
			return
		if ap <= self.save :
			self.cur_w -= amount
			print("No saves allowed,",self.name," takes ",amount, "wounds!")
			if self.cur_w <= 0 :
				self.die()
		else:
			for i in range(amount):
				res = dice()
				if res >= self.save:
					print(self.name,"'s save succesful, rolled",res,"save",self.save,"+")
				else:
					print(self.name,"'s save unsuccesful, rolled",res,"and is wounded!","Save",self.save,"+")
					self.cur_w -= 1
					if self.cur_w <= 0 :
						self.die()	
						return			

	def die(self):
		print(self.name,"died!")

	def show_info(self):
		print("-------------------------------")
		print(self.name)
		print("Rank :",self.rank)
		print("BS :",self.bs)
		print("WS :",self.ws)
		print("S :",self.s)
		print("T :",self.t)
		print("Max W :",self.w)
		print("Current W :",self.cur_w)
		print("I :",self.i)
		print("A :",self.a)
		print("Save :",self.save)
		print("Inv Save:",self.inv_save)
		print("Weapons : ")
		for x in range(len(self.weapons)):
			print("	"+str(x), ": ")
			self.weapons[x].show_info()
		print("CC Weapons : ")
		for x in range(len(self.cc_weapons)):
			print("	"+str(x), ": ")
			self.cc_weapons[x].show_info()
		print("-------------------------------") 

		
def cr_acolyte(name):
	return Unit(name,"Acolyte",3,3,3,3,1,3,1,5,7,[cr_lasgun()],[cr_base_ccw()])

"""
class Acolyte(Unit):
	t = 3
	weapons = [cr_lasgun()]
	bs = 3
	w = 1
	save = 5
	rank = "Acolyte"
	def __init__(self, _name):
		self.name =_name

"""



print("SADFSADF")