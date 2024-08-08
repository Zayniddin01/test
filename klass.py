class User:
    def __init__(self, n_name, f_name, email) -> None:
        self.nick_name = n_name
        self.full_name = f_name
        self.mail = email
    
    def get_info(self):
        j = f"Foydalanuvchi: {self.nick_name}, Full name: {self.full_name}, Email: {self.mail}"
        return j

user1 = User("Solo78", "Musayev Zayniddin", "zmusayev789@gmail.com")
user2 = User("Shota18", "Musayev Ziyoviddin", "musaziyo48@gmail.com")

print(user1.get_info())