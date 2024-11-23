#1) შექმენით სია შემდგარი მინიმუმ 5 ელემენტისგან. წაუშალეთ ამ სიას ბოლო ორი ელემენტი და დაბეჭდეთ ის


# num_list = [1, 2, 3, 4, 5]

# print(num_list[:-2])



#2) შექმენით ცვლადი, სადაც შეინახავთ სთრინგს. slicing-ის მეშვეობით დაბეჭდეთ ის უკუღმა

# name = "irakli"

# print(name[::-1])



#3) შექმენით რიცხვების სია შემგარი 10 მინიმუმ ელემენტისგან. გაიგეთ ამ სიაში ყველაზე პატარა და დიდი რიცხვი, შემდეგ კი დაბეჭდეთ მათი ჯამი


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# lowest_number = numbers[0]

# highest_number = numbers[0]




# for i in numbers:
#     if i < lowest_number:
#         lowest_number = i
#     elif i > highest_number:
#         highest_number = i
     
# print(highest_number + lowest_number)
    

# print(lowest_number)
# print(highest_number)




#4) შექმენით ცვლადი სადაც შეინახავთ სთრინგს და გაიგეთ, არის თუ არა ის პალინდრომი(პალინდრომი არის ისეთი სიტყვა, რომელიც ორივე მხრიდან ერთნაირად იკითხება, მაგალითად, "ana"...)


# name = "ana"

# name = name.lower()

# print(name == name[::-1])

    

#5) შექმენით რიცხვების სია, გადაუარეთ მას for loop-ით, გაიგეთ რამდენი ლუწი და რამდენი კენტი რიცხვი გვაქვს სიაში და დაბეჭდეთ მათი რაოდენობა


# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_count = 0

# odd_count = 0

# for i in number:
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1


# print("სიაში არის" , even_count , "ლუწი რიცხვი")
# print("სიაში არის" , odd_count , "კენტი რიცხვი")


#6) შექმენით სია, სადაც გექნებათ 1-ანები და 0-ანები, შექმენით ახალი სია, რომელიც თავიდან იქნება ცარიელი. for loop-ით გადაუარეთ პირველ სიას და თუ საიტერაციო ცვლადის მნიშვნელობა იქნება 1, ახალ სიაში ჩაამატეთ True, სხვა შემთხვევაში False. საბოლოოდ დაბეჭდეთ ახალი სია



# num = [1, 0, 1, 0]

# empty = []

# for i in num:
#     if i == 1:
#         empty.append(True)
#     else:
#         empty.append(False)


# print(empty)







