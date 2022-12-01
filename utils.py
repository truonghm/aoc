def read_input(day:int, year:int) -> str:
	with open(f"input/{year}/input_{year}{day}.txt", "r") as f:
		return f.read()