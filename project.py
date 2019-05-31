# Egyptian Rat Slap simulator
import random as rd
import more_itertools as mit


def main():
	nPlayers = 4
	skills = [1, 2, 2, 3] # higher number = faster reaction time
	# nDecks = int((nPlayers / 4) + 1)
	deck, nCards = getDeck()
	rd.shuffle(deck)
	hands = deal(deck, nPlayers)

	# nPlayers = len(hands)
	winner = None
	curPlayer = 0
	pile = []

	while(not winner): # each iteration of loop is one person's turn
		printgame(pile, hands, curPlayer)

		# skip over players with empty hands
		if (not hands[curPlayer]):
			curPlayer += 1
			curPlayer %= len(hands)

		# put down a card
		topCard = hands[curPlayer].pop()
		if not hands[curPlayer]:
			hands.pop(curPlayer)

		pile.append(topCard)

		nTries = isFace(topCard)
		if nTries >= 0:
			faceCard(pile, hands, curPlayer)

		if checkSlap(pile):
			taker = winSlap(len(hands))
			hands[taker] = pile + hands[taker]
			printgame(pile, hands, curPlayer)
			pile.clear()
			curPlayer = taker
		printgame(pile, hands, curPlayer)

		winner = checkWinner(hands, nCards)

		if (ntries < 0): # normal mode
			curPlayer += 1
			curPlayer %= len(hands) # loop back to first player
	# return winner
	print()

def getDeck(nDecks=1, jokers=False):
	deck = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']*4
	if jokers:
		deck.append('J')
		deck.append('J')
	return (deck * nDecks, len(deck))

def deal(deck, nPlayers):
	return [(list(p)) for p in mit.distribute(nPlayers, deck)]

def burn(deck, player):
	deck.insert(0, player.pop())
	if not hands[curPlayer]:
		hands.pop(curPlayer)

def checkWinner(hands, nCards):
	for p in hands:
		if int(len(p) is nCards):
			return p
	return None

def winSlap(nPlayers=4):
	taker = rd.randrange(nPlayers)
	return taker

def checkSlap(pile, double=True, sandwich=True, topBottom=False,\
		jokers=False, addToTen=False, runs=False, marriage=False):
	
	if double and len(pile) > 1 and pile[-2] == pile[-1]:
		return True 
	if sandwich and len(pile) > 2 and pile[-3] == pile[-1]:
		return True 
	return False



def isFace(topCard):
	# return card == 'J' \
	# 	or card == 'Q' \
	# 	or card == 'K' \
	# 	or card == 'A'

	nTries = -1
	if   topCard == 'J':
		nTries = 1
	elif topCard == 'Q':
		nTries = 2
	elif topCard == 'K':
		nTries = 3
	elif topCard == 'A':
		nTries = 4
	return nTries

def faceCard(pile, hands, curPlayer):
	curPlayer += 1
	curPlayer %= len(hands) # loop back to first player
	if not pile:
		return

	nTries = -1
	topCard = pile[-1]
	if   topCard == 'J':
		nTries = 1
	elif topCard == 'Q':
		nTries = 2
	elif topCard == 'K':
		nTries = 3
	elif topCard == 'A':
		nTries = 4
	return nTries
	for i in range(nTries):
		# print(curPlayer)
		if not hands[curPlayer]:
			curPlayer = (curPlayer + 1) % len(hands)
		card = hands[curPlayer].pop()
		pile.append(card)


		if checkSlap(pile):
			taker = winSlap(len(hands))
			hands[taker] = pile + hands[taker]
			printgame(pile, hands, curPlayer)
			pile.clear()
			curPlayer = taker
		printgame(pile, hands, curPlayer)



		if isFace(card):
			faceCard(pile, hands, curPlayer)
		
	taker = (curPlayer-1) % len(hands) # last player
	hands[taker] = pile + hands[taker]
	pile.clear()

def printgame(pile, hands, curPlayer):
	# print(curPlayer)
	print("\n*****> " + str(pile))
	# print([str(h) + '\n' for h in hands])
	for h in hands:
		print(str(h))

def play(hands, nCards, nPlayers):
	
	return

main()