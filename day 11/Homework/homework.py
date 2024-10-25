#1) 1) გააიაზრეთ ეს კოდი, დაკომენტარეთ თითოეული კოდი

secret_pass = "luka1234"                   #Original Password
user_pass = ''                             #variable that will stores users guessed password

tries = 3                                  #

while tries > 0 and user_pass != secret_pass:
    user_pass = input("Enter your password (you have " + str(tries) + " tries left): ")
    tries = tries - 1

    if user_pass == secret_pass:
        print("Access granted!")
    elif tries == 0:
        print("You've reached the maximum number of tries. Access denied!")
    else:
        print("Access denied! Try again.")



#2) დაითვალეთ რამდენი ლუწი რიცხვია 1-დან 50-ის ჩათვლით(გამოიყენეთ for loop-ი)


#sum = 0

#for i in range(1, 50):
    #if i % 2 == 0:
        #sum = sum + 1
#print(sum)


#3) დაბეჭდეთ 1-დან 100-მდე ყველა ლუწი რიცხვის საშუალო არითმეტიკული. გამოიყენეთ while loop-ი.(დაგჭირდებათ ორი ცვლადის შექმნა, ერთში შეინახავთ ჯამს, მეორეში რაოდენობას)



#i = 1
#even = 0
#even_count = 0

#while i < 100:
#     if i % 2 == 0:
#         even += i
#         even_count += 1
#     i = i + 1
    
# print(even / even_count)


#4) დაბეჭდეთ ყველა რიცხვი 1-დან 30-მდე, რომელიც იყოფა 3-ზე(გამოიყენეთ while loop-ი)

# i = 1

# while i < 30:
#     if i % 3 == 0:
#         print(i)
#     i += 1



#5) მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ მიღებული რიცხვის ყველა გამყოფი(გამოიყენეთ for loop-ი)


# user_number = int(input("Enter The number: "))

# for i in range(1, user_number + 1):
#     if user_number % i == 0:
#         print(i)



#6 დაწერეთ პროგრამა, რომელიც მომხარებელს შემოატანინებს რიცხვს და დაბეჭდავს ეს რიცხვი დადებითია, უარყოფითია თუ 0-ია

# user_number = int(input("Enter The number: "))

# if user_number == 0:
#     print("Zero")
# elif user_number > 0:
#     print("Positive")
# else:
#     print("Negative")

        
        










   



    














#7) დაწერეთ პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს და გაიგებს არის თუ არა ის ნაკიანი(წელი როდესაც თებერვალში 29 დღე გვაქვს). ნაკიანი არის წელი თუ ის იყოფა 4-ზე და არ იყოფა 100-ზე ან იყოფა 400-ზე.(გამოიყენეთ and და or ოპერატორები)


#user_year = int(input("Enter a year: "))


#if user_year % 4 == 0 and user_year % 100 != 0 or user_year % 400 == 0:
    #print("Nakiani")
#else:
    #print("ar aris nakiani")












#8) მომხმარებელს შემოატანინეთ რიცხვი 1-დან 100-ის ჩათვლით(ეს იქნება მისი ქულა). თუ მაგალითად 90-დან 100-ის ჩათვლით ექნება ქულა გამოუტანეთ "Your grade is A", თუ 80-დან 90-მდე, გამოუტანეთ "Your grade is B", თუ 70-დან 80-მდე გამოუტანეთ "Your grade is C", სხვა შემთხვევაში გამოუტანეთ "Your grade is D"


#user_num = int(input("Enter Number From 1-100: "))

#print("Your Number is:" , user_num)


#if user_num >= 90:
    #print("Your grade is A")
#elif user_num >= 80 and user_num < 90:
    #print("Your grade is B")
#elif user_num >= 70 and user_num < 80:
    #print("Your Grade is C")
#else:
    #print("Your Grade is D")






