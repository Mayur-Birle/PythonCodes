# n > 2
# return all prime number upto n

def sieveOfEratosthenes(n):
	prime = [True]*(n+1);
	prime[0] = prime[1] = False;
	ans = []
	p = 2
	while(p*p < n+1):
		if prime[p] == True:
			for j in range(p*p,n+1,p):
				prime[j] = False
		p += 1

	for i in range(n+1):
		if prime[i]:
			ans.append(i)
	return ans

print(sieveOfEratosthenes(100))
