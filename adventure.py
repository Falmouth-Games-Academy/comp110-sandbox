

def Start():
	print "Your adventure begins! What do you do?"
	print "1: go east"
	print "2: go west"
	input = raw_input()
	if input == '1':
		EncounterDuck()
	elif input == '2':
		GetDeported()
	else:
		Start()

def EncounterDuck():
	pass

def GetPoisoned():
	pass

def PsychoDuck():
	pass

def GetDeported():
	pass

def AngryMob():
	pass

def OnShip():
	pass

def HitIceberg():
	print ('Well since you decided to hit an iceberg. You start to hear screams from the many people on board you are about to kill.')
	print ('It\'s just as well that they don\'t have lifeboats on board deportation ships as you definitely deserve what your about to get...')
	print ('DEAD')

def HappyEnding():
	pass

if __name__ == '__main__':
	Start()
