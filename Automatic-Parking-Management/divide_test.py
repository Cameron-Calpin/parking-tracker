xlength = 1280
ylength = 720
length = 30

for i in range(length):
	# print(i + 1)
	j = i + 1
	if (xlength % j == 0 and ylength % j == 0):
		print(j)
		print("dimensions: ", xlength / j, ylength / j)