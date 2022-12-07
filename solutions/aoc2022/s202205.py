
"""
https://adventofcode.com/2022/day/5
"""
import numpy as np
import pandas as pd
import re
from io import StringIO

def __separate_instr(s):
	move_no = int(re.findall("(?<=move\s)(.*?)(?=\sfrom)", s)[0])
	from_no = int(re.findall("(?<=from\s)(.*?)(?=\sto)", s)[0])
	to_no = int(re.findall("(?<=to\s)(.*?)$", s)[0])
	return move_no,from_no, to_no

def __transform_stacks(s):
	s = re.sub(r"\s\d+\s\s", "", s)
	s = re.sub(r"\s\d+\s", "", s)
	s = s.replace("] [", ",")
	s = s.replace("] ", ",")
	s = s.replace(" [", ",")
	s = s.replace("[", "")
	s = s.replace("]", "")
	s = s.replace("    ", "#,")
	s = s.replace("   ", "#")

	return s

def solve_part1(data):
	
	stacks, instr = data.split("\n\n")
	instr = [__separate_instr(i) for i in instr.split("\n") if i != '']

	stacks = __transform_stacks(stacks)
	stacks = "" + ",".join([str(i+1) for i in range(9)]) + "\n" + stacks

	stacks_list = pd.read_csv(
		StringIO(stacks), 
		sep=",", 
		).T.values.tolist()

	st = [[c for c in st if c != '#'] for st in stacks_list]

	for i in instr:
		mv, fr, to = i
		st[to-1]  = st[fr-1][:mv][::-1] + st[to-1]
		st[fr-1] = st[fr-1][mv:]

	return "".join([s[0] for s in st])

def solve_part2(data):
	stacks, instr = data.split("\n\n")
	instr = [__separate_instr(i) for i in instr.split("\n") if i != '']

	stacks = __transform_stacks(stacks)
	stacks = "" + ",".join([str(i+1) for i in range(9)]) + "\n" + stacks

	stacks_list = pd.read_csv(
		StringIO(stacks), 
		sep=",", 
		).T.values.tolist()

	st = [[c for c in st if c != '#'] for st in stacks_list]

	for i in instr:
		mv, fr, to = i
		st[to-1]  = st[fr-1][:mv][::1] + st[to-1]
		st[fr-1] = st[fr-1][mv:]

	return "".join([s[0] for s in st])
