import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QFont, QColor, QTextCursor
from PyQt5.QtCore import Qt

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

    def get_job(self):
        jobs = [
            {"name": "Mühendis", "salary": 5000, "satisfaction": 10, "improvement": 5, "intensity": 10, "reputation": 5},
            {"name": "Doktor", "salary": 7000, "satisfaction": 8, "improvement": 10, "intensity": 15, "reputation": 10},
            {"name": "Öğretmen", "salary": 4000, "satisfaction": 12, "improvement": 7, "intensity": 8, "reputation": 6}
        ]
        self.job = random.choice(jobs)
        return f"Yeni işiniz: {self.job['name']}"

    def quit_job(self):
        if self.job:
            message = f"{self.job['name']} işinden ayrıldınız."
            self.job = None
            return message
        else:
            return "Şu anda bir işiniz yok."

    def ask_for_raise(self):
        if self.job:
            success_chance = self.smartness + (100 - self.job['intensity'])
            if random.randint(0, 100) < success_chance:
                self.job['salary'] += 1000
                return "Zam aldınız!"
            else:
                return "Zam isteğiniz reddedildi."
        else:
            return "Şu anda bir işiniz yok."

    def work_hard(self):
        if self.job:
            self.job['intensity'] += 5
            return "Daha çok çalıştınız ve yoğunluk arttı."
        else:
            return "Şu anda bir işiniz yok."

    def work_less(self):
        if self.job and self.job['intensity'] > 0:
            self.job['intensity'] -= 5
            return "Daha az çalıştınız ve yoğunluk azaldı."
        else:
            return "Şu anda bir işiniz yok veya yoğunluk zaten minimumda."

    def exercise(self):
        self.money -= 50
        self.health += 10
        self.charisma += 5
        return "Egzersiz yaptınız."

    def play_games(self):
        self.money -= 30
        self.health -= 5
        self.happiness += 10
        return "Oyun oynadınız."

    def study(self):
        self.money -= 40
        self.health -= 5
        self.smartness += 10
        return "Ders çalıştınız."

    def show_stats(self):
        return f"Sağlık: {self.health}, Para: {self.money}, Zeka: {self.smartness}, Karizma: {self.charisma}, Mutluluk: {self.happiness}"

class RetroUI(QWidget):
    def __init__(self):
        super().__init__()
        self.character = Character()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Retro Yaşam Simülasyonu")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: black;")

        layout = QVBoxLayout()

        self.text_area = QTextEdit(self)
        self.text_area.setFont(QFont("Courier", 12))
        self.text_area.setStyleSheet("color: green; background-color: black;")
        self.text_area.setReadOnly(True)
        layout.addWidget(self.text_area)

        self.input_line = QLineEdit(self)
        self.input_line.setFont(QFont("Courier", 12))
        self.input_line.setStyleSheet("color: green; background-color: black;")
        self.input_line.returnPressed.connect(self.handle_action)
        layout.addWidget(self.input_line)

        self.setLayout(layout)
        self.update_ui("Oyun başlıyor...")

    def update_ui(self, message):
        self.character.age_up()
        self.text_area.clear()
        self.text_area.append(f"Yaş: {self.character.age}\n")
        self.text_area.append(self.character.show_stats() + "\n\n")
        self.text_area.append("Aksiyonlar:\n")
        self.text_area.append("1- İşe gir\n")
        self.text_area.append("2- İstifa et\n")
        self.text_area.append("3- Zam iste\n")
        self.text_area.append("4- Çok çalış\n")
        self.text_area.append("5- Az çalış\n")
        self.text_area.append("6- Egzersiz yap\n")
        self.text_area.append("7- Oyun oyna\n")
        self.text_area.append("8- Ders çalış\n")
        self.text_area.append("\n" + message + "\n")
        self.text_area.append("\nBir aksiyon seçin ve Enter'a basın: ")
        self.input_line.clear()
        self.input_line.setFocus()

    def handle_action(self):
        action = self.input_line.text()
        if action.isdigit():
            action = int(action)
            if action == 1:
                message = self.character.get_job()
            elif action == 2:
                message = self.character.quit_job()
            elif action == 3:
                message = self.character.ask_for_raise()
            elif action == 4:
                message = self.character.work_hard()
            elif action == 5:
                message = self.character.work_less()
            elif action == 6:
                message = self.character.exercise()
            elif action == 7:
                message = self.character.play_games()
            elif action == 8:
                message = self.character.study()
            else:
                message = "Geçersiz aksiyon."
            self.update_ui(message)
        else:
            self.update_ui("Geçersiz aksiyon. Lütfen bir sayı girin.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = RetroUI()
    ex.show()
    sys.exit(app.exec_())