# 2) შექმენით ცვლადები და შეინახეთ სხვადასხვა მონაცემთა ტიპის მნიშვნელობები. შემდეგ შეამოწმეთ თითოეული ცვლადის მონაცემთა ტიპი.
name = "irakli"
age = 17
height = 1.82
is_handsome = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_handsome))



# 3) მომხარებელს შემოატანინეთ რიცხვი და შეამოწმეთ მისი ტიპი, ისე რომ დაგიბრუნდეთ integer
age = int(input("enter your number: "))
print(type(age))



# 4) გააკეთეთ 5-5 მაგალთი შედარების ოპერატორებზე
print(5 > 10)
print(10 < 15)
print(23.5 >= 14.5)
print(50 <= 23)
print(5 == 5)
print(5 != 5)



# 5) დაბეჭდეთ ყველა შესაძლო ვარიანტი and და or ოპერატორებზე
# and - და
# or - ან

#and ოპერატორის დროს, ყველა პირობა უნდა კმაყოფილდებოდეს
print(True and False) #False
print(False and True) #False
print(False and False) #False
print(True and True) #True

# #or ოპერატორის დროს, საკმარისია კმაყოფილდებოდეს მხოლოდ ერთი პირობა
print(True or False) #True
print(False or True) #True
print(True or True) #True
print(False or False) #False



# 6) მომხარებელს შემოატანინეთ მისი ასაკი, როგორც სტრინგი და დაბეჭდეთ მისი ტიპი. შემდეგ შეუცვალეთ მას მონაცემთა ტიპი ჯერ integer-ად, შემდეგ float-ად (ყოველ გარდაქმნაზე დაბეჭდეთ შედეგი)

user_age = input("Enter your age: ") 
print(type(user_age))

user_age = int(user_age)
print(type(user_age))

user_age = float(user_age)
print(type(user_age))


# 7) მომხარებელს შემოატანინეთ მისი საყვარელი რიცხვი და გაიგეთ არის თუ არა ის ლუწი
num = int(input("Enter your favorite number: "))

if (num % 2) == 0:
    print("Luwia")
else:
     print("Kentia")


# 8) მომხარებელს შემოატანინეთ მისი ასაკი და სახელი, შემდეგ შეამოწმეთ არის თუ არა ის სრულწლოვანი და უდრის თუ არა მისი სახელი თქვენს სახელს

name = input("Enter your name: ")
age = int(input("Enter your age: "))
my_name = "irakli"

print(age >= 18 and name == my_name)