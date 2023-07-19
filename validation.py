def validate_dec(or_func):
	def wrap_func(x,y):
		try:
			float(x)
			float(y)
			r = or_func(x,y)
		except ValueError:
			print("Wrong type was given")
		else:
			return r
	return wrap_func 

@validate_dec
def adder(x,y):
	return float(x) + float(y)


x = input("Enter the first number: ")
y = input("Enter the second number: ")
print(adder(x,y))