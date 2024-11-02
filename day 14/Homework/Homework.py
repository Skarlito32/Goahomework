#6) შექმენით სია სადაც ჩაამატებთ 1-დან 100-მდე ყველა ლუწ რიცხვს. საბოლოოდ დაპრინტეთ ეს სია(გამოიყენეთ for loop)


# even_numbers = []


# for num in range(1, 101):
#     if num % 2 == 0:
#         even_numbers.append(num)



# print(even_numbers)




#7) შექმენით სია სადაც ჩაამატებთ ყველა რიცხვს 1-დან 50-ის ჩათვლით. შემდეგ გადაუარეთ for loop-ით და ამ სიიდან წაშალეთ ყველა კენტი რიცხვი. საბოლოოდ დაპრინტეთ მიღებული სია



# numbers = []


# for i in range(1, 51):
#     numbers.append(i)

# print(numbers)


# for i in numbers:
#     if i % 2 != 0:
#         numbers.remove(i)


# print(numbers)





#8) შექმენით ხილების სია სადაც გექნებათ მინიმუმ 10 ელემენტი, while loop-ის გამოყენებით წაშალეთ სიის ბოლო ელემენტი იქამდე სანამ სიაში არ დარჩება ორი ელემენტი. ყოველი ელემენტის წაშლისას დაბეჭდეთ ხილების სია



# fruits = ["Apple", "Strawberry", "Orange", "Mango", "pear", "banana", "watermelon", "Grapefruit", "Cherries", "lemon"]


# while len(fruits) != 2:
#     fruits.pop(-1)
#     print(fruits)





#9) შექმენით პროგრამა, რომელიც დაითვლის თუ რამდენჯერ შედის სიაში რიცხვი 1 numbers = [1,2,0,1,32,1,30,1,1,21,1,1,1] (ამისათვის გადაუარეთ სიას for loop-ით)



# numbers = [1,2,0,1,32,1,30,1,1,21,1,1,1]

# one_count = 0


# for i in numbers:
#     if i == 1:
#         one_count += 1



# print(one_count)





#10) შექმენით ორი ცარიელი სია, for loop-ის გამოყენებით მომხარებელს 5-ჯერ შემოატანინეთ ნებისმიერი სიტყვა. თუ შემოტანილი სიტყვის სიგრძე არ აღემატება 5-ს ჩაამატეთ პირველ სიაში, სხვა შემთხვევაში მეორეში. საბოლოოდ დაბეჭდეთ ორივე სია

more_than_five = []

less_than_five = []


for i in range(5):
    random_word = input("Enter Random Word: ")

    if len(random_word) >= 5:
        more_than_five.append(random_word)
    else:
        less_than_five.append(random_word)



print(more_than_five)
print(less_than_five)

        











