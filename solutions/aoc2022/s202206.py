
"""
https://adventofcode.com/2022/day/5
"""
import numpy as np
import pandas as pd
import re
from io import StringIO

def solve_part1(data):
	
	length = 4
	marker = data[:length]

	if len(marker) == len(set(marker)):
		return length

	for n, c in enumerate(data[length:]):
		if len(marker) == length and len(marker) == len(set(marker)):
			return n + length
		marker = marker[1:] + c


def solve_part2(data):

	length = 14
	marker = data[:length]

	if len(marker) == len(set(marker)):
		return length

	for n, c in enumerate(data[length:]):
		if len(marker) == length and len(marker) == len(set(marker)):
			return n + length
		marker = marker[1:] + c