#თქვენი დავალებაა შექმნათ მარტივი ჩატ-ბოტი, რომელიც კოდის გაშვებისთანავე მიესალმება მომხარებელს და ჰკითხავს "How are your?", თუ მომხარებელი შეიყვანს, "Normal" დაბეჭდეთ "Bot:I hope you will get better", სხვა შემთხვევაში თუ შემოიყვანს "Great", დაუბეჭდეთ "Bot:Good! Have a nice day", ხოლო თუ შემოიყვანა "Sad" ან "Super Sad" დაუბეჭდეთ "Bot:It's sad". საბოლოოდ დაბეჭდეთ "Good bye!" და გათიშეთ while ციკლი. ამისათვის მას გადაეცით სწორი პირობა(მინიშნება: შექმენით ცვლადი რომლის მნიშვნელობა თავიდან იქნება False, while ციკლს პირობად გაუწერეთ ეს ცვლადი, თუ მომხარებელმა სწორი ინფორმაცია შემოიყვანა მისი ნიშვნელობა გახდება True და როცა ყველა პირობა შესრულდება while ციკლი გაითიშება).

# თუ მომხარებელი შემოიყვანს ისეთ ინფორმაციას რაზეც თქვენი ბოტი არ არის დაპროგრამირებული, დაბეჭდეთ "Bot: Sorry, I didn't understand, repeat."(ამ შემთხვევაში while ციკლისთვის შექმნილი ცვლადის მნიშვნელობა არ იცვლება და ციკლი არ წყვეტს მუშაობას)

# დაგჭირდებათ: while loop; input; if/else; and or.

# თქვენი სურვილით დაამატეთ სხვა ფუნქციები და გააუმჯობესეთ ჩატ-ბოტი



chat_bot = True


print("Bot: How are your?")


while chat_bot:
    user_input = input("You: ")

    if user_input == "Normal":
        print("Bot: I hope you will get better")
    elif user_input == "Great":
        print("Bot: Good! Have a nice day")
    elif user_input == "Sad" or user_input == "Super Sad":
        print("Bot: It's sad")
    else:
        print("Bot: Sorry, I didn't understand, repeat.")
        chat_bot = False

print("Good Bye")

 




