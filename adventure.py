

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
  print "You have traveled too far west and accidently swam across a border. You then get discoverd by the border police"
  print "1: Do you decide to run and stay illegally?"
  print "2: Do you decide to leave peacefully with the border police?"
  input = raw_input()
  if input == '1':
    AngryMob()
  elif input == '2':
    OnShip()

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
