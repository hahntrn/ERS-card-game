# Egyptian Rat Slap simulator
import random as rd
import more_itertools as mit


def main():
	nPlayers = 2
	reactionTimes = [1, 2, 2, 3] # higher number = faster reaction time
	# nDecks = int((nPlayers / 4) + 1)
	deck = getDeck()
	rd.shuffle(deck)
	hands = deal(deck, nPlayers)


	winner = -1
	curPlayer = 0
	pile = []
	debt = -1

	while(winner < 0): # each iteration of loop is one person's turn
		printgame(pile, hands, curPlayer)

		# skip over players with empty hands
		while hands[curPlayer] == []:
			curPlayer = (curPlayer + 1) % len(hands)

		# put down a card
		topCard = hands[curPlayer].pop()
		pile.append(topCard)
		
		# check for slaps and winner
		if checkSlap(pile):
			taker = winSlap(len(hands))
			hands[taker] = pile + hands[taker]
			pile.clear()
			curPlayer = taker
			continue
		winner = checkWinner(hands, nCards)
		if winner >= 0:
			return winner

		# analyze card

		cardCost = isFace(topCard)

		print(debt)
		# topCard is a facecard
		if cardCost > 0: 
			debt = cardCost
			curPlayer = (curPlayer + 1) % len(hands)
			continue

		# topCard is a number

		# normal mode, numbers
		if (debt < 0): 
			curPlayer = (curPlayer + 1) % len(hands)

		# curPlayer still owes prevPlayer cards
		if debt > 0:
			debt -= 1
			continue

		if debt == 0:
			taker = (curPlayer - 1) % len(hands)
			hands[taker] = pile + hands[taker]
			pile.clear()
			curPlayer = taker
			debt = -1
			continue
	# printgame(pile, hands, curPlayer)

def getDeck(nDecks=1, jokers=False):
	deck = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']*2
	if jokers:
		deck.append('J')
		deck.append('J')
	return deck * nDecks

def deal(deck, nPlayers):
	return [(list(p)) for p in mit.distribute(nPlayers, deck)]

def burn(deck, player):
	deck.insert(0, player.pop())
	if not hands[curPlayer]:
		hands.pop(curPlayer)

def incr(curPlayer, hands):
	return (curPlayer + 1) % len(hands)

def checkWinner(hands, nCards):
	for i in range(len(hands)):
		if int(len(hands[i]) is nCards):
			return i
	return -1

def winSlap(reactionTimes, nPlayers=4):
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

def printgame(pile, hands, curPlayer):
	# print(curPlayer)
	print("\n*****> " + str(pile))
	# print([str(h) + '\n' for h in hands])
	for h in hands:
		print(str(h))

main()
