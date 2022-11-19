for _ in range(int(input())):
	x, y, z = map(int, input().split())
	ans = 0
	for mask in range(8):
		nx = ny = nz = 0
		if mask & 1:
			nx += 1
			ny += 1
		if mask & 2:
			nx += 1
			nz += 1
		if mask & 4:
			nz += 1
			ny += 1
		if nx > x or ny > y or nz > z:
			continue
		have = bin(mask)[2:].count('1')
		have += (nx < x) + (ny < y) + (nz < z)
		ans = max(ans, have)
	print(ans)