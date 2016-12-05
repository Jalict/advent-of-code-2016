import re
inst = open('first_input','rw')

input_example = 'R5, L5, R5, R3'
valid = 0
invalid = 0
triangles = 0


p = re.compile('\s*\d{0,9}')    # Remove the commas and whitespace

for line in inst:
    triangles += 1
    nums = p.findall(line)

    if(int(nums[0]) + int(nums[1]) >= int(nums[2])):
        valid += 1
        print int(nums[0]),"\t",int(nums[1]),"\t",int(nums[2]),"\ttrue"
    else:
        invalid += 1
        print int(nums[0]),"\t",int(nums[1]),"\t",int(nums[2]),"\tfalse"

print "valid:",valid
print "invalid:",invalid
print "triangles:",triangles
