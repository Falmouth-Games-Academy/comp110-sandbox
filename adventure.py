

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
	print "After heading east, you see something orange poking out of some nearby bushes."
	print "Upon closer inspection, you realise that it is the bill of a duck."
	print "The duck leaps out of the bushes and smirks at you. He tells you his name is Villanden."
	print "'It's nice to meet you, Villanden', you say, as your stomach rumbles."
	print "What do you want to do?"
	print "1: eat duck"
	print "2: befriend duck"
	input = raw_input()
	if input == '1':
		GetPoisoned()
	if input == '2':
		PsychoDuck()
	else:
		EncounterDuck()

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
	print ('Well since you decided to hit an iceberg. You start to hear screams from the many people on board you are about to kill.')
	print ('It\'s just as well that they don\'t have lifeboats on board deportation ships as you definitely deserve what your about to get...')
	print ('DEAD')

def HappyEnding():
	pass

if __name__ == '__main__':
	Start()
