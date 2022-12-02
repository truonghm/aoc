"""
https://adventofcode.com/2022/day/2
"""

def solve_part1(data):

	player1 = 'ABC'
	player2 = 'XYZ'

	score = 0
	for round in data.split("\n"):
		if round == '':
			continue

		p1, p2 = round.split(" ")
		
		index_p1_next = (player1.index(p1) + 1) % len(player1)
		index_p1 = player1.index(p1) % len(player1)
		index_p2 = player2.index(p2) % len(player2)

		score += index_p2 + 1
		if index_p1 == index_p2:
			score += 3
		elif index_p1_next == index_p2:
			score += 6

	return score

def solve_part2(data):

	player1 = 'ABC'
	player2 = 'XYZ'

	score = 0
	for round in data.split("\n"):
		if round == '':
			continue

		p1, p2 = round.split(" ")
		
		index_p1_next = (player1.index(p1) + 1) % len(player1)
		index_p1_prev = (player1.index(p1) + len(player1) - 1) % len(player1)
		index_p1 = player1.index(p1) % len(player1)
		index_p2 = player2.index(p2) % len(player2)

		score += index_p2 * 3
		if p2 == 'Y':
			score += index_p1 + 1
		elif p2 == 'Z':
			score += index_p1_next + 1
		else:
			score += index_p1_prev + 1


	return score

def solve_part1_old(data):
	scores1 = {'X': 1, 'Y': 2, 'Z': 3}
	scores2 = {
		'A X': 3,
		'B Y': 3,
		'C Z': 3,
		'A Y': 6,
		'B Z': 6,
		'C X': 6,
		'A Z': 0,
		'B X': 0,
		'C Y': 0, 
		}
	total_score = 0
	for round in data.split("\n"):
		if round == '':
			continue
		a, b = round.split(" ")
		total_score += scores1[b] + scores2[round]
	
	return total_score


def solve_part2_old(data):
	scores1 = {'X': 0, 'Y': 3, 'Z': 6}
	scores2 = {
		'A X': 3, # C
		'B Y': 2, # B
		'C Z': 1, # A
		'A Y': 1, # A
		'B Z': 3, # C
		'C X': 2, # B
		'A Z': 2, # B
		'B X': 1, # A
		'C Y': 3, # C
		}
	total_score = 0
	for round in data.split("\n"):
		if round == '':
			continue
		a, b = round.split(" ")
		total_score += scores1[b] + scores2[round]
	
	return total_score