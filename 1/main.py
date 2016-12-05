import re

input_example = 'R5, L5, R5, R3'
p = re.compile('[A-Z][0-9]')    # Remove the commas and whitespace

coord = [0,0]
facing = 0
for move in p.findall(input_example):
    direction = move[0:1]
    amount = move[1:2]

    if direction == 'R':
        facing
