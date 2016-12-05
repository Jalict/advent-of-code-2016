inst = open('input','rw')

keypad = [
    ['0','0','1','0','0'],
    ['0','2','3','4','0'],
    ['5','6','7','8','9'],
    ['0','A','B','C','0'],
    ['0','0','D','0','0']
]

x = 1
y = 1

pwd = ""

for line in inst:
    for char in line:
        if(char == 'U' and y > 0):
            y = y-1
        elif(char == 'D' and y < 2):
            y = y+1
        elif(char is 'L' and x > 0):
            x = x-1
        elif(char == 'R' and x < 2):
            x = x+1
        elif(char == ' '):
            continue
    pwd += str(keypad[y][x])
print pwd
