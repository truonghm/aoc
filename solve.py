from utils import read_input
import getopt, sys
import datetime

def solve(day:int, year:int):
	data = read_input(day=day, year=year)
	solutions = __import__(name = f"solutions.aoc{year}.s{year}{day}", fromlist=[None])
	
	s1 = solutions.solve_part1(data)
	s2 = solutions.solve_part2(data)
	return s1, s2

def get_args():
	day, year = '01', datetime.datetime.today().year

	opts, args = getopt.getopt(sys.argv[1:], shortopts = "dy", longopts=["day=", "year="])

	if len(opts) > 0:
		for opt, arg in opts:
			if opt in ["-d", "--day"]:
				if arg.isnumeric():
					if int(arg) >= 1 and int(arg) <= 25:
						day = str(int(arg)).zfill(2)
					else:
						raise ValueError("The input day is invalid (has to be between 1 and 25, inclusive).")

			if opt in ["-y", "--year"]:
				if arg.isnumeric():
					if int(arg) >= 2015:
						year = str(int(arg))
					else:
						raise ValueError("The input year is invalid (has to be greater than or equal to 2015).")

	return day, year

if __name__ == "__main__":
	s1, s2 = solve(*get_args())
	print(s1, s2)
	# data = read_input(day='01', year='2022')
	# solve_part1(data)