#2) მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ, რამდენჯერ შედის შემოტანილი რიცხვი 100-ში. გააკეთეთ ყველაზე მოკლე გზით(ამისათვის გამოიყენეთ გაყოფის სწორი ტიპი)


user_num = int(input("Enter Random Number: "))

print("Your Number is:" , user_num)

Number = 100

print(Number // user_num)



#3)while ციკლის გამოყენებით გამოიტანეთ 1-დან 20-მდე ყველა კენტი რიცხვის ჯამი


number = 1

while number<21:
    print(number)
    number = number + 2



#4)მომხარებელს შემოატანინეთ ორი რიცხვი და დაბეჭდეთ ის, რომელიც არის მეტი. თუ ორივე რიცხვი ტოლია დაბეჭდეთ "Both numbers are equal"


user_num1 = int(input("Enter Random Number1: "))

print("Your Number Is:" , user_num1)

user_num2 = int(input("Enter Random Number2: "))

print("You Number is:" , user_num2)


if user_num1 > user_num2:
    print(user_num1 , "is greater than" , user_num2)
elif user_num1 == user_num2:
    print("Both numbers are equal")
else:
    print(user_num2 , "is greater than" , user_num1)


#5)მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ შემოტანილი რიცხვის ფაქტორიალი(დასერჩეთ რა არის ფაქტორიალი)








#6)მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში. შემდეგ დაბეჭდეთ შემოტანილი რიცხვის ჩათვლით ყველა რიცხვის კვადრატის ჯამი



user_number1 = int(input("Enter Random Number: "))


sum = user_number1

for i in range(user_number1):
    sum += i * i
    print(sum)





#7)თამაში "რიცხვის გამოცნობა". შექმენით ცვლადი და შეინახეთ რომელიმე რიცხვი 1-დან 20-ის ჩათვლით(ეს იქნება ჩაფიქრებული რიცხვი). გამოიყენეთ while loop-ი და მომხარებელს შემოატანინეთ რიცხვი იქამდე სანამ არ გამოიცნობს მას. თუ მომხარებლის მიერ შემოტანილი რიცხვი მეტია ჩაფიქრებულზე, დაპრინტეთ To high, თუ ნაკლებია Too low, ხოლო იმ შემთხვევაში თუ მომხარებელი გამოიცნობს რიცხვს დაპრინტეთ "You win"


user_number2 = 18

print("Your thought number is: " , user_number2)

print("Choose One")


num = 0

while num < 25:
    print(num)
    num = num + 1


if num == user_number2:
    print("Winer")

   

