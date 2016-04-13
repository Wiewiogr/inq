##create to_hit chart
def cr_to_hit_cc(tab):
	for i in range(10):
		tmp = []
		for j in range(10):
			res = 0
			if i > j :
				res = 3
			elif 2 * i + 1 >= j:
				res = 4
			else : 
				res = 5
			tmp.append(res)
		tab.append(tmp)
##create to wound chart
def cr_to_wound(tab):
	for i in range(10):
		tmp = []
		for j in range(10):
			res = 4 - i + j
			if res < 2 :
				res = 2
			elif res == 7:
				res = 6
			elif res > 7: 
				res = 7
			tmp.append(res)
		tab.append(tmp)
#create to hit in ranged
def cr_to_hit_ranged(tab):
	for i in range(1,6):
		tab.append(7-i)




to_hit_ranged = []
cr_to_hit_ranged(to_hit_ranged)
to_wound = []
cr_to_wound(to_wound)
to_hit_cc = []
cr_to_hit_cc(to_hit_cc)
