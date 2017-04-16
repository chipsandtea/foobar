# Christopher Hsiao 2017
# if y%x == 0, then all of y's multiples can be appended to the list of x's multiples.
# Consider a bucket w/ hash of num and bucket w/ their multiples.

def answer(l):
	# way to store whether or not a number has already been seen. 
    triples = 0
    lucky_doubles = [0] * len(l)
    for i in range(len(l)):
    	for j in range(i):
    		if l[i] % l[j] == 0:
    			lucky_doubles[i] += 1
    for i in range(len(l)):
    	for j in range(i):
    		if l[i] % l[j] == 0:
    			triples += lucky_doubles[j]
    return triples

# given a lucky double, (x, y), for any z s.t. z%y == 0 ,(x,y,z) is a lucky triple
