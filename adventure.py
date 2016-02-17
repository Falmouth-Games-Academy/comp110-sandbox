

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
	print "You are on the ship and notice that the Capitain or the crew is nowhere to be seen. Angry at the officials for deporting you"
	print "you decide to release your anger in one of two ways....."
	print "1: Steer the ship into an iceberg and therefore killing everyone and in the process reenact Titanic"
	print "2: Do nothing and go Home"
	input = raw_input()
	if input == '1':
		HitIceberg()
	elif input == '2':
		HappyEnding()
	else:
		OnShip()


def HitIceberg():
	pass

def HappyEnding():
	pass

if __name__ == '__main__':
	Start()
