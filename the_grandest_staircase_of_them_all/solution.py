def partitions_dp(n):
	p = [[0 for x in range(201)] for y in range(201)]
	p[1][1] = 1
	p[2][2] = 1
	for i in range(3, 201):
		for j in range(1, i+1):
			# if the numbers are the same, then just take OPT(i, j-1)
			if i - j == 0:
				p[i][j] = 1 + p[i][j-1]
			elif i - j < j:
				p[i][j] = p[i-j][i-j] + p[i][j-1]
			elif i-j == j:
				p[i][j] = p[j][j-1] + p[i][j-1]
			elif i-j > j:
				p[i][j] = p[i-j][j-1] + p[i][j-1]
	return p[n][n] - 1


#OPT(j) = maximum num of ways to sum to j
