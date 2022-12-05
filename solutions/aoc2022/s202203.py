
"""
https://adventofcode.com/2022/day/3
"""

def solve_part1(data):

	item_set = [chr(i) for i in range(97,123)] + [chr(i) for i in range(65, 91)]
	# print(item_set)
	total = 0
	for line in data.split("\n"):
		if line == '':
			continue

		mid = int(len(line)/2)
		# print(mid)
		half1 = set(line[:mid])
		half2 = set(line[mid:])
		share_points = sum([item_set.index(i) + 1 for i in half1 if i in half2])
		# print([i for i in half1 if i in half2], share_points)
		# print(share_points)
		total += share_points
		# break
	return total

def solve_part2(data):

	item_set = [chr(i) for i in range(97,123)] + [chr(i) for i in range(65, 91)]
	# print(item_set)
	total = 0
	data_split = [line for line in data.split("\n") if line != '']
	groups = [data_split[i:min(i+3, len(data_split))] for i in range(0,len(data_split),3)]

	for g in groups:
		print(g)
		shared_set = set(g[0])
		for e in g[1:]:
			shared_set.intersection_update(e)

		shared_points = sum([item_set.index(i) + 1 for i in shared_set])
		# print([i for i in half1 if i in half2], share_points)
		# print(share_points)
		total += shared_points
		# break
	return total

