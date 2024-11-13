#1) დაასრულეთ წინა გაკვეთილით პრეზენტაცია და ასევე გააკეთეთ პრეზენტაცია ინტერნეტზე(როგორ მუშაობს ის და როგორ უკავშირდება ერთი კომპიუტერი მეორეს)


#დავასრულე 15ტე დავალება


#2) შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე დიდი რიცხვი


# number_lyst = [5, 123 , 23 , 623, 123, 432, 127]  # რიცხვების სია

# higest_number = number_lyst[0]                                                                                    

# for i in number_lyst:
#     if i > higest_number:
#         higest_number = i

# print(higest_number)



# print("Highest Number:", higest_number)




#3) შექმენით რიცხვების სია და დაბეჭდეს სიის თითოეული რიცხვის ფაქტორიალი

    
# numbers = [1, 2, 3, 4, 5, 6, 7, 8,]

# for number in numbers:
#     sum = 1
    
#     for i in range(1, number + 1):
#         sum *= i

#     print(sum)











#4) შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე პატარა რიცხვი


# number_lyst = [5, 123 , 23 , 623, 123, 432, 127]

# lowest_number = number_lyst[0]


# for number_lyst in number_lyst:
#     if number_lyst < lowest_number:
#         lowest_number = number_lyst


# print("Lowest Number:" , lowest_number)



#5) შექმენით რიცხვების სია სადაც გექნებათ დადებითი და უარყოფითი რიცხვები, შემდეგ შექმენით ახალი სია სადაც გექნებათ მხოლოდ უარყოფითი რიცხვები და დაბეჭდეთ ის(გამოიყენეთ while).


# numbers = [1, 2, 5, -3, -10, 23 ,-1]

# negatives = []

# i = 0


# while i < len(numbers):
#     if numbers[i] < 0:
#         negatives.append(numbers[i])
#     i += 1

# print(negatives)







#6) შექმენით რიცხვების სია და დაპრინტეთ სიის თითოეული ელემენტი უკუღმა(გამოიყენეთ range() ფუქნცია ან შექმენით ცვლადი)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # for i in range(len(numbers)-1 ,0, -1):
# #     print(numbers[i])


# for i in numbers[::-1]:
#     print(i)






# 7) შექმენით სიმბოლოების სია, სადაც იქნება დუბლიკატები. შექმენით ახალი სია სადაც ყველა სიმბოლო მხოლოდ ერთხელ გვხვდება

# random_names = ["Irakli", "Giorgi", "Giorgi", "Gigi", "nika", "Mariami", "NIka", 5, 5]

# result = []


# for i in random_names:
#     if result.count(i) == 0:
#         result.append(i)




# print(result)




# for i in random_names:
#     if i not in result:
#         result.append(i)


# print(result)






# 8) შექმენით ცლვადი სადაც შეინახავთ string-ს, შემდეგ შექმენით ახალი ცვლადი სადაც შეინახავთ ამ სტრინგს შემოტრიალებულად და დაბეჭდეთ ის



# name = "gega"

# print(name[::-1])





#9) დაწერეთ პროგრამა, რომელიც მომხამრებელს შემოატანინებს რიცხვს და აბრუნებს სიას, სადაც იქნება გამდოცემული რიცხვის ყველა გამყოფი



# number = int(input("Enter Your Number: "))

# result = []

# for i in range(1,number + 1):
#     if number % i == 0:
#         result.append(i)


# print(result)







#10) შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს და დაპრინტავს რომელი საუკუნეა ის

# year = int(input("Enter Year: "))
# print(year // 100 + 1)





