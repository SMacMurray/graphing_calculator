import numpy as np
import matplotlib.pyplot as plt
import math

def util(term, num, operator):
	if operator == "+":
		term = term + num
	if operator == "-":
		term = term - num
	if operator == "*":
		term = term * num
	if operator == "/":
		term = term / num
	if operator == "^":
		term = term ** num
	return term

def make_equation(x, y, equation, i, num, term, tmp, operator):
	while i < len(equation):
		e = equation[i]
		i = i+1

		#num is what the function is/will be operating on
		#when the function reaches an operator, operate on num using the stored operator and then assign new operator
		#all operations assign to term. add term to y when current iteration finds + or -

		
		if e == "x":
			num = x
			continue
		if e == "e":
			num = math.e
			continue
		if e == "+" or e == "-":
			term = util(term, num, operator)
			y = y + term
			term = np.array(0)
			tmp = ""
			operator = e
			continue
		if e == "*" or e == "/" or e == "^":
			term = util(term, num, operator)
			tmp = ""
			operator = e
			continue

		#multidigit numbers/strings concatenate to tmp
		tmp = tmp + e

		#various functions
		if tmp == "sin(":
			num, i = make_equation(x,np.array(0),equation,i,np.array(0),np.array(0),"","+")
			num = np.sin(num)
			continue
		if tmp == "cos(":
			num, i = make_equation(x,np.array(0),equation,i,np.array(0),np.array(0),"","+")
			num = np.cos(num)
			continue
		if tmp == "tan(":
			num, i = make_equation(x,np.array(0),equation,i,np.array(0),np.array(0),"","+")
			num = np.tan(num)
			continue
		if tmp == "log(":
			num, i = make_equation(x,np.array(0),equation,i,np.array(0),np.array(0),"","+")
			num = np.log10(num)
			continue
		if tmp == "ln(":
			num, i = make_equation(x,np.array(0),equation,i,np.array(0),np.array(0),"","+")
			num = np.log(num)
			continue

		#parenthesis
		if e == "(":
			num, i = make_equation(x,np.array(0),equation,i,np.array(0),np.array(0),"","+")
			continue
		if e == ")":
			term = util(term, num, operator)
			y = y + term
			return y, i

		#convert tmp to an int and assign it to num for the next iteration
		if tmp.isnumeric() == True:
			num = np.array(int(tmp))
		
	#final operation after loop
	term = util(term, num, operator)
	y = y + term
	return y

def main():
	x = np.linspace(-10,10,100)
	y = np.array(0)
	equation = input()
	y = make_equation(x, y, equation, 0, np.array(0), np.array(0), "", "+")

	plt.axhline(y=0, color="black")
	plt.axvline(x=0, color="black")
	plt.plot(x,y)
	plt.grid()

	plt.show() 

if __name__ == '__main__':
	main()

