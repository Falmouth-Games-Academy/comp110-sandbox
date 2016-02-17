

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
	print "You try being friendly with the duck. The duck doesn't want to be friends. The duck wants nothing but your death. You are paralyzed by fear and can't run. The duck attacks you. You are killed by a duck."
	print "Game over."
	
	print "Play again?"
	print "1: Yes"
	print "2: No"
	input = raw_input()
	if input == '1':
		Start()
	
	

def GetDeported():
	pass

def AngryMob():
	pass

def OnShip():
	pass

def HitIceberg():
	pass

def HappyEnding():
	pass

if __name__ == '__main__':
	Start()
