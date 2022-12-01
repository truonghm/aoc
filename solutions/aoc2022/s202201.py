"""
https://adventofcode.com/2022/day/1
"""

def solve_part1(data):
	
	max = 0
	for elve in data.split("\n\n"):
		calories = elve.split("\n")
		# print(calories)
		total_cal = 0
		for c in calories:
			try:
				total_cal += int(c)
			except ValueError:
				pass
		if total_cal >= max:
			max = total_cal

	return max

def solve_part2(data):
	
	top3 = [0,0,0]
	sum_top3 = 0
	all_cal = []
	for i, elve in enumerate(data.split("\n\n")):
		calories = elve.split("\n")
		# print(calories)
		cal = 0
		for c in calories:
			try:
				cal += int(c)
			except ValueError:
				pass

		all_cal.append(cal)

		min_top3 = min(top3)
		if cal > min_top3:
			top3.pop(top3.index(min_top3))
			top3.append(cal)
		# print(top3)

	return sum(top3)
	