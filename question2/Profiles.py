from Person import Person

# 8 users
user1 = Person("Tan Jing Ming", "Male", "🎮 'Eat. Sleep. Game. Repeat.' | Anime fan", "Public", "2002-05-17")
user2 = Person("Sofia Ahmad", "Female", "Travel addict. Coffee fiend ☕. Loves street photography.", "Public", "2001-11-03")
user3 = Person("JY Lim", "Male", "Night owl 🌙 | Meme curator 😂 | Student", "Private", "2003-07-21")
user4 = Person("Ethan Koh Yi Ming", "Male", "Founder | Dog dad | Coffee enthusiast ☕", "Private", "1988-12-02")
user5 = Person("Thanu Raj", "Male", "Digital marketer. Amateur chef. Weekend hiker.", "Public", "1990-03-11")
user6 = Person("Helen Lee Jia Rong", "Female", "Retired teacher. I enjoy gardening and reading novels.", "Private", "1955-02-28")
user7 = Person("Robert Lim", "Male", "Photography & family time 🪷", "Public", "1948-06-15")
user8 = Person("David Chuah", "Male", "Engineer | Marathon runner 🏃 | Amateur guitarist 🎸", "Public", "1972-05-05")

# list of users
users = [user1, user2, user3, user4, user5, user6, user7, user8]

# test print all names
if __name__ == "__main__":
    print("All users:")
    print("-" * 100)
    for user in users:
        print(user)
        print("-" * 100)
