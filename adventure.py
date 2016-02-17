

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
	print "You are attacked by an angry mob like in The Simpsons Movie, but there was no sink hole for you to escape down so you died."
	print "RIP YOU"

def OnShip():
	pass

def HitIceberg():
	pass

def HappyEnding():
	pass

if __name__ == '__main__':
	Start()
