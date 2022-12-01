from utils import download_input, get_args

if __name__ == "__main__":
	day, year = get_args()
	input_path = download_input(day=day, year=year)
	print(f"Input for day {day}, year {year} is saved to {input_path}")