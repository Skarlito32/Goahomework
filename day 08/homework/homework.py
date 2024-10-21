#2)გამოიტანეთ თქვენი სახელი და გვარი იმდენჯერ, რამდენი წლისაც ხართ


for i in range (17):
    print("Irakli Mebonia")


#3)გამოიტანეთ ტერმინალში რიცხვები 1-დან 20-ის ჩათვლით




for i in range(21):
    print(i)



#4)გამოიტანეთ ტერმინალში რიცხვები 20-დან 0-მდე




for i in range(20, 0, -1):   
    print(i)




#5)გამოითვალეთ 1-დან 50-ის ჩათვლით ყველა რიცხვის ჯამი და დაპრინტეთ საბოლოო შედეგი


sum = 1

for i in range(50):
    sum = sum + i
print(sum)



#6)დაბეჭდეთ 1-დან 5-ის ჩათვლით რიცხვთა კვადრატი(n * n)


sum = 0

for i in range(5):
    sum += i * i
print(sum)





#7)დაბეჭდეთ ყველა ლუწი რიცხვის ჯამი 1-დან 10-ის ჩათვლით


sum = 0

for i in range(0, 10, 2):
    sum = sum + i
print(sum)



#8)მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ცვლადში, შემდეგ კი 0-დან შემოტანილი რიცხვის ჩათვლით შეამოწმეთ, თუ ლუწია დაბეჭდეთ რიცხვი is Even, სხვა შემთხვევაში რიცხვი is Odd;(მაგალითად 4, ლუწია ამიტომაც დაბეჭდავთ "4 is Even")

user_num = int(input("Enter a number: "))

for num in range(0,user_num + 1):
    if num % 2 == 0:
        print(str(num) + " is Even")
    else:
        print(str(num) + " Is odd")

      









