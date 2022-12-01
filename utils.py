import requests
import os
import sys
from dotenv import load_dotenv
import getopt, sys
import datetime
load_dotenv()

def read_input(day:int, year:int) -> str:
	try:
		with open(f"input/{year}/input_{year}{day}.txt", "r") as f:
			return f.read()
	except:
		raise FileNotFoundError(f"The provided day ({day}) and/or year ({year}) does not match any input file.")

def download_input(day:int, year:int) -> str:
	res = requests.get(f"https://adventofcode.com/{year}/day/{int(day)}/input", cookies = {'session': os.getenv("SESSION_ID")} )

	if res.status_code != 200:
		raise ValueError(f"Cannot find an input for the provided day ({day}) and/or year ({year}). Returned status sode is {res.status_code}.")
	input_path = f"input/{year}/input_{year}{day}.txt"
	with open(input_path, "w") as f: 
		f.write(res.text)

	return input_path

def get_args():
	today = datetime.datetime.today()
	day = today.day
	year = today.year

	opts, args = getopt.getopt(sys.argv[1:], shortopts = "dy", longopts=["day=", "year="])

	if len(opts) > 0:
		for opt, arg in opts:
			if opt in ["-d", "--day"]:
				if arg.isnumeric():
					if int(arg) >= 1 and int(arg) <= 25:
						day = str(int(arg)).zfill(2)
					else:
						raise ValueError("The input day is invalid (has to be between 1 and 25, inclusive).")
			else:
				if day >= 25:
					raise ValueError("No day provided, using day of current date, which is not valid for any input (Day must be between 1 and 25, inclusive).")
				else:
					day = str(day).zfill(2)

			if opt in ["-y", "--year"]:
				if arg.isnumeric():
					if int(arg) >= 2015:
						year = str(int(arg))
					else:
						raise ValueError("The input year is invalid (has to be greater than or equal to 2015).")
			else:
				if year < 2015:
					raise ValueError("No year provided, using year of current date, which is not valid for any input (has to be greater than or equal to 2015).")
				else:
					year = str(year)

	return day, year