
#1) while ციკლის გამოყენებით დაპრინტეთ 1-დან 50-მდე ყველა 4-ის ჯერადი რიცხვის კუბი

#num = 4

#while num < 50:
    #print(num **3)
    #num = num + 4







#2) შექმენით რიცხვების დიაპაზონი 1-დან 100-მდე, შეამოწმეთ თუ რიცხვი იყოფა 3-ზე დაბეჭდეთ "Fizz" და გვერდზე მიუწერეთ რიცხვი. თუ რიცხვი იყოფა 5-ზე დაბეჭდეთ "Buzz" და გვერდზე მიუწერეთ რიცხვი, ხოლო თუ იყოფა 3-ზეც და 5-ზეც დაბეჭდეთ "FizzBuzz" და გვერდზე მიუწერეთ რიცხვი



#for i in range(1, 100 + 1):                                          #დიაპაზონი როშევქმნათ საჭიროა For Loop- ი
    #print(i)                                                         # აქ უკვე გვჭირდება If elif Operatori            
    #if i % 3 == 0 and i % 5 == 0:
        #print(i , "FizzBuzz")
    #elif i % 3 == 0:
        #print(i , "Fizz")
    #elif i % 5 == 0:
        #print(i , "Buzz")
    
        
        




#3) შექმენით ორი ცვლადი, პირველში შეინახეთ 1-დან 20-ის ჩათვლით ყველა ლუწი რიცხვის ჯამი, მეორეში კი ყველა კენტის. აიყვანეთ ორივე მე-5 ხარისხში და დაპრინტეთ ის, რომელიც არის მეტი


#even_sum = 0
# odd_sum = 0

# for i in range(1, 20 + 1):
#     if i % 2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i





# if even_sum ** 5 > odd_sum ** 5:
#     print("Even Sum is Greater Than Odd_Sum" , even_sum **5 ,)
# else:
#     print("Odd Sum is Greater Than Even_Sum" , odd_sum ** 5)








#4) True or False and 5 > 3 or "name" == "name" and 123 == "123" and 5 >= 5 <--- გაიგეთ რას გამოიტანს ეს კოდი და ახსენით რატომ.

              #False                          #false              
#True or False and 5 > 3 or "name" == "name" and 123 == "123" and 5 >= 5 <        #პასუხი არის True - რადგან True or False - იქნება True and 5>3 -True  შემდეგ 5>3 or "name" == "name" - True and 123 == "123 - false and 5>= 5  - False"





#5) მომხარებელს შემოატანინეთ რიცხვი და გაიგეთ არის თუ არა ის მარტივი, თუ მარტივია დაპრინტეთ "Number is prime", სხვა შემთხვევაში "Number is not prime"(მარტივია რიცხვი, რომელიც იყოფა მარტო თავის თავზე და ერთზე)

#user_num = int(input("Enter The Number: "))
#print("Your Number Is:", user_num)

#if user_num % 2 == 0:
    #print("Number is not prime")
#else:
    #print("Number is prime")