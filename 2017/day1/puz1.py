def inverseCaptcha(seq):
	return sum([int(seq[i]) for i in range(len(seq)) if (i < len(seq)-1 and seq[i] == seq[i+1]) or ((i==len(seq)-1) and seq[i] == seq[0])])
