input = open("./input.txt")
lines = input.readlines()

left = []
right = []
distance = 0

for _, line in enumerate(lines):
  [l, r] = line.split("   ")
  left.append(int(l))
  right.append(int(r))

left.sort()
right.sort()


for i, _ in enumerate(left):
  distance += abs(left[i] - right[i])

print(distance)