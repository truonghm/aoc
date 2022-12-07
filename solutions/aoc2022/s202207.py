
"""
https://adventofcode.com/2022/day/4
"""
import os

def __build_dir_list(data):
    dir_list = {"root": []}
    fullpath = 'root'
    for n, line in enumerate(data.split("\n")):
        # if n > 20:
        #     break
        if line == "":
            continue
        
        if line.startswith("$"):
            if line == '$ ls':
                continue
            elif line.startswith("$ cd"):
                if line.endswith("/"):
                    continue
                elif line.endswith(".."):
                    fullpath = os.path.dirname(fullpath)
                
                else:
                    fullpath = os.path.join(fullpath, line.split(" ")[2])
                    # print(fullpath)
                    dir_list[fullpath] = []
        else:
            a, b = line.split()
            if a.isnumeric():
                # print(current)
                fullpath_split = fullpath.split("/")
                for n, dir in enumerate(fullpath_split):
                    dir_list["/".join(fullpath_split[:n+1])].append(int(a))
                # print('added:', a, b, f'to {fullpath}')

    return dir_list

def solve_part1(data):
    dir_list = __build_dir_list(data)

    total_size = 0
    for k, v in dir_list.items():
        if k == 'root':
            continue

        file_size = sum(v) 
        if file_size <= 100000:
            total_size += file_size

    return total_size

def solve_part2(data):
    dir_list = __build_dir_list(data)

    total_size = sum(dir_list['root'])
    remaining_size = 70000000 - total_size
    min_size = sum(dir_list['root'])
    for files in dir_list.values():
        file_size = sum(files)
        if remaining_size + file_size < 30000000:
            continue
        if file_size < min_size:
            min_size = file_size

    return min_size
