#2)  შექმენით string-ების სია, გადაუარეთ მას for loop-ით და დაბეჭდეთ სიაში არსებული ყველა სიტყვის სიმბოლოთა რაოდენობა


# chars = ["Luka", "Irakli", "Nika", "Giorgi"]

# for char in chars:
#         print("სიმბოლოათა რაოდენობა", len(char))



#3) შექმენით რიცხვების სია, while loop-ის გამოყენებით გაიგეთ ამ სიაში ყველა ლუწი რიცხვის ჯამი და დაპრინტეთ


# num_lyst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# even = 0


# i = 0

# while i < len(num_lyst):
#     if num_lyst[i] % 2 == 0:
#         even += num_lyst[i]
#     i += 1


# print("ლუწი რიცხვების ჯამი არის:", even)


#4) შექმენით სახელების სია, გადაუარეთ მას for loop-ით და დაბეჭდეთ ამ სიიდან მხოლოდ ის სახელები, რომლებიც იწყებიან "A"-ზე

# name_lysts = ["Gigi", "Teona", "Salome", "toko", "Anastasia", "Anamaria"]


# for name_lyst in name_lysts:
#     if name_lyst[0] == "A":
#         print(name_lyst)



#5) შექმენით რიცხვების სია, სადაც გექნებათ დუბლიკატები. გადაუარეთ მას for loop-ით და დაბეჭდეთ მხოლოდ ისეთი რცხვების ჯამი, რომლებიც არ მეორდება სიაში


# numbers = [4, 6, 2, 9, 10, 10, 2, 4, 65, 1]

# no_duplicate_sum = 0


# for number in numbers:
#     if numbers.count(number) == 1:
#         no_duplicate_sum += number



# print(no_duplicate_sum)



#6) შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს რიცხვს და დაბეჭდავს 1-დან შემოტანილ რიცხვამდე ყველა მარტივ რიცხვს

# user_num = int(input("შეიყვანეთ რიცხვი: "))


# for i in range(1, user_num):















#7) შექმენით სია შემდგარი 5 ელემენტისგან. slicing-ის გამოყენებით დაბეჭდეთ მე-3 და მე-4 ელემენტები



# char = ["a", "b", "c", "d", "e"]

# print(char[2:4])


#8) შექმენით რიცხვების სია, შემდგარი 10 ელემენტისგან. slicing-ის გამოყენებით დაბეჭდეთ სიის ყოველი მეორე ელემენტი


# char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# print(char[::2])



#9) შექმენით ცვლადი, სადაც შეინახავთ string-ს. დაბეჭდეთ სთრინგის ბოლო სამი სიმბოლო(გამოიყენეთ slicing და მინუსიანი ინდექსები)


# name = "Irakli"

# print(name[-3:])



#10) შექმენით რიცხვების სია, დაბეჭდეთ სია თავიდან ბოლომდე slicing-ის გამოყენებით 

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(num[::])