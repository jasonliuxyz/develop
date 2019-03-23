

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]

L = []
for i in range(4):
	L.append([row[i] for row in matrix])
print(L)
		

 
