import random

class Character:
    def __init__(self):
        self.health = 100
        self.money = 1000
        self.smartness = 50
        self.charisma = 50
        self.happiness = 50
        self.job = None
        self.age = 0

    def age_up(self):
        self.age += 1
        print(f"Yaş: {self.age}")

    def get_job(self):
        jobs = [
            {"name": "Mühendis", "salary": 5000, "satisfaction": 10, "improvement": 5, "intensity": 10, "reputation": 5},
            {"name": "Doktor", "salary": 7000, "satisfaction": 8, "improvement": 10, "intensity": 15, "reputation": 10},
            {"name": "Öğretmen", "salary": 4000, "satisfaction": 12, "improvement": 7, "intensity": 8, "reputation": 6}
            # Daha fazla meslek ekleyebilirsiniz
        ]
        self.job = random.choice(jobs)
        print(f"Yeni işiniz: {self.job['name']}")

    def quit_job(self):
        if self.job:
            print(f"{self.job['name']} işinden ayrıldınız.")
            self.job = None
        else:
            print("Şu anda bir işiniz yok.")

    def ask_for_raise(self):
        if self.job:
            success_chance = self.smartness + (100 - self.job['intensity'])
            if random.randint(0, 100) < success_chance:
                self.job['salary'] += 1000
                print("Zam aldınız!")
            else:
                print("Zam isteğiniz reddedildi.")
        else:
            print("Şu anda bir işiniz yok.")

    def work_hard(self):
        if self.job:
            self.job['intensity'] += 5
            print("Daha çok çalıştınız ve yoğunluk arttı.")
        else:
            print("Şu anda bir işiniz yok.")

    def work_less(self):
        if self.job and self.job['intensity'] > 0:
            self.job['intensity'] -= 5
            print("Daha az çalıştınız ve yoğunluk azaldı.")
        else:
            print("Şu anda bir işiniz yok veya yoğunluk zaten minimumda.")

    def exercise(self):
        self.money -= 50
        self.health += 10
        self.charisma += 5
        print("Egzersiz yaptınız.")

    def play_games(self):
        self.money -= 30
        self.health -= 5
        self.happiness += 10
        print("Oyun oynadınız.")

    def study(self):
        self.money -= 40
        self.health -= 5
        self.smartness += 10
        print("Ders çalıştınız.")

    def show_stats(self):
        print(f"Sağlık: {self.health}, Para: {self.money}, Zeka: {self.smartness}, Karizma: {self.charisma}, Mutluluk: {self.happiness}")

def main():
    character = Character()

    while character.age < 100:  # Oyunun süresi veya sonu belirlenebilir
        character.age_up()
        character.show_stats()

        # Kullanıcıdan aksiyon seçmesini isteyin
        print("Aksiyonlar: 1- İşe gir, 2- İstifa et, 3- Zam iste, 4- Çok çalış, 5- Az çalış, 6- Egzersiz yap, 7- Oyun oyna, 8- Ders çalış")
        action = int(input("Aksiyon seçin: "))

        if action == 1:
            character.get_job()
        elif action == 2:
            character.quit_job()
        elif action == 3:
            character.ask_for_raise()
        elif action == 4:
            character.work_hard()
        elif action == 5:
            character.work_less()
        elif action == 6:
            character.exercise()
        elif action == 7:
            character.play_games()
        elif action == 8:
            character.study()
        else:
            print("Geçersiz aksiyon.")

        # Oyun döngüsü devam eder

if __name__ == "__main__":
    main()