for number in range(1,21):
    print(number)

numbers = list(range(1,21))
print (numbers)
min = min(numbers)
print(min)
max = max(numbers)
print(max)
sum = sum(numbers)
print(sum)

even_numbers = list(range(2, 21, 2 ))
for even_number in even_numbers:
    print(even_number)

threes = list(range(3, 31, 3))
print(threes)

cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)
print(cubes)

cubes_2 = [value **3 for value in range(1,11)]
print(cubes_2)
print(f"The first three item of this list are {cubes_2[:3]}")

for item in cubes_2[:3]:
    print(item)
