def memoize(or_func):
	cache = {}
	def wrap(*args):
		if args in cache:
			return cache[args]
		r = or_func(*args)
		cache[args] = r
		return r
	return wrap

@memoize
def fib(n):
	if n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

n = int(input("Enter the index: "))
print(fib(n)) 