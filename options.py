from squad import *

fight_opt = {1 : lambda tmp : tmp.show_members,
			2 : lambda who, target, weapon : who.shoot(target,weapon)  }

print("1 - show squad members")
print("2 - shoot")
print("3 - attack")
print("4 - skip")
