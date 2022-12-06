
"""
https://adventofcode.com/2022/day/4
"""

def solve_part1(data):

	count = 0
	for line in data.split("\n"):
		if line == "":
			continue

		pairs = line.split(",")
		def get_bound(pair):
			return (int(i) for i in pair.split("-"))

		bound1a, bound1b = get_bound(pairs[0])
		bound2a, bound2b = get_bound(pairs[1])

		# x = False
		if bound2a >= bound1a and bound2b <= bound1b:
			# x = True
			count += 1
		elif bound1a >= bound2a and bound1b <= bound2b:
			count += 1

		# print("[", bound1a, bound1b, "]", "[", bound2a, bound2b, "]", x)

	return count

def solve_part2(data):

	count = 0
	for line in data.split("\n"):
		if line == "":
			continue

		pairs = line.split(",")
		def get_bound(pair):
			return (int(i) for i in pair.split("-"))

		bound1a, bound1b = get_bound(pairs[0])
		bound2a, bound2b = get_bound(pairs[1])

		x = False
		if max(bound1a, bound2a) <= min(bound1b, bound2b):
			x = True
			count += 1

		print("[", bound1a, bound1b, "]", "[", bound2a, bound2b, "]", x)

	return count