#2) შექმენით სია სადაც, შეიტანთ მინიმუმ 10 რიცხვს, გადაუარეთ for ციკლის დახმარებით და დაბეჭდეთ თითოეული რიცხვი კენტია თუ ლუწი.


# number_list = [1,2,3,4,5,6,7,8,9,10]

# for i in (number_list):
#     if i % 2 == 0:
#         print(i , "Even")
#     else:
#         print(i , "Odd")


# #3) შექმენით სახელების სია სადაც გექნებათ მინიმუმ 10 სახელი, დაბეჭდეთ ამ სიიდან მხოლოდ ის სახელები რომლების ინდექსებიც არის ლუწი

# name_lyst = ["Irakli", "Giorgi", "Nino", "Mariam", "Lasha", "Tamari", "Ana", "David", "LevanEka", "Anzori"]

# for i in range(len(name_lyst)):
#     if i % 2 == 0:
#         print(name_lyst[i])



#4) შექმენით სია სადაც გექნებათ 10 რიცხვი, თქვენი დავალებაა გაიგოთ ამ სიაში ყველა ლუწი და კენტი რიცხვიოს ჯამი და დაბეჭდოთ



# number_list2 = [1,2,3,4,5,6,7,8,9,10] 


# ცვლადები ლუწი და კენტი რიცხვების ჯამისთვის

# even_sum = 0

# odd_sum = 0

# for num in number_list2:
#     if num % 2 == 0:
#         even_sum += num
#     else:
#         odd_sum += num
        


# print("ლუწი რიცხვების ჯამი:", even_sum)

# print("კენტი რიცხვების ჯამი:", odd_sum)




#5) შექმენით სია სადაც გექნებათ 10 რიცვი, შემდეგ შექმენით ახალი სია, სადაც ჩაამატებთ პირველი სიიდან ყველა ლუწ რიცხვს და გაიგებთ მათ საშუალო არითმეტიკულს.(ახალ სიაზე გამოიყენეთ len() ფუნქცია)



numbers = [1,2,3,4,5,6,7,8,9,10]

even_num = [num for num in numbers if num % 2 == 0]


average_even = sum(even_num) / len(even_num)



print("პირველი სია:", numbers)
print("ლუწ რიცხვების სია:", even_num)
print("ლუწ რიცხვების საშუალო არითმეტიკული:", average_even)
