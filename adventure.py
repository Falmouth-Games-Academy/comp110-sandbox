

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
	print "You approach the duck ready to eat it."
	print "It's so delicious looking you can barely restrain yourself."
	print "You lunge at the duck and swallow it whole!"
	print "Two hours later..."
	print "While eating the duck seemed like a good plan, you hadn't noticed it was a poisoned drug using duck."
	print "You died."

def PsychoDuck():
	pass

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
