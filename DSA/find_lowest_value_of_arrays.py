my_arrays = [7,12,9,4,11,3,5,70,2,32]
minValue = my_arrays[0]
for i in my_arrays:
    if minValue > i:
        minValue = i
print("The Min Value Is :", minValue)