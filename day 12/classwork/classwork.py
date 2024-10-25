#1) მომხარებელს შემოატანინეთ ორი რიცხვი, აიყვანეთ ისინი მე-3 ხარისხში და გაიგეთ მათი ჯამი, თუ ჯამი ლუწია დაპრინტეთ "Result is Even", სხვა შემთვევაში "Result is Odd"



user_num1 = int(input("Enter Random Number1: "))

user_num2 = int(input("Enter Random Number2: "))

user_num1 = user_num1 ** 3

user_num2 = user_num2 ** 3

print("Your Number1 in the 3rd degree will be: " , user_num1)

print("Your Number2 in the 3rd degree will be: " , user_num2)

sum = user_num1 + user_num2

print(sum)

if user_num1 + user_num2 % 2 == 0:
    print("Result is Even")
else:
    print("Result is Odd")