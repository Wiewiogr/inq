from random import randint
from weapon import * 
from units import *
from squad import *
from options import *
from fight import *

fight_opt = {1 : lambda tmp : tmp.show_members,
			3 : lambda who, target, weapon : who.shoot(target,weapon),
			4 : lambda who, target, weapon : who.attack(target,weapon),
			2 : lambda who : who.show_info()  }


me = cr_acolyte("Andrzej")
enemy = cr_acolyte("Jurek")
henchmans = Squad()
henchmans.units = {"Andrzej":cr_acolyte("Andrzej"),
					"Seba" : cr_acolyte("Seba"),
					"Janusz" : cr_acolyte("Janusz")}
henchmans.show_members()


ene = Squad()
ene.units = {"Anj":cr_acolyte("Andrzej"),
					"Sb" : cr_acolyte("Seba"),
					"Jan" : cr_acolyte("Janusz")}
me.attack(enemy,0)
me.show_info()

fig = Fight(henchmans,ene)
fig.beg()

while False != fig.is_end:
	unit = fig.next()
	print("-------------------------------")
	choice = "safsd"
	print("Next unit : ",unit) #dodac kolesia
	if unit in fig.allies.units :
		while choice != "1" and choice != "2" and choice != "3" and choice != "4":
			print("What you want to do?")
			print("1 - show squad members")
			print("2 - show member info")
			print("3 - shoot")
			print("4 - attack")
			choice = input("Your choice : ")
			if choice == "1":
				fig.allies.show_members()
				choice = "SADFSDA"
			elif choice == "2":
				fig.allies.units[unit].show_info()
				choice = "sfdsa"
			elif choice == "3":
				fig.enemy.show_members()
				who = input("Who do you want to attack : ")
				print("Weapons : ")
				for x in range(len(fig.allies.units[unit].weapons)):
					print("	"+str(x), ": ")
					fig.allies.units[unit].weapons[x].show_info()
				weap = input("Which weapon : ")
				fig.allies.units[unit].shoot(fig.enemy.units[who],int(weap))
			elif choice == "4":
				fig.enemy.show_members()
				who = input("Who do you want to attack : ")
				print("Weapons : ")
				for x in range(len(fig.allies.units[unit].cc_weapons)):
					print("	"+str(x), ": ")
					fig.allies.units[unit].cc_weapons[x].show_info()
				weap = input("Which weapon : ")
				fig.allies.units[unit].attack(fig.enemy.units[who],int(weap))
			
			



	






