# Argument <- Number N || Output Nth Number of Fibonacii Series
def fibonacii(nth):
	if(nth<0):	return ':P'
	if(nth<=1):    return nth;
	return fibonacii(nth-1)+fibonacii(nth-2);	

# Argument <- Number || Output -> RevesedNumber
def reverse_number(num):
	ans = 0
	while(num>0):
		ans = ans*10 + num%10
		num //= 10
	return ans

# Argument <- Number || Output -> True if number if palindrome else False
def palindrome(num):
	if reverse_number(num) == num:
		return True
	return False

# Argument <- Number || Output -> Binary String of Number
def toBinary(num):
	if(num == 1):
		return '1'
	elif(num == 0):
		return '0'
	else:
		return toBinary(num//2)+str(num%2)

# Argument <- Binary Number || Output -> Decimal Number
def bin2Dec(x):
	ans = 0
	i = 1
	while(x>0):
		ans += x%10 * i
		i += i;
		x //= 10
	return ans;

# Argument <- Number1, Number2 || Output -> GCD(Highest Common Factor) of Numbers ;)
def GCD(a,b):
	if(b==0):
		return a;
	return GCD(b,a%b);

# Argument <- Number1, Number2 || Output -> LCM of Numbers
def LCM(a,b):
	# a*b = LCM(a,b) * HCF(a,b)
	return a*b // GCD(a,b);

# Argument <- Number || Output -> Factorial of number
def fact(x):
	if(x < 0):
		return 'Not Possible';
	if(x <= 1):
		return 1
	return x*fact(x-1)

# Argument <- Number || Output -> True if prime else False
def checkPrime(x):
	if(x == 2):    return True
	if(x%2 == 0 or x in [0,1]):    return False
	for i in range(3,x//2,2):
		if x%i == 0:
			return False;
	return True;

# Argument <- Number || Output -> True if number is armstrong else False
def armStrong(x):
	ans = 0
	temp = x
	while(temp > 0):
		ans += (temp%10)**4
		temp = temp//10
	if ans == x:
		return True
	return False

# Argument <- Number || Output -> True if number is strong else False
def strong(x):

print('Thanks for visiting here :) ');
