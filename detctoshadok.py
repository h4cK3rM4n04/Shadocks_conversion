#shadok = ["GA","BU","ZO","MEU"]
var = 0
def dectoshadok(chaine):
	res = chaine // 4
	global var
	if chaine == 0 or chaine == 1:
		return chaine
	while res != 0:
		res = chaine // 4
		i = chaine % 4
print(dectoshadok(0))