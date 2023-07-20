def authenticate_dec(or_func):
	def wrap_func(pass_guess):
		ls = ['a1234567','abcd1234','awsd5678']
		try:
			ls.index(pass_guess) 
			r = or_func(pass_guess)
		except ValueError:
			print("User is not logged in")
		else:
			return r
	return wrap_func 

@authenticate_dec
def login_check(pass_guess):
	return pass_guess


pass_guess = input("Enter the password: ")
print(login_check(pass_guess))