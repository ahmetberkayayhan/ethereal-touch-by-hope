import sys
import random
import pyfiglet
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer

class Character:
    def __init__(self):
        self.health = 100
        self.money = 1000
        self.smartness = 50
        self.charisma = 50
        self.happiness = 50
        self.job = None
        self.age = 20

    def age_up(self):
        self.age += 1
        money_change = random.randint(-200, -50)
        health_change = random.randint(-5, -1)
        smartness_change = random.randint(-5, -2)

        self.money += money_change
        self.health += health_change
        self.smartness += smartness_change

        if self.money < 0:
            self.money = 0
        if self.health < 0:
            self.health = 0
        if self.smartness < 0:
            self.smartness = 0

    def get_job(self):
        jobs = [
            {"name": "Engineer", "salary": 5000, "satisfaction": 10, "improvement": 5, "intensity": 10, "reputation": 5},
            {"name": "Doctor", "salary": 7000, "satisfaction": 8, "improvement": 10, "intensity": 15, "reputation": 10},
            {"name": "Teacher", "salary": 4000, "satisfaction": 12, "improvement": 7, "intensity": 8, "reputation": 6}
        ]
        self.job = random.choice(jobs)

    def quit_job(self):
        self.job = None

    def ask_for_raise(self):
        if self.job:
            success_chance = self.smartness + (self.job['intensity'])
            if random.randint(0, 100) < success_chance:
                self.job['salary'] += 1000

    def work_hard(self):
        if self.job:
            self.job['intensity'] += 5

    def work_less(self):
        if self.job and self.job['intensity'] > 0:
            self.job['intensity'] -= 5

    def exercise(self):
        self.money -= 50
        self.health += 3
        self.charisma += 1

    def play_games(self):
        self.money -= 30
        self.health -= 2
        self.happiness += 10

    def study(self):
        self.money -= 40
        self.health -= 5
        self.smartness += 10

    def show_stats(self):
        return (f"Health: {self.health}, Money: {self.money}, Smartness: {self.smartness}, Charisma: {self.charisma}, "
                f"Happiness: {self.happiness}, Age: {self.age}, Job: {self.job['name'] if self.job else 'None'}")

class ClickableLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("color: #FFD700;")

    def mousePressEvent(self, event):
        self.clicked.emit()

class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ethereal Touch")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #000000;")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        ethereal_touch_ascii = pyfiglet.figlet_format("Ethereal Touch", font="slant")
        self.ethereal_touch_label = ClickableLabel(f"<pre>{ethereal_touch_ascii}</pre>", self)
        self.ethereal_touch_label.setFont(QFont("Courier", 20))
        layout.addWidget(self.ethereal_touch_label)

        press_start_ascii = pyfiglet.figlet_format("Press Start", font="slant")
        self.press_start_label = ClickableLabel(f"<pre>{press_start_ascii}</pre>", self)
        self.press_start_label.setFont(QFont("Courier", 10))
        self.press_start_label.setStyleSheet("color: #34B233;")
        layout.addWidget(self.press_start_label)

        # Pyfiglet kullanarak "© 2024 Rosehead Midhill" ASCII sanatı oluşturun
        rosehead_ascii = pyfiglet.figlet_format("2024 Rosehead", font="slant")
        midhill_ascii = pyfiglet.figlet_format("Midhill", font="slant")

        # Rosehead ve Midhill ASCII sanatını yanyana yerleştirin (aralarında sadece bir boşluk olacak şekilde)
        combined_ascii = "\n".join(a + " " + b for a, b in zip(rosehead_ascii.splitlines(), midhill_ascii.splitlines()))
        combined_ascii_label = QLabel(f"<pre>{combined_ascii}</pre>", self)
        combined_ascii_label.setFont(QFont("Courier", 8))  # Font boyutunu küçülttük
        combined_ascii_label.setStyleSheet("color: #007AC8;")  # Mavi renk
        combined_ascii_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(combined_ascii_label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blink_text)
        self.timer.start(500)

        self.blink_state = True

        self.press_start_label.mousePressEvent = self.start_game
        self.ethereal_touch_label.mousePressEvent = self.show_ascii_art

    def blink_text(self):
        if self.blink_state:
            self.press_start_label.setStyleSheet("color: #34B233;")
        else:
            self.press_start_label.setStyleSheet("color: #000000;")
        self.blink_state = not self.blink_state

    def start_game(self, event):
        self.game_window = GameWindow()
        self.game_window.show()
        self.close()

    def show_ascii_art(self, event):
        ascii_window = QMainWindow(self)
        ascii_window.setWindowTitle("ASCII Art")
        ascii_window.setGeometry(150, 150, 800, 600)
        ascii_window.setStyleSheet("background-color: #000000;")

        ascii_widget = QWidget(ascii_window)
        ascii_window.setCentralWidget(ascii_widget)
        ascii_layout = QVBoxLayout(ascii_widget)

        ascii_art = """
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                      ████                                                                  
                                                                 █████████████                                                              
                                                           █████████       ██████████                                                       
                                                    █████████████             ██████████████                                                
                                                 ██████      ███    ██████     ████     ██████                                              
                                                 ███       ████   ███████████   ████       ████                                             
                                                ███     ██████   ████████ ████   ███ ███    ███                                             
                                                ███   █████████  █████ ███████   █████████  ████                                            
                                                ███   █████████   ███████████   ██████████  ████                                            
                                                ███ ██  ███ █████    ██████   ██████████████████                                            
                                              █████████ ██   ███████   ██████████████████████████                                           
                                             ██████████████    ███████████████████████████████████                                          
                                             ███  ██████████      ████████████████ ██████████  ████                                         
                                            ███     ██████████     ███████████    █████████     ███                                         
                                            ██         ███████████████         ██████████        ███                                        
                                           ████  ██       ████████      ██████████████      ████████                                        
                                            ██████████     ██████  █████████████████     ███████████                                        
                                           █████████████    ████  █████████████████    █████████████                                        
                                          ████████████████   ██████████████████████  ████████████████                                       
                                         ████   ███████████████████████████████████████████████   ████                                      
                                        ████      ███████████████████████████████  ███████████     ████                                     
                                       ████        █████████████  ███████████   █████████████       ████                                    
                                       ████         ████████████████         ███████████████         ████                                   
                                      ████          ████████████████████████████████████████          ███                                   
                                     ████        ██████████████████████████████████████████████       ████                                  
                                     ████    ███████ █████████████████████████████████████  ██████     ████                                 
                                     ████████████      ███████████████    ███████████████      ████████████                                 
                                    ██████████      █████   ███████           ██████   ████       █████████                                 
                                    ██████        ████   ██████                   █████   ████       ██████                                 
                                    ████        ████  ██████                         █████  ████        ███                                 
                                    ████     ███████████                                ██████████     ████                                 
                             ██████████████████████████████████████████████████████████████████████████████████████                         
                   █████████████████████████████████████████████████████████████████████████████████████████████████████                    
                   █████        ██████        ████       █████        ███   ████   ███         ████     █████        █████                  
                   ███           ████          ███   ██   ████   ████████   ████   ███    █████████     █████         ████                 
                   ███    ███     ███   ████   ██    █████████   ████████   ████   ███    █████████      █████   ███    ███                 
                   ███    ████    ██    ████   ███     ███████       ████          ███    ████████       █████   ████    ███                
                   ███    ████    ██    ████   ████       ████       ████          ███        ████       ████   ████    ███                
                   ███    █      ███    ████   ███████     ███   ████████   ████   ███    ████████   ██   ████   ████    ███                
                   ███         █████    ████   █████████   ███   ████████   ████   ███    ████████        ████   ████    ███                
                   ███         █████    ████   ████  ███   ███   ████████   ████   ███    ███████          ███   ████    ███                
                   ███    █    █████    ███    ███        ████        ███   ████   ███         ██    ██    ███   ████    ███                
                   ███    ██    █████         █████      █████        ██     ██     ██         ██   ████   ███   ████    ███                
                   ███    ███    █████       ███████████████████████████████████████████████████    ████    ██           ███                
                   ███    ███      ██████████████████████████████████████████████████████████████████████████           ███                 
                   ███    ██████████████████████████  ███  █  ██    ███ ██  ██ ███ █████ ██████████████████████████████████                 
                   ████████████████        █████████   █   █  ██  █  ██     ██ ███ █████ ████████████        ████████████                   
                   ███████                  ████████  █ █  █  ██  █  ██ ██  ██ ███ █████ ███████████                                        
                                               █████  ███  █  ██    ███ ██  ██ ███    ██    ██████                                          
                                                 ██████████████████████████████████████████████                                             
                                                   ██████████████████████████████████████████                                               
                                                      ████████████████████████████████████                                                  
                                                           ██████████████████████████                                                       
                                                                 ██████████████                                                             
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
        """

        ascii_label = QLabel(f"<pre>{ascii_art}</pre>", ascii_window)
        ascii_label.setFont(QFont("Courier", 8))
        ascii_label.setStyleSheet("color: #FFFFFF;")
        ascii_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        ascii_layout.addWidget(ascii_label)

        ascii_window.show()

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.character = Character()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ethereal Touch - Game")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #000000;")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.stats_label = QLabel(self.character.show_stats(), self)
        self.stats_label.setFont(QFont("Courier", 10))
        self.stats_label.setStyleSheet("color: #FFFFFF;")
        layout.addWidget(self.stats_label)

        self.actions_input = QLineEdit(self)
        self.actions_input.setPlaceholderText("Choose your actions (separated by commas):")
        layout.addWidget(self.actions_input)

        self.action_button = QPushButton("Perform Actions", self)
        self.action_button.clicked.connect(self.perform_actions)
        layout.addWidget(self.action_button)

        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

    def perform_actions(self):
        actions = self.actions_input.text().split(',')
        self.character.age_up()
        self.output_text.append(f"Age: {self.character.age}")

        for action in actions:
            action = action.strip()
            if action == '1':
                self.character.get_job()
                self.output_text.append(f"Your new job: {self.character.job['name']}")
            elif action == '2':
                self.character.quit_job()
                self.output_text.append("You quit your job.")
            elif action == '3':
                self.character.ask_for_raise()
                self.output_text.append("You asked for a raise.")
            elif action == '4':
                self.character.work_hard()
                self.output_text.append("You worked harder.")
            elif action == '5':
                self.character.work_less()
                self.output_text.append("You worked less.")
            elif action == '6':
                self.character.exercise()
                self.output_text.append("You exercised.")
            elif action == '7':
                self.character.play_games()
                self.output_text.append("You played games.")
            elif action == '8':
                self.character.study()
                self.output_text.append("You studied.")
            else:
                self.output_text.append("Invalid action.")

        self.stats_label.setText(self.character.show_stats())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash_screen = SplashScreen()
    splash_screen.show()
    sys.exit(app.exec_())