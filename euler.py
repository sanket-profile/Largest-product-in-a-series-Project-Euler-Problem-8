def adja(s):
	s = str(s)
	maxval = 0
	for i in range(1000-13+1):
		a = s[i:13+i]
		val  = 1
		for i in a:
			if '0' in  a:
				break
			else:
				val = val * int(i)
		if val > maxval:
			maxval = val
		else:
			pass
	return(maxval)
