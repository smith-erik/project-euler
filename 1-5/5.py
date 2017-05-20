def findSmalletDivisible(maxLoops):
	i = 21
	while i < maxLoops:
		for n in range(2,21):
			if i % n != 0:
				break
			# return i

		i += 1
	return None

x = findSmalletDivisible(10000)
print(str(x))