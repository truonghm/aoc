from utils import read_input, get_args

def solve(day:int, year:int):
	data = read_input(day=day, year=year)
	solutions = __import__(name = f"solutions.aoc{year}.s{year}{day}", fromlist=[None])
	
	s1 = solutions.solve_part1(data)
	s2 = solutions.solve_part2(data)
	return s1, s2

if __name__ == "__main__":
	s1, s2 = solve(*get_args())
	print(s1, s2)
	# data = read_input(day='01', year='2022')
	# solve_part1(data)