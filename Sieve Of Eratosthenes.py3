# n > 2
# return all prime number upto n

def sieveOfEratosthenes(n):
	prime = [True]*(n+1);
	prime[0] = prime[1] = False;
	ans = []

	for i in range(2,n+1):
		if prime[i] == True:
			for j in range(i*i,n+1,i):
				prime[j] = False

	for i in range(n+1):
		if prime[i]:
			ans.append(i)
	return ans

print(sieveOfEratosthenes(100))
