đó
xong r

from math import*
def y(x0):
	y0 = pow(x0,3) + 2*pow(x0,2) - 4*x0 +1
	return y0
	
xy = [(-5, -20),(-4, -15),(-3, 4),(-2, 9),(-1, 7),(0, 1),(1, -7),(2, -9),(4, 81),(5, 130)]
y0 = []
A = []
B = []
for i in xy:
	y0.append(y(i[0]))
	if y(i[0]) == i[1]:
		A.append(i)
	else: B.append(i)
print(A)
print(B)
print(y0)
sumA = 0
sumB = 0

for j in A:
	sumA += j[1]
for j in B:
	sumB += j[1]
result = abs(sumA - sumB)
print(result)
