input = open("./input.txt")
lines = input.readlines()

similarity = 0
numberMap = {}
left =  []
right = []

for i, line in enumerate(lines):
  [l,r] = line.split("   ")
  left.append(int(l))
  right.append(int(r))

for i, a in enumerate(left):
  count = 0

  for b in right:
    if a == b:
      count +=1

  numberMap[i] = (a, count)

for row in numberMap:
  (l,r) = numberMap[row]
  similarity += abs(l*r)

print(similarity)