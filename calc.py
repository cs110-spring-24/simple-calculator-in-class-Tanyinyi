num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
op=input("Enter the operator:")

if op=="+":
	total=num1 + num2
	print(f"{num1}+{num2}={total}")
elif op=="-":
	total2=num1-num2
	print(f"{num1}-{num2}={total2}")
elif op=="*":
	total3=num1 * num2
	print(f"{num1}-{num2}={total3}")
elif op=="/" and num2!=0:
	total4=num1/num2
	print(f"{num1}/{num2}={total4}")
elif op=="/" and num2==0:
	print(f"{num1}/{num2}, does not exist")
elif op=="**":
	total5=num1**num2
	print(f"{num1}**{num2}={total5}")
elif op=="//":
	total6=num1//num2
	print(f"{num1}//{num2}={total6}")
elif op=="%":
	total7=num1%num2
	print(f"{num1}%{num2}={total7}")
else:
	print("you print an invalid operator, please a correct later")